---
name: performance-review
description: Deep dive performance analysis with campaign-level data. Pulls detailed platform metrics, compares against benchmarks, evaluates decision outcomes, and provides actionable recommendations.
---

# Performance Review

## Purpose
Deep dive analysis with campaign-level data.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Read client vault:
   - `benchmarks/performance-benchmarks.md` for KPI targets
   - `decisions/` for recent decisions
   - `lessons/` for relevant learnings
   - `anomalies/` for recent anomalies
3. Pull detailed platform data if available:
   - Campaign-level: spend, impressions, clicks, CTR, CPC, conversions, CPA, ROAS
   - Last 7 days vs previous 7 days comparison
4. Compare against benchmarks
5. Check if recent decisions are playing out as expected
6. Reference `vault/_agency/playbooks/` for best practices
7. Auto-save per vault rules:
   - Anomalies to `anomalies/` if any metric is outside acceptable range (check for duplicates first)
   - Weekly snapshot to `snapshots/`
   - Flag decision outcomes for Jake to review
   - Auto-trigger score-decisions skill (`.claude/skills/score-decisions/SKILL.md`) against all active decisions. Append 4D scores to decision notes.

## Output Format

### Overall Health
One sentence summary.

### Platform-by-Platform Breakdown
For each platform with data:
- Key metrics with week-over-week trends
- Campaign-level performance highlights and lowlights
- What's working and what's not
- Comparison against benchmarks

### Decision Outcomes
How recent decisions are performing. Reference specific decision notes. Flag any ready for review.

### Recommendations
Specific, actionable next steps with reasoning. Reference playbooks and benchmarks. Prioritize by impact.

### Saved to Vault
List any auto-saved notes with file paths.

## Rules
- Be specific with numbers. Always include actual values and percentage changes.
- If live data is unavailable, say so plainly. Do not invent metrics.
- Compare against client benchmarks, not arbitrary numbers.
- For TruNiagen: apply LTV multiplier when evaluating ROAS. Raw ROAS understates actual value.
- For Bella Luna: remember the 10x+ ROAS threshold and two-campaign structure.
- Flag decision outcomes but do not auto-convert to lessons.
