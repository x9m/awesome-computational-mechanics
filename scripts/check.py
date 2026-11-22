#!/usr/bin/env python3
"""Validate data/repos.yml and the files generated from it.

  python3 scripts/check.py           check data and generated files
  python3 scripts/check.py --write   regenerate README.md and archive.md
  python3 scripts/check.py --online  also check every repo (needs an authenticated gh)
"""
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = [
    "Finite and boundary element methods",
    "Meshfree and particle methods",
    "Soft-body, real-time and differentiable simulation",
    "Constitutive modeling and material identification",
    "Multiscale and homogenization",
    "Thermal, multiphysics and additive manufacturing",
    "Optimization and inverse problems",
    "Physics-informed learning and energy methods",
    "Surrogates and reduced-order models",
    "Meshing, pre- and post-processing",
    "Courses, references and agents for mechanics",
]
FIELDS = {"url", "category", "description", "language", "license", "note", "status"}
URL = re.compile(r"https://github\.com/([\w.-]+/[\w.-]+)")


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
            errors.append(f"line {number}: invalid GitHub URL")
            continue
        entry["name"] = match.group(1)
        if entry["name"].lower() in seen:
            errors.append(f"line {number}: duplicate {entry['name']}")
        seen.add(entry["name"].lower())
        if entry["category"] not in CATEGORIES:
            errors.append(f"line {number}: unknown category")
        if entry["status"] not in ("listed", "inactive"):
            errors.append(f"line {number}: unknown status")
        if not entry["description"].endswith(".") or not entry["license"]:
            errors.append(f"line {number}: incomplete description or license")
        entries.append(entry)
    return entries, errors


def anchor(title):
    return re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")


def item(entry):
    facts = "; ".join(filter(None, [entry["language"], f"license: {entry['license']}"]))
    note = f" **Note:** {entry['note']}." if entry["note"] else ""
    return f"- [{entry['name']}]({entry['url']}) - {entry['description']} _({facts})_{note}"


def render(entries):
    listed = [e for e in entries if e["status"] == "listed"]
    inactive = sorted((e for e in entries if e["status"] == "inactive"), key=lambda e: e["name"].lower())
    groups = {c: sorted((e for e in listed if e["category"] == c), key=lambda e: e["name"].lower())
              for c in CATEGORIES}
    out = [
        "# Awesome Mechanical Simulation", "",
        "A collection of public repositories for mechanical simulation: solid and structural mechanics, "
        "soft bodies, biomechanics, particle methods, and machine learning applied to them.", "",
        f"It lists {len(listed)} repositories, plus {len(inactive)} archived or unmaintained ones in "
        "[archive.md](archive.md).", "",
        "> **Before you rely on this list:** it started from one person's GitHub stars, so it is not complete. "
        "Descriptions were drafted with AI from README excerpts, file listings and repository metadata. "
        "The code was not run or validated, and a listing is not an endorsement. "
        "License labels are a convenience, not legal advice. \"None found\" means no license was found "
        "in the places checked, so do not assume you may reuse that code. Public does not always mean open source.",
        "", "## Contents", "",
    ]
    out += [f"- [{c}](#{anchor(c)}) ({len(g)})" for c, g in groups.items() if g]
    out += ["- [Contributing](#contributing)", ""]
    for category, group in groups.items():
        if group:
            # The blank lines inside <details> are required for GitHub to render the Markdown list.
            out += ["<details>", f"<summary><h2>{category}</h2></summary>", "",
                    *map(item, group), "", "</details>", ""]
    out += ["## Contributing", "", "Corrections and additions are welcome. See [contributing.md](contributing.md)."]
    archive = [
        "# Archived and unmaintained", "",
        "These projects are archived on GitHub or described by their authors as unmaintained. "
        "The main list is in [README.md](README.md).", "", *map(item, inactive),
    ]
    return {"README.md": "\n".join(out) + "\n", "archive.md": "\n".join(archive) + "\n"}


def probe(entry):
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
