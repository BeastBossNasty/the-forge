---
name: weekly-report
description: Weekly performance summary with decision outcome tracking. Pulls platform data if available, compares against benchmarks, and tracks how recent decisions are performing.
---

# Weekly Report

## Purpose
Weekly performance summary with decision outcome tracking.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Read client vault:
   - `benchmarks/performance-benchmarks.md` for KPI targets
   - `decisions/` for decisions from the past 7-14 days
   - `lessons/` for relevant learnings
   - `anomalies/` for recent anomalies
3. Pull platform data if available (7-day vs previous 7-day comparison)
4. Compare against benchmarks
5. Check if recent decisions are playing out as expected
6. Reference `vault/_agency/playbooks/` for best practices
7. Auto-save per vault rules:
   - Weekly snapshot to `snapshots/` with filename `YYYY-MM-DD-weekly-snapshot.md`
   - Anomalies to `anomalies/` if any metric is outside acceptable range (check for duplicates first)
   - Flag decision outcomes for Jake to review (do not auto-convert decisions to lessons)

## Output Format

### Overall Health
One sentence summary of account performance this week.

### Platform Breakdown
Metrics, trends, what's working, what's not. Compare against benchmarks.

### Decision Outcomes & 4D Scores
How recent decisions are performing. Reference specific decision notes. Flag any that are ready for review (validated or failed).
**Auto-trigger:** Run the score-decisions skill (`.claude/skills/score-decisions/SKILL.md`) against all decisions from the past 14 days. Append scoring results to decision notes. Highlight any with confidence > 70% that should be converted to lessons or reverted.

### Recommendations
Specific, actionable next steps with reasoning. Reference playbooks and benchmarks.

### Saved to Vault
List any auto-saved notes (snapshots, anomalies) with file paths.

## Rules
- Be specific with numbers. "CPA decreased 12% to $24.80" not "CPA improved."
- If live data is unavailable, say so plainly. Do not invent metrics.
- Compare against client benchmarks, not arbitrary numbers.
- Flag decision outcomes but do not auto-convert to lessons. Jake decides.
