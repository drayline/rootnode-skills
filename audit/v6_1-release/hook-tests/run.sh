#!/bin/bash
# run.sh — acceptance harness for the rootnode-code hook scripts (rootnode-code 6.1.0).
# Cases: design/root_DESIGN_verify_gate_fix.md §4 rows 1–17, the lockout cases (L rows) from the 6.1.0
# session prompt, and cases added during the build (B, G, P, R, U rows). Each case builds a fresh temp
# folder, pipes hook-input JSON to the script under test with CLAUDE_PLUGIN_DATA pointed at a temp state
# folder and TMPDIR at another temp folder (so a fallback write is seen), and prints one row: id,
# expected, observed exit codes in order, files in the state folders, files the scripts changed in the
# repo folder, verdict. Exits 1 on any FAIL. Row 15 is the operator's check and is not counted.
#
# Usage: bash audit/v6_1-release/hook-tests/run.sh                    # plugins/rootnode-code/scripts
#        bash audit/v6_1-release/hook-tests/run.sh --ref origin/main   # the scripts committed at a git ref
#        bash audit/v6_1-release/hook-tests/run.sh --scripts <dir>
#        KEEP=1 keeps the temp folders and prints where they are.
set -u
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO=$(cd "$HERE/../../.." && pwd)
FIX="$HERE/fixtures"
SCRIPTS="$REPO/plugins/rootnode-code/scripts"
TMPROOT=$(mktemp -d "${TMPDIR:-/tmp}/rn-hooktests.XXXXXX") || { echo "run.sh: cannot create a temp folder" >&2; exit 2; }
if [ "${KEEP:-0}" = 1 ]; then echo "temp: $TMPROOT"; else trap 'rm -rf "$TMPROOT"' EXIT; fi
case "${1:-}" in
--scripts) SCRIPTS=$(cd "${2:?--scripts needs a folder}" && pwd) || exit 2 ;;
--ref)
  mkdir -p "$TMPROOT/ref" || exit 2
  for f in $(git -C "$REPO" ls-tree --name-only "${2:?--ref needs a git ref}" plugins/rootnode-code/scripts/); do
    git -C "$REPO" show "$2:$f" > "$TMPROOT/ref/${f##*/}" || exit 2
  done
  SCRIPTS="$TMPROOT/ref" ;;
"") ;;
*) echo "usage: run.sh [--scripts <dir> | --ref <git ref>]" >&2; exit 64 ;;
esac

unset VERIFY_GATE_OFF MIGRATIONS_GUARD_OFF CLAUDE_CODE_REMOTE CLAUDE_CODE_STOP_HOOK_BLOCK_CAP CLAUDE_PLUGIN_DATA CLAUDE_PROJECT_DIR
export GIT_AUTHOR_NAME=harness GIT_AUTHOR_EMAIL=harness@example.invalid
export GIT_COMMITTER_NAME=harness GIT_COMMITTER_EMAIL=harness@example.invalid
command -v jq >/dev/null || { echo "run.sh: the harness needs jq" >&2; exit 2; }

path_without() {  # $1 = tool -> PATH with every folder that holds it removed
  local out="" d IFS=:
  for d in $PATH; do [ -x "$d/$1" ] || [ -x "$d/$1.exe" ] || out=${out:+$out:}$d; done
  printf '%s' "$out"
}
NOJQ=$(path_without jq); NOGIT=$(path_without git)

