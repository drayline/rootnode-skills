#!/bin/bash
# gate-baseline.sh — SessionStart. Records the tree fingerprint the verify gate compares against, in a repository
# whose .claude/rootnode-gates.json has a "verify" section. Writes nothing else, prints nothing, always exits 0.
[ "${VERIFY_GATE_OFF:-0}" = "1" ] && exit 0          # off-switch, shared with the Stop gate
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/gate-lib.sh" 2>/dev/null || { echo "rootnode-code: gate-lib.sh not found; verify gate inactive" >&2; exit 0; }
gate_verify_setup "$(cat)" >/dev/null              # design §7.2 steps 1–7; an existing baseline is kept
exit 0
