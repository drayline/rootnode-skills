# root.node — Design: rootnode-code hook fix (verify gate and migrations guard)

```
root · DESIGN · verify-gate-fix · v1.0 · 2026-11-24
Status: LOCKED 2026-11-24 as the build spec for rootnode-code 6.1.0. D1, D2, D3, D6 approved by Aaron; D4, D5 and §3a A1–A4 taken as recommended under his instruction "go with your recommendations" (all are config defaults, reversible in a patch). §7 is the build specification.
Inputs: shared_SH_112326-0642 (SIGNAL), root_SH_112426-0735 (career), root_SH_112426-0745 (UCIS)
Repo read: drayline/rootnode-skills @ 8670edc280256af4132f2ecdec80923db857b4e0 (main, shallow clone, 2026-11-24)
```

Labels: **VERIFIED** (read or run this session) · **INFERENCE** · **UNVERIFIED**.

## 1. What was verified

| # | Fact | Source | Label |
|---|---|---|---|
| 1 | The repo copy equals the synced copy the three handoffs read. `verify-tests.sh` = `d384a64cfdc3040d43b53959ab1a85f7035f4207d0ee19e1edca151fee86c8f4`; `hooks.json` = `c93d038ffd61ecd6a50f39c25d0ac844c06700fec9ba511474aceb188d1926e5`; plugin version 6.0.0 | `sha256sum` on the clone | VERIFIED |
| 2 | `has_test_command` returns true for a bare `tests`, `test` or `spec` folder (line 14), for an existing evidence file (line 6), and for ten config files by name alone (lines 10–13) | `plugins/rootnode-code/scripts/verify-tests.sh` | VERIFIED |
| 3 | The script never checks whether the session changed a file. Evidence expires on a 300-second clock (lines 37–38) | same | VERIFIED |
| 4 | The counter is deleted when `stop_hook_active` is false (line 34), so the cap is per stop chain | same; SIGNAL and career logs | VERIFIED |
| 5 | Nothing in the plugin writes the evidence file. The block message tells the model to record the result itself | script line 36; `README.md` | VERIFIED |
| 6 | The README says "chat loads the skills and ignores the hooks". This is false: three chat sessions were blocked. The README is the defect | `plugins/rootnode-code/README.md`; the three handoffs | VERIFIED |
| 7 | Stop input carries `stop_hook_active`, `last_assistant_message`, `background_tasks`, `session_crons` plus the common fields (`session_id`, `transcript_path`, `cwd`, …) | code.claude.com/docs/en/hooks, Stop section | VERIFIED |
| 8 | Claude Code caps consecutive stop-hook continuations at 8; the count resets when Claude calls a tool; `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` raises it | same | VERIFIED |
| 9 | Stop has no matcher, and `if` is evaluated on tool events only. A Stop handler cannot be filtered in `hooks.json`; the script must decide | same | VERIFIED |
| 10 | Hook commands get `CLAUDE_PLUGIN_DATA` (persistent plugin data folder), `CLAUDE_PROJECT_DIR`, `CLAUDE_PLUGIN_ROOT`, and `CLAUDE_CODE_REMOTE` ("true" in remote web environments, unset in the local CLI) | same, environment variables | VERIFIED |
| 11 | This chat session has `CLAUDE_CODE_REMOTE=true`, `CLAUDE_CODE_SESSION_ORIGIN=claude_ai_chat`, `CLAUDE_CODE_ENTRYPOINT=remote_cowork`, and the folder `/root/.claude/plugins/data/rootnode-code-synced` | `env` in this session | VERIFIED (the last two variables are not documented; do not build on them) |
| 12 | `SessionStart` (source `startup`/`resume`/`clear`/`compact`/`fork`) and `CwdChanged` (`old_cwd`, `new_cwd`) exist | same docs | VERIFIED |
| 13 | Whether a project `settings.json` `env` value reaches a plugin hook process | docs say only "inherits the parent environment" | UNVERIFIED (UCIS Item 58 stays open; the design below does not depend on it) |
| 14 | `guard-migrations.sh` has the same class of defect. In an empty folder with no `migrations` directory, `rm *` and `find . -name '*'` exit 2, and the guard writes `.claude/guard.log` there. `rm *.tmp` and `ls` exit 0 | ran the script in a temp folder | VERIFIED |

## 2. Root cause (one statement)

Both hooks decide from text and folder names, in every folder, on every surface. Neither asks whether the repository wants the gate, and the Stop gate does not ask whether the session changed anything. The eight causes in SH 112426-0745 (R1–R8) and the six in SH 112426-0735 are the same defect seen from different projects.

