# Refuter brief — catalog v5.0.1 content branch, rev 3, cycle 1

You are the Refuter for branch `release/v5.0.1` in the repository at the current working directory. You review; you do not edit. Work only from the artifacts named below and return the format in field 6.

**Shell rule.** Run one pipeline per Bash call. Do not use loops, `&&` or `||` chains, `;`, or subshells; they are denied. Allowed commands: `git diff`, `git show`, `git log`, `git grep`, `tr`, `sha256sum`, `grep`. Example of an allowed call: `git show HEAD:README.md | tr -d '\r' | sha256sum`. Prefer Read, Grep and Glob for reading files. Note: Git for Windows `grep` drops a CR at line end, so a `grep -c` for `\r` returns 0 even on CRLF text; do not use it as a CR check.

## 1. Goal

Decide whether the branch implements spec §9 and §10 exactly, and whether anything in the full diff `git diff origin/main...HEAD` regresses what rev 1 and rev 2 established. Earlier ACCEPTs covered that content (rev 1 cycle 1, diff digest `457185ca…`; rev 2 cycle 1, diff digest `433bd4ec…`). Those receipts are bound to smaller diffs; this review binds to the digest in field 9.

## 2. In scope

- The spec: `design/root_DESIGN_catalog_v5.0.1_patch.md`, rev 3 + §10. Read it from HEAD: `git show HEAD:design/root_DESIGN_catalog_v5.0.1_patch.md`. §9 and §10 are new.
- The branch diff: `git diff origin/main...HEAD` (7 commits: `a88d449`, `6a257f9`, `0cab5c8`, `4538de0`, then rev 3's `7b22885` (commit 5), `05e30d9` (commit 6), `d991e02` (commit 7)). `git diff 4538de0 HEAD` isolates rev 3.
- The staged sources, on disk and untracked (read with Read): `design/staging-kf/root_CC_ENVIRONMENT_GUIDE.md`, `release-notes-v5.0.1-config.py`, `catalog-v5.0.1.md`, `CHANGELOG_v5.0.1_entry.md`.

## 3. May change

Nothing. Do not write, stage, commit or delete any file.

## 4. Verify against external artifacts

- **S1.** In both `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md` §6 and `rootnode-cc-design/references/cc-skills-and-hooks-composition.md` §5 "Bounded Stop hooks": the old sentence "Set the hook's caps to release first — …" occurs 0 times; the staged CC_EG replacement text ("Keep the no-progress cap N at or below the host cap, … so M never meets the host cap.") occurs once and verbatim; the reference's whole host-cap paragraph is a verbatim substring of the mirror. In the sketch, the comment line under `MAX_TOTAL=` is gone and the `MAX=` comment reads `# N: 2 interactive, 8 unattended; keep N ≤ CLAUDE_CODE_STOP_HOOK_BLOCK_CAP (default 8)`. The mirror's LF digest at HEAD equals the staged file's.
- **S2.** The guard's glob candidate line is `for X in migrations ./migrations ../migrations x/migrations`.
- **S3.** The "What the guard cannot see" paragraph sits after the guard sketch, carries the spec's content, and names only mechanisms the doc quotes in field 8 support. Check each claim in the paragraph against a quote.
- **S4.** The erratum is in spec §9; §4 G5 itself is unchanged (append-only).
- **S5.** Commit 7 holds exactly the six files §9 S5 lists; `design/audit-artifacts/v4.2/scratch/` is not tracked.
- **§10.** The config, umbrella and `CHANGELOG.md` LF digests at HEAD equal spec §10; `CHANGELOG.md` at HEAD is `origin/main` content + one blank line + the staged entry; the 12 `release-notes/rootnode-*-v5.0.1.md` digests equal spec §10; no other file in `release-notes/` changed; the umbrella invariants at the end of §10 hold, and each umbrella link's version matches that Skill's `metadata.version` at HEAD.
- **No regression.** Rev 3 touches no Skill file other than the composition reference; versions stay 12 at `5.0.1` and 15 at `5.0.0`; `git diff origin/main -- generate_release_notes.py build_release_artifacts.py` still changes only `CATALOG_VERSION`; the rev 1/rev 2 content of the composition reference (A1 rule text, two caps, R4 guard rules (a)–(c), R1 host-cap paragraph apart from the S1 sentence) is intact.

## 5. Not to do

- Do not raise items outside §9 and §10 as must-fixes. Report them as notes in the JSON's `notes` array. A regression of rev 1 or rev 2 content is a must-fix.
- Do not propose new features or improvements beyond the spec (§9 freeze).
- Do not review files outside the diff, except the staged sources named in field 2.
- Do not re-open the spec's §1 triage or its decisions.

## 6. Return format

Line 1: `Verdict Dictated: no`
Line 2: `Refuter <diff digest you computed>`
Then exactly one JSON object:

```json
{"verdict": "ACCEPT" | "REWORK" | "blocked", "must_fix": [{"id": "M1", "locator": "<file>:<line or quoted content>", "issue": "<what is wrong against which spec row>"}], "notes": ["<out-of-scope observation>"], "blocked_reason": ""}
```

`must_fix` is empty unless the verdict is REWORK. `blocked_reason` is non-empty only when the verdict is `blocked`.

## 7. Cap

At most 20 `must_fix` items and 10 `notes`, each at most 300 characters, and at most 6,000 characters for the whole reply.

## 8. Known

- The spec is accepted (2026-10-29; rev 2 and rev 3 the same day). §9 freezes the cut; §10 is planned release content, not findings.
- Scope rules from the controlling session prompt (`root_CC_release_v5.0.1`, pasted inline):
  - Commit 5: composition reference, CC_EG mirror, spec. Commit 6: the 12 per-Skill notes, the umbrella notes, the config, `CHANGELOG.md`. Commit 7: the six S5 files.
  - `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md` is the approved sync from `design/staging-kf/` (repo halt #5), copied with `tr -d '\r'`.
  - The per-Skill notes were generated by `py -3 generate_release_notes.py --config audit/v5_0_1-patch/release-notes-v5.0.1-config.py` (Python 3.14.3), which printed `Counts OK` (A 9, B 2, C 1, total 12).
- Builder disclosures (judge them; do not take them as settled):
  - S3: the paragraph names the `Edit` deny rule and `sandbox.filesystem.denyWrite`, the platforms the sandbox covers, the native-Windows gap, and `sandbox.failIfUnavailable`. The S3 row says "the Claude Code mechanism"; the paragraph names two because the docs split coverage between them (file tools versus subprocesses). The example `Edit(migrations/**)` deny rule is the any-depth form, matching the guard's `*/migrations/*` scope.
  - S5: G8 scan of the six files found 0 keys or tokens, 0 emails, 0 home paths; one first-name mention in prose in `root_CC_DESIGN_v42_spec.md:234` was left as is.
- Doc quotes for S3, fetched 2026-10-30 (HTTP 200), verbatim:
  - `https://code.claude.com/docs/en/permissions.md` (90,325 bytes), Read and Edit warning: "Read and Edit deny rules apply to Claude's built-in file tools, to file commands Claude Code recognizes in Bash, such as `cat`, `head`, `tail`, `sed`, and `tee`, and to the targets of Bash [redirections](#redirections) such as `> file` and `< file`. They don't apply to a command that reads files without naming them, such as `grep -r pattern .` run from the directory that holds the file, or to arbitrary subprocesses that read or write files indirectly, like a Python or Node script that opens files itself. For OS-level enforcement that blocks all processes from accessing a path, [enable the sandbox](https://code.claude.com/docs/en/sandboxing.md)."
  - Same doc: "**Deny and ask rules**: `Read(secrets/**)` matches a directory named `secrets` at any depth under the current directory, so the rule also applies to nested copies." and the table row "| `Edit(src/**)` as a deny or ask rule | Yes | Yes |".
  - Same doc: "Use `Edit(docs/**)` in place of `Write(docs/**)`, `NotebookEdit(docs/**)`, or `MultiEdit(docs/**)`".
  - `https://code.claude.com/docs/en/sandboxing.md` (107,528 bytes): "The sandbox runs on macOS, Linux, and WSL2. On native Windows, Claude Code runs commands unsandboxed. To use the sandbox on a Windows machine, run Claude Code inside a WSL2 distribution."
  - Same doc: "**Sandboxing** provides OS-level enforcement that restricts what shell commands can access at the filesystem and network level. It applies to Bash, PowerShell, and [Monitor](https://code.claude.com/docs/en/tools-reference.md#monitor-tool) tool commands and their child processes."
  - Same doc: "You can also deny write or read access using `sandbox.filesystem.denyWrite` and `sandbox.filesystem.denyRead`" and "The sandbox is off by default. To turn it on, run `/sandbox` in a session, … or set [`sandbox.enabled`](https://code.claude.com/docs/en/settings-reference#sandbox-enabled) to `true`".
  - Same doc: "By default, if the sandbox can't start because a dependency is missing or the platform is unsupported, Claude Code runs commands without sandboxing. To make Claude Code exit at startup instead, set [`sandbox.failIfUnavailable`](https://code.claude.com/docs/en/settings-reference#sandbox-failifunavailable) to `true`."
  - Same doc: "Move Windows users into a supported environment: have them run Claude Code inside WSL2 or a container".
  - `https://code.claude.com/docs/en/settings-reference.md` (442,747 bytes): "Claude Code adds your [permission rules](https://code.claude.com/docs/en/sandboxing.md#permission-rules) to the same lists: `Edit` allow and deny rules to `allowWrite` and `denyWrite`, `Read` deny rules to `denyRead`" and, for path prefixes, "`./` or no prefix | Relative to the project root for project settings".
- Gate results (end state, LF-normalized):

| ID | Result | Evidence |
|---|---|---|
| G1 | PASS | `git diff --name-status origin/main`: 97 rows (63 A, 34 M) = the 76 rev 2 rows, unchanged in status, + 21 new (15 §10, 6 §9 S5); classifier: 38 D9a evidence, 25 Skill content, 15 §10, 6 §9 S5, 5 §8.3, 3 §8.2, 2 §3 C mirrors, 1 CC_EG mirror, 1 spec, 1 §3 B F2; 0 unexpected; 0 `.jsonl` |
| G2 | PASS | Parsed `metadata.version`: 12 at `5.0.1`, 15 at `5.0.0` |
| G3 | PASS | S1 old 0 / new 1 in mirror and reference; whole paragraph found in mirror (`grep -cF` = 1); S2 line; S3 paragraph present |
| G4 | PASS | `quick_validate.py rootnode-cc-design` exit 0 |
| G5 | PASS | 16 of 16 rows, N = 2, M = 6, sketch extracted from the committed reference |
| G5b | PASS | 35 of 35 rev 2 rows + `rm -rf ../mig*` = 2; 23 audit rows; probes `ls migrations \| xargs rm` and `Get-ChildItem migrations \| Remove-Item` stay 0 (the S3 limit) |
| G6 | PASS | CC_EG mirror HEAD blob = `eab94f3f…`; 0 CR bytes (counted with `tr -cd '\r' \| wc -c`, positive control 2) in all 97 committed blobs |
| G7 | PASS | 29 artifacts, 24 `-cp` + 5 `-cc`; `dist/rootnode-catalog-v5.0.1.zip` |
| G8 | PASS | Six S5 files: 0 keys or tokens, 0 emails, 0 replacements |
| G9 | PASS | `Counts OK`; 12 note digests = spec §10; `release-notes/` gained only the 13 v5.0.1 files |
| G10 | PASS | Config, umbrella, CHANGELOG digests = spec §10; umbrella: 27 links, 12 `/v5.0.1)`, 15 `/v5.0)`, 0 `]](`, one `## Download`, 0 version mismatches; all 15 `/v5.0` tags exist on origin |
| G11 | PASS | Only `CATALOG_VERSION` `"v5.0"` → `"v5.0.1"` |

## 9. Digests

- Spec, `git show HEAD:design/root_DESIGN_catalog_v5.0.1_patch.md | tr -d '\r' | sha256sum` → `f891223c8b8c33faa525d61598de96eaeec3c28a1a3883bb95b2cfa18bed7585`
- Diff, `git diff origin/main...HEAD | tr -d '\r' | sha256sum` → `9e4e9c4ffc700ed2a6e4d8f970015dbfeb081e5223742864be0ce5a46682ff87`

Recompute both first, one call each. If either differs, return `blocked` with the mismatch as `blocked_reason`.
