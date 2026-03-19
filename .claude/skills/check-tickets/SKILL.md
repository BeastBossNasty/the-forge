---
name: check-tickets
description: Advance all open tickets for a client. Complete work, close finished items, flag blockers, and request human input when needed.
---

# Check Tickets

## Purpose
Advance all open tickets. Complete work, close finished items, flag blockers.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Read all files in `vault/_clients/[client]/tickets/`
3. Find every ticket with `status: open` or `status: in-progress`
4. For each ticket, review the acceptance criteria checklist
5. If criteria can be completed now: do the work, check off criteria, add a timestamped note
6. If all criteria are checked: set `status: closed`, add a completion note with timestamp
7. If blocked: note why, skip to next
8. If needs human input: flag and move on
9. If a closed ticket produced a learning: write it to `lessons/` and link it back to the ticket
10. Check for overdue tickets (past their `due:` date). If found, auto-save an anomaly to `anomalies/` (check for existing notes first to prevent duplicates).

## Output Format

### Tickets Closed
List of tickets that were fully completed and closed this run.

### In Progress
What was advanced and what remains on each ticket.

### Blocked
What's stuck and why.

### Needs Your Input
Decisions or approvals required from Jake.

### Overdue
Tickets past their due date.

### Saved to Vault
List any auto-saved notes (lessons from closed tickets, overdue anomalies).

## Rules
- Only check off criteria that are genuinely completed.
- Add timestamped notes when advancing work (format: `[YYYY-MM-DD HH:MM] Note text`).
- Do not close tickets with unchecked criteria.
- Check for duplicate anomaly notes before saving overdue alerts.
