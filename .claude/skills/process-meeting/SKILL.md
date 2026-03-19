---
name: process-meeting
description: Extract structured information from a meeting transcript or notes. Creates meeting note, decision notes, and optionally tickets for action items.
---

# Process Meeting

## Purpose
Extract structured information from a meeting transcript or notes.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Read the transcript or notes provided by Jake (pasted in conversation or pointed to a file).
3. Extract:
   - Decisions made
   - Action items with owners and due dates
   - Key insights or discussion points
   - Follow-up dates
4. Create a meeting note in `vault/_clients/[client]/meetings/` with filename `YYYY-MM-DD-meeting-topic.md`
5. For each decision extracted: create a separate decision note in `decisions/` (follow the save-decision skill format)
6. For each action item: ask Jake if a ticket should be created in `tickets/`
7. Link everything together with `[[wikilinks]]`

## Meeting Note Format

```markdown
---
type: meeting
client: [client-slug]
date: YYYY-MM-DD
time: "HH:MM"
status: active
source: meeting-processor
importance: medium
tags: [meeting]
related:
  - "[[decision-note]]"
  - "[[ticket-note]]"
---

# [Meeting title / topic]

## Attendees
[List of attendees]

## Key Decisions
[Decisions made -- each also saved as a separate decision note]

## Action Items
- [ ] [Action item] -- Owner: [name] -- Due: [date]

## Notes
[Any other important context or discussion points]
```

## Rules
- Every decision gets its own decision note, not just a line in the meeting note.
- Action items need owners and due dates. Ask Jake if not clear from the transcript.
- Link all created notes back to the meeting note and to each other.
- Ask before creating tickets for action items (don't auto-create).
