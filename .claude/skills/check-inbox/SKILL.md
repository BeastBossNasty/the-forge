---
name: check-inbox
description: Poll the Forge Gmail inbox for new task emails. Classify each email, route to the appropriate skill, execute or create tickets, and send reply emails with results.
---

# Check Inbox

## Purpose
Poll the Forge Gmail inbox (voltage.the.forge@gmail.com) for unread emails, classify tasks, and route them for execution or approval.

## Sending Emails
To send a reply, use the send script:
```bash
python scripts/send_email.py "<to_address>" "<subject>" "<body>"
```
This sends directly from voltage.the.forge@gmail.com. No drafts, no manual review needed.

## Steps

1. Read `vault/_forge/inbox-config.md` for configuration (authorized senders, classification rules, gating tiers)
2. Use Gmail MCP to search for unread emails: `gmail_search_messages` with query `is:unread`
3. For each unread email:
   a. Read the full message with `gmail_read_message`
   b. **Sender check:** Verify sender is on the authorized list. If not, skip and log it.
   c. **Classify the task:** Analyze subject + body against the classification keywords in inbox-config.md
   d. **Extract client name:** Look for client references (truniagen, bella-luna, sandbox, etc.). If no client is mentioned, note it as "client unspecified."
   e. **Route based on tier:**

### Auto-Execute Tier
If the task maps to a read-only skill (briefing, reflect, check-tickets, weekly-report, performance-review):
1. Run the matched skill using the client vault
2. Send a reply email via `scripts/send_email.py` with the skill output
3. Save a processing log entry (see format below)

### Approval Tier
If the task maps to a write skill (save-decision, create-ticket, process-meeting):
1. Create a ticket in the relevant client's `tickets/` folder describing the requested action
2. Set ticket status to `open` with tag `email-intake`
3. Send a reply: "Got it. I've created a ticket for [summary]. Waiting for your approval before executing. Run `/check-tickets [client]` to review and advance."
4. Save a processing log entry

### Escalation Tier
If the task involves live platforms, money, credentials, or is ambiguous:
1. Create a high-priority ticket in the relevant client's `tickets/` (or `_forge/` if no client)
2. Send a reply: "This request needs your direct input before I can act. I've flagged it as [reason]. Details in ticket: [filename]"
3. Save a processing log entry

### Unclassifiable
If the email doesn't match any known pattern:
1. Send a reply: "I received your email but I'm not sure what action to take. Can you clarify? Here's what I understood: [summary of email content]"
2. Create a ticket tagged `email-intake, needs-clarification`

4. After processing all emails, output a summary

## Processing Log Format
Save to `vault/_forge/learnings/` as `YYYY-MM-DD-inbox-processing.md` (append if file already exists for today):

```
### [HH:MM] Email from [sender]
**Message ID:** [Gmail message ID -- REQUIRED for dedup]
**Subject:** [subject]
**Classification:** [auto-execute | approval | escalate | unclassifiable]
**Skill matched:** [skill name or "none"]
**Client:** [client or "unspecified"]
**Action taken:** [what was done]
```

## Output Format

### Inbox Summary
- Emails processed: [count]
- Auto-executed: [count and brief descriptions]
- Awaiting approval: [count and brief descriptions]
- Escalated: [count and brief descriptions]
- Unclassifiable: [count and brief descriptions]
- Unauthorized senders: [count, if any]

### Actions Taken
List each email and what was done.

### Emails Sent
List reply emails sent with recipient and subject.

## Deduplication
The Gmail MCP does not have a "mark as read" tool. Processed emails stay unread in Gmail. To avoid reprocessing:
1. Every processed email's Gmail message ID is recorded in the processing log (the `**Message ID:**` field)
2. Before processing any email, search ALL processing log files (not just today's) for the message ID using Grep
3. If the message ID is already in any log file, skip it entirely
4. Future fix: add Gmail label "processed" via Gmail API or MCP update

## Rules
- All replies are SENT directly via scripts/send_email.py. No drafts.
- Never auto-execute anything that modifies live ad platforms.
- Never process emails from unauthorized senders (log them and skip).
- If client is unspecified in an auto-execute task, send a reply asking which client instead of guessing.
- Check for duplicate tickets before creating new ones (same subject from same day).
- Follow Voltage brand voice in all replies (no em dashes, plain English, confident and direct).
