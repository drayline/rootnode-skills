# Rigor check — cc-design (catalog v6.1, spec §7.8 behavioral)

Briefs `B1.txt`, `B2.txt`, `B3.txt` hold the spec text verbatim. `run.sh` runs one brief through a child `claude -p` (Claude Code 2.1.317, `claude-opus-5-5`, default effort) in a fresh temp folder outside any repository, with the plugin under test loaded by `--plugin-dir`, the brief on stdin, `--max-budget-usd 4`, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=0`, `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` and `--setting-sources project,local`. The last two keep the operator's global CLAUDE.md and the account's synced plugins out of the child; a probe showed both would otherwise load. `score.sh` scores the final result text with `grep` and `wc`. Outputs are in `out/` (`.md` result text, `.meta` instrument record). The raw stream-json files carry account-level init data and are kept outside the repository with the session report.

**Instrument check.** Every run's init record lists `rootnode-code:cc-design`, with `rootnode-code@inline` at the version under test (6.1.0 for the control, 6.2.0 otherwise) and no synced copy beside it. A probe under `--safe-mode` loaded the plugin but listed no plugin Skills, so safe mode was not used.

**Scorer.** v1 required "merge"/"release" and "gate" on one line and did not count "guard" as a mechanism word. The first B2 fix-pass output names a "**Gates:**" heading with a "**Merge:** green CI plus approval…" item, and says "Migrations already on `main` can't be changed … A guard blocks Claude from editing them" — both assertions met in substance, missed by the regexes. v2 accepts a Gates heading with a Merge or Release item within four lines, and "guard". Every output was re-scored with v2; v1 totals are in `results-v1.txt`, v2 rows in `results-v2.txt`. The control fails under both.

| Run | Plugin | Skill invoked | Cost USD | v1 | v2 | Misses (v2) |
|---|---|---|---|---|---|---|
| B1 positive control | 6.1.0 (`origin/main`) | yes | 0.43 | 2/4 | 2/4 | no `Rigor:` first line; no list of actions that need no approval |
| B1 test pass | 6.2.0 | yes | 0.46 | 4/4 | 4/4 | — |
| B2 test pass | 6.2.0 | yes | 0.72 | 1/3 | 1/3 | `Rigor: standard` came third, after a note that file writes were declined; no gate named |
| B3 test pass | 6.2.0 | **no** | 0.28 | 2/3 | 2/3 | no `Rigor:` line — the child wrote the prompt without invoking cc-design |
| B1 fix pass | 6.2.0 + fix | yes | 0.45 | 4/4 | 4/4 | — |
| B2 fix pass | 6.2.0 + fix | yes | 1.63 | 1/3 | 3/3 | — |
| B3 fix pass | 6.2.0 + fix | **no** | 0.28 | 2/3 | 2/3 | as the test pass |

Positive control: B1 on 6.1.0 fails 2 of 4 assertions, so the assertions can see the change.

**Fix pass (one).** After the B2 test pass, cc-design was changed so that the `Rigor:` line is the very first line, before any note about files, tools or assumptions, and so that standard and strict outputs name each gate as a gate ("Merge gate: …", with who passes it and on what evidence) — `SKILL.md` Step 4, `cc-methodology-patterns.md` §10a, and a Gate block in the autonomous-prompt template.

**Remaining miss — goes to the next patch.** B3 ("Write a session prompt to fix one typo in README.md.") did not invoke cc-design in either pass; the plugin was loaded and the Skill listed. The model judged a one-line task too small for the Skill. Its output still met the other two assertions (no subagent or reviewer role; 34 and 17 lines). The fix is a triggering change — the description names "CC prompts" but not "session prompt" — and the spec does not change descriptions in this cut.

**Not shown by this check.** One run per brief per pass, so run-to-run variation is unmeasured. In `-p` mode the child cannot get write approval, so B2 outputs describe files it tried to write; in B2's fix pass the child wrote its files to its own scratchpad and returned a summary, so the scored text is that summary, not the full design.
