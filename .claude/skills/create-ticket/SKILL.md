---
name: create-ticket
description: Create a trackable work item with clear acceptance criteria, priority, due date, and links to related vault notes.
---

# Create Ticket

## Purpose
Create a trackable work item with clear acceptance criteria.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Parse the task from conversation context, or ask Jake to describe it.
3. Determine:
   - Short title
   - Description (what needs to be done and why)
   - Acceptance criteria (specific, checkable items)
   - Priority/importance (low, medium, high)
   - Due date (ask Jake if not obvious)
   - Assignee (if applicable)
4. Check for related projects, decisions, or pipeline items to link
5. Create the ticket in `vault/_clients/[client]/tickets/` with filename `YYYY-MM-DD-short-description.md`

## Note Format

```markdown
---
type: ticket
client: [client-slug]
date: YYYY-MM-DD
status: open
source: manual
confidence: 0.8
importance: [low | medium | high]
tags: [ticket]
related:
  - "[[related-note]]"
due: YYYY-MM-DD
assignee: ""
---

# [Short title]

## Description
[What needs to be done and why]

## Acceptance Criteria
- [ ] [Criteria 1]
- [ ] [Criteria 2]

## Notes
(Agent adds timestamped notes as work progresses)
```

## Rules
- Acceptance criteria must be specific and checkable, not vague.
- Always include a due date. Ask Jake if one isn't obvious.
- Link to related vault notes when relevant.
