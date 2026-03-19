---
type: playbook
date: 2026-03-18
status: active
source: manual
tags: [meta-ads, playbook, best-practices]
---

# Meta Ads Playbook

## Campaign Structure
- Separate prospecting and retargeting into distinct campaigns
- Use CBO for prospecting
- Use ABO for retargeting when you need precise frequency control
- 3-5 ad sets per campaign max -- more dilutes learning

## Targeting
- Default to broad targeting for prospecting at $100+/day spend
- Only use interest targeting when: launching new product with no pixel data, spend under $50/day, or testing a specific niche hypothesis
- Lookalike audiences: start with 1% purchase LAL, expand to 3-5% when 1% saturates
- Exclude purchasers from prospecting (180-day window)

## Budget Scaling
- Scale in 10-20% increments, not more
- Wait 3-4 days between scaling moves for the algorithm to restabilize
- If CPA spikes after scaling, wait 48h before reverting -- it often corrects

## Creative
- Minimum 3 active creatives per ad set to avoid fatigue
- Replace creatives when CTR drops 30%+ from peak or frequency exceeds 3x
- UGC-style consistently outperforms polished brand content for prospecting
- Test one variable at a time (hook, format, CTA) -- not multiple

## Retargeting
- 1-7 day window: highest intent, highest bids
- 8-30 day window: moderate intent, standard bids
- Watch frequency -- above 6x means audience is too small or budget too high
- Dynamic product ads (DPA) for e-commerce clients with 50+ SKUs

## Measurement
- Use 7-day click, 1-day view attribution
- Don't trust Meta ROAS at face value -- cross-reference with GA4 and backend data
- Check platform vs backend CPA weekly -- if gap exceeds 20%, investigate

## Common Mistakes
- Scaling budget too fast (>30% at once) -- kills CPA
- Too many ad sets competing -- consolidate
- Not excluding converters from prospecting -- wastes spend
- Judging creative performance before 1,000 impressions
