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
CATEGORIES = [
    "Finite and boundary element methods",
    "Virtual element method",
    "Third medium contact",
    "Meshfree and particle methods",
    "Soft-body, real-time and differentiable simulation",
    "Multibody dynamics and biomechanics",
    "Constitutive modeling and material identification",
    "Multiscale and homogenization",
    "Thermal, multiphysics and additive manufacturing",
    "Optimization and inverse problems",
    "Physics-informed learning and energy methods",
    "Surrogates and reduced-order models",
    "Meshing, pre- and post-processing",
    "Courses, references and agents for mechanics",
]
FIELDS = {"url", "category", "description", "language", "license", "note", "status", "source"}
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


def load():
    entries, errors, seen = [], [], set()
    lines = (ROOT / "data/repos.yml").read_text(encoding="utf-8").splitlines()
    for number, line in enumerate(lines, 1):
        if not line.strip() or line.startswith("#"):
            continue
        try:
            entry = json.loads(line.removeprefix("- "))
        except ValueError as exc:
            errors.append(f"line {number}: invalid entry ({exc})")
            continue
        if not isinstance(entry, dict) or set(entry) != FIELDS:
            errors.append(f"line {number}: fields must be {sorted(FIELDS)}")
            continue
        match = URL.fullmatch(entry["url"])
        if not match:
            errors.append(f"line {number}: invalid or unsupported repository URL")
            continue
        entry["host"], entry["name"], entry["ref"], entry["path"] = match.groups()
        if entry["url"].lower() in seen:
            errors.append(f"line {number}: duplicate {entry['name']}")
        seen.add(entry["url"].lower())
        if entry["source"] not in SOURCES:
            errors.append(f"line {number}: unknown source")
        if entry["category"] not in CATEGORIES:
            errors.append(f"line {number}: unknown category")
        if entry["path"] and entry["host"] != "github.com":
            errors.append(f"line {number}: links into a repository are supported for GitHub only")
        if entry["status"] not in ("listed", "inactive"):
            errors.append(f"line {number}: unknown status")
        if not entry["description"].endswith(".") or not entry["license"]:
            errors.append(f"line {number}: incomplete description or license")
        entries.append(entry)
    return entries, errors


def anchor(title):
    return re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")


def section(title, body):
    # GitHub opens a collapsed section only when a link uses the full "user-content-" ID
    # and its target is inside <details> but outside <summary>.
    # The target repeats the title because the heading scrolls under GitHub's sticky bar.
    # The blank lines are required for GitHub to render the Markdown inside.
    return ["<details>", f"<summary><h2>{title}</h2></summary>",
            f'<p id="open-{anchor(title)}"><sub><b>{title}</b> · '
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
    groups = {c: sorted((e for e in listed if e["category"] == c), key=lambda e: e["name"].lower())
              for c in CATEGORIES}
    sections = [(c, len(g), ([INTROS[c], ""] if c in INTROS else []) + table(g))
                for c, g in groups.items() if g]
    count = {s: sum(e["source"] == s for e in listed) for s in SOURCES}

    out = [
        "# Awesome Mechanical Simulation", "",
        "A collection of public repositories for mechanical simulation: solid and structural mechanics, "
        "soft bodies, biomechanics, particle methods, and machine learning applied to them.", "",
        f"It has {len(listed)} entries covering {len({(e['host'], e['name']) for e in listed})} repositories: "
        f"{count['stars']} from the maintainer's GitHub stars, {count['own']} by the maintainer, "
        f"{count['following']} from accounts the maintainer follows, "
        f"{count['collaborator']} where those accounts are collaborators, {count['topic']} found by topic search "
        f"and {count['major']} major projects chosen editorially. "
        f"Another {len(inactive)} archived or unmaintained ones are in [archive.md](archive.md).", "",
        "> **Before you rely on this list:** it is not complete. "
        "Descriptions were drafted with AI from README excerpts, file listings and repository metadata. "
        "The code was not run or validated, and a listing is not an endorsement. "
        "License labels are a convenience, not legal advice. \"None found\" means no license was found "
        "in the places checked, so do not assume you may reuse that code. Public does not always mean open source.",
        "", "## Contents", "",
    ]
    out += [f"- [{title}](#user-content-open-{anchor(title)}) ({size})" for title, size, _ in sections]
    out += ["- [Contributing](#contributing)", ""]
    for title, _, body in sections:
        out += section(title, body)
    out += ["## Contributing", "", "Corrections and additions are welcome. See [contributing.md](contributing.md)."]
    archive = [
        "# Archived and unmaintained", "",
        "These projects are archived on GitHub or described by their authors as unmaintained. "
        "The main list is in [README.md](README.md).", "", *table(inactive),
    ]
    return {"README.md": "\n".join(out) + "\n", "archive.md": "\n".join(archive) + "\n"}


def probe_gitlab(entry):
    name = entry["name"]
    api = f"https://{entry['host']}/api/v4/projects/{urllib.parse.quote(name, safe='')}"
    # curl uses the system's certificate store, which some Python installs cannot find.
    result = subprocess.run(["curl", "-fsS", "--max-time", "30", api], capture_output=True, text=True)
    if result.returncode:
        return f"{name}: lookup failed ({result.stderr.strip()})"
    project = json.loads(result.stdout)
    if project["path_with_namespace"] != name:
        return f"{name}: moved to {project['path_with_namespace']}"
    if project.get("archived") and entry["status"] != "inactive":
        return f"{name}: archived, set status to inactive"
    return None


def probe(entry):
    if entry["host"] != "github.com":
        return probe_gitlab(entry)
    name = entry["name"]
    result = subprocess.run(["gh", "api", f"repos/{name}"], capture_output=True, text=True)
    if result.returncode:
        return f"{name}: lookup failed ({result.stderr.strip()})"
    repo = json.loads(result.stdout)
    if repo["full_name"] != name:
        return f"{name}: moved to {repo['full_name']}"
    if repo["private"]:
        return f"{name}: no longer public"
    if repo["archived"] and entry["status"] != "inactive":
        return f"{name}: archived, set status to inactive"
    if entry["path"]:
        target = f"repos/{name}/contents/{entry['path']}?ref={entry['ref']}"
        result = subprocess.run(["gh", "api", target], capture_output=True, text=True)
        if result.returncode:
            return f"{name}: {entry['path']} not found ({result.stderr.strip()})"
    return None


def main():
    args = set(sys.argv[1:])
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
            with ThreadPoolExecutor(8) as pool:
                errors += filter(None, pool.map(probe, entries))
    for error in errors:
        print("ERROR", error)
    print(f"{len(entries)} entries, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