# --- hook input ------------------------------------------------------------------------------
jesc() { local s=${1//\\/\\\\}; s=${s//\"/\\\"}; printf '%s' "$s"; }
wpath() { if command -v cygpath >/dev/null; then cygpath -w "$1"; else printf '%s' "$1"; fi; }  # the form Claude Code sends
in_stop()  { printf '{"session_id":"%s","transcript_path":"","cwd":"%s","permission_mode":"default","hook_event_name":"Stop","stop_hook_active":%s}' "$2" "$(jesc "$(wpath "$1")")" "$3"; }
in_start() { printf '{"session_id":"%s","transcript_path":"","cwd":"%s","hook_event_name":"SessionStart","source":"startup"}' "$2" "$(jesc "$(wpath "$1")")"; }
in_tool()  { printf '{"session_id":"s1","transcript_path":"","cwd":"%s","hook_event_name":"PreToolUse","tool_name":"%s","tool_input":{"%s":"%s"}}' "$(jesc "$(wpath "$1")")" "$2" "$3" "$(jesc "$4")"; }

# --- case framework --------------------------------------------------------------------------
PASSN=0; FAILN=0; OPN=0; SHARED="$TMPROOT/shared-state"; mkdir -p "$SHARED"
new_case() { T=$(mktemp -d "$TMPROOT/c.XXXXXX"); R="$T/${1:-repo}"; S="$T/state"; mkdir -p "$R" "$S" "$T/tmp"; X=(); RFX=""; ERR=""; OUT=""; V=PASS; }
mkrepo() {  # [config fixture] -> a committed git repo with a package.json test script and a tests folder
  cp "$FIX/package.json" "$R/package.json"; mkdir -p "$R/tests"; echo "// test" > "$R/tests/t.test.js"; echo one > "$R/a.txt"
  if [ -n "${1:-}" ]; then mkdir -p "$R/.claude"; cp "$FIX/$1.json" "$R/.claude/rootnode-gates.json"; fi
  git -C "$R" init -q -b main && git -C "$R" -c core.safecrlf=false add -A && git -C "$R" commit -qm init
}
edit() { echo "edit $RANDOM" >> "$R/${1:-a.txt}"; }
rootp() { git -C "$R" rev-parse --show-toplevel; }
snap() { (cd "$R" && find . -type f -print0 | sort -z | xargs -0 -r sha256sum) 2>/dev/null; }
hook() {  # <script> <stdin> [VAR=value ...] [-- args ...]: runs from $R, appends the exit code to X
  local s=$1 in=$2 before after envs=(); shift 2
  while [ $# -gt 0 ] && [ "$1" != -- ]; do envs+=("$1"); shift; done; [ "${1:-}" = -- ] && shift
  if [ ! -f "$SCRIPTS/$s" ]; then X+=("n/a"); ERR=""; OUT=""; return; fi
  before=$(snap)
  ( cd "$R" && printf '%s' "$in" | env TMPDIR="$T/tmp" CLAUDE_PLUGIN_DATA="$(wpath "$S")" ${envs[@]+"${envs[@]}"} "$BASH" "$SCRIPTS/$s" "$@" >"$T/out" 2>"$T/err" )
  X+=("$?"); ERR=$(cat "$T/err"); OUT=$(cat "$T/out")
  after=$(snap)
  RFX="$RFX$(diff <(printf '%s\n' "$before") <(printf '%s\n' "$after") | sed -n 's/^[<>] \\\{0,1\}[0-9a-f]* *\*\{0,1\}\.\///p' | sort -u | tr '\n' ' ')"
}
exits() { local IFS=,; printf '%s' "${X[*]:-}"; }
scount() { find "$S" "$T/tmp" -type f 2>/dev/null | wc -l | tr -d ' '; }
glog() { find "$S" -name gate.log -type f 2>/dev/null | head -1; }
logn() {  # <action> [root] -> gate.log rows with that action (for that root)
  local f; f=$(glog); [ -n "$f" ] || { echo 0; return; }
  tr -d '\r' < "$f" | awk -F'\t' -v a="$1" -v r="${2:-}" '$3 == a && (r == "" || $4 == r)' | wc -l | tr -d ' '
}
msgcmd() {  # the record command the block message names -> MS MROOT MEV
  local l; l=$(printf '%s\n' "$ERR" | sed -n 's/^bash "\([^"]*\)" "\([^"]*\)" "\([^"]*\)"$/\1|\2|\3/p' | head -1)
  IFS='|' read -r MS MROOT MEV <<< "$l"
}
chk() { "$@" || V=FAIL; }
is() { [ "$(exits)" = "$1" ]; }
has() { case "$ERR" in *"$1"*) ;; *) return 1 ;; esac; }
norepo() { [ -z "$RFX" ]; }
nostate() { [ "$(scount)" = 0 ]; }
row() {  # id expected [state column]
  local st=${3:-$(scount)}
  printf '| %s | %s | %s | %s | %s | %s |\n' "$1" "$2" "$(exits)" "$st" "${RFX:-none}" "$V"
  if [ "$V" = PASS ]; then PASSN=$((PASSN + 1)); else FAILN=$((FAILN + 1)); fi
}

echo "rootnode-code hook harness · scripts $SCRIPTS · $(uname -s) · bash $BASH_VERSION"
echo
echo "| id | expected | exit codes | state files | repo writes | result |"
echo "|---|---|---|---|---|---|"

# --- design spec §4 --------------------------------------------------------------------------
new_case; mkdir -p "$R/spec"; echo "a: 1" > "$R/spec/x.yaml"
hook gate-baseline.sh "$(in_start "$R" s1)"; hook verify-tests.sh "$(in_stop "$R" s1 false)"
chk is 0,0; chk norepo; chk nostate
row 1 "no git, only spec/x.yaml, no config: start, stop exit 0; no state anywhere"

new_case; mkrepo; hook gate-baseline.sh "$(in_start "$R" s1)"; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"
chk is 0,0; chk norepo; chk nostate
row 2 "repo with tests, no config, file edited: exit 0; no state"

new_case; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s1)"; chk [ -z "$OUT" ]
hook verify-tests.sh "$(in_stop "$R" s1 false)"
chk is 0,0; chk norepo
row 3 "config (enforce), tree unchanged since baseline: exit 0; start prints nothing"

