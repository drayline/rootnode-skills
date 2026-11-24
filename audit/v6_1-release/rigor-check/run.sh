#!/bin/bash
# run.sh — runs one rigor-check brief through a child `claude -p` (spec §7.8, behavioral check for cc-design).
# Usage: bash run.sh <brief file> <plugin dir or zip> <label> <out dir>
# The child starts in a fresh temp folder outside any repository, with the plugin loaded by --plugin-dir,
# the brief on stdin, a spend cap, no subagent nesting, no CLAUDE.md files, and only project/local settings
# (so the account's synced plugins do not load beside the plugin under test). Writes <label>.jsonl (stream),
# <label>.md (the final result text) and <label>.meta (plugin source and version, whether
# rootnode-code:cc-design was listed, whether the Skill was invoked, cost, result subtype).
set -u
BRIEF=$(cd "$(dirname "$1")" && pwd)/$(basename "$1"); PLUGIN=$2; LABEL=$3; OUT=$(mkdir -p "$4" && cd "$4" && pwd)
WORK=$(mktemp -d "${TMPDIR:-/tmp}/rn-rigor.XXXXXX") || exit 2
cd "$WORK" || exit 2
git rev-parse --show-toplevel >/dev/null 2>&1 && { echo "run.sh: $WORK is inside a repository" >&2; exit 2; }
CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=0 CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 \
  claude -p --setting-sources project,local --plugin-dir "$PLUGIN" --model "${MODEL:-claude-opus-5-5}" \
  --max-budget-usd "${BUDGET:-4}" --output-format stream-json --verbose < "$BRIEF" > "$OUT/$LABEL.jsonl" 2> "$OUT/$LABEL.err"
echo "exit=$?" >> "$OUT/$LABEL.err"
py -3 -I - "$OUT/$LABEL.jsonl" "$OUT/$LABEL.md" "$OUT/$LABEL.meta" <<'PY'
import json, sys
src, md, meta = sys.argv[1:4]
init, result, skill_calls = None, None, []
for line in open(src, encoding="utf-8"):
    try: d = json.loads(line)
    except ValueError: continue
    if d.get("type") == "system" and d.get("subtype") == "init": init = d
    if d.get("type") == "assistant":
        for c in d.get("message", {}).get("content", []):
            if c.get("type") == "tool_use" and c.get("name") == "Skill":
                skill_calls.append(c.get("input", {}).get("skill"))
    if d.get("type") == "result": result = d
open(md, "w", encoding="utf-8", newline="\n").write((result or {}).get("result") or "")
rc = [p for p in (init or {}).get("plugins", []) if p.get("name") == "rootnode-code"]
lines = [
  "plugin=" + ";".join(f"{p.get('source')} {p.get('version')}" for p in rc),
  "cc_design_listed=" + str("rootnode-code:cc-design" in (init or {}).get("skills", [])),
  "skill_calls=" + ",".join(str(s) for s in skill_calls),
  "model=" + str((init or {}).get("model")),
  "claude_code_version=" + str((init or {}).get("claude_code_version")),
  "result_subtype=" + str((result or {}).get("subtype")),
  "cost_usd=" + str((result or {}).get("total_cost_usd")),
  "num_turns=" + str((result or {}).get("num_turns")),
]
open(meta, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print("\n".join(lines))
PY
rm -rf "$WORK"
