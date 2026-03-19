---
type: benchmark
client: bowling
date: 2026-03-18
status: active
source: manual
importance: high
tags: [meta-ads, benchmarks, cpa, rubric]
---

# Bowling.com Performance Benchmarks

**Product:** Bowling equipment and accessories (e-commerce)
**Strategy model:** CPA-focused
**Meta Ad Account:** act_1935937429809554

## No LTV Adjustment
Standard e-commerce. AOV ~$153.

## CPA-to-ROAS Translation
- CPA $10 target = ~15.3x ROAS
- CPA $12 worry = ~12.75x ROAS

## Attribution
7-day click attribution window

## Tier Classification (evaluated top-down)

| Tier | ROAS (CPA equivalent) | Action | Budget Change |
|------|----------------------|--------|---------------|
| Healthy | >= 15.0x (CPA < ~$10) | SCALE | +20% |
| Caution | >= 12.0x (CPA $10-$12) | HOLD | 0% |
| Floor | < 12.0x (CPA > $12) | CUT | -20% |

## Hard Stop Protocols

| Protocol | Trigger | Action |
|----------|---------|--------|
| Absolute Kill | $200+ spend, 0 purchases | PAUSE (unless >5 initiate checkouts, then FLAG) |
| CPC Spike | $100+ spend, CPC > $0.25 | FLAG (normal range $0.08-$0.11) |
| Zombie Purge | 5+ days active, <$20/day spend, ROAS < 10.0x | PAUSE |

## Scaling Constraints
- Max change: 20% per move
- Buffer between moves: 90 minutes
- Max adjustments per ad set per 24h: 3
- No seesaw: 12 hours between opposite moves
- Min budget floor: $10.00
- Cutoff hour: 2 PM

## Campaign Structure
- Single campaign, single "Broad Match" ad set
- Rolling average window: 3 days
- Intent to scale as CPA allows