new_case; S=$SHARED; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s4)"; edit; hook verify-tests.sh "$(in_stop "$R" s4 false)"
chk is 0,2; chk has "$(rootp)"; chk has no-evidence; chk has record-test-evidence.sh; chk norepo
row 4 "config (enforce), edited, no evidence: block naming root, reason, record script" shared

new_case; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s1)"; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"; msgcmd
hook record-test-evidence.sh "" -- "$MROOT" "$MEV"; hook verify-tests.sh "$(in_stop "$R" s1 true)"
chk is 0,2,0,0; chk [ -f "$MS" ]; chk norepo
row 5 "edited, evidence recorded with the command the message prints: stop exit 0"

new_case; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s1)"; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"; msgcmd
hook record-test-evidence.sh "" -- "$MROOT" "$MEV"; hook verify-tests.sh "$(in_stop "$R" s1 true)"
edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"
chk is 0,2,0,0,2; chk has stale-evidence; chk norepo
row 6 "evidence recorded, then a new edit: block (stale-evidence)"

new_case; mkrepo enforce; git init -q --bare "$T/remote.git"; git -C "$R" remote add origin "$T/remote.git"; git -C "$R" push -q origin main 2>/dev/null
hook gate-baseline.sh "$(in_start "$R" s1)"; edit; git -C "$R" -c core.safecrlf=false commit -qam work; git -C "$R" push -q origin main 2>/dev/null
chk [ -z "$(git -C "$R" status --porcelain)" ]
hook verify-tests.sh "$(in_stop "$R" s1 false)"; msgcmd; hook record-test-evidence.sh "" -- "$MROOT" "$MEV"; hook verify-tests.sh "$(in_stop "$R" s1 true)"
chk is 0,2,0,0; chk norepo
row 7 "work committed and pushed, clean tree: block until evidence matches"

new_case; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s1)" CLAUDE_CODE_REMOTE=true; edit
hook verify-tests.sh "$(in_stop "$R" s1 false)" CLAUDE_CODE_REMOTE=true
chk is 0,0; chk norepo
row 8 "CLAUDE_CODE_REMOTE=true, surfaces default: exit 0"

