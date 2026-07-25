#!/usr/bin/env python3
"""generate_release_notes.py — Version-agnostic release-notes generator for the
rootnode Skills catalog.

Authored during the v4.0 alignment cycle (D7 expansion) as a v-agnostic
successor to `audit/v3_1-release/generate_release_notes.py`. That v3.1 artifact
hardcoded the version throughout and its TIER_LABEL dict carried
"Opus-recommended (T3)" — the exact label the v4.0 D2 decision retired — so it
could not be used unmodified for v4.0. Rather than duplicate the pattern with
another version-hardcoded artifact per cycle, this repo-root tool takes version
and tier labels as parameters and drives skill data from a per-cycle config
file. Each release cycle authors its own config; the generator stays stable.

Usage:
    python generate_release_notes.py --config path/to/config.py

Or, with an output-directory override (useful for dry-runs):
    python generate_release_notes.py --config <path> --out-dir /tmp/notes-dryrun

Config file must define (as module-level names):
    VERSION           — string, e.g. "4.0" (used in filenames as "-v{VERSION}.md"
                        and in the "### v{VERSION} Catalog Release" header)
    TIER_LABEL        — dict mapping "T1"/"T2"/"T3" to display strings, e.g.
                        {"T1": "Model-compatible (T1)", ...}
    CATALOG_RELEASE   — string, the shared blurb appearing under the
                        "### v{VERSION} Catalog Release" header
    VARIANT_A         — list of (name, tier, description) tuples for CP-only
                        Skills (flat `-cp.zip` install)
    VARIANT_B         — list of (name, tier, description) tuples for CC-only
                        Skills (wrapper `-cc.zip` install)
    VARIANT_C         — list of (name, tier, description) tuples for dual-surface
                        Skills (both `-cp.zip` and `-cc.zip`)
    EXPECTED_COUNTS   — dict {"A": <int>, "B": <int>, "C": <int>, "total": <int>}
                        for the count-assertion gate

Output:
    One file per Skill at <out-dir>/<skill-name>-v<VERSION>.md
    Default <out-dir>: <repo-root>/release-notes/

Non-zero exit if any expected count is unmet.
"""

import argparse
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent


def load_config(config_path: Path):
    """Load a Python config module by path."""
    if not config_path.exists():
        print(f"ERROR: config file not found: {config_path}", file=sys.stderr)
        sys.exit(2)
    spec = importlib.util.spec_from_file_location("release_notes_config", str(config_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    required = ["VERSION", "TIER_LABEL", "CATALOG_RELEASE",
                "VARIANT_A", "VARIANT_B", "VARIANT_C", "EXPECTED_COUNTS"]
    missing = [name for name in required if not hasattr(mod, name)]
    if missing:
        print(f"ERROR: config missing required names: {', '.join(missing)}", file=sys.stderr)
        sys.exit(2)
    return mod


def variant_a_body(name, tier, desc, tier_label, catalog_release, version):
    """Chat-Project (CP-only) — flat -cp.zip install."""
    return f"""{desc}

**Surface:** Chat-Project • **Tier:** {tier_label[tier]}

### Install

Download `{name}-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

### v{version} Catalog Release

{catalog_release}
"""


def variant_b_body(name, tier, desc, tier_label, catalog_release, version):
    """Claude Code (CC-only) — wrapper -cc.zip install."""
    return f"""{desc}

**Surface:** Claude Code • **Tier:** {tier_label[tier]}

### Install

Download `{name}-cc.zip` below, extract it into `~/.claude/skills/` (user-level — available across every repo) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v{version} Catalog Release

{catalog_release}
"""


def variant_c_body(name, tier, desc, tier_label, catalog_release, version):
    """Dual-surface — both -cp.zip and -cc.zip."""
    return f"""{desc}

**Surface:** Chat-Project + Claude Code • **Tier:** {tier_label[tier]}

### Install

**Chat-Project:** Download `{name}-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

**Claude Code:** Download `{name}-cc.zip` below, extract it into `~/.claude/skills/` (user-level) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v{version} Catalog Release

{catalog_release}
"""


def main():
    parser = argparse.ArgumentParser(
        description="Generate per-Skill release notes from a per-cycle config file."
    )
    parser.add_argument("--config", required=True, type=Path,
                        help="Path to Python config file (see docstring)")
    parser.add_argument("--out-dir", type=Path, default=None,
                        help="Output directory (default: <repo-root>/release-notes/)")
    args = parser.parse_args()

    config = load_config(args.config)
    out_dir = args.out_dir if args.out_dir else (REPO_ROOT / "release-notes")
    out_dir.mkdir(parents=True, exist_ok=True)

    counts = {"A": 0, "B": 0, "C": 0}

    for (name, tier, desc) in config.VARIANT_A:
        body = variant_a_body(name, tier, desc, config.TIER_LABEL,
                              config.CATALOG_RELEASE, config.VERSION)
        (out_dir / f"{name}-v{config.VERSION}.md").write_text(body, encoding="utf-8")
        counts["A"] += 1

    for (name, tier, desc) in config.VARIANT_B:
        body = variant_b_body(name, tier, desc, config.TIER_LABEL,
                              config.CATALOG_RELEASE, config.VERSION)
        (out_dir / f"{name}-v{config.VERSION}.md").write_text(body, encoding="utf-8")
        counts["B"] += 1

    for (name, tier, desc) in config.VARIANT_C:
        body = variant_c_body(name, tier, desc, config.TIER_LABEL,
                              config.CATALOG_RELEASE, config.VERSION)
        (out_dir / f"{name}-v{config.VERSION}.md").write_text(body, encoding="utf-8")
        counts["C"] += 1

    total = sum(counts.values())
    print(f"Wrote to {out_dir}:")
    print(f"  Variant A (CP-only) = {counts['A']}")
    print(f"  Variant B (CC-only) = {counts['B']}")
    print(f"  Variant C (dual)    = {counts['C']}")
    print(f"  total               = {total}")

    expected = config.EXPECTED_COUNTS
    problems = []
    if counts["A"] != expected["A"]:
        problems.append(f"Variant A expected {expected['A']}, got {counts['A']}")
    if counts["B"] != expected["B"]:
        problems.append(f"Variant B expected {expected['B']}, got {counts['B']}")
    if counts["C"] != expected["C"]:
        problems.append(f"Variant C expected {expected['C']}, got {counts['C']}")
    if total != expected["total"]:
        problems.append(f"Total expected {expected['total']}, got {total}")

    if problems:
        print("FAIL: " + "; ".join(problems), file=sys.stderr)
        sys.exit(1)

    print("Counts OK")


if __name__ == "__main__":
    main()
