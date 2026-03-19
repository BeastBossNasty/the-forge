---
type: benchmark
client: haba
date: 2026-03-18
status: active
source: manual
importance: high
tags: [meta-ads, benchmarks, conservative, rubric]
---

# HABA USA Performance Benchmarks

**Product:** German-made wooden toys (parent company of Bella Luna)
**Strategy model:** Conservative e-commerce
**Meta Ad Account:** act_941543396233578

## No LTV Adjustment
Standard e-commerce. Small budget account (~$50/day).

## Account Context
- Struggling to scale with American audiences
- Median daily ROAS: 4.78x, 25th percentile: 2.83x
- Does NOT use CBO campaigns (ad set level only)
- Must EXCLUDE Amazon traffic/LPV campaign: "HABA | Traffic LPV ABO | Amazon"

## Tier Classification (evaluated top-down)

| Tier | ROAS | Action | Budget Change |
|------|------|--------|---------------|
| Healthy | >= 4.0x | SCALE | +20% |
| Caution | >= 2.0x | HOLD | 0% |
| Floor | < 2.0x | CUT | -20% |

## Hard Stop Protocols

| Protocol | Trigger | Action |
|----------|---------|--------|
| Absolute Kill | $100+ spend, 0 purchases | PAUSE (lower threshold for small budget) |
| High CPC Warning | $50+ spend, CPC > $2.50 | FLAG (CPC range $0.14-$2.17) |
| Zombie Purge | 5+ days active, <$10/day spend, ROAS < 1.5x | PAUSE (tighter for small budget) |

## Scaling Constraints
- Max change: 20% per move
- Buffer between moves: 90 minutes
- Max adjustments per ad set per 24h: 3
- No seesaw: 12 hours between opposite moves
- Min budget floor: $5.00 (lower for small budget account)
- Cutoff hour: 2 PM

## Campaign Structure
- ABO only (no CBO)
- Rolling average window: 7 days

## Pacing
- Google Sheets ID: 1_BUPAYue9IVDAy37s9qWr6KBSl6Y5KMfM0ps_OnaHZM
- Worksheet: Haba company projections