new_case; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s1)"; edit
hook verify-tests.sh "$(in_stop "$R" s1 false)" VERIFY_GATE_OFF=1
chk is 0,0; chk norepo
row 9 "VERIFY_GATE_OFF=1, edited, no evidence: exit 0"

new_case; mkdir -p "$R/.claude"; cp "$FIX/enforce.json" "$R/.claude/rootnode-gates.json"
hook verify-tests.sh "$(in_stop "$R" s1 false)"
chk is 0; chk norepo; chk [ "$(logn skip)" = 1 ]
row 10 "not a git working copy, config present: exit 0, one log line (state folder)"

new_case; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s1)"; edit
chk [ -z "$(PATH=$NOJQ command -v jq)" ]
hook verify-tests.sh "$(in_stop "$R" s1 false)" "PATH=$NOJQ"
chk is 0,0; chk [ "$(printf '%s\n' "$ERR" | grep -c .)" = 1 ]; chk has jq; chk norepo
row 11 "no jq, config, edited: exit 0, one stderr line naming jq"

new_case; S=$SHARED; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s12)"; edit
for a in false true true false true false; do hook verify-tests.sh "$(in_stop "$R" s12 $a)"; done
chk is 0,2,2,0,2,0,0; chk [ "$(logn block "$(rootp)")" = 3 ]; chk [ "$(logn release "$(rootp)")" = 3 ]; chk norepo
row 12 "caps 2/4: stops F,T,T,F,T,F -> 2,2,release,2,release,release; session total kept" shared

new_case; hook guard-migrations.sh "$(in_tool "$R" Bash command 'rm *')"
chk is 0; chk norepo; chk nostate
row 13 "guard, no config, rm * in an empty folder: exit 0, no .claude/guard.log"

new_case; mkrepo guard; hook guard-migrations.sh "$(in_tool "$R" Edit file_path "$(wpath "$R/migrations/001_init.sql")")"
chk is 2; chk norepo; chk [ "$(logn block)" = 1 ]
row 14 "guard enabled, Edit under migrations/: exit 2; audit row in the state folder"

X=(); RFX=""; printf '| %s | %s | %s | %s | %s | %s |\n' 15 "C:\\Projects\\modelcast-SIGNAL with the config, local session: full gate" - - - operator; OPN=$((OPN + 1))

new_case; S=$SHARED; mkrepo watch; hook gate-baseline.sh "$(in_start "$R" s16)"; edit; hook verify-tests.sh "$(in_stop "$R" s16 false)"
chk is 0,0; chk [ "$(logn would-block "$(rootp)")" = 1 ]; chk norepo
row 16 "mode watch (default), edited, no evidence: exit 0, one would-block line" shared

new_case; hook gate-status.sh "" -- --state "$SHARED"
chk is 0; chk eval 'case "$OUT" in *"verify gate: block 4, would-block 1, release 3"*) ;; *) false ;; esac'
row 17 "gate-status.sh over rows 4, 12, 16: block 4, would-block 1, release 3" shared

# --- added during the build ------------------------------------------------------------------
new_case; mkrepo enforce; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"
chk is 0,2; chk norepo
row B1 "no SessionStart: first stop takes the baseline (exit 0), a later edit blocks"

new_case; mkrepo all; hook guard-migrations.sh "$(in_tool "$R" Bash command 'rm -rf migrations')" "PATH=$NOJQ"
chk is 2; chk norepo; chk [ "$(logn block)" = 1 ]
row G1 "guard enabled, no jq, command names migrations: exit 2; audit row outside the repo"

new_case; mkrepo guard; hook guard-migrations.sh "$(in_tool "$R" Bash command 'ls -la')"
chk is 0; chk norepo; chk nostate
row G2 "guard enabled, ls -la: exit 0, nothing written"

