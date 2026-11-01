#!/bin/bash
# guard-migrations.sh — Edit|Write|NotebookEdit|Bash|PowerShell guard; fails closed.
[ "${MIGRATIONS_GUARD_OFF:-0}" = "1" ] && exit 0      # off-switch; audit its use
IN=$(cat)
TOOL=$(printf '%s' "$IN" | jq -r '.tool_name // ""') &&
T=$(printf '%s' "$IN" | jq -r '.tool_input.file_path // .tool_input.notebook_path // .tool_input.command // ""') ||
  { echo "Input unreadable; rule holds. Next step: check jq and the hook input." >&2; exit 2; }
[ -n "$TOOL" ] || { echo "guard: no tool name in hook input — refusing (fail-closed); check the hook's stdin wiring" >&2; exit 2; }
P=$(printf '%s' "$T" | tr '\\' '/')                  # C:\repo\migrations\x -> C:/repo/migrations/x
HIT=""
case "$TOOL" in
Bash|PowerShell)
  if [ "$TOOL" = "Bash" ]; then RM='rm|mv'; CD='cd|pushd'; SEGCMD='rm|mv|find'; I=''
  else RM='remove-item|ri|del|erase|rd|rmdir|move-item|mi|move|rm|mv'; CD='cd|pushd|chdir|sl|set-location|push-location'
       SEGCMD=$RM; I=i; shopt -s nocasematch; fi                # PowerShell delete/move verbs and aliases, any case
  C=$(printf '%s' "$P" | tr -d "\"'"); S='(^|[;&|[:space:]])'; M='([^[:space:];&|]*/)?migrations([/[:space:];&|]|$)'
  printf '%s\n' "$C" | grep -Eq$I "${S}($RM)[[:space:]]([^;&|]*[[:space:]])?$M" && HIT=1           # rm/mv migrations/
  printf '%s\n' "$C" | grep -Eq "${S}find[[:space:]]([^;&|]*[[:space:]])?$M[^;&|]*-(delete|exec)" && HIT=1  # find migrations -delete
  printf '%s\n' "$C" | grep -Eq$I "${S}($CD)[[:space:]]+$M.*${S}($RM)[[:space:]]" && HIT=1        # cd migrations && rm …
  PRE='^(sudo|command|env|nohup|time|git|then|do|else|!|[A-Za-z_][A-Za-z0-9_]*=.*)$'   # prefixes before the command
  set -f
  while IFS= read -r SEG; do                       # per segment: split on ; && || | ( ) { } `
    set -- $SEG; while [ $# -gt 0 ] && [[ $1 =~ $PRE ]]; do shift; done
    [[ ${1:-} =~ ^($SEGCMD)$ ]] || continue        # only a delete/move/find segment's words count
    if [ "$1" = find ]; then                       # find over . ./ .. / ~ or no path, with no name filter
      A=" $* "; D=' -(delete|exec (rm|mv)) '; F=' -(i?name|path) '
      case "${2:--}" in .|./|..|/|'~'|-*) [[ $A =~ $D && ! $A =~ $F ]] && HIT=1 ;; esac
    fi
    for W in "$@"; do                              # a glob that can expand to migrations
      case "$W" in *[*?[]*) for X in migrations ./migrations ../migrations x/migrations; do [[ "$X" == $W ]] && HIT=1; done ;; esac
    done
  done < <(printf '%s\n' "$C" | tr ';&|(){}`' '\n\n\n\n\n\n\n\n')
  set +f ;;
*) case "$P" in migrations/*|*/migrations/*) HIT=1 ;; esac ;;
esac
[ -z "$HIT" ] && exit 0
mkdir -p .claude && echo "$(date -u +%FT%TZ) block $TOOL $P" >> .claude/guard.log ||   # audit row
  echo "guard: audit row not written" >&2
echo "migrations/ is protected. Next step: use the migration tool, then stop for review." >&2
exit 2
