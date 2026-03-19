---
name: daily-briefing
description: Generate a morning status briefing for a client. Reads vault data, pulls live metrics if available, compares against benchmarks, and flags items needing attention.
---

# Daily Briefing

## Purpose
Morning status update. What happened, what needs attention, what to do today.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Read the client's vault:
   - `benchmarks/performance-benchmarks.md` for KPI targets
   - `decisions/` for recent decisions (last 14 days)
   - `lessons/` for client-specific learnings
   - `anomalies/` for recent anomalies
   - `pipeline/content-calendar.md` for upcoming items
   - `tickets/` for open tickets
   - `projects/` for active projects
3. Check `vault/_agency/lessons/` for cross-client learnings that may apply
4. If a platform MCP or Browser MCP is available, pull today's performance data
5. Compare current performance against client benchmarks
6. Flag anything outside acceptable ranges
7. Auto-save per vault rules:
   - Anomalies: if any metric is outside the acceptable range defined in benchmarks, save to `anomalies/`. Check for existing anomaly notes with the same issue before creating duplicates.
   - Snapshots: if live data was pulled, save a dated snapshot to `snapshots/`.

## Output Format

### Performance Snapshot
Key metrics vs benchmarks. If live data is unavailable, state exactly what is missing. Do not invent metrics.

### Recent Decisions
What was decided recently and early signals on outcomes. Reference the decision notes.

### Flags
Anything that needs attention today: anomalies, overdue reviews, approaching deadlines, tickets due soon.

### Suggested Actions
What to consider doing today. Be specific and actionable.

### Saved to Vault
List any auto-saved notes (anomalies, snapshots) with file paths.

## Rules
- Never hallucinate metrics. Only report what you can actually see in a file or platform.
- If live data is unavailable, say so plainly.
- Compare against client benchmarks, not arbitrary numbers.
- Check for duplicate anomaly notes before saving.
