---
type: benchmark
client: truniagen
date: 2026-03-18
status: active
source: manual
importance: high
tags: [meta-ads, benchmarks, ltv, rubric]
---

# TruNiagen Performance Benchmarks

**Product:** NAD+ supplement (ChromaDex brand TruNiagen)
**Strategy model:** Conservative LTV-based
**Meta Ad Account:** act_196113284341625

## LTV Adjustment (Manny Math)
- Subscription LTV: $300.00
- LTV increment per sub: $210.00 ($300 LTV - ~$90 avg platform sub value)
- Formula: `Adj Sub ROAS = (Purchase Value + (Subscriptions x $210)) / Spend`
- One-time average value: $45.00 (fallback)
- TruNiagen is the ONLY client with LTV adjustment. Raw ROAS understates actual value.

## Custom Conversions
- Subscription: offsite_conversion.custom.345147406884130
- One-time purchase: offsite_conversion.custom.280776209851139

## Tier Classification (evaluated top-down)

| Tier | Adj Sub ROAS | Platform ROAS | NTB ROAS | Action | Budget Change |
|------|-------------|---------------|----------|--------|---------------|
| Healthy | >= 1.5x | >= 0.80x | >= 1.20x | SCALE | +20% |
| Caution | >= 1.2x | >= 0.60x | >= 1.10x | HOLD | 0% |
| Floor | < 1.2x | < 0.60x | < 1.10x | CUT | -20% |

## Hard Stop Protocols

| Protocol | Trigger | Action |
|----------|---------|--------|
| Absolute Kill | $200+ spend, 0 purchases | PAUSE (unless >5 initiate checkouts, then FLAG) |
| High CPC Warning | $100+ spend, CPC > $3.50 | FLAG |
| Zombie Purge | 5+ days active, <$20/day spend, ROAS < 0.80x | PAUSE |

## Scaling Constraints
- Max change: 20% per move
- Buffer between moves: 90 minutes
- Max adjustments per ad set per 24h: 3
- No seesaw: 12 hours between opposite moves
- Min budget floor: $10.00
- Cutoff hour: 2 PM (no upward scaling after)

## Campaign Structure
- Mix of ABO and CBO campaigns
- Exclude campaigns prefixed with "Instagram" (organic team boosts)
- Rolling average window: 3 days

## Key Metrics Tracked
- Purchases (total, subscription, one-time)
- Purchase conversion value
- Adj Sub ROAS (primary KPI)
- Platform ROAS, NTB ROAS
- Outbound clicks and CTR
- CPC, CPM, frequency
- Spend (daily and weekly)

## Pacing
- Google Sheets ID: 1qhuOSTYNWSHc9c8I_tpybyPRPE_FzNto
- Format: daily (one tab per month)
