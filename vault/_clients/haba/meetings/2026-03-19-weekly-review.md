---
type: meeting
client: haba
date: 2026-03-19
status: active
source: meeting-processor
tags: [weekly-review, mer, amazon-affiliate, pixel-health, audiences, grandparents]
related:
  - "[[performance-benchmarks]]"
  - "[[2024-account-restructure]]"
---

# Weekly Review -- HABA -- 2026-03-19

**Attendees:** Jake Brown, John Pike, Lee Anderson, CJ (Head of Bella Luna), Elizabeth (Head of HABA)

## Key Discussion Points

### MER Struggles
- HABA MER is struggling more than Bella Luna
- Ramped up Friday through the weekend, then pulled back because MER kept slipping
- Currently at $100/day Meta spend -- may need to pull back further
- Amazon affiliate spend now excluded from MER calculations
- Non-paid revenue ("other sales") appears down ~30% in Looker Studio -- needs verification
- Cross-network (PMax) down from $12K to $8.3K year over year
- Organic down ~$300, email up 12%, SMS up 140%

### Amazon Affiliate Test Results
- Campaign ran March 4-18, ~$535 total spend
- Jake initially reported 1.14x ROAS on the call
- Elizabeth corrected: she sees ~$870 in revenue = 1.74x ROAS
- CSV Jake received shows $551.77 revenue + $58.08 brand referral bonus = $609.85
- Discrepancy of ~$260 needs to be reconciled -- likely Amazon Attribution lookback window or different report view
- Performance improved after interest targeting was added (Amazon.com interest + Engaged Shoppers behavior)
- Interest addition caused learning phase reset which muddied the A/B comparison
- Both ad sets had identical targeting -- only difference was copy (A vs B)
- Copy A captured all downstream conversions (25 ATC, 1 pixel purchase) despite Copy B having slightly better CTR
- Worth testing again with: more SKUs, no mid-test audience changes, longer duration

### Pixel Health Concerns
- Elizabeth flagged: HABA shows "83% more purchases with CAPI" recommendation
- Purchase event match quality: 9.2/10 (excellent)
- Add to cart event match quality: potentially low -- needs investigation
- Bella Luna does NOT show this recommendation, suggesting its setup is cleaner
- Full pixel health audit needed for both accounts

### Audience Audit Needed
- Elizabeth called out HABA is using old/stale audience lists
- Bella Luna has 2x the custom audiences HABA does
- HABA has the same source lists available but isn't using them
- Need a dedicated session post-Easter to audit and rebuild audience strategy

### Grandparent Segmentation
- Both brands recently implemented age capture and shopper type tracking
- HABA skews heavily toward grandparents as buyers
- Strategy: create separate grandparent audience with differentiated messaging
  - Legacy angle: 100+ year German heritage
  - Heirloom quality: wooden, durable, multi-generational, toys that get passed down
- Jake has prior market research on this from onboarding to reference

### Looker Studio / Revenue Discrepancies
- Total sales showing $89K for last 30 days in Looker -- Elizabeth confirmed ~$80K in Shopify (excluding Collective and draft orders, excluding tax)
- With all figures included: ~$85K in Shopify
- Discrepancy likely from tax inclusion and Collective/draft order handling
- John wants to verify the Shopify revenue calculation Mike has in Looker
- Need to ensure apples-to-apples comparison year over year

### GA4 Follow-Up
- Lee dropped notes from previous GA4 meeting
- Revenue data not appearing at page level due to misconfiguration in how revenue maps to items
- Mike is working through fixes this weekend

## Action Items

- [ ] Reconcile Amazon affiliate numbers -- get Elizabeth's exact report to compare against CSV
- [ ] Build proper Amazon affiliate comparison report
- [ ] Full pixel health audit -- both HABA and Bella Luna
- [ ] Full audience audit -- both accounts, flag stale lists
- [ ] Grandparent audience segmentation plan with differentiated messaging
- [ ] Verify Looker Studio revenue calculation with Mike
- [ ] Schedule dedicated post-Easter audience strategy session
