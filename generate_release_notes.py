#!/usr/bin/env python3
"""generate_release_notes.py — Per-plugin release-notes generator for the
rootnode plugin marketplace.

Rewritten for the v6.0 plugin model. Through v5.0.1 this tool wrote one note
per Skill from VARIANT_A/B/C lists (the -cp flat and -cc wrapper zips); those
shapes retired at v6.0 and the per-cycle configs under audit/ that drove them
stay as history. The generator now writes one note per plugin. Each cycle
authors its own config; the generator stays stable.

Usage:
    python generate_release_notes.py --config path/to/config.py

Or, with an output-directory override (useful for dry-runs):
    python generate_release_notes.py --config <path> --out-dir <dir>

Config file must define (as module-level names):
    CATALOG_RELEASE   — string, the umbrella tag, e.g. "catalog-v6.0"; the
                        note links to releases/tag/<CATALOG_RELEASE> and names
                        it "root.node catalog v6.0"
    PLUGINS           — list of dicts, one per plugin, each with:
                          name     — plugin name, e.g. "rootnode-projects"
                          version  — must equal the plugin's plugin.json version
                          summary  — one line, printed in the run log
                          changes  — list of change bullets (strings, no "- ")
    EXPECTED_COUNT    — int, the number of notes the run must write

Read from the repo, not the config:
    plugins/<name>/.claude-plugin/plugin.json — displayName, version, description
    plugins/<name>/skills/*/SKILL.md          — name, metadata.version and
                                                metadata.predecessor
                                                ("rootnode-<name> v<prior>")

Output:
    One file per plugin at <out-dir>/<plugin>-v<version>.md
    Default <out-dir>: <repo-root>/release-notes/

Exit codes: 2 for a config or repo-data error, 1 for a count mismatch.
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
PLUGINS_DIR = REPO_ROOT / "plugins"
REPO_URL = "https://github.com/drayline/rootnode-skills"

PREDECESSOR = re.compile(r"^rootnode-(?P<name>[a-z0-9-]+) v(?P<prior>\d+\.\d+(?:\.\d+)?)$")

TEMPLATE = """# {display} v{version}

{description}

Part of [root.node catalog {catalog_label}]({repo}/releases/tag/{catalog_tag}).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `{plugin}`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install {plugin}@rootnode`.
- **Manual:** upload `{plugin}-v{version}.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
{skill_rows}

## Changes in v{version}

{change_bullets}

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
"""


def fail(msg: str, code: int = 2):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def load_config(config_path: Path):
    """Load a Python config module by path."""
    if not config_path.exists():
        fail(f"config file not found: {config_path}")
    spec = importlib.util.spec_from_file_location("release_notes_config", str(config_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    required = ["CATALOG_RELEASE", "PLUGINS", "EXPECTED_COUNT"]
    missing = [name for name in required if not hasattr(mod, name)]
    if missing:
        fail(f"config missing required names: {', '.join(missing)}")
    for i, p in enumerate(mod.PLUGINS):
        absent = [k for k in ("name", "version", "summary", "changes") if k not in p]
        if absent:
            fail(f"PLUGINS[{i}] missing {', '.join(absent)}")
        if not p["changes"]:
            fail(f"PLUGINS[{i}] ({p['name']}) has no change bullets")
    return mod


def read_manifest(plugin: str) -> dict:
    path = PLUGINS_DIR / plugin / ".claude-plugin" / "plugin.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        fail(f"cannot read {path}: {exc}")
    for key in ("name", "displayName", "version", "description"):
        if not manifest.get(key):
            fail(f"{path} has no {key}")
    if manifest["name"] != plugin:
        fail(f"{path} name {manifest['name']!r} != {plugin!r}")
    return manifest


def read_frontmatter(skill_md: Path) -> dict:
    """Top-level name plus metadata.version and metadata.predecessor. A line
    reader, not a YAML parser: these three keys are single-line scalars."""
    text = skill_md.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        fail(f"{skill_md} has no frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        fail(f"{skill_md} frontmatter is not closed")
    out, in_meta = {}, False
    for line in text[4:end].split("\n"):
        if line and not line[0].isspace():
            in_meta = line.startswith("metadata:")
            if line.startswith("name:"):
                out["name"] = line.split(":", 1)[1].strip().strip('"')
        elif in_meta:
            m = re.match(r'^\s+(version|predecessor):\s*"?([^"]*)"?\s*$', line)
            if m:
                out[m.group(1)] = m.group(2)
    for key in ("name", "version", "predecessor"):
        if key not in out:
            fail(f"{skill_md} frontmatter has no {key}")
    return out


def skill_rows(plugin: str) -> list:
    rows = []
    for skill_md in sorted((PLUGINS_DIR / plugin / "skills").glob("*/SKILL.md")):
        fm = read_frontmatter(skill_md)
        if fm["name"] != skill_md.parent.name:
            fail(f"{skill_md} name {fm['name']!r} != folder {skill_md.parent.name!r}")
        m = PREDECESSOR.match(fm["predecessor"])
        if not m or m.group("name") != fm["name"]:
            fail(f"{skill_md} predecessor {fm['predecessor']!r} is not 'rootnode-{fm['name']} v<prior>'")
        rows.append(f"| `{plugin}:{fm['name']}` | `rootnode-{fm['name']}` v{m.group('prior')} | {fm['version']} |")
    if not rows:
        fail(f"plugin {plugin} has no skills/*/SKILL.md")
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Generate per-plugin release notes from a per-cycle config file."
    )
    parser.add_argument("--config", required=True, type=Path,
                        help="Path to Python config file (see docstring)")
    parser.add_argument("--out-dir", type=Path, default=None,
                        help="Output directory (default: <repo-root>/release-notes/)")
    args = parser.parse_args()

    config = load_config(args.config)
    out_dir = args.out_dir if args.out_dir else (REPO_ROOT / "release-notes")
    out_dir.mkdir(parents=True, exist_ok=True)
    catalog_tag = config.CATALOG_RELEASE
    if not catalog_tag.startswith("catalog-v"):
        fail(f"CATALOG_RELEASE {catalog_tag!r} does not start with 'catalog-v'")
    catalog_label = catalog_tag[len("catalog-"):]

    written = []
    for p in config.PLUGINS:
        manifest = read_manifest(p["name"])
        if manifest["version"] != p["version"]:
            fail(f"{p['name']}: config version {p['version']} != plugin.json {manifest['version']}")
        rows = skill_rows(p["name"])
        body = TEMPLATE.format(
            display=manifest["displayName"], version=manifest["version"],
            description=manifest["description"], catalog_label=catalog_label,
            repo=REPO_URL, catalog_tag=catalog_tag, plugin=p["name"],
            skill_rows="\n".join(rows),
            change_bullets="\n".join(f"- {c}" for c in p["changes"]),
        )
        path = out_dir / f"{p['name']}-v{manifest['version']}.md"
        path.write_text(body, encoding="utf-8", newline="\n")
        written.append(path)
        noun = "Skill" if len(rows) == 1 else "Skills"
        print(f"  {path.name}: {len(rows)} {noun} - {p['summary']}")

    print(f"Wrote {len(written)} notes to {out_dir}")
    if len(written) != config.EXPECTED_COUNT:
        print(f"FAIL: expected {config.EXPECTED_COUNT} notes, wrote {len(written)}", file=sys.stderr)
        sys.exit(1)
    print("Count OK")


if __name__ == "__main__":
    main()
