---
type: decision
client: haba
date: 2026-03-19
status: pending-review
source: manual
confidence: 0.7
importance: medium
tags: [amazon-affiliate, traffic-campaign, test-results, interest-targeting]
related:
  - "[[performance-benchmarks]]"
  - "[[_INDEX]]"
---

# Amazon Affiliate Test Results -- Musical Eggs

## What Was Decided
Ran a 14-day traffic campaign (LPV objective) driving cold prospecting traffic to Amazon product listing for Musical Eggs via affiliate links. $535 total spend split evenly between two ad sets (Copy A and Copy B).

## Setup
- Campaign: HABA | Traffic LPV ABO | Amazon Affiliate | Musical Eggs
- Duration: March 4-18, 2026
- Budget: $250 lifetime per ad set ($500 total, spent $534.92)
- Targeting: Age 30-65, US, excluded all site shoppers/purchasers/viewers
- Mid-test change (March 13): Added Amazon.com interest + Engaged Shoppers behavior to both ad sets

## Results

### Meta Side
- 78,714 impressions, 53,803 reach
- 6,373 link clicks, 5,364 landing page views
- $0.10 cost per landing page view (excellent)
- 10.47% CTR (very strong)
- Copy B: slightly better CTR (10.74% vs 10.03%)
- Copy A: captured all pixel conversions (25 ATC, 1 purchase)

### Amazon Side (from Attribution CSV)
- 2,754 click-throughs (56% drop from Meta's 6,228 outbound clicks)
- 2,682 detail page views
- 197 add to carts (7.15% ATC rate from clicks)
- 22 purchases (0.80% CVR from clicks)
- $551.77 in product sales
- $58.08 brand referral bonus

### ROAS Calculation
- Base ROAS: $551.77 / $534.92 = 1.03x
- With Brand Referral Bonus: $609.85 / $534.92 = 1.14x
- Elizabeth's number (unreconciled): ~$870 / ~$500 = 1.74x
- **Discrepancy needs resolution before final scoring**

## Reasoning
Test was designed to evaluate whether Meta cold traffic could profitably drive Amazon sales for HABA products, specifically targeting non-site-visitors to avoid cannibalizing existing customers.

## Expected Outcome
Break-even to slightly positive ROAS on first test. Learn whether the model works before scaling to more SKUs.

## What Actually Happened
Traffic metrics were exceptional. Amazon conversion funnel was healthy. ROAS was positive but thin at our calculation (1.14x), potentially strong at Elizabeth's number (1.74x). Interest targeting addition showed conversion lift but muddied the A/B test by resetting learning phase on both ad sets simultaneously.

## Lessons
1. Never change targeting on all ad sets simultaneously -- always keep a control
2. Interest targeting (Amazon.com + Engaged Shoppers) likely improved conversion quality
3. The creative that drives more clicks (Copy B) isn't necessarily the one that drives conversions (Copy A got all ATCs)
4. Meta pixel is nearly blind to Amazon conversions -- must rely on Amazon Attribution data
5. Brand Referral Bonus adds meaningful value (~10.5% on top)

## Review Date
2026-03-26 -- After reconciling revenue discrepancy with Elizabeth
