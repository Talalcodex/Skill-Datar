# Platform compatibility

Core rule: write one portable SKILL.md (name + description frontmatter, markdown body). Keep platform specifics in adapters/ or the README.

Status labels: **Verified** (installed and invoked successfully, with evidence), **Partial** (follows the open Agent Skills format but not confirmed), **Untested**.

| Agent | Typical location / method | Default status |
|---|---|---|
| Claude (claude.ai) | Zip the skill folder as .skill/.zip and upload under Settings > Capabilities > Skills | Untested until installed |
| Claude Code | Folder in `~/.claude/skills/<name>/` or project `.claude/skills/<name>/` | Untested until installed |
| Claude Cowork | Upload/install as a skill or plugin | Untested |
| OpenAI Codex / Codex CLI | Agent Skills folders; check current Codex docs for the skills directory | Partial |
| Cursor | Agent Skills support or project rules; check current docs | Partial |
| GitHub Copilot | Agent skills / instruction files; check current docs | Partial |
| Gemini CLI, Windsurf, Cline | Verify current conventions first | Unverified |

Locations change between releases. If web access exists, check each platform's current documentation before writing install steps; otherwise state that the path is unconfirmed. Do not promise automatic activation anywhere.