## 3. Decisions for Aaron

| # | Decision | Recommendation | Rationale | Rejected |
|---|---|---|---|---|
| D1 | How a repository gets the gates | **Opt-in by a repo file.** Path `.claude/rootnode-gates.json`. No file → both hooks exit 0 and write nothing | The plugin ships skills and hooks together and syncs to every surface. A gate that nobody asked for was turned off in all three projects. A file travels with the repo, so it works where an environment variable does not (R5). `cc-design` adds the file when it designs an environment, which is where the choice belongs | Keep auto-detect with narrower markers (SIGNAL change 1): still gates repos that did not ask. Split the plugin (option E): not needed once the gate is opt-in |
| D2 | When an opted-in repo is gated | **Only when the tree changed in this session.** Fingerprint = `HEAD` + hash of `git status --porcelain` + hash of `git diff HEAD`, with the gate's own state excluded. Baseline at `SessionStart`, or at the first Stop that sees a repo root with no baseline. Same fingerprint → exit 0 | Answers "did this session change code", catches Bash edits and commits, and gives SIGNAL's start marker. A session that commits and pushes still differs from its baseline, so it is still gated | Edit/Write flag from PreToolUse (option B): misses Bash edits. Transcript parsing (O4): the docs warn the transcript can lag at Stop. "No diff against upstream" skip: skips the pushed-work case |
| D3 | What counts as evidence | **Evidence bound to the fingerprint, written by a plugin script.** Ship `scripts/record-test-evidence.sh`: it runs the command named in the config, then writes exit status and fingerprint. Evidence is valid while the fingerprint matches. Remove the 300-second clock. The block message names the script by absolute path | Removes the hand-written `"pass": true` (cause 5) and the clock (R3). A repo that already records evidence (career-pipeline `last-verify.json`) points the config at its own file and field | Keep the clock: it blocks unchanged trees |
| D4 | Remote sessions | **Config key `surfaces`, default `["local"]`.** When `CLAUDE_CODE_REMOTE` is `"true"` and the config does not list `remote`, exit 0 | Solves SIGNAL's second case (tests need Docker; a chat container has none). Uses a documented variable only | Hard skip of all remote sessions: a repo with cloud-runnable tests may want the gate there |
| D5 | Caps and state | **Per-session total cap, never reset by a new chain; state in `CLAUDE_PLUGIN_DATA`, keyed by `session_id` and repo root.** Keep `VERIFY_GATE_OFF` and the per-chain cap. Log line and block message name the repo root and the reason | Covers R4 and R8: no untracked files in consumer repos, no `.gitignore` duty. Fallback when the variable is unset: a temp folder (INFERENCE: the variable is set for synced plugins; the build tests it) | State in the repo |
| D6 | Scope of the cut | **One single-plugin release, `rootnode-code` 6.1.0**, containing both hooks, the record script, a test harness for the scripts, README, and the `cc-design` references that describe the gate. The migrations guard uses the same config: it acts only when the config enables it | Behavior change, so a minor version. Row 14 is the same defect; fixing it in the same cut follows the anti-churn rule. Do not wait for the Fable 5.2 cycle | Ship the Stop fix alone and leave the guard |

Consequence of D1 to accept: after 6.1.0 no repository is gated until it adds the file. `drayline/signal`, `drayline/career-pipeline` and `drayline/ucis` each need a small follow-up (add the config or not; remove `VERIFY_GATE_OFF`; UCIS removes its CLAUDE.md deviation row). An existing evidence file no longer opts a repo in (R6).

Known gap in D2: in a session that enters a repo after start, edits made before the first Stop in that repo are inside the baseline and are not gated. `CwdChanged` can take the baseline earlier; the build decides whether that is worth a third hook.

## 3a. Additions from `root_RESEARCH_gate_value_prop_20261103.md` (proposed 2026-11-24)

The gate research (§5, §8) sets rules that the D1 config can carry. These are additions, not changes to D1–D6.

