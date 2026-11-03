#!/usr/bin/env python3
"""
build_release_artifacts.py — Build the plugin release artifacts for the
rootnode-skills catalog.

This is the single release-packaging entry point. It writes one zip per plugin
directory under plugins/ into dist/, named from the plugin's own manifest:

  plugins/<plugin>/ -> dist/<plugin>-v<version>.zip

Each zip holds the plugin's contents at the zip root, with
.claude-plugin/plugin.json at the root as Upload plugin on claude.ai requires.
The plugin name already carries the rootnode- prefix.

Eval suites stay in the repo: evals/ is left out of the zip at the plugin root
and at each skill root. Shell scripts are stored as LF with mode 0755 so hooks
run on Linux and macOS no matter where the zip was built.

Full-build expectation: 6 plugins -> 6 zips.

Usage:
    python build_release_artifacts.py              # all plugins (asserts 6)
    python build_release_artifacts.py plugin ...   # specific plugins (by suffix or full name)
"""

import fnmatch
import json
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
PLUGINS_DIR = REPO_ROOT / "plugins"
DIST_DIR = REPO_ROOT / "dist"
PLUGIN_PREFIX = "rootnode-"
MANIFEST = ".claude-plugin/plugin.json"

EXPECTED_TOTAL = 6

# --- Exclusions ----------------------------------------------------------------
EXCLUDE_DIRS = {"__pycache__", "node_modules"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_FILES = {".DS_Store", ".gitattributes"}
ROOT_EXCLUDE_DIRS = {"evals"}  # excluded only at the plugin and skill roots


def should_exclude(rel_to_plugin: Path) -> bool:
    """rel_to_plugin is relative to the plugin folder: parts[0] = first subdir,
    and under skills/, parts[1] = skill folder and parts[2] = its first subdir."""
    parts = rel_to_plugin.parts
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    if parts[0] in ROOT_EXCLUDE_DIRS:
        return True
    if parts[0] == "skills" and len(parts) > 2 and parts[2] in ROOT_EXCLUDE_DIRS:
        return True
    if rel_to_plugin.name in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(rel_to_plugin.name, pat) for pat in EXCLUDE_GLOBS)


def read_version(plugin_path: Path) -> str:
    """The manifest is the source of truth for the zip name. A missing or
    malformed manifest stops the build rather than producing a misnamed zip."""
    manifest_path = plugin_path / MANIFEST
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"  FAIL: cannot read {manifest_path}: {exc}")
        sys.exit(1)
    if manifest.get("name") != plugin_path.name:
        print(f"  FAIL: {manifest_path} name {manifest.get('name')!r} "
              f"!= folder {plugin_path.name!r}")
        sys.exit(1)
    version = manifest.get("version")
    if not version:
        print(f"  FAIL: {manifest_path} has no version")
        sys.exit(1)
    return version


def write_zip(plugin_path: Path, version: str) -> Path:
    zip_path = DIST_DIR / f"{plugin_path.name}-v{version}.zip"
    # Built under a temporary name so a failed build cannot replace a good zip.
    tmp_path = zip_path.with_suffix(".zip.tmp")
    with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(plugin_path.rglob("*")):
            if not f.is_file():
                continue
            rel = f.relative_to(plugin_path)
            if should_exclude(rel):
                continue
            arcname = rel.as_posix()
            if f.suffix == ".sh":
                data = f.read_bytes()
                if b"\r" in data:
                    print(f"  FAIL: {arcname} has CRLF line endings; "
                          "it will not run on Linux or macOS")
                    sys.exit(1)
                info = zipfile.ZipInfo.from_file(f, arcname)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3  # Unix, so extractors honor the mode bits
                info.external_attr = 0o100755 << 16
                zf.writestr(info, data)
            else:
                zf.write(f, arcname)
    tmp_path.replace(zip_path)
    return zip_path


def manifest_at_root(zip_path: Path) -> bool:
    with zipfile.ZipFile(zip_path) as zf:
        return MANIFEST in zf.namelist()


def find_plugins(specific):
    if not PLUGINS_DIR.is_dir():
        return []
    plugins = sorted(p for p in PLUGINS_DIR.iterdir() if p.is_dir())
    if not specific:
        return plugins
    out = []
    for name in specific:
        norm = name if name.startswith(PLUGIN_PREFIX) else PLUGIN_PREFIX + name
        match = next((p for p in plugins if p.name == norm), None)
        if match:
            out.append(match)
        else:
            print(f"  SKIP: '{name}' not found")
    return out


def main():
    specific = sys.argv[1:] or None
    plugins = find_plugins(specific)
    if not plugins:
        print("No plugins found.")
        sys.exit(1)

    DIST_DIR.mkdir(exist_ok=True)
    built: list[Path] = []
    problems = []
    print(f"Building release artifacts for {len(plugins)} plugin(s) -> dist/\n")
    for plugin in plugins:
        z = write_zip(plugin, read_version(plugin))
        built.append(z)
        kb = z.stat().st_size / 1024
        print(f"  [OK] {z.name}  ({kb:.1f} KB)")
        if not manifest_at_root(z):
            problems.append(f"{z.name} has no {MANIFEST} at the zip root")

    total = len(built)
    print(f"\n{total} artifacts")

    if not specific and total != EXPECTED_TOTAL:
        problems.append(f"total {total} != {EXPECTED_TOTAL}")
    if problems:
        print("  FAIL: " + "; ".join(problems) + ". Check the plugins/ layout.")
        sys.exit(2)
    print("Done.")


if __name__ == "__main__":
    main()
