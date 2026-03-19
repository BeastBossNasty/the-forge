---
type: lesson
date: 2026-03-18
status: active
source: manual
importance: high
tags: [auto-save, vault, process]
---

# Auto-Save Findings Pattern

**Context:** Skills that pull live platform data need a consistent pattern for writing noteworthy findings back to the vault without requiring human approval for every write.

**Lesson:** Any skill pulling live data should write findings back to the vault following these rules:

**Auto-save (no human approval needed):**
- Anomalies: any metric outside the client's acceptable range goes to `anomalies/`
- Snapshots: periodic performance data captures go to `snapshots/`
- Always check for existing notes before creating new ones to prevent duplicates on repeated runs

**Never auto-save (requires human judgment):**
- Decisions
- Lessons
- Validated decisions being converted to lessons

When a decision outcome becomes clear (validated or failed), flag it in the output for Jake to act on. Do not auto-convert.

**Applies to:** All skills that access live platform data (briefing, weekly-report, performance-review)