new_case; mkrepo guard-off; hook guard-migrations.sh "$(in_tool "$R" Edit file_path "$R/migrations/001_init.sql")"
chk is 0; chk norepo; chk nostate
row G3 "migrations_guard.enabled false, Edit under migrations/: exit 0"

new_case "my repo"; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s1)"; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"; msgcmd
hook record-test-evidence.sh "" -- "$MROOT" "$MEV"; hook verify-tests.sh "$(in_stop "$R" s1 true)"
chk is 0,2,0,0; chk [ "$MROOT" = "$(rootp)" ]; chk norepo
row P1 "repo path with a space: block, record by the printed command, then exit 0"

new_case; mkrepo enforce
hook record-test-evidence.sh ""; hook record-test-evidence.sh "" -- "$R"
rm -f "$R/.claude/rootnode-gates.json"; hook record-test-evidence.sh "" -- "$R" "$T/ev.json"
cp "$FIX/invalid.json" "$R/.claude/rootnode-gates.json"; hook record-test-evidence.sh "" -- "$R" "$T/ev.json"
chk is 64,64,64,64; chk [ ! -e "$T/ev.json" ]; chk norepo; chk nostate
row R1 "record script: no args, one arg, no config, invalid config: exit 64, nothing written"

new_case; mkrepo fail; hook gate-baseline.sh "$(in_start "$R" s1)"; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"; msgcmd
hook record-test-evidence.sh "" -- "$MROOT" "$MEV"; hook verify-tests.sh "$(in_stop "$R" s1 true)"
chk is 0,2,3,2; chk has failing; chk [ "$(jq -r .pass "$MEV" 2>/dev/null | tr -d '\r')" = false ]; chk norepo
row R2 "failing command: record exits 3 and writes pass false; stop blocks (failing)"

new_case; mkrepo own-evidence; hook gate-baseline.sh "$(in_start "$R" s1)"; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)"; msgcmd
chk [ "$MEV" = "$(rootp)/.claude/state/last-verify.json" ]
hook record-test-evidence.sh "" -- "$MROOT" "$MEV"; hook verify-tests.sh "$(in_stop "$R" s1 true)"
chk is 0,2,0,0; chk [ "$RFX" = ".claude/state/last-verify.json " ]
row R3 "repo's own evidence path: record writes only that file; it does not change the fingerprint"

new_case; mkrepo own-evidence; hook gate-baseline.sh "$(in_start "$R" s1)"; edit
mkdir -p "$R/.claude/state"; echo '{"pass": true}' > "$R/.claude/state/last-verify.json"
hook verify-tests.sh "$(in_stop "$R" s1 false)"
chk is 0,2; chk has stale-evidence; chk norepo
row R4 "repo's own evidence without a fingerprint: block (stale-evidence)"

new_case; mkrepo clamp; hook gate-baseline.sh "$(in_start "$R" s1)"; edit
hook verify-tests.sh "$(in_stop "$R" s1 false)" CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=1; hook verify-tests.sh "$(in_stop "$R" s1 true)" CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=1
chk is 0,2,0; chk norepo
row R5 "max_blocks_chain 5 clamped to CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=1: second stop releases"

new_case; mkrepo enforce; hook gate-baseline.sh "$(in_start "$R" s1)"; mkdir -p "$R/newdir"; echo x > "$R/newdir/n.txt"
hook verify-tests.sh "$(in_stop "$R" s1 false)"; msgcmd; hook record-test-evidence.sh "" -- "$MROOT" "$MEV"; hook verify-tests.sh "$(in_stop "$R" s1 true)"
echo more >> "$R/newdir/n.txt"; hook verify-tests.sh "$(in_stop "$R" s1 false)"
chk is 0,2,0,0,2; chk norepo
row U1 "new untracked file: block; evidence; edit to the untracked file blocks again"