| # | Addition | Source in the research | Effect on the build |
|---|---|---|---|
| A1 | Config key `mode`: `watch` or `enforce`, default `watch`. In `watch` the Stop gate never exits 2; it logs each would-be block | §5 "Distrust before tuning", §8 "Watch mode by default" | One branch in the script; two matrix cases (16, 17) |
| A2 | `scripts/gate-status.sh`: prints, per gate, the count of blocks, would-be blocks, releases and the last reasons, read from the state folder | §5 "Gates that never visibly act", §8 "Add a status report" | Needed anyway once D5 moves the log out of the repo |
| A3 | Fold the `rootnode-code` items of the v6.0.1 queue into 6.1.0: the two "rootnode-cc-design Skill" prose mentions (`cc-design-brief.schema.json:5`, `cc-anti-patterns.md:5`) and the Windows `jq` CRLF lesson | SH 110226-2207 open items; anti-churn rule | Three small edits in the same plugin. Line numbers are from the handoff; the build verifies them |
| A4 | Record in the build context that the Stop hook from the synced install was never run before release ("Hook checks not yet run", Current State item 3), and that this defect is that gap | `root_build_context.md` Current State | Closeout entry and a new observation |

Matrix additions: (16) `mode: watch`, file edited, no evidence → exit 0 and one would-be-block log line; (17) `gate-status.sh` reports the counts written by cases 4, 12 and 16.

## 4. Acceptance matrix (merged from the three handoffs)

| # | Case | Expected |
|---|---|---|
| 1 | Folder with only `spec/x.yaml`, no config | exit 0, no state written anywhere |
| 2 | Repo with tests, no config | exit 0 |
| 3 | Config present, tree unchanged since baseline (answer-only turn) | exit 0 |
| 4 | Config present, file edited, no evidence | block; message names repo root, reason and the record script |
| 5 | Config present, file edited, passing evidence for the current fingerprint | exit 0 |
| 6 | Evidence recorded, then a new edit | block |
| 7 | Config present, work committed and pushed in the session | block until evidence matches |
| 8 | `CLAUDE_CODE_REMOTE=true`, config without `remote` | exit 0 |
| 9 | `VERIFY_GATE_OFF=1` | exit 0 |
| 10 | Not a git working copy, config present | documented behavior (proposed: exit 0 with one log line) |
| 11 | No `jq` | exit 0 with one stderr line naming `jq`; the gate is inactive, never a block (§7.2 step 4) |
| 12 | Caps: per-chain blocks then a logged release; session total not reset by a new user turn | as stated |
| 13 | Guard, no config: `rm *` in an empty folder | exit 0, no `.claude/guard.log` |
| 14 | Guard, config enables it: edit under `migrations/` | exit 2 |
| 15 | `C:\Projects\modelcast-SIGNAL` with the config, local Claude Code session | full gate |

## 5. Build route

Claude Code handoff point: after D1–D6 are approved. One `cc-design` prompt against `drayline/rootnode-skills`, written after reading that repo's `CLAUDE.md` and controls. The prompt builds the scripts and a harness that runs the matrix, updates README and the two `cc-design` reference files that name the gate (`cc-skills-and-hooks-composition.md`, `remediate-mode-execution.md`), bumps the version, and halts at the merge gate. Release follows the playbook's single-plugin cut.

## 6. Not checked

The other five plugins carry no `hooks/` folder in the listing read; only `rootnode-code` was read in full. Row 13. Whether `CLAUDE_PLUGIN_DATA` is set inside a hook process for a synced plugin in a cloud session (the folder exists; the variable was not read from inside a hook). 

## 7. Build specification

### 7.1 Config: `<repo root>/.claude/rootnode-gates.json`

```json
{
  "version": 1,
  "verify": {
    "mode": "watch",
    "command": "npm test",
    "surfaces": ["local"],
    "max_blocks_chain": 2,
    "max_blocks_session": 4,
    "evidence": { "path": ".claude/state/last-verify.json", "pass_field": "pass" }
  },
  "migrations_guard": { "enabled": true }
}
```

| Key | Required | Default | Meaning |
|---|---|---|---|
| `verify` | no | absent = Stop gate off | Section that turns the Stop gate on |
| `verify.mode` | no | `watch` | `watch` logs would-be blocks and exits 0. `enforce` blocks |
| `verify.command` | yes, when `verify` is present and `evidence` is absent | none | The test command `record-test-evidence.sh` runs at the repo root |
| `verify.surfaces` | no | `["local"]` | `local`, `remote`. `remote` means `CLAUDE_CODE_REMOTE` is `"true"` |
| `verify.max_blocks_chain` / `max_blocks_session` | no | 2 / 4 | D5 caps. The chain value is clamped to `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` (default 8) |
| `verify.evidence` | no | plugin-written evidence in the state folder | A repo's own evidence file. It must carry the fingerprint field `fingerprint` to pass; without it the gate treats the evidence as stale |
| `migrations_guard.enabled` | no | absent = guard off | Turns the PreToolUse guard on |

