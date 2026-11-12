#!/usr/bin/env python3
"""Maintain bundled upstream source snapshots. stdlib only. Run from repo root."""
import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "references/vendor/manifest.json"
MODULES = ROOT / "modules"


def paths():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for item in data["items"]:
        source = item["source"]
        path = item["path"]
        yield source, data["sources"][source], path, ROOT / "references/vendor" / source / path


def check():
    missing = []
    for source, repo, upstream_path, destination in paths():
        if not destination.is_file():
            missing.append(str(destination.relative_to(ROOT)))
    refs_missing = []
    ref_pattern = re.compile(r"(?<![A-Za-z0-9])(?:\\.\\./)*references/vendor/[\\w/ .+%-]+\\.(?:md|py)")
    # Check module-declared local files, without attempting to validate every external upstream link.
    for module in sorted(MODULES.glob("*.md")):
        data = module.read_text(encoding="utf-8")
        for match in ref_pattern.finditer(data):
            candidate = match.group(0).strip(" \\t\\r\\n)\\`")
            target = (module.parent / candidate).resolve()
            if not target.is_file():
                refs_missing.append(f"{module.name}: {candidate}")
    print(f"Bundled files: {sum(1 for _ in paths())}, absent: {len(missing)}; broken module references: {len(refs_missing)}")
    for name in missing:
        print("MISSING:", name)
    for name in refs_missing:
        print("BROKEN MODULE REF:", name)
    return 1 if missing or refs_missing else 0


def sync(yes=False):
    if not yes:
        print("Refusing network update without --yes. Review upstream changes and licenses afterwards.")
        return 2
    errors = []
    updated = 0
    for source, repo, path, destination in paths():
        url = f"https://raw.githubusercontent.com/{repo}/main/" + "/".join(urllib.parse.quote(segment) for segment in path.split("/"))
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "act-skills-router-sync/1"})
            with urllib.request.urlopen(req, timeout=30) as response:
                content = response.read()
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
            updated += 1
            print(f"UPDATED {source}/{path}")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            errors.append(f"{source}/{path}: {exc}")
    print(f"Updated {updated} files; errors {len(errors)}")
    for error in errors:
        print("ERROR:", error)
    print("Review git diff and newly introduced relative references; this is a curated snapshot, not a full recursive mirror.")
    return 1 if errors else check()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check mirrored files and module references offline")
    parser.add_argument("--sync", action="store_true", help="download tracked upstream files from main")
    parser.add_argument("--yes", action="store_true", help="acknowledge that --sync overwrites tracked snapshots")
    args = parser.parse_args()
    if args.sync:
        return sync(args.yes)
    return check()


if __name__ == "__main__":
    sys.exit(main())
