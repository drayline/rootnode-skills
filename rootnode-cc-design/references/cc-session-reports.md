# CC Session Reports

The output standard for the durable record a Claude Code run leaves behind. Read it when the deliverable is a CC initial prompt, session prompt, or autonomous prompt — every one of them ends with a "Write session report" item — and when designing the audit convention for a delivery repo.

For the prompt patterns this standard plugs into, see `cc-prompt-design-patterns.md` §6 and §10. For the end-of-sitting handoff document (a different artifact), see `rootnode-session-handoff` if available.

---

## Table of contents

1. Why a session report is mandatory
2. Where it goes and what it is called
3. The schema — computed, not narrated
4. Field rules
5. What the standard does not import
6. Paste-ready prompt block
7. Report template

---

## 1. Why a session report is mandatory

Two RSA runs produced no durable record: the prompt's scope never authorized a report write, and the completion report pasted into chat was gone with the chat. A run whose only record is a chat message cannot be audited, resumed by a different session, or compared with the next run. `[generalizable: RSA runs 2026-09, operator EVOLVE design 2026-09-17]`

The fix sits in the prompt, not in the agent's judgment: every CC prompt authorizes the report write in its scope and ends with a "Write session report" item. The item runs on every outcome — completed, halted, or blocked. A halted run needs the report most, because the next session starts from it.

**Computed, not narrated.** The report records state the run can compute — SHAs, LF digests, `git diff --name-status` rows, gate results with their evidence, findings with locators — and names what it does not prove. A narrated report ("all tests pass", "updated the three files") is a memory of the work, and memories drift from the artifact. Every field below is filled by copying command output, per the bookkeeping-in-tools principle (`cc-prompt-design-patterns.md` §2, P6). `[generalizable]`

---

## 2. Where it goes and what it is called

- **Directory:** the delivery repo's own audit convention, carried in the design brief as `report_dir` (`schema/cc-design-brief.schema.json`). Default `reports/`. Repos differ — RSA uses `reports/`; rootnode-skills uses `audit/phase-XX/` and `design/audit-artifacts/vN.N/` — which is why the location is a brief parameter and not a constant.
- **Filename:** `<descriptive_name>_{YYYYMMDD-HHMM}Z.md`, from `date -u +%Y%m%d-%H%M`. A date alone collides on same-day runs; the `HHMM` stamp matches the session-handoff convention.
- **Commit:** the report is not committed by the prompt that writes it. It rides the next commit cycle, so the run's own commit set stays exactly what the prompt authorized.

---

## 3. The schema — computed, not narrated

| Field | Content | Why computed |
|---|---|---|
| `prompt` | governing prompt path + its LF-sha256 | Provenance, not identity — a field belongs in a fingerprint only if a human-visible change moves it |
| `outcome` | `COMPLETED` / `HALTED <trigger #>` / `BLOCKED` | `BLOCKED` is distinct from "nothing to report" |
| `started` / `ended` | UTC from `date -u` | Never hand-written |
| `pre_state` | branch, HEAD SHA, `git status --porcelain \| wc -l` | Report-only — the end-state rule forbids halting on it |
| `post_state` | HEAD SHA or "uncommitted", plus LF-sha256 per replaced file, matched to the prompt's end-state digests | The halt binds here |
| `files_changed` | rows from `git diff --name-status <pre_sha>` plus untracked files; count summed from the rows | Summary-vs-itemization rule |
| `gates` | id · command · `PASS` / `FAIL` / `NOT_RUN` · evidence (quoted output line or log path) | `NOT_RUN` ≠ `PASS` |
| `findings` | F-n · severity · `path:line` · open / resolved · owner; IDs persist across continuation prompts | A content-anchored ledger |
| `operator_decisions` | the verbatim reply + the halt it answered | Never summarized |
| `observations` | each tagged `[observed]` or `[inferred]` | Separates what was seen from what was concluded |
| `not_verified` | mandatory; "None identified." when empty | A criterion that silence can satisfy measures nothing |
| `kf_deltas` | pointer to the surfaced KF-update blocks, or "none — confirmed" | Mirrors session-handoff's gate; the report does not duplicate the handoff |

---

## 4. Field rules

