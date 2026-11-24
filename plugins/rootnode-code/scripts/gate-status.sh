#!/bin/bash
# gate-status.sh [--state <dir>] [repo root] — per gate, the count of blocks, would-be blocks and releases, and the
# last five log lines, for every repository or one. Reads the state folder the hooks write: CLAUDE_PLUGIN_DATA, or
# --state with the plugin's data folder (or its gates folder).
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/gate-lib.sh" 2>/dev/null || { echo "rootnode-code: gate-lib.sh not found" >&2; exit 0; }
STATE=""; ONE=""
while [ $# -gt 0 ]; do
  case "$1" in
  --state) STATE=${2:-}; shift 2 2>/dev/null || shift ;;
  --state=*) STATE=${1#--state=}; shift ;;
  -h|--help) echo "usage: gate-status.sh [--state <dir>] [repo root]"; exit 0 ;;
  *) ONE=$1; shift ;;
  esac
done
STATE=${STATE//'\'//}
if [ -z "$STATE" ]; then STATE=$(gate_state_dir)
elif [ -f "$STATE/gates/gate.log" ] || [ ! -f "$STATE/gate.log" ]; then STATE="$STATE/gates"; fi
if [ -n "$ONE" ]; then R=$(gate_root "$ONE"); ONE=${R:-${ONE//'\'//}}; fi
echo "rootnode-code gate status"
echo "state: $STATE"
echo "repository: ${ONE:-all}"
if [ ! -f "$STATE/gate.log" ]; then
  echo "no gate activity recorded here."
  for d in "$HOME"/.claude/plugins/data/*/gates; do
    [ -f "$d/gate.log" ] && echo "log found: gate-status.sh --state \"$d\""
  done
  exit 0
fi
tr -d '\r' < "$STATE/gate.log" | awk -F'\t' -v one="$ONE" '
  one == "" || $4 == one {
    n[$2 SUBSEP $3]++; last[++k] = $0
  }
  END {
    printf "verify gate: block %d, would-block %d, release %d\n", n["verify" SUBSEP "block"], n["verify" SUBSEP "would-block"], n["verify" SUBSEP "release"]
    printf "migrations guard: block %d\n", n["guard" SUBSEP "block"]
    print "last " (k < 5 ? k : 5) " lines:"
    for (i = (k > 5 ? k - 4 : 1); i <= k; i++) print "  " last[i]
  }'
exit 0
