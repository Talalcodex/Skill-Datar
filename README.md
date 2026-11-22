# Skill-Datar

Engineers complete, secure, portable AI agent skills from a rough idea, prompt, workflow, or existing skill, and prepares them for marketplace submission (e.g. Agensi.io).

**Version:** 1.0.0 | **Format:** open Agent Skills (`SKILL.md`) | **Readiness:** Draft (not yet executed in any agent)

## What it does
- Analyzes your idea and picks a mode (Quick / Professional / Advanced)
- Builds the full skill folder: SKILL.md, references, templates, examples, tests
- Runs a security review and a structural validator
- Writes test cases and honest PASS / FAIL / NOT TESTED reports
- Produces marketplace listing copy and install guides

## Install
- **Claude (claude.ai):** upload `skill-datar.skill` (or the zipped folder) under Settings > Capabilities > Skills.
- **Claude Code:** copy this folder to `~/.claude/skills/skill-datar/` (or `.claude/skills/skill-datar/` in a project).
- **Other agents (Codex, Cursor, Copilot, Gemini CLI, ...):** copy the folder to that agent's skills directory; check its current docs for the path. Compatibility is partial/untested.

## Use
Say: "Create a skill that ...", "Improve this prompt into a skill", or "Audit and package my skill for Agensi".

## Validate a skill
```bash
python scripts/validate_skill.py path/to/skill-folder
```

## Known limitations
- Platform install paths change; verify against current docs.
- Test scenarios are written but only run if the host agent can execute them.
- Does not certify security or guarantee marketplace approval.

## License
MIT (see LICENSE). Change if you prefer another license.