# --- lockout: a hook that cannot read its input, config or tools never blocks ---------------
new_case; mkrepo all; edit
hook verify-tests.sh ""; hook gate-baseline.sh ""; hook guard-migrations.sh ""
chk is 0,0,0; chk norepo
row L1 "empty stdin (verify, baseline, guard; config enables both): exit 0"

new_case; mkrepo all; edit
hook verify-tests.sh '{"cwd": "x", '; hook gate-baseline.sh '{"cwd": '; hook guard-migrations.sh '{"tool_name": "Edit", '
chk is 0,0,0; chk norepo
row L2 "malformed JSON on stdin (verify, baseline, guard): exit 0"

new_case; mkrepo all; edit
chk [ -z "$(PATH=$NOGIT command -v git)" ]
hook gate-baseline.sh "$(in_start "$R" s1)" "PATH=$NOGIT"; hook verify-tests.sh "$(in_stop "$R" s1 false)" "PATH=$NOGIT"
hook guard-migrations.sh "$(in_tool "$R" Edit file_path "$R/src/x.js")" "PATH=$NOGIT"
chk is 0,0,0; chk norepo
row L3 "git not on PATH (baseline, verify, guard): exit 0"

new_case; mkrepo all
hook gate-baseline.sh "$(in_start "$R" s1)" "PATH=$NOJQ"; edit; hook verify-tests.sh "$(in_stop "$R" s1 false)" "PATH=$NOJQ"
hook guard-migrations.sh "$(in_tool "$R" Bash command 'ls -la')" "PATH=$NOJQ"
chk is 0,0,0; chk norepo
row L4 "jq not on PATH (baseline, verify, guard on ls): exit 0"

new_case "my repo"; mkrepo all
hook gate-baseline.sh "$(in_start "$R" s1)"; hook verify-tests.sh "$(in_stop "$R" s1 false)"
hook guard-migrations.sh "$(in_tool "$R" Bash command 'ls -la')"; hook guard-migrations.sh "$(in_tool "$R" Edit file_path "$R/src/x.js")"
chk is 0,0,0,0; chk norepo
row L5 "repo path with a space, unchanged tree (baseline, verify, guard x2): exit 0"

new_case; mkrepo invalid; edit
hook gate-baseline.sh "$(in_start "$R" s1)"; hook verify-tests.sh "$(in_stop "$R" s1 false)"
hook guard-migrations.sh "$(in_tool "$R" Edit file_path "$R/migrations/001_init.sql")"
chk is 0,0,0; chk norepo
row L6 "config is not valid JSON (baseline, verify, guard on migrations/): exit 0"

new_case; mkrepo all; hook gate-baseline.sh "$(in_start "$R" s1)"; edit
if [ -f "$SCRIPTS/gate-lib.sh" ]; then
  mkdir -p "$T/nolib"; cp "$SCRIPTS"/*.sh "$T/nolib/"; rm -f "$T/nolib/gate-lib.sh"; KEEPS=$SCRIPTS; SCRIPTS="$T/nolib"
  hook verify-tests.sh "$(in_stop "$R" s1 false)"; hook gate-baseline.sh "$(in_start "$R" s2)"
  hook guard-migrations.sh "$(in_tool "$R" Edit file_path "$R/migrations/001_init.sql")"
  hook record-test-evidence.sh "" -- "$R" "$T/ev.json"; hook gate-status.sh ""
  SCRIPTS=$KEEPS; chk [ ! -e "$T/ev.json" ]
fi
chk is 0,0,0,0,0,0; chk norepo
row L8 "gate-lib.sh missing (verify, baseline, guard on migrations/, record, status): exit 0"

for f in "$SCRIPTS"/*.sh; do
  new_case; "$BASH" -n "$f" 2>/dev/null; X=("$?")
  chk is 0; row "L7" "bash -n ${f##*/}" -
done

echo
echo "countable rows: $((PASSN + FAILN)) · PASS $PASSN · FAIL $FAILN · operator $OPN"
[ "$FAILN" = 0 ]
