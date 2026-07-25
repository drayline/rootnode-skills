#!/usr/bin/env python3
"""
build_release_artifacts.py — Build the surface-mapped, suffixed release artifacts
for the rootnode-skills catalog.

This is the single release-packaging entry point. It supersedes the manual
two-script dance (build_releases.py for flat + package_skill.py for wrapper),
producing every release zip with the correct shape, surface suffix, and naming.

For each (Skill, surface) it writes one zip into dist/:
  - CP surface -> FLAT zip    (contents at zip root)              -> rootnode-<skill>-cp.zip
  - CC surface -> WRAPPER zip (nested rootnode-<skill>/ folder)   -> rootnode-<skill>-cc.zip

Why the two shapes:
  - CP (Claude.ai Projects) Skill upload reads SKILL.md at the zip ROOT -> flat.
  - CC keeps each Skill as a folder at ~/.claude/skills/rootnode-<skill>/.
    The wrapper zip contains that folder, so extraction yields the ready-named
    folder to drop in. A flat CC zip would extract loose files -> broken install.

Surface map (THE single place to edit if catalog surface assignments change):
  CC_ONLY : ships -cc only
  DUAL    : ships both -cp and -cc
  (every other rootnode-* folder ships -cp only)

Full-build expectation: 22 cp-only + 3 cc-only + (2 dual x 2) = 29 artifacts
                        = 24 '-cp' (flat) + 5 '-cc' (wrapper).

On a full build it also writes dist/rootnode-catalog-<VERSION>.zip: a single
bundle of all 29 zips. Upload it to the catalog umbrella release so users can
grab the whole catalog in one download. (Per-Skill releases still carry the
individual zips; the bundle is the "give me everything" path.) The bundle is
written only on a full build, never on a specific-skill subset.

Usage:
    python build_release_artifacts.py             # all skills (asserts 29)
    python build_release_artifacts.py skill ...   # specific skills (by suffix or full name)
"""

import fnmatch
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
DIST_DIR = REPO_ROOT / "dist"
SKILL_PREFIX = "rootnode-"

# --- Surface map: names are the part AFTER the rootnode- prefix ----------------
CC_ONLY = {"critic-gate", "mode-router", "repo-hygiene"}
DUAL = {"skill-builder", "cc-design"}
# Everything else under rootnode-* is CP-only.

EXPECTED_TOTAL = 29
EXPECTED_CP = 24
EXPECTED_CC = 5

# Names the all-Skills bundle written on full builds (uploaded to the
# catalog-<ver> umbrella release). Bump this per catalog release.
CATALOG_VERSION = "v4.0"

# --- Exclusions (ported from package_skill.py) ---------------------------------
EXCLUDE_DIRS = {"__pycache__", "node_modules"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_FILES = {".DS_Store"}
ROOT_EXCLUDE_DIRS = {"evals"}  # excluded only at the skill root, not when nested deeper


def should_exclude(rel_to_parent: Path) -> bool:
    """rel_to_parent is relative to skill_path.parent: parts[0] = skill folder,
    parts[1] = first subdir."""
    parts = rel_to_parent.parts
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    if len(parts) > 1 and parts[1] in ROOT_EXCLUDE_DIRS:
        return True
    if rel_to_parent.name in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(rel_to_parent.name, pat) for pat in EXCLUDE_GLOBS)


def surfaces_for(short_name: str) -> list[str]:
    if short_name in CC_ONLY:
        return ["cc"]
    if short_name in DUAL:
        return ["cp", "cc"]
    return ["cp"]


def write_zip(skill_path: Path, surface: str) -> Path:
    zip_path = DIST_DIR / f"{skill_path.name}-{surface}.zip"
    # FLAT (cp):   anchor = skill folder  -> arcnames are contents at zip root.
    # WRAPPER (cc): anchor = parent        -> arcnames are nested under rootnode-<skill>/.
    anchor = skill_path if surface == "cp" else skill_path.parent
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(skill_path.rglob("*")):
            if not f.is_file():
                continue
            if should_exclude(f.relative_to(skill_path.parent)):
                continue
            zf.write(f, f.relative_to(anchor).as_posix())
    return zip_path


def write_bundle(zip_paths: list[Path]) -> Path:
    """Bundle every per-Skill zip into one archive for the catalog release, so a
    user can download the whole catalog in a single file. Each inner zip sits at
    the bundle root and remains the installable unit (unzip the bundle -> 29 zips
    -> upload/install the ones you want)."""
    bundle = DIST_DIR / f"rootnode-catalog-{CATALOG_VERSION}.zip"
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as zf:
        for z in sorted(zip_paths):
            zf.write(z, z.name)
    return bundle


def find_skills(specific):
    skills = sorted(
        p for p in REPO_ROOT.iterdir()
        if p.is_dir() and p.name.startswith(SKILL_PREFIX)
    )
    if not specific:
        return skills
    out = []
    for name in specific:
        norm = name if name.startswith(SKILL_PREFIX) else SKILL_PREFIX + name
        match = next((s for s in skills if s.name == norm), None)
        if match:
            out.append(match)
        else:
            print(f"  SKIP: '{name}' not found")
    return out


def main():
    specific = sys.argv[1:] or None
    skills = find_skills(specific)
    if not skills:
        print("No skills found.")
        sys.exit(1)

    DIST_DIR.mkdir(exist_ok=True)
    cp_n = cc_n = 0
    built: list[Path] = []
    print(f"Building release artifacts for {len(skills)} skill(s) -> dist/\n")
    for skill in skills:
        short = skill.name[len(SKILL_PREFIX):]
        for surface in surfaces_for(short):
            z = write_zip(skill, surface)
            built.append(z)
            kb = z.stat().st_size / 1024
            shape = "flat" if surface == "cp" else "wrapper"
            print(f"  [OK] {z.name}  ({shape}, {kb:.1f} KB)")
            if surface == "cp":
                cp_n += 1
            else:
                cc_n += 1

    total = cp_n + cc_n
    print(f"\n{total} artifacts: {cp_n} -cp (flat) + {cc_n} -cc (wrapper)")

    if not specific:
        problems = []
        if total != EXPECTED_TOTAL:
            problems.append(f"total {total} != {EXPECTED_TOTAL}")
        if cp_n != EXPECTED_CP:
            problems.append(f"-cp {cp_n} != {EXPECTED_CP}")
        if cc_n != EXPECTED_CC:
            problems.append(f"-cc {cc_n} != {EXPECTED_CC}")
        if problems:
            print("  FAIL (full build): " + "; ".join(problems)
                  + ". Check the surface map / catalog count.")
            sys.exit(2)
        bundle = write_bundle(built)
        mb = bundle.stat().st_size / (1024 * 1024)
        print(f"\nBundle: {bundle.name}  ({len(built)} zips, {mb:.2f} MB)"
              f"  -> upload to the catalog-{CATALOG_VERSION} release")
    print("Done.")


if __name__ == "__main__":
    main()