No file, or a file without a section: that hook exits 0 and writes nothing.

### 7.2 Stop gate (`scripts/verify-tests.sh`), in order

1. `VERIFY_GATE_OFF=1` → exit 0.
2. Read stdin once. Repo root = `git rev-parse --show-toplevel` from the input's `cwd` (fall back to the process directory). Not a git working copy → exit 0.
3. No config, or no `verify` section → exit 0, no state written.
4. No `jq` → one line on stderr ("rootnode-code: jq not found; verify gate inactive"), exit 0. A gate that cannot read its config does not block (gate research §5, lockout).
5. Surface not listed in `surfaces` → exit 0.
6. State folder = `${CLAUDE_PLUGIN_DATA:-${TMPDIR:-/tmp}/rootnode-code}/gates`. Per-session files under `sessions/<session_id>/<root key>/`; evidence under `evidence/<root key>.json`; log `gate.log`. Root key = first 16 hex of sha256 of the root path.
7. Fingerprint = sha256 over: `git rev-parse HEAD` (or `none`), `git status --porcelain`, and `git diff HEAD`, with the configured in-repo evidence path excluded. No baseline for this session and root → write it, exit 0.
8. Fingerprint equals the baseline → exit 0.
9. Evidence exists, its `fingerprint` equals the current one, and its pass field is `true` → delete the chain counter, exit 0.
10. Otherwise this is a would-be block. Log one line: UTC time, `block` or `would-block` or `release`, root, reason (`no-evidence`, `stale-evidence`, `failing`), chain count, session count. `watch` → exit 0. `enforce` → count; over either cap → log `release`, exit 0; else print the message and exit 2.
11. Chain counter is deleted when `stop_hook_active` is false. The session counter is never reset.

Block message (one line, then the command): `rootnode-code verify gate: <root> changed in this session and has no passing test evidence for the current tree (<reason>). Next step: run` followed by `bash "<abs path>/record-test-evidence.sh" "<root>" "<abs evidence path>"`. The message carries both paths because a Bash tool call does not receive `CLAUDE_PLUGIN_DATA` or the session id (the check needs a carrier).

### 7.3 Other scripts

| Script | Event | Behavior |
|---|---|---|
| `scripts/gate-baseline.sh` | `SessionStart` (new entry in `hooks.json`, timeout 10) | Steps 1–7 of §7.2 only: writes the baseline when a `verify` config exists; always exits 0 |
| `scripts/record-test-evidence.sh <root> <evidence path>` | run by the model or a person | Reads `verify.command`, runs it at the root, writes `{"pass":bool,"exit":n,"command":"…","fingerprint":"…","at":"<UTC>"}`; the fingerprint is computed after the run; exits with the test exit code. Missing arguments, config or command → usage line, exit 64, nothing written |
| `scripts/gate-status.sh [root]` | run by a person | Prints counts of `block`, `would-block`, `release` and the last five log lines, for all roots or one. Reads the same state folder; takes `CLAUDE_PLUGIN_DATA` from the environment or `--state <dir>` |
| `scripts/guard-migrations.sh` | `PreToolUse` (unchanged matcher) | After the off-switch: resolve the root as in §7.2 step 2; no config or `migrations_guard.enabled` not `true` → exit 0. With `jq`: current parsing, unchanged. Without `jq`: the current substring fallback applies only when the config file exists and contains `"migrations_guard"`. The audit row goes to `gate.log` in the state folder, not to `.claude/guard.log` |

A shared `scripts/gate-lib.sh` (root, state folder, fingerprint, config read) is allowed; every script must still exit 0 when the library is missing. Shell scripts are LF, mode 0755, bash, and run on Git Bash for Windows, macOS and Linux (`sha256sum` or `shasum -a 256`).

### 7.4 Documentation in the same cut

`plugins/rootnode-code/README.md`: rewrite the hook section for §7 (opt-in file, watch then enforce, surfaces, caps, status script, off-switches) and remove the sentence that says chat ignores the hooks. `cc-skills-and-hooks-composition.md`: update the two `<!-- shipped: … -->` blocks to the new scripts (the packager fails on drift) and the prose around them. `remediate-mode-execution.md`: its example uses a repo-local `.claude/hooks/verify-tests.sh`; change it only where it states the plugin hook's behavior. Root `README.md`: line 49 says "Chat ignores hooks." and that the hooks run in every repository where the plugin is enabled; replace both statements with the opt-in rule, and adjust the `rootnode-code` table row only if its wording is now false (line number read 2026-11-24 at `8670edc`; locate by text). Plus A3.
