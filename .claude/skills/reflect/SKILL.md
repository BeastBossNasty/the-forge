---
name: reflect
description: Independent analysis of a client's vault. Looks for overdue reviews, contradictions, patterns, gaps, opportunities, and risks. Vault-only analysis, no live data.
---

# Reflect

## Purpose
Independent analysis. Not answering a specific question -- forming observations about patterns, risks, and opportunities the account manager might not have asked about.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Read the client's full vault:
   - `decisions/` -- all decisions, especially status and review dates
   - `lessons/` -- client-specific learnings
   - `anomalies/` -- past and current anomalies
   - `benchmarks/performance-benchmarks.md` -- KPI targets
   - `brand/` -- brand voice, creative guidelines, audiences
   - `pipeline/content-calendar.md` -- upcoming work
   - `projects/` -- active projects and task status
   - `tickets/` -- open and in-progress tickets
   - `meetings/` -- recent meeting notes
   - `stakeholders/` -- key contacts
3. Check `vault/_agency/lessons/` for cross-client learnings that apply
4. Check `vault/_agency/playbooks/` for relevant best practices
5. Analyze holistically. Look for:
   - **Overdue reviews:** decisions or anomalies past their review date
   - **Contradictions:** recent decisions that conflict with existing lessons or benchmarks
   - **Patterns:** recurring themes across decisions (repeated reverts, same issue resurfacing)
   - **Stale data:** benchmarks, brand docs, or pipeline items not updated in a while
   - **Gaps:** missing context that would help future briefings
   - **Opportunities:** things working well that could be doubled down on
   - **Risks:** upcoming deadlines with unfinished dependencies, projects with no progress

## Output Format

### Overdue Reviews
Decisions or anomalies past their review date.

### Patterns
Recurring themes, repeated issues, or trends across the vault.

### Contradictions and Gaps
Conflicting information or missing context.

### Opportunities
What's working that could be expanded.

### Risks
Upcoming deadlines, stalled projects, unresolved blockers.

### Recommendation
The single most important thing to address right now.

## Rules
- Do NOT pull live platform data. This is vault-only analysis.
- Keep it concise and opinionated. This is a second opinion, not a status report.
- Do not auto-save anything. Present observations only. Jake decides what to act on.
