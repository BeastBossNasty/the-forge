---
type: playbook
date: 2026-03-18
status: active
source: manual
tags: [rubric, scoring, 4d, decision-engine, playbook]
---

# Rubric Engine Playbook

## Overview
Every client has a rubric that defines how ad sets are classified into tiers (Healthy/Caution/Floor) and what actions to take. The rubric is stored in each client's `benchmarks/performance-benchmarks.md` file.

## Rubric Components

### 1. Tier Classification
Every client has 3 tiers evaluated top-down (first match wins):
- **Healthy:** Performance above target. Action: SCALE (increase budget).
- **Caution:** Performance acceptable but below target. Action: HOLD (no changes).
- **Floor:** Performance below breakeven. Action: CUT (decrease budget).

Thresholds vary by client. Some use ROAS, some use CPA-derived ROAS, one (TruNiagen) uses LTV-adjusted ROAS.

### 2. Hard Stop Protocols
Safety nets that fire independent of tier classification:
- **Absolute Kill:** High spend + zero purchases = pause immediately
- **CPC Warning:** High spend + abnormal CPC = flag for review
- **Zombie Purge:** Old + low-spend + poor ROAS = pause

Thresholds are calibrated per client based on their budget size and normal CPC ranges.

### 3. Scaling Constraints
Universal rules that apply to all clients:
- Max 20% budget change per move
- 90-minute buffer between moves to same ad set
- Max 3 adjustments per ad set per 24 hours
- No seesaw (up then down) within 12 hours
- No upward scaling after 2 PM
- Minimum budget floors ($5-$10 depending on client)

### 4. LTV Adjustment (TruNiagen only)
Formula: `Adj Sub ROAS = (Purchase Value + (Subscriptions x $210)) / Spend`
This is the ONLY client with LTV adjustment. All other clients use raw platform ROAS.

### 5. Gradient Scaling (Bella Luna only)
Instead of flat 20% for all healthy ad sets, Bella Luna scales proportionally:
- 5% at 10x ROAS (healthy floor) up to 20% at 20x+ ROAS
- Linear interpolation between

## 4D Decision Scoring
All decisions are automatically scored over time using 4-dimensional signal weighting:
1. **Temporal decay:** Recent signals weighted more heavily
2. **Contextual lift:** Decisions made in similar conditions get more weight
3. **Outcome trust:** Decisions that worked get boosted, ones that failed get penalized
4. **Category success:** Decision categories with high success rates get boosted

See the score-decisions skill for implementation details.

## Client Rubric Quick Reference

| Client | Model | Primary KPI | Healthy Threshold | Caution | Floor |
|--------|-------|-------------|-------------------|---------|-------|
| TruNiagen | LTV Conservative | Adj Sub ROAS | >= 1.5x | >= 1.2x | < 1.2x |
| Bella Luna | Momentum Aggressive | ROAS | >= 10.0x (gradient) | >= 5.0x | < 5.0x |
| Bowling.com | CPA-focused | ROAS (~CPA) | >= 15.0x (~$10 CPA) | >= 12.0x | < 12.0x |
| GGB | Standard E-com | ROAS | >= 4.0x | >= 2.0x | < 2.0x |
| HABA | Conservative | ROAS | >= 4.0x | >= 2.0x | < 2.0x |

## Meta Ad Account IDs

| Client | Account ID |
|--------|-----------|
| TruNiagen | act_196113284341625 |
| Bella Luna | act_551906995157520 |
| Bowling.com | act_1935937429809554 |
| GGB | act_646330722224163 |
| HABA | act_941543396233578 |
