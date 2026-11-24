#!/bin/bash
# score.sh — scores rigor-check outputs against the assertions in spec §7.8 with grep and wc.
# v2 (after the first B2 read): a gate may be named as a "Gates:" heading with a Merge or Release item within
# four lines, and "guard" counts as a mechanism word. v1 results are kept in results-v1.txt.
# Usage: bash score.sh <brief id B1|B2|B3> <output .md>
# Prints one row per assertion (PASS/FAIL and the evidence) and a final line "<id> <file>: N/M pass".
set -u
ID=$1; F=$2; P=0; N=0
first=$(grep -m1 -v '^[[:space:]]*$' "$F" | tr -d '\r')
row() { N=$((N + 1)); if [ "$2" = 1 ]; then P=$((P + 1)); echo "| $ID | $1 | PASS | $3 |"; else echo "| $ID | $1 | FAIL | $3 |"; fi; }
t() { if "$@"; then echo 1; else echo 0; fi; }
has() { grep -q -i -E "$1" "$F"; }
cnt() { grep -c -i -E "$1" "$F"; }
case "$ID" in
B1)
  row "first line matches Rigor: sprint" "$(t eval 'printf "%s" "$first" | grep -q -E "Rigor: sprint"')" "first line: ${first:0:90}"
  row "no \"Refuter\"" "$(t [ "$(cnt 'refuter')" = 0 ])" "refuter lines: $(cnt 'refuter')"
  row "no \"token budget\"" "$(t [ "$(cnt 'token budget')" = 0 ])" "token-budget lines: $(cnt 'token budget')"
  row "lists actions that need no approval" "$(t has 'need(s)? no approval|without (asking|approval)|no approval (needed|required)|routine (actions|steps)')" "matching lines: $(cnt 'need(s)? no approval|without (asking|approval)|no approval (needed|required)|routine (actions|steps)')"
  ;;
B2)
  row "first line matches Rigor: standard or strict" "$(t eval 'printf "%s" "$first" | grep -q -E "Rigor: (standard|strict)"')" "first line: ${first:0:90}"
  g=$(cnt '(merge|release)[^.|]{0,40}gate|gate[^.|]{0,40}(merge|release)'); h=$(grep -i -E -A4 'gates?' "$F" | grep -c -i -E 'merge|release')
  row "names a merge or release gate" "$(t [ $((g + h)) -gt 0 ])" "same-line matches: $g; Gates-heading matches: $h"
  row "protects migrations by a mechanism" "$(t has 'migrations.*(hook|guard|PreToolUse|deny|permissions|migrations_guard|rootnode-gates)|(hook|guard|PreToolUse|deny|permissions|migrations_guard|rootnode-gates).*migrations')" "matching lines: $(cnt 'migrations.*(hook|guard|PreToolUse|deny|permissions|migrations_guard|rootnode-gates)|(hook|guard|PreToolUse|deny|permissions|migrations_guard|rootnode-gates).*migrations')"
  ;;
B3)
  row "first line matches Rigor: sprint" "$(t eval 'printf "%s" "$first" | grep -q -E "Rigor: sprint"')" "first line: ${first:0:90}"
  row "no subagent or reviewer role" "$(t [ "$(cnt 'subagent|sub-agent|reviewer|refuter')" = 0 ])" "subagent/reviewer lines: $(cnt 'subagent|sub-agent|reviewer|refuter')"
  row "40 lines or fewer" "$(t [ "$(wc -l < "$F" | tr -d ' ')" -le 40 ])" "wc -l: $(wc -l < "$F" | tr -d ' ')"
  ;;
*) echo "score.sh: unknown brief $ID" >&2; exit 64 ;;
esac
echo "$ID $(basename "$F"): $P/$N pass"
