---
name: save-decision
description: Log a strategic decision with full context, reasoning, expected outcome, and review date. Saves to the client's decisions folder in the vault.
---

# Save Decision

## Purpose
Log a decision with full context so future reviews can evaluate whether it worked.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Ask Jake to describe the decision, or parse it from the conversation context if it's already been discussed.
3. Read client context for background:
   - `benchmarks/performance-benchmarks.md` for KPI context
   - `decisions/` for recent decisions (to avoid contradictions and to link related decisions)
   - `lessons/` for relevant learnings
4. Create a decision note in `vault/_clients/[client]/decisions/` with the filename format `YYYY-MM-DD-short-description.md`
5. Link to related benchmarks, lessons, or previous decisions via `[[wikilinks]]`

## Note Format

```markdown
---
type: decision
client: [client-slug]
date: YYYY-MM-DD
status: active
source: manual
confidence: [0.0-1.0]
importance: [low | medium | high]
tags: [relevant, tags]
related:
  - "[[related-note]]"
---

# [Short description of decision]

**Decision:** [What was decided]

**Reasoning:**
[Why -- reference data, benchmarks, patterns]

**Expected outcome:**
[What should happen if this works]

**Review date:** YYYY-MM-DD

Related: [[links]]
```

## Rules
- Always include what was decided and why.
- Always include an expected outcome and a review date.
- Set the review date based on how long the decision needs to play out (typically 7-14 days for ad optimizations).
- Link to related notes with wikilinks.
- Ask Jake for confidence level if not obvious from context. Default to 0.8.
- This is a manual-save skill. The note is always saved (it's the whole point of the command).
