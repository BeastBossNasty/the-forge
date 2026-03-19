---
name: analyze-rulesets
description: Analyze client performance data against existing rubric rulesets and suggest threshold adjustments based on historical outcomes and 4D scoring patterns.
---

# Analyze Rulesets

## Purpose
Review each client's rubric thresholds (tier classifications, hard stops, scaling constraints) against actual performance data and scored decision outcomes. Suggest adjustments to rulesets that are too aggressive, too conservative, or misaligned with reality.

## When to Run
- Manually via `/analyze-rulesets [client]` or `/analyze-rulesets all`
- Automatically during `/self-improve` (runs across all clients)
- After a client has accumulated 10+ scored decisions (enough data to detect patterns)

## Steps

1. **Read the client's rubric:** `vault/_clients/[client]/benchmarks/performance-benchmarks.md`
2. **Read scored decisions:** All decisions in `vault/_clients/[client]/decisions/` that have 4D scores
3. **Read historical snapshots:** `vault/_clients/[client]/snapshots/` for performance trajectory
4. **Read anomalies:** `vault/_clients/[client]/anomalies/` for recurring threshold breaches
5. **Read agency lessons:** `vault/_agency/lessons/` for cross-client patterns

6. **Analyze each rubric component:**

### Tier Threshold Analysis
- What percentage of ad sets consistently land in each tier?
- Are the thresholds too tight (everything is in "floor") or too loose (everything is "healthy")?
- How do scored decisions correlate with tier placement? (Did "scale" decisions at the healthy threshold actually improve performance?)
- Suggested adjustment: if >60% of "healthy" scale decisions worsened, the threshold is too low

### Hard Stop Analysis
- How often do hard stops fire? (Too frequent = thresholds too sensitive, too rare = not protective enough)
- What percentage of hard stop actions were correct in hindsight? (Did paused ad sets actually deserve it?)
- Are there patterns the hard stops miss? (E.g., slow bleed that never triggers a threshold but degrades performance)

### Scaling Constraint Analysis
- Is the 20% max change appropriate? (Check if scaled ad sets frequently overshoot or undershoot)
- Is the 90-minute buffer sufficient? (Check for seesaw patterns)
- Is the 2 PM cutoff optimal? (Check if late-day data would have justified scaling)

### Cross-Client Pattern Detection
- Are similar adjustments succeeding across multiple clients?
- Are certain types of decisions consistently failing across clients?
- Apply learnings from high-performing clients (Bella Luna) to struggling ones (HABA)

7. **Generate recommendations:**
   - Specific threshold changes with reasoning and confidence
   - New defense protocols if gaps are identified
   - Sunset recommendations for rules that never fire or always fire incorrectly

## Output Format

### Ruleset Analysis: [Client]

**Data basis:** [X] scored decisions, [Y] snapshots, [Z] anomalies

#### Tier Thresholds
| Tier | Current Threshold | Hit Rate | Decision Outcomes | Recommendation |
|------|------------------|----------|-------------------|----------------|
| Healthy | [current] | [X%] | [Y% improved] | [keep/adjust to Z] |
| Caution | [current] | [X%] | [Y% neutral] | [keep/adjust to Z] |
| Floor | [current] | [X%] | [Y% worsened] | [keep/adjust to Z] |

#### Hard Stops
| Protocol | Fire Rate | Accuracy | Recommendation |
|----------|-----------|----------|----------------|
| [name] | [X per month] | [Y% correct] | [keep/adjust/remove] |

#### Scaling Constraints
[Analysis and recommendations]

#### Cross-Client Insights
[Patterns that apply from other clients]

### Proposed Ruleset Changes
[Specific changes with confidence levels and reasoning]

## Rules
- Never auto-modify rulesets. All changes are proposals for Jake to review.
- Require minimum 10 scored decisions before suggesting tier changes.
- Require minimum 5 hard stop events before suggesting protocol changes.
- Always show the data supporting each recommendation.
- Confidence levels: HIGH (>80% of data supports change), MEDIUM (50-80%), LOW (<50%, flagged as exploratory).
- Save analysis results to `vault/_clients/[client]/lessons/` as a dated ruleset-analysis note (requires Jake's approval to convert to permanent lesson).
