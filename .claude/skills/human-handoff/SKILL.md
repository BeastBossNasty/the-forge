---
name: human-handoff
description: Handle tasks that require human intervention. Create a structured handoff request, notify Jake via email, and pause execution until human input is received.
---

# Human Handoff

## Purpose
When The Forge encounters a task that requires human intervention (logging into a platform, visual verification, approval of sensitive action, etc.), this skill creates a structured handoff, pauses execution, and notifies Jake.

## When to Use
- A task requires logging into a platform The Forge doesn't have MCP access to
- Visual verification is needed (reviewing creative assets, checking a live page)
- A sensitive action needs human approval beyond the normal gating tiers
- A task requires interacting with a UI that The Forge can't automate
- Payment or financial action is needed
- A third-party needs to be contacted by phone or in person

## Steps

1. **Document the handoff:**
   Create a handoff ticket:
   - If client-scoped: save to `vault/_clients/[client]/tickets/`
   - If Forge-scoped (no client, e.g., from self-improve or capability-sprint): save to `vault/_forge/improvement-queue/`
   ```yaml
   type: ticket
   status: open
   source: [originating-skill]
   importance: [based on urgency]
   tags: [human-handoff, ticket]
   assignee: "Jake"
   # Include resume context so the blocked task can continue:
   resume_skill: [skill that was running when handoff was triggered]
   resume_context: [serialized state: client, step number, partial results, etc.]
   ```

2. **Include clear instructions:**
   - What needs to be done (specific, step-by-step)
   - Why The Forge can't do it (missing access, requires visual check, etc.)
   - What information The Forge needs back to continue
   - Any context from the current task (URLs, account names, data gathered so far)
   - What The Forge will do once the human step is complete

3. **Notify Jake:**
   Send an email via `scripts/send_email.py`:
   ```
   Subject: [Forge] Human action needed: [short description]
   Body: [Summary of what's needed, link to ticket file, urgency level]
   ```

4. **Pause and wait:**
   - Note in the ticket that The Forge is paused on this step
   - The ticket's acceptance criteria should include a checkbox for the human step
   - When Jake runs `/check-tickets [client]`, the ticket will surface as needing input

5. **Resume after human action:**
   - When the ticket's human step is checked off, The Forge reads `resume_skill` and `resume_context` from the ticket frontmatter
   - The Forge re-invokes the originating skill with the saved context, skipping already-completed steps
   - If `resume_skill` or `resume_context` is missing, The Forge asks Jake what to do next instead of silently failing
   - Jake can also manually trigger the next step by running the relevant command directly

## Handoff Ticket Format

```markdown
---
type: ticket
client: [client-slug]
date: YYYY-MM-DD
status: open
source: [originating-skill]
importance: [high | medium]
tags: [human-handoff, ticket]
related:
  - "[[originating-project-or-ticket]]"
due: YYYY-MM-DD
assignee: "Jake"
---

# Human Action Needed: [Short description]

## What's Needed
[Step-by-step instructions for the human action]

## Why The Forge Can't Do This
[Specific reason: no MCP access, needs visual review, requires credentials, etc.]

## Context
[Any data, URLs, or progress from the current task]

## What Happens After
[What The Forge will do once this step is complete]

## Acceptance Criteria
- [ ] [Human step described clearly]
- [ ] Notify The Forge by checking this box and running /check-tickets
```

## Output Format

### Handoff Created
- Ticket: [filepath]
- Assigned to: Jake
- Reason: [why human needed]
- Email notification: [sent/failed]
- Blocked task: [what's waiting on this]

## Rules
- Always send an email notification. Don't rely on Jake finding the ticket.
- Be specific about what needs to be done. Don't say "check the campaign" -- say "log into Meta Ads Manager, navigate to Campaign ID 123456, verify the budget is set to $180/day."
- Include everything Jake needs to complete the step without asking follow-up questions.
- Set an appropriate due date based on urgency.
- If the originating task was from an email, include the original email context.
