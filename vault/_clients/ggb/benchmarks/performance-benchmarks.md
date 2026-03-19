---
type: benchmark
client: ggb
date: 2026-03-18
status: active
source: manual
importance: high
tags: [meta-ads, benchmarks, ecommerce, rubric]
---

# GourmetGiftBaskets.com Performance Benchmarks

**Product:** Gourmet gift baskets (e-commerce)
**Strategy model:** Standard e-commerce ROAS
**Meta Ad Account:** act_646330722224163

## No LTV Adjustment
Pure e-commerce, no subscription model.

## Tier Classification (evaluated top-down)

| Tier | ROAS | Action | Budget Change |
|------|------|--------|---------------|
| Healthy | >= 4.0x | SCALE | +20% |
| Caution | >= 2.0x | HOLD | 0% |
| Floor | < 2.0x | CUT | -20% |

## Hard Stop Protocols

| Protocol | Trigger | Action |
|----------|---------|--------|
| Absolute Kill | $200+ spend, 0 purchases | PAUSE (unless >5 initiate checkouts, then FLAG) |
| High CPC Warning | $100+ spend, CPC > $4.00 | FLAG (higher AOV = higher CPCs) |
| Zombie Purge | 5+ days active, <$20/day spend, ROAS < 0.80x | PAUSE |

## Scaling Constraints
- Max change: 20% per move
- Buffer between moves: 90 minutes
- Max adjustments per ad set per 24h: 3
- No seesaw: 12 hours between opposite moves
- Min budget floor: $10.00
- Cutoff hour: 2 PM

## Campaign Structure
- Standard e-commerce campaigns
- Rolling average window: 7 days (longer due to gift basket seasonality)
