Run the code-review skill to audit code, data accuracy, or system gaps: $ARGUMENTS

Read and follow the skill instructions in .claude/skills/code-review/SKILL.md

Modes:
- No arguments: review uncommitted changes via Codex CLI
- "report [client]": data audit the latest report for that client
- "gaps": run gap analysis on the full system
- [filepath]: review a specific file
