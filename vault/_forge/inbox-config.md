---
type: preferences
date: 2026-03-18
status: active
source: manual
tags: [inbox, email, config, phase-2]
---

# Forge Inbox Configuration

**Inbox:** voltage.the.forge@gmail.com
**Poll interval:** Every 15 minutes (via scheduled task)
**Manual trigger:** `/check-inbox`

## Authorized Senders
Only process emails from these addresses. All others are ignored and flagged.
- jakeb11@gmail.com (Jake Brown -- primary user)

## Task Classification

### Auto-Execute (read-only, no approval needed)
These skills run immediately and draft a reply with results:
- `briefing` -- client status briefing
- `reflect` -- vault analysis
- `check-tickets` -- advance open tickets
- `weekly-report` -- weekly performance summary
- `performance-review` -- deep dive analysis

### Requires Approval (creates/modifies vault data)
These create a pending ticket and draft a "waiting for approval" reply:
- `save-decision` -- logs a strategic decision
- `create-ticket` -- creates new work items
- `process-meeting` -- creates multiple linked notes

### Always Escalate (never auto-execute)
These draft an escalation reply and create a high-priority ticket:
- Anything touching live ad platforms (budget changes, campaign edits, creative uploads)
- Anything unclear or ambiguous
- Anything from an unrecognized sender
- Anything mentioning money, billing, or access credentials

## Email Classification Keywords

### Skill Matching Patterns
- briefing/status/update/morning/how are things -> `briefing`
- reflect/analyze/patterns/review vault/second opinion -> `reflect`
- tickets/tasks/advance/check on/progress -> `check-tickets`
- weekly/week report/7 day/last week -> `weekly-report`
- performance/deep dive/campaign data/metrics -> `performance-review`
- decision/decided/we're going to/let's do -> `save-decision`
- ticket/task/todo/need to/action item -> `create-ticket`
- meeting/transcript/call notes/discussion -> `process-meeting`

### Escalation Triggers
- budget/spend/money/cost/billing
- password/credentials/access/login
- delete/remove/shut down/cancel
- urgent + unclear context

## Processing Rules
1. Search for unread emails in inbox
2. Check sender against authorized list
3. Classify the task using subject + body content
4. Extract client name if mentioned (default: ask in reply)
5. Route to appropriate skill tier (auto-execute, approval, escalate)
6. Execute or create ticket depending on tier
7. Draft reply with results or status
8. Mark email as read after processing
