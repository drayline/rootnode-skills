#!/bin/bash
# verify-tests.sh — Stop guard; fails closed; bounded.
[ "${VERIFY_GATE_OFF:-0}" = "1" ] && exit 0          # off-switch; audit its use
EV=.claude/state/last-test-evidence.json; CT=.claude/state/verify-gate.count
MAX="${VERIFY_GATE_MAX_BLOCKS:-2}"; mkdir -p .claude/state   # N: 2 interactive, 8 unattended; keep N ≤ CLAUDE_CODE_STOP_HOOK_BLOCK_CAP (default 8)
HOST="${CLAUDE_CODE_STOP_HOOK_BLOCK_CAP:-8}"; [ "$MAX" -le "$HOST" ] 2>/dev/null || MAX=$HOST   # enforce N ≤ host cap
MAX_TOTAL="${VERIFY_GATE_MAX_TOTAL:-$((MAX * 3))}"           # M: 3×N [assumption — tune per repo]
INPUT=$(cat)                                                 # read stdin once
block() {  # $1 = on-task reason naming the next step
  KEY=$(sha256sum "$EV" 2>/dev/null | cut -c1-16); KEY=${KEY:-none}
  LAST=""; N=0; TOTAL=0; [ -f "$CT" ] && read -r LAST N TOTAL < "$CT"
  if [ "$LAST" = "$KEY" ]; then N=$((N + 1)); else N=1; fi
  TOTAL=$((${TOTAL:-0} + 1))
  echo "$KEY $N $TOTAL" > "$CT"; echo "$(date -u +%FT%TZ) block $KEY $N $TOTAL" >> .claude/state/verify-gate.log
  if [ "$N" -gt "$MAX" ] || [ "$TOTAL" -gt "$MAX_TOTAL" ]; then   # bound 2: release, logged
    echo "$(date -u +%FT%TZ) release $KEY $N $TOTAL" >> .claude/state/verify-gate.log; exit 0
  fi
  echo "$1" >&2; exit 2
}
ACTIVE=true                                          # bound 1: no jq or unreadable input = continuation
command -v jq >/dev/null && ACTIVE=$(printf '%s' "$INPUT" | jq -r '.stop_hook_active // false' 2>/dev/null || echo true)
[ "$ACTIVE" = "true" ] || rm -f "$CT"                # a new stop chain resets the counter
command -v jq >/dev/null || block "jq not found — evidence not evaluated; caps still apply"
[ -f "$EV" ] || block "Next step: run the test suite and record the result to $EV."
AGE=$(($(date +%s) - $(stat -c %Y "$EV" 2>/dev/null || stat -f %m "$EV")))
[ "$AGE" -le 300 ] || block "Next step: re-run the test suite; the evidence is over 5 minutes old."
[ "$(jq -r '.pass' "$EV")" = "true" ] || block "Next step: fix the failures recorded in $EV and re-run the suite."
rm -f "$CT"; exit 0