- **Commands, not prose.** Each computed field names the command that produced it. The model copies the output; it does not count, hash, or summarize in its head.
- **Pre-state is report-only.** A stale starting condition is recorded, never halted on. The halt binds to `post_state` digests (`cc-prompt-design-patterns.md` §10, end-state rule; LF-normalize before hashing).
- **Counts come from rows.** `files_changed` is a list first; the count is the number of rows, computed when the report is written. A headline count that disagrees with its rows is a defect in the report.
- **Gates have three results.** A gate whose tool was unavailable, or whose command failed to start, is `NOT_RUN` with the reason as evidence — never `PASS`. A bounded Stop hook that released on its no-progress cap is recorded `NOT_RUN` (`cc-skills-and-hooks-composition.md` §5).
- **`BLOCKED` is not empty.** A run that could not inspect what it was asked to inspect reports `BLOCKED` with the cause, never an empty findings list (`cc-delegation-patterns.md` §3).
- **Finding IDs persist.** A finding keeps its F-n from first report to resolution across continuation prompts, so a later report shows which findings closed, which stayed open, and which are new.
- **Decisions are verbatim.** Paste the operator's reply exactly, with the halt number it answered. A paraphrase loses the ambiguity the continuation-phrase gate exists to catch.
- **Assumption tags survive.** A `[speculation]` or `[assumption]` tag carried from the brief stays on the fact in the report until the operator confirms it (`source-grading-and-tagging.md` §4).
- **`not_verified` is never omitted.** Write what the run did not check — a gate not run, a path not exercised, a claim taken from a doc rather than the running version. "None identified." is written only after looking.

---

## 5. What the standard does not import

From awslabs/aidlc-workflows the standard takes the ledger and the `blocked` outcome; it does not take the 121-event audit taxonomy, sharded event logs, hook-emitted audit rows, or readiness and risk scores. A single-prompt report is a final snapshot, not an event stream. A deployment that needs an event stream designs it as a hook-backed log separately; the report then points at the log. `[practitioner: awslabs/aidlc-workflows v2.11.1 audit-and-review slice; not adopted]`

The report is not a session handoff. The handoff is written when a design sitting closes and carries forward intent; the report is written by the CC run and records computed state. Where both exist, the report's `kf_deltas` field points at the handoff rather than repeating it.

---

## 6. Paste-ready prompt block

Add the scope line and the final item to every CC prompt. Fill `<report_dir>` from the brief and `<run_name>` from the prompt's own name.

```markdown
## Scope — in-scope (addition)
- Write the session report to <report_dir>/<run_name>_<YYYYMMDD-HHMM>Z.md
  (stamp from `date -u +%Y%m%d-%H%M`). Do not commit it; it rides the next commit cycle.

## Pre-flight — record for the report (report-only; never a halt condition)
- `date -u +%Y-%m-%dT%H:%MZ`
- `git branch --show-current`
- `git rev-parse HEAD`
- `git status --porcelain | wc -l`

## Final item — Write session report
Write the report on every outcome — COMPLETED, HALTED <trigger #>, or BLOCKED —
before ending the turn. Fill each field by copying command output:
- prompt: this file's path and `tr -d '\r' < <prompt path> | sha256sum`
- post_state: `git rev-parse HEAD` (or "uncommitted"), and for each replaced file
  `tr -d '\r' < <file> | sha256sum`, matched against this prompt's end-state digests
- files_changed: `git diff --name-status <pre_sha>` plus
  `git ls-files --others --exclude-standard`; the count is the number of rows
- gates: one row per gate — id, command, PASS / FAIL / NOT_RUN, quoted evidence line or log path
- operator_decisions: each reply verbatim, with the halt it answered
- not_verified: required; write "None identified." only after checking
Use the template in cc-session-reports.md §7.
```

---

## 7. Report template

```markdown
---
prompt: <path> @ <LF-sha256>
outcome: COMPLETED | HALTED <trigger #> | BLOCKED
started: <date -u output>
ended: <date -u output>
---

# Session report — <run name>

## Pre-state (report-only)
| Branch | HEAD | Dirty paths |
|---|---|---|
| <branch> | <sha> | <n> |

## Post-state
HEAD: <sha | uncommitted>

| File | LF-sha256 | Expected (prompt) | Match |
|---|---|---|---|

## Files changed — <n> rows
<git diff --name-status rows, then untracked files>

## Gates
| ID | Command | Result | Evidence |
|---|---|---|---|

## Findings
| ID | Severity | Locator | Status | Owner |
|---|---|---|---|---|

## Operator decisions
> <verbatim reply> — answered halt <#>

## Observations
- [observed] <what the run saw>
- [inferred] <what the run concluded>

## Not verified
- <item> — or "None identified."

## KF deltas
<pointer to surfaced blocks> | none — confirmed
```

---

## End of CC session reports reference
