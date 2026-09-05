#!/usr/bin/env python3
"""Check package structure, links, pinned provenance, and illustrative input IDs."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


def main():
    package = Path(__file__).resolve().parents[1]
    repository = package.parent
    errors = []
    provenance = json.loads((package / "provenance.json").read_text())
    revision = provenance["upstream_revision"]
    expected = set(provenance["skills"])
    actual = {p.parent.name for p in (package / "skills").glob("*/SKILL.md")}
    if actual != expected:
        errors.append(f"Skill set differs: missing={expected-actual}, extra={actual-expected}")

    for name in sorted(actual):
        path = package / "skills" / name / "SKILL.md"
        text = path.read_text()
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"{path.relative_to(repository)}: missing frontmatter")
            continue
        header = match.group(1)
        if f"name: {name}" not in header.splitlines():
            errors.append(f"{name}: frontmatter name does not match directory")
        if not re.search(r"^description: .+", header, re.M):
            errors.append(f"{name}: missing description")
        if "disable-model-invocation" in header:
            errors.append(f"{name}: unexpected Cursor-specific invocation policy")
        if "../../RUNTIME_CONTRACT.md" not in text:
            errors.append(f"{name}: shared runtime contract is not linked")

    for path in package.rglob("*.md"):
        text = path.read_text()
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.exists():
                errors.append(f"{path.relative_to(repository)}: broken link {target}")

    for path, source in provenance["sources"].items():
        result = subprocess.run(
            ["git", "show", f"{revision}:{path}"], cwd=repository,
            capture_output=True, check=False,
        )
        if result.returncode:
            errors.append(f"Upstream source missing at pinned revision: {path}")
            continue
        if hashlib.sha256(result.stdout).hexdigest() != source["sha256"]:
            errors.append(f"Pinned source hash differs: {path}")
        current = repository / path
        if not current.is_file() or current.read_bytes() != result.stdout:
            errors.append(f"Retained upstream reference differs: {path}")
        for destination in source["destinations"]:
            if not (package / destination).is_file():
                errors.append(f"Missing mapped destination: {destination}")

    for name, sources in provenance["skills"].items():
        for source in sources:
            if source not in provenance["sources"]:
                errors.append(f"{name}: unrecorded source {source}")

    spec = json.loads((package / "examples" / "notes-acceptance.json").read_text())
    ids = [criterion["id"] for criterion in spec["criteria"]]
    if not ids or len(ids) != len(set(ids)):
        errors.append("Example acceptance criteria are empty or duplicated")
    for criterion in spec["criteria"]:
        if not criterion.get("outcome") or not criterion.get("observation_boundary"):
            errors.append(f"Example criterion lacks observable outcome: {criterion.get('id')}")

    if (package / "LICENSE").read_bytes() != (repository / "pstack/LICENSE").read_bytes():
        errors.append("Adapted package must preserve the upstream MIT notice")

    if errors:
        print("Library checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(actual)} skills, Markdown links, {len(provenance['sources'])} pinned sources, license, and example IDs.")
    print("Static package checks only; no agents, browser sessions, or cloud services were exercised.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
