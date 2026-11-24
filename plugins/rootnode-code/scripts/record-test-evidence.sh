#!/bin/bash
# record-test-evidence.sh <repo root> <evidence path> — runs verify.command from .claude/rootnode-gates.json at the
# repository root and records the result for the current tree. The verify gate's block message prints this command
# with both paths filled in. Exits with the test command's exit code; 64 on a usage error, with nothing written.
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/gate-lib.sh" 2>/dev/null || { echo "rootnode-code: gate-lib.sh not found; nothing recorded" >&2; exit 0; }
usage() { echo "usage: record-test-evidence.sh <repo root> <evidence path> ($1); nothing recorded" >&2; exit 64; }
[ $# -eq 2 ] && [ -n "$1" ] && [ -n "$2" ] || usage "two arguments required"
command -v jq >/dev/null || usage "jq not found"
ROOT=$(gate_root "$1"); [ -n "$ROOT" ] || usage "$1 is not a git working copy"
CFG="$ROOT/$GATE_CONFIG"; [ -f "$CFG" ] || usage "$CFG not found"
CMD=$(gate_jq '.verify.command // empty | strings' "$CFG") || usage "$CFG is not valid JSON"
[ -n "$CMD" ] || usage "$CFG has no verify.command"
OUTF=${2//'\'//}; STATE=$(gate_state_dir); KEY=none; gate_evidence    # EV_REL and EV_FIELD come from the config
(cd "$ROOT" && bash -c "$CMD"); RC=$?
FP=$(gate_fingerprint "$ROOT" "$EV_REL")             # after the run, so files the tests rewrite are included
[ -n "$FP" ] || { echo "rootnode-code: cannot fingerprint $ROOT; nothing recorded" >&2; exit 70; }
PASS=false; [ "$RC" = 0 ] && PASS=true
mkdir -p "$(dirname "$OUTF")" &&
  jq -n --argjson pass "$PASS" --argjson exit "$RC" --arg command "$CMD" --arg fingerprint "$FP" \
    --arg at "$(date -u +%FT%TZ)" --arg f "$EV_FIELD" \
    '{pass: $pass, exit: $exit, command: $command, fingerprint: $fingerprint, at: $at} + {($f): $pass}' \
    > "$OUTF.tmp.$$" && mv -f "$OUTF.tmp.$$" "$OUTF" ||
  { rm -f "$OUTF.tmp.$$"; echo "rootnode-code: cannot write $OUTF; nothing recorded" >&2; exit 70; }
echo "rootnode-code: recorded pass=$PASS (exit $RC) for $ROOT in $OUTF" >&2
exit "$RC"
