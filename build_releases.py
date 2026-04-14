"""
build_releases.py — Package rootnode skills into upload-ready zips for GitHub Releases.

Usage:
    python build_releases.py          # Zip all skills
    python build_releases.py skill1 skill2  # Zip specific skills only

Output: dist/ folder containing one .zip per skill.
Each zip contains the skill folder as root, ready to upload directly to a Claude Project.
"""

import os
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent
DIST_DIR = REPO_ROOT / "dist"
SKILL_PREFIX = "rootnode-"


def find_skills(specific: list[str] | None = None) -> list[Path]:
    """Find skill folders in the repo root."""
    skills = sorted(
        p for p in REPO_ROOT.iterdir()
        if p.is_dir() and p.name.startswith(SKILL_PREFIX)
    )

    if specific:
        # Match by full name or suffix (e.g., "behavioral-tuning" matches "rootnode-behavioral-tuning")
        filtered = []
        for name in specific:
            normalized = name if name.startswith(SKILL_PREFIX) else f"{SKILL_PREFIX}{name}"
            match = next((s for s in skills if s.name == normalized), None)
            if match:
                filtered.append(match)
            else:
                print(f"  SKIP: '{name}' not found")
        return filtered

    return skills


def zip_skill(skill_path: Path, dist_dir: Path) -> Path:
    """Zip a single skill folder. Returns the zip path."""
    zip_name = f"{skill_path.name}.zip"
    zip_path = dist_dir / zip_name

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(skill_path.rglob("*")):
            if file.is_file():
                arcname = file.relative_to(skill_path)
                zf.write(file, arcname)

    return zip_path


def main():
    specific = sys.argv[1:] if len(sys.argv) > 1 else None

    skills = find_skills(specific)
    if not skills:
        print("No skills found.")
        return

    DIST_DIR.mkdir(exist_ok=True)

    print(f"Building {len(skills)} skill package(s) → dist/\n")

    for skill in skills:
        zip_path = zip_skill(skill, DIST_DIR)
        size_kb = zip_path.stat().st_size / 1024
        print(f"  ✓ {zip_path.name} ({size_kb:.1f} KB)")

    print(f"\nDone. {len(skills)} packages in dist/")


if __name__ == "__main__":
    main()
