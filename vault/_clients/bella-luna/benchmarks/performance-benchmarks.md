---
type: benchmark
client: bella-luna
date: 2026-03-18
status: active
source: manual
importance: high
tags: [meta-ads, benchmarks, scaling, rubric]
---

# Bella Luna Toys Performance Benchmarks

**Product:** Waldorf-style wooden toys (premium DTC)
**Strategy model:** Aggressive momentum-based with gradient scaling
**Meta Ad Account:** act_551906995157520

## No LTV Adjustment
Standard e-commerce DTC. No subscription model. Adj ROAS = Platform ROAS.

## Tier Classification (evaluated top-down)

| Tier | ROAS | Action | Budget Change |
|------|------|--------|---------------|
| Healthy | >= 10.0x | GRADIENT SCALE | 5-20% (see curve) |
| Caution | >= 5.0x | HOLD | 0% |
| Floor | < 5.0x | CUT | -20% |

## Gradient Scaling Curve (unique to Bella Luna)
Instead of flat 20% for all healthy ad sets, scale proportionally to ROAS:
- ROAS 20x+ -> 20% scaling (full send)
- ROAS 15x -> ~12.5% scaling
- ROAS 12x -> ~8% scaling
- ROAS 10x -> 5% scaling (healthy floor)
Linear interpolation between 10x and 20x.

## Hard Stop Protocols

| Protocol | Trigger | Action |
|----------|---------|--------|
| Absolute Kill | $200+ spend, 0 purchases | PAUSE (unless >5 initiate checkouts, then FLAG) |
| High CPC Warning | $100+ spend, CPC > $1.50 | FLAG (normal range $0.32-$0.97) |
| Zombie Purge | 5+ days active, <$15/day spend, ROAS < 3.0x | PAUSE |

## Scaling Constraints
- Max change: 20% per move
- Buffer between moves: 90 minutes
- Max adjustments per ad set per 24h: 3
- No seesaw: 12 hours between opposite moves
- Min budget floor: $10.00
- Cutoff hour: 2 PM

## Campaign Structure
- Clean two-campaign structure (Consolidated Primary CBO + Seasonal ABO)
- Rolling average window: 3 days

## Creative Strategy
- Seasonal creative rotation
- UGC-style outperforms polished brand content
- Replace creatives when CTR drops 30%+ from peak or frequency exceeds 3x

## Pacing
- Google Sheets ID: 1W5Vhi0BSjg6XS055kMCl_A6NBLk0jsuy7BY4Z5DZ7IE
- Worksheet: 2026
