#!/usr/bin/env python3
"""Create the 27 v3.1 GitHub releases sequentially.

Each invocation = one `gh release create <skill>/v3.1` call with:
  --target main
  --title "<skill> v3.1"
  --notes-file release-notes/<skill>-v3.1.md
  <attached zip(s)>

Single-surface Skills attach one zip; the two dual-surface Skills attach
both -cp and -cc to a single release. On any non-zero exit, the script
stops immediately (no blast continuation) per the v3.1 session prompt's
halt rule for Phase B.8.
"""
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
RELEASE_NOTES = REPO_ROOT / "release-notes"
DIST = REPO_ROOT / "dist"

# 22 Variant-A (cp-only single-zip) Skills
CP_ONLY = [
    "rootnode-prompt-compilation",
    "rootnode-prompt-validation",
    "rootnode-project-audit",
    "rootnode-project-brief",
    "rootnode-anti-pattern-detection",
    "rootnode-behavioral-tuning",
    "rootnode-memory-optimization",
    "rootnode-context-budget",
    "rootnode-global-audit",
    "rootnode-full-stack-audit",
    "rootnode-session-handoff",
    "rootnode-handoff-trigger-check",
    "rootnode-profile-builder",
    "rootnode-identity-blocks",
    "rootnode-reasoning-blocks",
    "rootnode-output-blocks",
    "rootnode-block-selection",
    "rootnode-domain-software-engineering",
    "rootnode-domain-business-strategy",
    "rootnode-domain-content-communications",
    "rootnode-domain-research-analysis",
    "rootnode-domain-agentic-context",
]

# 3 Variant-B (cc-only single-zip) Skills
CC_ONLY = [
    "rootnode-critic-gate",
    "rootnode-mode-router",
    "rootnode-repo-hygiene",
]

# 2 Variant-C (dual-surface; attach both -cp and -cc) Skills
DUAL = [
    "rootnode-skill-builder",
    "rootnode-cc-design",
]


def assets_for(skill, variant):
    if variant == "A":
        return [DIST / f"{skill}-cp.zip"]
    if variant == "B":
        return [DIST / f"{skill}-cc.zip"]
    return [DIST / f"{skill}-cp.zip", DIST / f"{skill}-cc.zip"]


def create_release(skill, variant):
    notes = RELEASE_NOTES / f"{skill}-v3.1.md"
    assets = assets_for(skill, variant)
    for a in assets:
        if not a.is_file():
            raise FileNotFoundError(f"Missing zip: {a}")
    if not notes.is_file():
        raise FileNotFoundError(f"Missing notes: {notes}")
    tag = f"{skill}/v3.1"
    title = f"{skill} v3.1"
    cmd = [
        "gh", "release", "create", tag,
        "--target", "main",
        "--title", title,
        "--notes-file", str(notes),
    ] + [str(a) for a in assets]
    print(f"\n=== {tag} (variant {variant}, {len(assets)} asset(s)) ===")
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        print(r.stderr.strip(), file=sys.stderr)
        raise RuntimeError(f"gh release create failed for {tag} (exit {r.returncode})")


def main():
    queue = (
        [(s, "A") for s in CP_ONLY]
        + [(s, "B") for s in CC_ONLY]
        + [(s, "C") for s in DUAL]
    )
    total = len(queue)
    assert total == 27, f"queue total expected 27, got {total}"
    print(f"Creating {total} releases sequentially. Halt-on-first-failure active.")
    for i, (skill, variant) in enumerate(queue, 1):
        print(f"\n[{i}/{total}]", end=" ")
        create_release(skill, variant)
    print(f"\nAll {total} releases created.")


if __name__ == "__main__":
    main()
