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

Full-build expectation: 6 plugins -> 6 zips. A full build first deletes every
dist/*.zip so a stale zip from an earlier layout or version cannot sit beside
the new ones; a partial build deletes nothing.

Every build first checks embedded copies: a Skill reference that marks a
fenced block with <!-- shipped: <repo path> --> must carry that file in the
next fenced block, equal after LF normalization (one trailing newline is
ignored). A mismatch stops the build with exit 2 before any zip is written.

Usage:
    python build_release_artifacts.py              # all plugins (asserts 6)
    python build_release_artifacts.py plugin ...   # specific plugins (by suffix or full name)
"""

import fnmatch
import json
import re
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

# --- Embedded copies -------------------------------------------------------------
SHIPPED_MARKER = re.compile(r"<!--\s*shipped:\s*(\S+)\s*-->")
FENCE_OPEN = re.compile(r"^(`{3,}|~{3,})")


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


def _lf(text: str) -> str:
    text = text.replace("\r\n", "\n")
    return text[:-1] if text.endswith("\n") else text


def _next_fenced_block(lines, start):
    """Body of the first fenced block at or after lines[start], or None."""
    for i in range(start, len(lines)):
        m = FENCE_OPEN.match(lines[i])
        if not m:
            continue
        fence = m.group(1)
        for j in range(i + 1, len(lines)):
            s = lines[j].rstrip()
            if s and set(s) == {fence[0]} and len(s) >= len(fence):
                return "\n".join(lines[i + 1:j])
        return None  # opened but never closed
    return None


def check_embedded_copies() -> int:
    """Compare each <!-- shipped: path --> block with the file it names.
    Returns the number of markers checked; exits 2 on the first mismatch."""
    checked = 0
    for ref in sorted(PLUGINS_DIR.glob("*/skills/*/references/**/*")):
        if not ref.is_file():
            continue
        try:
            lines = _lf(ref.read_text(encoding="utf-8")).split("\n")
        except (OSError, UnicodeDecodeError):
            continue  # not a text reference; nothing to check
        for n, line in enumerate(lines):
            m = SHIPPED_MARKER.search(line)
            if not m:
                continue
            rel_ref = ref.relative_to(REPO_ROOT).as_posix()
            shipped_rel = m.group(1)
            shipped = REPO_ROOT / shipped_rel
            block = _next_fenced_block(lines, n + 1)
            if block is None:
                print(f"  FAIL: {rel_ref}:{n + 1}: marker for {shipped_rel} "
                      "has no closed fenced block after it")
                sys.exit(2)
            try:
                want = _lf(shipped.read_bytes().decode("utf-8"))
            except (OSError, UnicodeDecodeError) as exc:
                print(f"  FAIL: {rel_ref}:{n + 1}: cannot read shipped file "
                      f"{shipped_rel}: {exc}")
                sys.exit(2)
            if block != want:
                got_l, want_l = block.split("\n"), want.split("\n")
                k = next((i for i, (a, b) in enumerate(zip(got_l, want_l)) if a != b),
                         min(len(got_l), len(want_l)))
                got_s = got_l[k] if k < len(got_l) else "<end of block>"
                want_s = want_l[k] if k < len(want_l) else "<end of file>"
                print(f"  FAIL: embedded copy differs from the shipped file\n"
                      f"    reference: {rel_ref}\n"
                      f"    shipped:   {shipped_rel}\n"
                      f"    first differing line {k + 1}:\n"
                      f"      reference: {got_s}\n"
                      f"      shipped:   {want_s}")
                sys.exit(2)
            checked += 1
    return checked


def clear_stale_zips() -> int:
    """Full build only: remove every dist/*.zip before writing new ones."""
    removed = 0
    for z in sorted(DIST_DIR.glob("*.zip")):
        try:
            z.unlink()
        except OSError as exc:
            print(f"  FAIL: cannot delete stale {z.name}: {exc}")
            sys.exit(1)
        removed += 1
    return removed


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

    print(f"Embedded copies checked: {check_embedded_copies()}")
    DIST_DIR.mkdir(exist_ok=True)
    if not specific:
        print(f"Stale zips deleted from dist/: {clear_stale_zips()}")
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
