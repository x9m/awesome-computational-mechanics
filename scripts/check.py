#!/usr/bin/env python3
"""Validate data/repos.yml and the files generated from it.

  python3 scripts/check.py           check data and generated files
  python3 scripts/check.py --write   regenerate README.md and archive.md
  python3 scripts/check.py --online  also check every repo (needs network and an authenticated gh)
"""
import json
import re
import subprocess
import sys
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
        "Fracture, boundary and scaled boundary methods",
        "Solver interfaces and utilities",
        "Teaching and compact codes",
    ],
    "Virtual element method": [
        "VEM libraries",
        "Elasticity",
        "Dynamics and fracture",
        "Coupled fields and electronic packaging",
        "Topology optimization with VEM",
        "Introductory VEM codes",
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
    ],
    "Constitutive modeling and material identification": [
        "Neural network constitutive models",
        "Unsupervised model discovery",
        "Material subroutines and libraries",
        "Experimental parameter identification",
    ],
    "Multiscale and homogenization": [
        "FFT-based homogenization",
        "Crystal plasticity",
    ],
    "Thermal, multiphysics and additive manufacturing": [
        "Heat transfer and bio-heat",
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
        "Graph neural networks",
        "Biomechanical surrogates",
        "Response histories and operator learning",
        "Frameworks and introductory studies",
    ],
    "Meshing, pre- and post-processing": [
        "Mesh generation",
        "Mesh processing and formats",
        "Visualization and export",
        "Sample geometry",
    ],
    "Courses, references and agents for mechanics": [
        "Courses and tutorials",
        "Curated lists",
        "Agents for mechanics",
    ],
}
FIELDS = {"url", "category", "subtopic", "description", "language", "license", "note", "status", "source"}
BATCH = 50  # repositories per GraphQL request
SOURCES = ("stars", "own", "following", "collaborator", "topic", "major")
URL = re.compile(
    r"https://(github\.com|gitlab\.com|gitlab\.onelab\.info|gitlab\.dune-project\.org)/([\w.-]+/[\w.-]+)"
    # Optionally, a file or folder inside a GitHub repository.
    r"(?:/(?:tree|blob)/([\w.-]+)/([\w./-]+))?"
)
INTROS = {
    "Virtual element method":
        "The virtual element method (VEM) generalizes finite elements to polygonal and polyhedral elements.",
    "Third medium contact":
        "Third medium contact (TMC) models contact by meshing the gap with a very compliant fictitious material. "
        "Some links open the relevant file inside a larger project. DTU's MATLAB TopTMC code is not in a "
        "repository and can be downloaded from the [TopOpt software page]"
        "(https://www.topopt.mek.dtu.dk/apps-and-software).",
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
        if not isinstance(value, str):
            found.append(f"{key} must be a string")
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
    if entry["source"] not in SOURCES:
        found.append("unknown source")
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
        except ValueError as exc:
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


def anchor(title):
    return re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")


def target(topic, subtopic=None):
    return f"open-{anchor(topic)}" + (f"--{anchor(subtopic)}" if subtopic else "")


def link(text, topic, subtopic=None):
    return f"[{text}](#user-content-{target(topic, subtopic)})"


def section(body, topic, subtopic=None):
    # GitHub opens collapsed sections, and all their parents, only when a link uses the full
    # "user-content-" ID and its target is inside <details> but outside <summary>.
    # The target repeats the title because the heading scrolls under GitHub's sticky bar.
    # The blank lines are required for GitHub to render the Markdown inside.
    heading = f"<h3>{subtopic}</h3>" if subtopic else f"<h2>{topic}</h2>"
    title = f"{topic} › <b>{subtopic}</b>" if subtopic else f"<b>{topic}</b>"
    return ["<details>", f"<summary>{heading}</summary>",
            f'<p id="{target(topic, subtopic)}"><sub>{title} · '
            '<a href="#contents">Back to contents</a></sub></p>',
            "", *body, "", "</details>", ""]


def cell(text):
    # An unescaped pipe would start a new column.
    return text.replace("|", "\\|")


def row(entry):
    notes = []
    if entry["source"] == "own":
        notes.append("**By the list maintainer.**")
    if entry["note"]:
        notes.append(f"{entry['note']}.")
    # Break after the owner so long names do not push the Note column out of view.
    name = entry["name"].replace("/", "/<br>", 1)
    cells = [f"[{name}]({entry['url']})", entry["description"],
             entry["language"], entry["license"], " ".join(notes)]
    return "| " + " | ".join(map(cell, cells)) + " |"


def table(entries):
    return ["| Name | Descriptions | Languages | License | Note |",
            "| --- | --- | --- | --- | --- |",
            *map(row, entries)]


def render(entries):
    listed = [e for e in entries if e["status"] == "listed"]
    inactive = sorted((e for e in entries if e["status"] == "inactive"), key=lambda e: e["name"].lower())
    topics = []  # (topic, number of entries, [(sub-topic, its entries)])
    for topic, subtopics in TOPICS.items():
        groups = [(sub, sorted((e for e in listed if e["category"] == topic and e["subtopic"] == sub),
                               key=lambda e: e["name"].lower()))
                  for sub in subtopics]
        groups = [(sub, group) for sub, group in groups if group]
        if groups:
            topics.append((topic, sum(len(group) for _, group in groups), groups))
    count = {s: sum(e["source"] == s for e in listed) for s in SOURCES}

    out = [
        "# Awesome Computational Mechanics", "",
        "A collection of public repositories for computational mechanics: solid and structural mechanics, "
        "soft bodies, biomechanics, particle methods, and machine learning applied to them.", "",
        f"It has {len(listed)} entries: "
        f"{count['stars']} from the maintainer's GitHub stars, {count['own']} by the maintainer, "
        f"{count['following']} from accounts the maintainer follows, "
        f"{count['collaborator']} where those accounts are collaborators, {count['topic']} found by topic search "
        f"and {count['major']} major projects chosen editorially. "
        f"Together they cover {len({(e['host'], e['name']) for e in listed})} repositories. "
        f"Another {len(inactive)} archived or unmaintained ones are in [archive.md](archive.md).", "",
        "> **Before you rely on this list:** it is not complete. "
        "Descriptions were drafted with AI from README excerpts, file listings and repository metadata. "
        "The code was not run or validated, and a listing is not an endorsement. "
        "License labels are a convenience, not legal advice. \"None found\" means no license was found "
        "in the places checked, so do not assume you may reuse that code. Public does not always mean open source.",
        "", "## Contents", "",
    ]
    for topic, size, groups in topics:
        out += [f"- {link(topic, topic)} ({size})",
                "  - " + " · ".join(f"{link(sub, topic, sub)} ({len(group)})" for sub, group in groups)]
    out += ["- [Contributing](#contributing)", ""]
    for topic, _, groups in topics:
        body = [INTROS[topic], ""] if topic in INTROS else []
        for sub, group in groups:
            body += section(table(group), topic, sub)
        out += section(body[:-1], topic)
    out += ["## Contributing", "", "Corrections and additions are welcome. See [contributing.md](contributing.md)."]
    archive = [
        "# Archived and unmaintained", "",
        "These projects are archived on GitHub or described by their authors as unmaintained. "
        "The main list is in [README.md](README.md).", "", *table(inactive),
    ]
    return {"README.md": "\n".join(out) + "\n", "archive.md": "\n".join(archive) + "\n"}


def fetch(command):
    """Run a command that prints JSON. Return (data, error message)."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=90)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, str(exc)
    try:
        data = json.loads(result.stdout)
    except ValueError:
        return None, result.stderr.strip() or "response was not JSON"
    return data, result.stderr.strip()


def probe_gitlab(entry):
    name = entry["name"]
    api = f"https://{entry['host']}/api/v4/projects/{urllib.parse.quote(name, safe='')}"
    # curl uses the system's certificate store, which some Python installs cannot find.
    project, error = fetch(["curl", "-fsS", "--max-time", "30", api])
    if not isinstance(project, dict) or "path_with_namespace" not in project:
        return [f"{name}: lookup failed ({error or 'unexpected response'})"]
    if project["path_with_namespace"] != name:
        return [f"{name}: moved to {project['path_with_namespace']}"]
    if project.get("archived") and entry["status"] != "inactive":
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
            expression = json.dumps(f"{entry['ref']}:{entry['path']}")
            target = f" target: object(expression: {expression}) {{ __typename }}"
        queries.append(f"r{index}: repository(owner: {owner}, name: {repo}) "
                       f"{{ nameWithOwner isPrivate isArchived{target} }}")
    response, error = fetch(["gh", "api", "graphql", "-f", "query={" + " ".join(queries) + "}"])
    # gh exits non-zero when any repository is missing, but still returns data for the others.
    data = response.get("data") if isinstance(response, dict) else None
    if not isinstance(data, dict):
        return [f"GitHub lookup of {len(batch)} entries failed ({error or 'unexpected response'})"]

    errors = []
    for index, entry in enumerate(batch):
        name, repo = entry["name"], data.get(f"r{index}")
        if not repo:
            errors.append(f"{name}: not found or not accessible")
        elif repo["nameWithOwner"] != name:
            errors.append(f"{name}: moved to {repo['nameWithOwner']}")
        elif repo["isPrivate"]:
            errors.append(f"{name}: no longer public")
        elif repo["isArchived"] and entry["status"] != "inactive":
            errors.append(f"{name}: archived, set status to inactive")
        elif entry["path"] and not repo.get("target"):
            errors.append(f"{name}: {entry['path']} not found")
    return errors


def probe_all(entries):
    github = [e for e in entries if e["host"] == "github.com"]
    batches = [github[i:i + BATCH] for i in range(0, len(github), BATCH)]
    gitlab = [e for e in entries if e["host"] != "github.com"]
    with ThreadPoolExecutor(4) as pool:
        results = [*pool.map(probe_github, batches), *pool.map(probe_gitlab, gitlab)]
    return [error for result in results for error in result]


def main():
    args = set(sys.argv[1:])
    if args & {"-h", "--help"}:
        print(__doc__)
        return 0
    if args - {"--write", "--online"}:
        sys.exit(__doc__)
    entries, errors = load()
    if not errors:
        for filename, text in render(entries).items():
            path = ROOT / filename
            if "--write" in args:
                path.write_text(text, encoding="utf-8")
            elif not path.exists() or path.read_text(encoding="utf-8") != text:
                errors.append(f"{filename}: out of date, run with --write")
        if "--online" in args:
            errors += probe_all(entries)
    for error in errors:
        print("ERROR", error)
    print(f"{len(entries)} entries, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
