#!/bin/bash
# verify-tests.sh — Stop gate. Acts only in a repository whose .claude/rootnode-gates.json has a "verify" section,
# only when the tree changed in this session, and only without passing evidence for the current tree.
# Watch mode (the default) logs would-be blocks and never blocks; enforce mode blocks, bounded by two caps.
[ "${VERIFY_GATE_OFF:-0}" = "1" ] && exit 0          # 1. off-switch; audit its use
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/gate-lib.sh" 2>/dev/null || { echo "rootnode-code: gate-lib.sh not found; verify gate inactive" >&2; exit 0; }
IN=$(cat)                                            # 2. read stdin once
gate_verify_setup "$IN" || exit 0                    # 2–7: inactive, or the baseline was just taken
[ "$(gate_input "$IN" .stop_hook_active)" = true ] || rm -f "$SD/chain"   # 11. a new stop chain resets the chain count
[ "$FP" = "$(cat "$SD/baseline" 2>/dev/null)" ] && exit 0                 # 8. unchanged since the baseline
REASON=no-evidence                                   # 9. evidence bound to the current fingerprint
if [ -f "$EV" ]; then
  REASON=$(gate_jq --arg fp "$FP" --arg f "$EV_FIELD" \
    'if .fingerprint != $fp then "stale-evidence" elif .[$f] == true then "ok" else "failing" end' "$EV")
  case "$REASON" in ok|failing|stale-evidence) ;; *) REASON=stale-evidence ;; esac
fi
[ "$REASON" = ok ] && { rm -f "$SD/chain"; exit 0; }
int() { case "$1" in ''|*[!0-9]*) echo "$2" ;; *) echo "$1" ;; esac; }   # 10. a would-be block
NC=$(int "$(cat "$SD/chain" 2>/dev/null)" 0); NT=$(int "$(cat "$SD/total" 2>/dev/null)" 0)
if [ "$(gate_jq '.verify.mode // "watch"' "$CFG")" != enforce ]; then
  gate_log verify would-block "$ROOT" "$REASON" "chain=$NC" "session=$NT"; exit 0
fi
HOST=$(int "${CLAUDE_CODE_STOP_HOOK_BLOCK_CAP:-}" 8)
MAXC=$(int "$(gate_jq '.verify.max_blocks_chain // empty' "$CFG")" 2); [ "$MAXC" -le "$HOST" ] || MAXC=$HOST
MAXS=$(int "$(gate_jq '.verify.max_blocks_session // empty' "$CFG")" 4)
NC=$((NC + 1)); NT=$((NT + 1)); echo "$NC" > "$SD/chain"; echo "$NT" > "$SD/total"   # the session count never resets
if [ "$NC" -gt "$MAXC" ] || [ "$NT" -gt "$MAXS" ]; then
  gate_log verify release "$ROOT" "$REASON" "chain=$NC" "session=$NT"; exit 0
fi
gate_log verify block "$ROOT" "$REASON" "chain=$NC" "session=$NT"
echo "rootnode-code verify gate: $ROOT changed in this session and has no passing test evidence for the current tree ($REASON). Next step: run" >&2
echo "bash \"$HERE/record-test-evidence.sh\" \"$ROOT\" \"$EV\"" >&2
exit 2
