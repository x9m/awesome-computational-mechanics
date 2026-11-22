#!/usr/bin/env python3
"""Validate data/repos.yml and the files generated from it.

  python3 scripts/check.py           check data and generated files
  python3 scripts/check.py --write   regenerate README.md, archive.md and topics/
  python3 scripts/check.py --online  also check every repo and link (needs network and an authenticated gh)
"""
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Topics and their sub-topics, in the order the README shows them.
TOPICS = {
    "Finite and boundary element methods": [
        "General-purpose frameworks",
        "Structural and solid mechanics solvers",
        "Differentiable and GPU finite elements",
        "Phase-field fracture",
        "Fracture, boundary and scaled boundary methods",
        "Unfitted and embedded methods",
        "Smoothed finite elements",
        "Beams, rods and shells",
        "Solver interfaces and utilities",
        "Teaching and compact codes",
    ],
    "Finite volume methods": [
        "Solid mechanics and fluid-solid interaction",
    ],
    "Virtual element method": [
        "VEM libraries",
        "Elasticity",
        "Dynamics and fracture",
        "Coupled fields and electronic packaging",
        "Topology optimization with VEM",
        "Introductory VEM codes",
    ],
    "Contact mechanics": [
        "Contact formulations",
        "Incremental potential contact",
    ],
    "Third medium contact": [
        "Modules and examples in FEM libraries",
        "Optimization and metamaterials",
        "Standalone study codes",
    ],
    "Meshfree and particle methods": [
        "Material point method",
        "Smoothed particle hydrodynamics",
        "Meshless methods",
        "Peridynamics",
        "Discrete and coarse-grained particle models",
    ],
    "Soft-body, real-time and differentiable simulation": [
        "Real-time finite elements",
        "Soft robotics",
        "Position-based and implicit dynamics",
        "Differentiable simulation",
        "Manipulation benchmarks",
    ],
    "Multibody dynamics and biomechanics": [
        "Physics engines for multibody systems",
        "Musculoskeletal biomechanics",
        "Cardiovascular mechanics",
    ],
    "Constitutive modeling and material identification": [
        "Neural network constitutive models",
        "Unsupervised model discovery",
        "Material subroutines and libraries",
        "Experimental parameter identification",
    ],
    "Multiscale and homogenization": [
        "FFT-based homogenization",
        "FE² and computational homogenization",
        "Inverse homogenization",
        "Crystal plasticity",
    ],
    "Thermal, multiphysics and additive manufacturing": [
        "Heat transfer and bio-heat",
        "Thermoelasticity",
        "Additive manufacturing",
        "Multiphysics coupling",
    ],
    "Optimization and inverse problems": [
        "Topology optimization solvers",
        "Learning-based topology optimization",
        "Inverse problems",
    ],
    "Physics-informed learning and energy methods": [
        "Deep energy methods",
        "Residual-based networks",
        "PINN libraries and examples",
    ],
    "Surrogates and reduced-order models": [
        "Stress-field prediction",
        "Deformation and reduced dynamics",
        "Projection-based model reduction",
        "Graph neural networks",
        "Biomechanical surrogates",
        "Response histories and operator learning",
        "Frameworks and introductory studies",
        "Benchmark datasets",
    ],
    "Meshing, pre- and post-processing": [
        "Mesh generation",
        "Mesh processing and formats",
        "Visualization and export",
    ],
    "Linear, eigenvalue and nonlinear solvers": [
        "Solver toolkits",
        "Dense linear algebra",
        "Sparse direct solvers",
        "Iterative solvers and preconditioners",
        "Nonlinear solvers, time integration and continuation",
        "Eigenvalue solvers",
        "Matrix-free operators and partitioning",
    ],
    "Verification, validation and uncertainty": [
        "Code and solution verification",
        "Benchmarks and reference solutions",
        "Experimental data for validation",
        "Calibration and Bayesian inference",
        "Uncertainty and sensitivity analysis",
    ],
    "Courses, references and agents for mechanics": [
        "Courses and tutorials",
        "Element definitions and form languages",
        "Reproducible research software",
        "Curated lists",
        "Agents for mechanics",
    ],
}
FIELDS = {"url", "category", "subtopic", "description", "language", "license", "note", "status", "maintainer"}
NAME_WIDTH = 18  # characters on one line of the name column
BATCH = 50  # repositories per GraphQL request
URL = re.compile(
    r"https://(github\.com|gitlab\.com|gitlab\.onelab\.info|gitlab\.dune-project\.org)/([\w.-]+/[\w.-]+)"
    # Optionally, a file or folder inside a GitHub repository.
    # A "/" in a branch name is written %2F, to tell it apart from the path.
    r"(?:/(?:tree|blob)/([\w.-]+(?:%2[Ff][\w.-]+)*)/([\w./-]+))?"
)
MARKDOWN_LINK = re.compile(r"\]\((https?://(?:[^()\s]|\([^()\s]*\))+)\)")
# Names to show where owner/repository would not be recognizable.
DISPLAY_NAMES = {
    "https://gitlab.com/codeaster/src": "code_aster",
    "https://gitlab.com/yade-dev/trunk": "YADE",
    "https://github.com/KratosMultiphysics/Examples/tree/master/structural_mechanics/validation":
        "KratosMultiphysics/Examples (structural)",
    "https://github.com/KratosMultiphysics/Examples/tree/master/contact_structural_mechanics/validation":
        "KratosMultiphysics/Examples (contact)",
}
# Former titles of sub-topics, whose links must keep working.
FORMER_TITLES = {
    "Courses and tutorials": ["Textbooks and numerical tutorials"],
}
# The "Start here" table: (goal, link text, URL of an entry, topic to browse next, sub-topic or None).
START = [
    ("Learn finite elements", "Imperial College course", "https://github.com/finite-element/finite-element-course",
     "Finite and boundary element methods", "Teaching and compact codes"),
    ("Write a solver in Python", "scikit-fem", "https://github.com/kinnala/scikit-fem",
     "Finite and boundary element methods", "General-purpose frameworks"),
    ("Simulate soft tissue", "FEBio", "https://github.com/febiosoftware/FEBio",
     "Soft-body, real-time and differentiable simulation", "Real-time finite elements"),
    ("Model contact", "IPC Toolkit", "https://github.com/ipc-sim/ipc-toolkit",
     "Contact mechanics", None),
    ("Learn material laws from data", "EUCLID", "https://github.com/EUCLID-code/EUCLID-hyperelasticity",
     "Constitutive modeling and material identification", "Unsupervised model discovery"),
    ("Try virtual elements", "50 lines of VEM", "https://github.com/oliversutton/50LinesOfVEM",
     "Virtual element method", None),
    ("Solve large systems", "PETSc", "https://gitlab.com/petsc/petsc",
     "Linear, eigenvalue and nonlinear solvers", None),
    ("Verify and validate a model", "SimEval", "https://github.com/OSEL-DAM/SimEval",
     "Verification, validation and uncertainty", None),
]
BANNER = [
    '<p align="center">',
    '<img src="assets/banner.png" width="420" '
    'alt="A soft cube with circular cuts at 0, 25 and 50 mm of stretch, colored by displacement">',
    "<br>",
    '<sub>Soft-tissue cube simulated with <a href="https://github.com/x9m/JANP-DJTLED-GPU">JANP-DJTLED</a> '
    '(<a href="assets/LICENSE">MIT</a>)</sub>',
    "</p>",
]
INTROS = {
    "Virtual element method":
        "The virtual element method (VEM) generalizes finite elements to polygonal and polyhedral elements.",
    "Third medium contact":
        "Third medium contact (TMC) models contact by meshing the gap with a very compliant fictitious material. "
        "Some links open the relevant file inside a larger project. DTU's MATLAB TopTMC code is not in a "
        "repository and can be downloaded from the [TopOpt software page]"
        "(https://www.topopt.mek.dtu.dk/apps-and-software).",
    "Linear, eigenvalue and nonlinear solvers":
        "The right solver depends on the structure of the discrete problem.\n\n"
        "- **Symmetric positive definite**, as in many compressible elasticity problems: use Cholesky, "
        "or conjugate gradients with a preconditioner. For smoothed-aggregation multigrid, supply the rigid body modes.\n"
        "- **Symmetric indefinite**, as in mixed formulations and frictionless Lagrange multiplier contact: use an LDLᵀ "
        "factorization, MINRES with a positive definite preconditioner, or GMRES with a block preconditioner.\n"
        "- **Nonsymmetric**, as with friction or non-associated plasticity: use LU, or GMRES or BiCGSTAB "
        "with a preconditioner.\n"
        "- **Snap-through and buckling**: the tangent becomes singular. Arc-length continuation can pass a "
        "limit point, where load-controlled Newton fails. Following a buckled branch from a bifurcation also "
        "needs an imperfection or branch switching.\n"
        "- **Any system**: a small residual does not guarantee a small error when the matrix is ill-conditioned.\n\n"
        "Further reading: "
        "[Davis et al. (2016)](https://doi.org/10.1017/S0962492916000076) on direct methods, "
        "[Saad (2003)](https://doi.org/10.1137/1.9780898718003) on iterative methods, "
        "[Benzi et al. (2005)](https://doi.org/10.1017/S0962492904000212) on saddle point problems and "
        "[Higham (2002)](https://doi.org/10.1137/1.9780898718027) on accuracy and stability.",
    "Verification, validation and uncertainty":
        "These answer different questions, and passing one does not imply passing the others.\n\n"
        "- **Code verification**: are the equations implemented correctly? Compare observed and expected "
        "convergence rates on exact or manufactured solutions "
        "([Roache, 2002](https://doi.org/10.1115/1.1436090)).\n"
        "- **Solution verification**: how large is the numerical error in this result? Study mesh, time step "
        "and solver tolerances ([Roy, 2005](https://doi.org/10.1016/j.jcp.2004.10.036)).\n"
        "- **Validation**: does the model represent reality for its intended use? Compare with experiments "
        "that were not used for calibration. Agreement with another simulation is not validation.\n"
        "- **Uncertainty quantification**: how much do uncertain inputs, model form and numerical error affect "
        "the prediction ([Roy and Oberkampf, 2011](https://doi.org/10.1016/j.cma.2011.03.016))?\n\n"
        "Guidance: "
        "[ASME V&V 10](https://webstore.ansi.org/standards/asme/asme102019r2025) for solid mechanics (paid), "
        "[NASA-STD-7009B](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf) "
        "for models and simulations, "
        "[ten rules for credible simulation in healthcare](https://doi.org/10.1186/s12967-020-02540-4) and "
        "the book by [Oberkampf and Roy (2010)](https://doi.org/10.1017/CBO9780511760396). "
        "Published cardiac benchmarks: [Land et al. (2015)](https://doi.org/10.1098/rspa.2015.0641) and "
        "[Aróstica et al. (2025)](https://doi.org/10.1016/j.cma.2024.117485).",
}


