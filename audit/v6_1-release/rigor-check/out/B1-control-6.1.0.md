I used the cc-design skill but kept it light. A one-person tool with no production data doesn't need subagents, custom skills, MCP servers, hooks, or a design-brief interview, so I left those out.

The one real risk is that **renaming can destroy files**: a name collision can overwrite a photo, or a test or manual run can touch your actual photo library. Everything below is aimed at that. Nearly all the protection is built into the tool itself rather than into Claude Code configuration.

## 1. Environment

| Layer | What | Why |
|---|---|---|
| `CLAUDE.md` | ~40 lines, below | Commands, the safety rules and what's in scope |
| `.claude/settings.json` | Allow pytest and read-only git commands | Fewer permission prompts during the test loop |
| Hooks | None | A hook can't reliably tell a run on your photo library from any other run. Making dry-run the default and refusing to overwrite are stronger protections, and they also protect you when you use the tool yourself |
| Skills / subagents / MCP | None | Nothing they would fix. Revisit only if a real problem shows up |
| Git | `git init` before the first session if you haven't | Lets you undo anything Claude does |

**`.claude/settings.json`**
```json
{
  "permissions": {
    "allow": [
      "Bash(pytest:*)",
      "Bash(python -m pytest:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)"
    ]
  }
}
```

**`CLAUDE.md`**
```markdown
# photo-renamer

Personal CLI: renames photo files to their EXIF capture date. Single user, Windows.

## Commands
- Test: `python -m pytest -q`
- Run (dry): `python -m photorename <dir>`  — prints planned renames, changes nothing
- Run (real): `python -m photorename <dir> --apply`

## Safety rules (non-negotiable)
- Dry-run is the default. Only `--apply` touches the filesystem.
- Never overwrite an existing file. On collision, append `_1`, `_2`, …
- Never delete files. Rename only.
- Tests use pytest `tmp_path` only. Never point the tool or a test at a real
  photo directory (e.g. ~/Pictures, OneDrive). Generate fixture images in tests
  with Pillow; do not commit binary photos.
- Re-running on an already-renamed folder must be a no-op.

## Behavior spec
- Date source, in order: EXIF DateTimeOriginal → DateTimeDigitized → DateTime.
  No EXIF date → skip and report (do NOT fall back to file mtime unless
  `--fallback-mtime` is passed).
- Name format: `YYYY-MM-DD_HHMMSS<ext>`, extension lowercased.
- Sidecars (`.xmp`, `.aae`) with the same stem are renamed alongside their photo.
- Exit code non-zero if any file was skipped due to error.

## Conventions
- Keep EXIF reading, name planning, and filesystem ops in separate functions;
  planning is pure and is where most tests live.
- Dependencies: Pillow only. Ask before adding anything else (e.g. pillow-heif for HEIC).

## Stop and ask if
- Existing tests fail before you've changed anything.
- A change would weaken any safety rule above.
- You need a new dependency.
- The spec is ambiguous for a case you've hit (e.g. timezone offsets, burst
  shots with identical timestamps beyond the suffix rule).
```

## 2. First session prompt

Start Claude Code in plan mode (Shift+Tab) for this first session, so you approve the plan before any files change.

```
Read CLAUDE.md, then look at what already exists in the repo (code, tests,
pyproject/requirements). Run the test suite and tell me the result before
changing anything.

Goal for this session: a working dry-run + --apply rename for JPEGs, per the
behavior spec in CLAUDE.md.

Approach:
1. Propose a short plan: module layout, function boundaries (read date / plan
   renames / execute plan), and the test list. Wait for my OK.
2. Write tests first, using Pillow to generate JPEGs with EXIF in tmp_path.
   Must cover: normal rename, collision suffixing, missing EXIF skipped,
   idempotent re-run, sidecar follows photo, dry-run changes nothing,
   --apply never overwrites.
3. Implement until green. Run the full suite after each meaningful change.

Out of scope this session: HEIC/RAW, timezone handling, recursion into
subfolders, mtime fallback. Note anything you think belongs on that list.

Done means: all tests pass, and `python -m photorename <tmp dir>` shows a
sensible dry-run. Finish with a short summary: files changed, test count
and result, anything you skipped or are unsure about. Don't commit; I'll
review and commit.
```

## 3. When to change this setup

- **Claude does the same wrong thing twice:** add one line to CLAUDE.md. Use a hook only if the CLAUDE.md line doesn't stop it.
- **You add HEIC or RAW support:** update the dependency rule and decide how to handle timezones before that session starts.
- **CLAUDE.md passes ~100 lines:** trim it. At this project's size, a long CLAUDE.md is a bad sign.

I made a few product choices on your behalf: no fallback to the file's modified time unless you pass a flag, sidecar files get renamed with their photo, and the name format is `YYYY-MM-DD_HHMMSS`. Change them in the spec before the first session if you want different behaviour.

I dropped some things the skill normally includes: the design-brief interview, saved session-report files and subagent planning. The short summary at the end of the session prompt replaces the reports.