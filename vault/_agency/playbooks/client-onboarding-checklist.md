---
type: playbook
date: 2026-03-18
status: active
source: manual
tags: [onboarding, process, checklist]
---

# Client Onboarding Checklist

## Setup
- [ ] Run `scripts/bootstrap_client.sh <slug> "<Name>"` to create client folder
- [ ] Populate `benchmarks/performance-benchmarks.md` with KPI targets
- [ ] Populate `brand/brand-voice.md` with brand guidelines
- [ ] Populate `brand/creative-guidelines.md` with creative specs
- [ ] Populate `brand/target-audiences.md` with audience definitions
- [ ] Add key stakeholders to `stakeholders/`
- [ ] Set up content calendar in `pipeline/content-calendar.md`

## Platform Access
- [ ] Confirm ad platform access (Meta, Google, etc.)
- [ ] Verify tracking pixels/tags are installed
- [ ] Confirm conversion events are firing correctly
- [ ] Cross-reference platform data with backend/GA4

## Initial Analysis
- [ ] Run `/briefing [client]` to generate first status
- [ ] Run `/reflect [client]` to identify gaps in the vault
- [ ] Create initial project tickets for any setup work needed
