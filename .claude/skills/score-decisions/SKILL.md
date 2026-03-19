---
name: score-decisions
description: Automatically score past decisions using 4D signal weighting (temporal decay, contextual lift, outcome trust, category success). Runs automatically as part of briefing, weekly-report, and performance-review skills.
---

# Score Decisions (4D Signal Weighting)

## Purpose
Automatically evaluate past decisions to determine if they improved, maintained, or worsened performance. Uses a 4-dimensional scoring model ported from Command Center Zap. This skill runs AUTOMATICALLY as part of briefing, weekly-report, and performance-review -- it is not called directly by Jake.

## When This Runs
- Automatically during `/briefing [client]` -- scores any decisions with passed review dates
- Automatically during `/weekly-report [client]` -- scores decisions from past 7-14 days
- Automatically during `/performance-review [client]` -- scores all active decisions
- Automatically during `/self-improve` -- identifies scoring patterns across clients

## 4D Signal Weighting Model

### Dimension 1: Temporal Decay
Weight decreases exponentially over time. Recent signals matter more.
- Half-life: 15-30 days (adaptive based on historical accuracy)
- High-accuracy contexts get longer half-life (signals trusted longer)
- Formula: `decay = exp(-0.693 * days_elapsed / half_life)`

### Dimension 2: Contextual Lift
Boost signals that match the current context:
- **Seasonal relevance:** Decisions made in similar seasonal periods get more weight (Q4 holiday decisions are more relevant during Q4)
- **State similarity:** Decisions made when the account was in a similar performance state (spend level, ROAS range, CPA range) get more weight
- Combined max lift: 0.8 (80% boost)

### Dimension 3: Outcome Trust
Weight based on how the decision actually performed:
- **Improved** (score >= 0.10): 1.2x boost -- trust decisions that worked
- **Neutral** (-0.10 to 0.10): 0.9x -- slightly discount inconclusive results
- **Worsened** (score <= -0.10): 0.7x penalty -- discount decisions that hurt

### Dimension 4: Category Success
Weight based on the category's historical success rate:
- High-success categories (>70% improved): 1.15x boost
- Low-success categories (<30% improved): 0.8x penalty
- Categories: scaling, creative, targeting, bidding, budget-cut, hold

### Composite Score
`final_weight = temporal_decay * (1 + contextual_lift) * outcome_trust * category_success`
Clamped to range: 0.1 to 1.5

## Outcome Scoring Model
When evaluating whether a decision improved performance:
- 40% weight: ROAS delta (did ROAS improve after the decision?)
- 30% weight: CPC delta (did CPC improve?)
- 15% weight: Spend efficiency (did we get more for less?)
- 15% weight: Purchase volume (did conversion volume hold or grow?)

Classification:
- Score >= 0.10: `improved`
- Score between -0.10 and 0.10: `neutral`
- Score <= -0.10: `worsened`

## Steps (when triggered by another skill)

1. Read all decisions in `vault/_clients/[client]/decisions/` with status `active`
2. For each decision with a review date that has passed:
   a. Read the decision's expected outcome
   b. Compare pre-decision metrics (from the decision note's context) against current metrics (from snapshots or live data)
   c. Calculate the outcome score (40% ROAS + 30% CPC + 15% efficiency + 15% volume)
   d. Classify as improved/neutral/worsened
   e. Apply the 4D weighting to determine confidence in the assessment
   f. Add a scored note to the decision file with timestamp
3. For decisions that are clearly improved or worsened:
   - Flag them in the skill output for Jake to act on
   - Suggest converting improved decisions to lessons
   - Suggest reviewing/reverting worsened decisions
4. Save scoring results to the decision note (append, don't overwrite)

## Scoring Note Format (appended to decision files)

```
## 4D Score -- [date]
**Outcome:** [improved | neutral | worsened] (score: [X.XX])
**Confidence:** [X.X]% (weighted by temporal decay, context similarity, outcome trust, category success)
**ROAS delta:** [+/-X.X%]
**CPC delta:** [+/-X.X%]
**Recommendation:** [convert to lesson | review and consider reverting | continue monitoring]
```

## Rules
- Never auto-convert decisions to lessons. Only flag for Jake.
- Never auto-revert decisions. Only recommend.
- If no metrics are available for comparison, note "insufficient data" and skip scoring.
- Always show the math: what changed, by how much, and why the score is what it is.
- Score relative to the CLIENT'S OWN benchmarks, not arbitrary numbers.
- The 4D model runs silently during other skills. Only surface results when they're actionable.
