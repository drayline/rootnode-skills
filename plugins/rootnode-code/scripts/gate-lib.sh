#!/bin/bash
# gate-lib.sh — shared by the rootnode-code gate scripts: repo root, opt-in config, state folder, tree fingerprint.
# Sourced, never run. A script that cannot source it exits 0, so a missing library never blocks.
export GIT_OPTIONAL_LOCKS=0                          # git status must not rewrite the repository's index
GATE_CONFIG=.claude/rootnode-gates.json              # the opt-in file; no file = no gate

gate_jq() {                                          # jq -r without the CR that jq on Windows adds to each line
  local out; out=$(jq -r "$@" 2>/dev/null) || return 1
  printf '%s\n' "${out//$'\r'/}"
}
gate_input() {                                       # $1 = hook input, $2 = field -> its value, or empty
  command -v jq >/dev/null && printf '%s' "$1" | gate_jq "$2 // empty"
}
gate_sha() {                                         # stdin -> 64 hex characters; fails without a sha256 tool
  if command -v sha256sum >/dev/null; then sha256sum | cut -c1-64
  elif command -v shasum >/dev/null; then shasum -a 256 | cut -c1-64
  else return 1; fi
}
gate_root() {                                        # $1 = folder -> top level of its git working copy, or empty
  [ -n "$1" ] && git -C "$1" rev-parse --show-toplevel 2>/dev/null
}
gate_state_dir() {                                   # the plugin's data folder, or a temp fallback; never the repo
  local d=${CLAUDE_PLUGIN_DATA:-${TMPDIR:-/tmp}/rootnode-code}
  printf '%s/gates' "${d//'\'//}"
}
gate_log() {                                         # gate action root detail... -> one tab-separated line in gate.log
  local f out; out=$(date -u +%FT%TZ)
  for f in "$@"; do out+=$'\t'"${f//[$'\t\r\n']/ }"; done
  mkdir -p "$STATE" 2>/dev/null && printf '%s\n' "$out" >> "$STATE/gate.log" 2>/dev/null
}
gate_evidence() {                                    # sets EV (absolute), EV_REL (in-repo path the fingerprint leaves out), EV_FIELD
  local p; p=$(gate_jq '.verify.evidence.path? // empty | strings' "$CFG"); p=${p//'\'//}
  EV_FIELD=$(gate_jq '.verify.evidence.pass_field? // empty | strings' "$CFG"); EV_FIELD=${EV_FIELD:-pass}
  EV_REL=""
  if [ -z "$p" ]; then EV="$STATE/evidence/$KEY.json"; return 0; fi
  case "$p" in /*|[A-Za-z]:/*) EV=$p ;; *) EV="$ROOT/${p#./}" ;; esac
  case "$EV" in "$ROOT"/*) EV_REL=${EV#"$ROOT"/} ;; esac
  case "/$EV_REL/" in */../*) EV_REL="" ;; esac    # a path that climbs out is not left out
}
gate_fingerprint() {                                 # $1 = root, $2 = in-repo path to leave out -> sha256 of the tree state
  local ps=(-- .); [ -n "$2" ] && ps+=(":(exclude,literal)$2")
  {
    git -C "$1" rev-parse -q --verify HEAD || echo none
    git -C "$1" status --porcelain --untracked-files=all "${ps[@]}"
    git -C "$1" diff HEAD --no-color --no-ext-diff "${ps[@]}" ||
      git -C "$1" diff --cached --no-color --no-ext-diff "${ps[@]}"            # no commit yet
    git -C "$1" -c core.quotePath=false ls-files -o --exclude-standard "${ps[@]}" |
      git -C "$1" hash-object --stdin-paths                                    # contents of untracked files
  } 2>/dev/null | gate_sha
}
gate_verify_setup() {                                # design §7.2 steps 2–7, shared by the Stop gate and the SessionStart baseline
  # $1 = hook input. Returns 0 with ROOT CFG STATE KEY SD EV EV_REL EV_FIELD FP set when the gate goes on;
  # returns 1 when the hook should exit 0 (inactive, or the baseline was just taken).
  local dir on sid surf
  STATE=$(gate_state_dir)
  dir=$(gate_input "$1" .cwd); dir=${dir:-$PWD}
  ROOT=$(gate_root "$dir")
  if [ -z "$ROOT" ]; then                            # 2. not a git working copy: inactive, noted when the folder asks for a gate
    [ -f "$dir/$GATE_CONFIG" ] && gate_log verify skip "$dir" not-a-git-repo
    return 1
  fi
  CFG="$ROOT/$GATE_CONFIG"
  [ -f "$CFG" ] || return 1                          # 3. no config: nothing written
  if ! command -v jq >/dev/null; then                # 4. a gate that cannot read its config does not block
    grep -q '"verify"' "$CFG" 2>/dev/null && echo "rootnode-code: jq not found; verify gate inactive" >&2
    return 1
  fi
  on=$(gate_jq '(.verify | type) == "object"' "$CFG") ||
    { echo "rootnode-code: $CFG is not valid JSON; verify gate inactive" >&2; return 1; }
  [ "$on" = true ] || return 1                       # 3. no verify section
  if [ -z "$(gate_jq '(.verify.command // empty | strings), (.verify.evidence.path? // empty | strings)' "$CFG")" ]; then
    echo "rootnode-code: $CFG has no verify.command; verify gate inactive" >&2; return 1
  fi
  surf=local; [ "${CLAUDE_CODE_REMOTE:-}" = true ] && surf=remote
  jq -e --arg s "$surf" '(.verify.surfaces // ["local"]) | if type == "array" then index($s) != null else . == $s end' \
    "$CFG" >/dev/null 2>&1 || return 1               # 5. surface not listed
  sid=$(gate_input "$1" .session_id); sid=${sid//[^A-Za-z0-9_-]/_}
  [ -n "$sid" ] || { echo "rootnode-code: hook input has no session_id; verify gate inactive" >&2; return 1; }
  KEY=$(printf '%s' "$ROOT" | gate_sha | cut -c1-16)  # 6. state folder, keyed by session and root
  [ -n "$KEY" ] || { echo "rootnode-code: no sha256sum or shasum; verify gate inactive" >&2; return 1; }
  SD="$STATE/sessions/$sid/$KEY"
  mkdir -p "$SD" "$STATE/evidence" 2>/dev/null ||
    { echo "rootnode-code: cannot create $STATE; verify gate inactive" >&2; return 1; }
  gate_evidence
  FP=$(gate_fingerprint "$ROOT" "$EV_REL")           # 7. fingerprint; the first one in a session is the baseline
  [ -n "$FP" ] || { echo "rootnode-code: cannot fingerprint $ROOT; verify gate inactive" >&2; return 1; }
  [ -f "$SD/baseline" ] || { printf '%s\n' "$FP" > "$SD/baseline"; return 1; }
  return 0
}