def unique_keys(pairs):
    keys = [key for key, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError("repeated key")
    return dict(pairs)


def problems(entry):
    """Return what is wrong with an entry's fields, before any of them are used."""
    if not isinstance(entry, dict) or set(entry) != FIELDS:
        return [f"fields must be {sorted(FIELDS)}"]
    found = []
    for key, value in sorted(entry.items()):
        if key == "maintainer":
            if not isinstance(value, bool):
                found.append("maintainer must be true or false, without quotes")
        elif not isinstance(value, str):
            found.append(f"{key} must be a string")
        elif re.search("[\ud800-\udfff]", value):
            # UTF-8 cannot encode these, so the files could not be written.
            found.append(f"{key} must be valid Unicode")
        elif value != value.strip() or len(value.splitlines()) > 1:
            found.append(f"{key} must be one line without surrounding spaces")
    if found:
        return found

    match = URL.fullmatch(entry["url"])
    if not match:
        found.append("invalid or unsupported repository URL")
    else:
        host, name, ref, path = match.groups()
        parts = name.split("/") + (path.split("/") if path else [])
        if name.endswith(".git") or ref in (".", "..") or {"", ".", ".."} & set(parts):
            found.append("URL must not contain '.', '..', empty parts or a .git suffix")
        if path and host != "github.com":
            found.append("links into a repository are supported for GitHub only")
    if entry["category"] not in TOPICS:
        found.append("unknown category")
    elif entry["subtopic"] not in TOPICS[entry["category"]]:
        found.append(f"subtopic must be one of {TOPICS[entry['category']]}")
    if entry["status"] not in ("listed", "inactive"):
        found.append("unknown status")
    if not entry["description"].endswith(".") or not entry["description"].strip(".") or not entry["license"]:
        found.append("incomplete description or license")
    if entry["note"].endswith("."):
        found.append("note must not end with a period, one is added")
    return found


def load():
    entries, errors, seen = [], [], set()
    try:
        lines = (ROOT / "data/repos.yml").read_text(encoding="utf-8").split("\n")
    except (OSError, ValueError) as exc:
        return [], [f"cannot read data/repos.yml ({exc})"]
    for number, line in enumerate(lines, 1):
        if not line.strip() or line.startswith("#"):
            continue
        if not line.startswith("- "):
            errors.append(f"line {number}: entries must start with '- '")
            continue
        try:
            entry = json.loads(line[2:], object_pairs_hook=unique_keys)
        except (ValueError, RecursionError) as exc:
            errors.append(f"line {number}: invalid entry ({exc})")
            continue
        found = problems(entry)
        if found:
            errors += [f"line {number}: {problem}" for problem in found]
            continue
        entry["host"], entry["name"], entry["ref"], entry["path"] = URL.fullmatch(entry["url"]).groups()
        # Compare what is linked, so tree/ and blob/ links to the same path count as one.
        key = (entry["host"], entry["name"].lower(), entry["path"])
        if key in seen:
            errors.append(f"line {number}: duplicate {entry['name']}")
        seen.add(key)
        entries.append(entry)
    if not entries and not errors:
        errors.append("data/repos.yml has no entries")
    return entries, errors


def start_problems(entries):
    """Return what is wrong with the "Start here" table."""
    listed = {e["url"]: e for e in entries if e["status"] == "listed"}
    used = {(e["category"], sub) for e in listed.values() for sub in (None, e["subtopic"])}
    found = []
    for goal, _, url, topic, sub in START:
        if url not in listed:
            found.append(f"START, {goal}: {url} is not a listed entry")
        if (topic, sub) not in used:
            found.append(f"START, {goal}: no section {sub or topic}")
    return found


def anchor(title):
    # ASCII only: GitHub percent-encodes other characters in links but not in IDs, so they would not match.
    plain = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return re.sub(r"[^\w -]", "", plain.lower()).replace(" ", "-")


def page(topic):
    return f"topics/{anchor(topic)}.md"


def link(text, topic, subtopic=None):
    """Link from the README to a topic's page, or to a sub-topic on it."""
    return f"[{text}]({page(topic)}" + (f"#{anchor(subtopic)}" if subtopic else "") + ")"


def plain_heading_id(title):
    # GitHub's ID for a heading without its number. Unlike anchor(), it drops characters such as "²".
    return re.sub(r"[^a-z0-9_ -]", "", title.lower()).replace(" ", "-")


def readme_anchors(topic, subtopic=None):
    # The README used to hold every section. These IDs land old links on the index line that leads to the new page.
    ids = []
    for name in [subtopic, *FORMER_TITLES.get(subtopic, [])] if subtopic else [None]:
        ids += [plain_heading_id(name or topic), f"open-{anchor(topic)}" + (f"--{anchor(name)}" if name else "")]
    return "".join(f'<a id="{i}"></a>' for i in ids)


def topic_page(number, topic, groups):
    back = "[← Back to the main list](../README.md#contents)"
    out = [f"# {number}. {topic}", "", back, ""]
    if topic in INTROS:
        out += [INTROS[topic], ""]
    if len(groups) > 1:
        out += [f"- [{number}.{minor} {sub}](#{anchor(sub)}) ({len(group)})"
                for minor, (sub, group) in enumerate(groups, 1)] + [""]
    for minor, (sub, group) in enumerate(groups, 1):
        # Numbers follow the order of TOPICS and are left out of IDs, so renumbering does not break links.
        ids = "".join(f'<a id="{anchor(name)}"></a>' for name in [sub, *FORMER_TITLES.get(sub, [])])
        out += [f"## {ids}{number}.{minor} {sub}", "", *table(group), ""]
    return "\n".join([*out, back]) + "\n"


def cell(text):
    # An unescaped pipe would start a new column, and "<" would start HTML that can close a section.
    return text.replace("|", "\\|").replace("<", "&lt;")


def sort_key(entry):
    return DISPLAY_NAMES.get(entry["url"], entry["name"]).lower()


def wrap_name(text):
    # GitHub removes <wbr> and does not break inside words, so one long name would widen the whole table.
    lines, line = [], ""
    for part in re.split(r"(?<=[-_.])|(?<=[a-z])(?=[A-Z])", text):
        if line and len(line + part) > NAME_WIDTH:
            lines.append(line)
            line = ""
        line += part
    return "<br>".join([*lines, line])


def row(entry):
    notes = []
    if entry["maintainer"]:
        notes.append("**By the list maintainer.**")
    if entry["note"]:
        notes.append(f"{entry['note']}.")
    owner, slash, repo = DISPLAY_NAMES.get(entry["url"], entry["name"]).partition("/")
    name = f"{wrap_name(owner + slash)}<br>{wrap_name(repo)}" if slash else wrap_name(owner)
    # Language and license go under the name, as five columns do not fit on a narrow screen.
    # The link is not escaped: it holds the <br>, and names and URLs cannot contain "|" or "<".
    first = f"[{name}]({entry['url']})" + "".join(
        f"<br><sub>{cell(value)}</sub>" for value in (entry["language"], entry["license"]) if value)
    return "| " + " | ".join([first, cell(entry["description"]), cell(" ".join(notes))]) + " |"


def table(entries):
    return ["| Name, language and license | Description | Note |",
            "| --- | --- | --- |",
            *map(row, entries)]


def render(entries):
    listed = [e for e in entries if e["status"] == "listed"]
    inactive = sorted((e for e in entries if e["status"] == "inactive"), key=sort_key)
    topics = []  # (topic, number of entries, [(sub-topic, its entries)])
    for topic, subtopics in TOPICS.items():
        groups = [(sub, sorted((e for e in listed if e["category"] == topic and e["subtopic"] == sub),
                               key=sort_key))
                  for sub in subtopics]
        groups = [(sub, group) for sub, group in groups if group]
        if groups:
            topics.append((topic, sum(len(group) for _, group in groups), groups))
    out = [
        "# Awesome Computational Mechanics", "",
        f"**{len(listed)} entries for computational mechanics, from finite elements and soft tissue to solvers "
        "and validation**, with licenses, commercial-software requirements and known usage restrictions noted.", "",
        *BANNER, "",
        "## Start here", "",
        "| I want to | Start with | Then browse |",
        "| --- | --- | --- |",
        *(f"| {goal} | [{text}]({url}) | {link(sub or topic, topic, sub)} |"
          for goal, text, url, topic, sub in START),
        "", "## Contents", "",
        *(f"{number}. {link(topic, topic)} ({size})" for number, (topic, size, _) in enumerate(topics, 1)),
        "", "<details>",
        f"<summary>All {sum(len(groups) for _, _, groups in topics)} sub-topics</summary>", "",
    ]
    for number, (topic, size, groups) in enumerate(topics, 1):
        marker = f"{number}. "
        lines = [f"{readme_anchors(topic)}{link(topic, topic)} ({size})"]
        lines += [f"{number}.{minor} {readme_anchors(topic, sub)}{link(sub, topic, sub)} ({len(group)})"
                  for minor, (sub, group) in enumerate(groups, 1)]
        # <br> keeps the sub-topics in their topic's list item: Markdown lists cannot number 1.1, 1.2.
        out.append(marker + ("<br>\n" + " " * len(marker)).join(lines))
    out += ["", "</details>", "", f"[Archived and unmaintained projects](archive.md) ({len(inactive)})", ""]
    curated = link("curated lists", "Courses, references and agents for mechanics", "Curated lists")
    out += ["## Contributing", "", "Corrections and additions are welcome. See [contributing.md](contributing.md).", "",
            "## Acknowledgements", "",
            "Thanks to the authors and maintainers of the listed projects, and to those of the "
            f"{curated} that helped shape this collection. Descriptions and guides were drafted with the help of "
            "Claude Opus 5.5, an AI model by Anthropic."]
    archive = [
        "# Archived and unmaintained", "",
        "These projects are archived on GitHub or described by their authors as unmaintained. "
        "The main list is in [README.md](README.md).", "", *table(inactive),
    ]
    files = {page(topic): topic_page(number, topic, groups) for number, (topic, _, groups) in enumerate(topics, 1)}
    return {"README.md": "\n".join(out) + "\n", "archive.md": "\n".join(archive) + "\n", **files}


def fetch(command):
    """Run a command that prints JSON. Return (data, error message)."""
    try:
        # Not the locale's encoding, which is not UTF-8 on Windows.
        result = subprocess.run(command, capture_output=True, encoding="utf-8", errors="replace", timeout=90)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, str(exc)
    try:
        data = json.loads(result.stdout)
    except ValueError:
        return None, result.stderr.strip() or "response was not JSON"
    return data, result.stderr.strip()


def probe_gitlab(entry):
    name = entry["name"]
    # GitLab's REST API omits "archived" for requests without a login. GraphQL includes it.
    query = json.dumps({"query": f"{{ project(fullPath: {json.dumps(name)}) {{ fullPath archived }} }}"})
    api = f"https://{entry['host']}/api/graphql"
    # curl uses the system's certificate store, which some Python installs cannot find.
    response, error = fetch(["curl", "-fsS", "--max-time", "30",
                             "-H", "Content-Type: application/json", "-d", query, api])
    data = response.get("data") if isinstance(response, dict) else None
    if not isinstance(data, dict):
        return [f"{name}: lookup failed ({error or 'unexpected response'})"]
    project = data.get("project")
    if not project:
        return [f"{name}: not found, moved or not public"]
    if project["fullPath"] != name:
        return [f"{name}: moved to {project['fullPath']}"]
    if project.get("archived") is None:
        return [f"{name}: lookup failed (archived status missing)"]
    if project["archived"] and entry["status"] != "inactive":
        return [f"{name}: archived, set status to inactive"]
    return []


def probe_github(batch):
    """Check a batch of entries in one request.

    One REST request per repository used up the workflow token's 1,000 requests an hour in four runs.
    """
    queries = []
    for index, entry in enumerate(batch):
        owner, repo = map(json.dumps, entry["name"].split("/"))
        target = ""
        if entry["path"]:
            expression = json.dumps(f"{urllib.parse.unquote(entry['ref'])}:{entry['path']}")
            target = f" target: object(expression: {expression}) {{ __typename }}"
        queries.append(f"r{index}: repository(owner: {owner}, name: {repo}) "
                       f"{{ nameWithOwner isPrivate isArchived{target} }}")
    response, error = fetch(["gh", "api", "graphql", "-f", "query={" + " ".join(queries) + "}"])
    # gh exits non-zero when any repository is missing, but still returns data for the others.
    data = response.get("data") if isinstance(response, dict) else None
    if not isinstance(data, dict):
        return [f"GitHub lookup of {len(batch)} entries failed ({error or 'unexpected response'})"]

    # A null repository can also mean an outage or a rate limit, which is not a dead link.
    reasons = {e["path"][0]: e.get("type", "unknown error") for e in response.get("errors") or [] if e.get("path")}
    errors = []
    for index, entry in enumerate(batch):
        name, repo = entry["name"], data.get(f"r{index}")
        if not repo:
            reason = reasons.get(f"r{index}", "no reason given")
            problem = "not found or not accessible" if reason == "NOT_FOUND" else f"lookup failed ({reason})"
            errors.append(f"{name}: {problem}")
        elif repo["nameWithOwner"] != name:
            errors.append(f"{name}: moved to {repo['nameWithOwner']}")
        elif repo["isPrivate"]:
            errors.append(f"{name}: no longer public")
        elif repo["isArchived"] and entry["status"] != "inactive":
            errors.append(f"{name}: archived, set status to inactive")
        elif entry["path"] and not repo.get("target"):
            errors.append(f"{name}: {entry['path']} not found")
    return errors


def extra_links(entries):
    """Return the links in notes and introductions, which are not entries themselves."""
    texts = [*INTROS.values(), *(e["note"] for e in entries)]
    return sorted({url for text in texts for url in MARKDOWN_LINK.findall(text)} - {e["url"] for e in entries})


def probe_link(url):
    """Return (errors, warnings). Only an answer that proves a link is dead is an error."""
    doi = re.fullmatch(r"https?://(?:dx\.)?doi\.org/(.+)", url)
    # Publishers often refuse scripts, so ask doi.org whether the DOI is registered.
    address = f"https://doi.org/api/handles/{doi[1]}" if doi else url
    try:
        result = subprocess.run(["curl", "-sSL", "--max-time", "30", "-o", os.devnull, "-w", "%{http_code}", address],
                                capture_output=True, encoding="utf-8", errors="replace", timeout=90)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [], [f"{url}: could not check ({exc})"]
    status = result.stdout.strip()
    if result.returncode == 6:  # curl could not resolve the host
        return [f"{url}: host not found"], []
    if status in ("404", "410"):
        return [f"{url}: not found (HTTP {status})"], []
    if result.returncode or not status.startswith("2"):
        return [], [f"{url}: could not check ({result.stderr.strip() or 'HTTP ' + status}), open it in a browser"]
    return [], []


def probe_all(entries):
    """Return (errors, warnings)."""
    github = [e for e in entries if e["host"] == "github.com"]
    others = []
    for url in extra_links(entries):
        match = URL.fullmatch(url)
        if match and match[1] == "github.com":
            # Linked repositories get the same checks as entries, including for moves and archiving.
            github.append(dict(zip(("host", "name", "ref", "path"), match.groups()), status="listed"))
        else:
            others.append(url)
    batches = [github[i:i + BATCH] for i in range(0, len(github), BATCH)]
    gitlab = [e for e in entries if e["host"] != "github.com"]
    with ThreadPoolExecutor(4) as pool:
        results = [*pool.map(probe_github, batches), *pool.map(probe_gitlab, gitlab)]
        links = list(pool.map(probe_link, others))
    results += [found for found, _ in links]
    return [error for result in results for error in result], [warning for _, found in links for warning in found]


def main():
    # A Windows console may lack characters that appear in messages.
    sys.stdout.reconfigure(errors="backslashreplace")
    args = set(sys.argv[1:])
    if args & {"-h", "--help"}:
        print(__doc__)
        return 0
    if args - {"--write", "--online"}:
        sys.exit(__doc__)
    entries, errors = load()
    errors = errors or start_problems(entries)
    warnings = []
    if not errors:
        files = render(entries)
        for path in sorted((ROOT / "topics").glob("*.md")):
            if f"topics/{path.name}" not in files:
                errors.append(f"topics/{path.name}: not a current topic, delete it")
        for filename, text in files.items():
            path = ROOT / filename
            if "--write" in args:
                path.parent.mkdir(exist_ok=True)
                # Bytes keep "\n" line endings on Windows, and are encoded before the file is emptied.
                path.write_bytes(text.encode("utf-8"))
            elif not path.exists() or path.read_text(encoding="utf-8") != text:
                errors.append(f"{filename}: out of date, run with --write")
        if "--online" in args:
            found, warnings = probe_all(entries)
            errors += found
    for warning in warnings:
        print("WARNING", warning)
    for error in errors:
        print("ERROR", error)
    print(f"{len(entries)} entries, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
