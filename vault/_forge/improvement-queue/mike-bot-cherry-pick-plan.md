---
type: project
client: null
date: 2026-03-19
status: active
source: manual
importance: high
tags: [architecture, orchestration, self-improvement, cherry-pick]
---

# Mike's Bot Cherry-Pick Implementation Plan

## Context

Mike's autonomous agent ("TestAgent355") was given our Forge codebase and asked to do an architecture review + enhancement. It returned 22 new files and 6 modifications. This plan documents what to adopt, what to skip, and in what order.

**Source:** `C:\Users\jakeb\OneDrive\Desktop\the-forge-architecture-overhaul-master.zip`
**Analysis date:** 2026-03-19

---

## Phase 1: Orchestrator (Build First)

**Why first:** This is the single biggest capability gap between our version and Mike's. Without it, every task routes to a single skill. With it, complex multi-step projects (build a landing page, run a data pipeline, create a video ad campaign) get decomposed into phased work with quality gates.

### Files to Create
1. `.claude/skills/orchestrator/SKILL.md` -- Adapt from Mike's 268-line version
2. `.claude/commands/orchestrator.md` -- Slash command wrapper
3. `.claude/agents/orchestrator-agent.md` -- Autonomous project manager agent
4. `vault/_templates/project/project-plan.md` -- Project plan template with phase structure
5. `vault/_templates/project/_INDEX.md` -- Navigation page

### Key Design Decisions (Keep from Mike's Version)
- 6-step process: Initialize, Domain Detect, Decompose, Execute Loop, Finalize, Escalate
- Ticket-as-state approach (vault files track progress, no external state machine)
- Quality gates mandatory between phases (use code-review skill or manual check)
- 15-iteration safety stop (non-overridable)
- 3-cycle deadlock detection with auto-escalation to human-handoff
- Max 5 phases per project
- Budget enforcement integrated (already have budget-check skill)

### What to Change from Mike's Version
- **Remove domain detection stage for now.** We only do ad management. Domain routing adds complexity for capabilities we don't have. Hard-code ad-management domain. Add domain detection later when we expand scope.
- **Simplify the agent to single-project focus.** Mike's agent round-robins 5 concurrent projects. We should start with one project at a time. Less token burn, easier to debug.
- **Wire into existing project-agent.** Our project-agent already exists. Add orchestrator awareness (detect `source: orchestrator` in frontmatter, defer phase management).

### Modifications to Existing Files
- `project-agent.md` -- Add orchestrator-awareness check
- `CLAUDE.md` -- Add Orchestration section (brief, link to skill for details)

### Estimated Effort
Medium. ~2 hours. Mostly adapting Mike's skill to remove domain system references and simplify the agent.

---

## Phase 2: Sandbox-Test Upgrade (Build Second)

**Why second:** Our regression-test skill is basic. Mike's sandbox-test adds pre-flight snapshots, test file prefixing, per-scenario grading, and baseline comparison. These are all things that make testing reliable enough to trust automated skill deployment later.

### Files to Create
1. `.claude/skills/sandbox-test/SKILL.md` -- Adapt from Mike's 189-line version
2. `.claude/commands/sandbox-test.md` -- Slash command wrapper

### Key Design Decisions (Keep from Mike's Version)
- Pre-flight snapshot of sandbox state (file listing with sizes/dates)
- All test fixtures prefixed with `_test-` for easy cleanup identification
- Per-scenario grading (PASS/PARTIAL/FAIL) with specific criteria per skill type
- Frontmatter validation on all vault modifications
- Post-test baseline comparison (sandbox must be identical before and after)
- API-dependent skills get MOCK or SKIPPED designation
- Test report output with pass rate and specific failure details

### What to Change from Mike's Version
- **Remove draft skill testing.** We don't have the author-skill pipeline yet. Test installed skills only.
- **Add Codex CLI as a second reviewer.** After the skill runs its scenarios, have Codex review any files that were created during the test for code quality issues.

### Modifications to Existing Files
- `regression-test/SKILL.md` -- Update to call sandbox-test for individual skill testing, keep the "run all" orchestration

### Estimated Effort
Low-medium. ~1 hour. Mike's version is mostly adoptable as-is.

---

## Phase 3: Extract-Patterns (Build Third, But Later)

**Why third and later:** This skill mines completed projects for reusable patterns. We need completed projects first. After 2-4 weeks of daily usage with real decisions being logged and scored, we'll have enough data. Building it now would run against an empty dataset.

**When to build:** After we have 15+ scored decisions across at least 3 clients with real outcomes (improved/worsened/neutral).

### Files to Create
1. `.claude/skills/extract-patterns/SKILL.md` -- Adapt from Mike's 172-line version
2. `.claude/commands/extract-patterns.md` -- Slash command wrapper
3. `vault/_forge/patterns/_INDEX.md` -- Pattern library index

### Key Design Decisions (Keep from Mike's Version)
- 4 pattern types: success, anti-pattern, detection (early warning), process
- Structured format: trigger condition, recommended action, anti-pattern, evidence table
- Deduplication against existing patterns (same trigger + same action = skip)
- Minimum evidence threshold: single data point caps confidence at 0.5
- Pattern confidence increases with more corroborating evidence
- Mark projects with `patterns_extracted: true` to avoid re-processing

### What to Change from Mike's Version
- **Remove domain tagging.** We're ad-management only for now.
- **Add manual pattern creation.** Jake should be able to manually create patterns from experience, not just auto-extract. The skill should support both modes.
- **Lower the ambition.** Start with decision patterns only (what worked, what didn't). Skip process patterns until the orchestrator has run enough projects.

### Modifications to Existing Files
- `self-improve/SKILL.md` -- Add step to check for extractable patterns (but don't auto-run until threshold met)

### Estimated Effort
Low. ~45 min. The skill is well-defined. Most of the work is waiting for data.

---

## Phase 4: Project Plan Template (Build Anytime)

**Why anytime:** It's a single file with no dependencies. Useful immediately for manually creating project plans.

### Files to Create
1. `vault/_templates/project/project-plan.md` -- Adapt from Mike's version
2. `vault/_templates/project/_INDEX.md` -- Navigation page

### What to Change from Mike's Version
- **Remove orchestrator-specific fields** from required frontmatter (keep them optional)
- **Add a simpler "manual project" variant** that doesn't assume orchestrator management
- **Keep budget fields optional** (not all projects are budget-tracked)

### Estimated Effort
Trivial. ~15 min.

---

## DO NOT BUILD (Reasons Documented)

### Author-Skill Pipeline
**Problem:** Bootstrap paradox. Needs completed projects and validated patterns to generate good skills. We have almost none. Building this now would produce low-quality auto-generated skills that pollute the skill archive.
**When to reconsider:** After extract-patterns has produced 10+ validated patterns with confidence > 0.7.

### Domain System (Web-Dev, Data Processing, Research)
**Problem:** 3 of 4 domain files contain fabricated metrics and thresholds. We only do ad management. Adding routing for domains we can't service creates dead-end classification paths.
**When to reconsider:** When we actually take on a non-ad project (e.g., building a client website, running a data pipeline). At that point, create ONE new domain file from real project experience, not from imagination.

### Archive-Capability Skill
**Problem:** Depends on author-skill pipeline. Also, our existing capability-sprint already handles finding and archiving tools. This is a refinement of a system we haven't used enough yet.
**When to reconsider:** After author-skill is working and producing skills that need sanitization and promotion.

### CLAUDE.md Restructuring
**Problem:** Mike's bot moved Meta account IDs out, removed build phase labels, broke the quick-reference layout our skills depend on. The "domain-agnostic" restructuring makes CLAUDE.md harder to navigate for the current single-domain reality.
**Decision:** Keep our CLAUDE.md structure. It works. Generalize later if/when we add domains.

### Inbox Domain Routing
**Problem:** Adds a 3-stage classification flow referencing domain files that don't have backing skills. The current keyword-based classification works for our scope. Adding domain routing for non-existent domains creates false confidence.
**When to reconsider:** When we add a second domain and need routing between them.

---

## Build Order Summary

| Phase | What | When | Effort | Dependencies |
|-------|------|------|--------|-------------|
| 1 | Orchestrator + Agent + Template | Next build session | ~2 hours | None |
| 2 | Sandbox-Test upgrade | Same session or next | ~1 hour | None |
| 3 | Extract-Patterns | After 2-4 weeks of real usage | ~45 min | 15+ scored decisions |
| 4 | Project Plan Template | Anytime | ~15 min | None |

---

## Intel for Personal Version (Side Project)

Key architectural insights from Mike's bot worth noting for a future general-purpose agent:

1. **Domain plugin system is the right abstraction** for multi-purpose agents. Each domain is self-contained with its own KPIs, tier thresholds, scoring weights, and skill mappings. The Forge should stay single-domain. A personal version could implement this from day one.

2. **The orchestrator is domain-agnostic.** It decomposes goals, creates tickets, and manages phases. The domain file tells it WHAT to measure. This separation means the same orchestrator works for building a website, running a data scrape, or managing ad campaigns.

3. **Token arbitrage** (Mike's key insight from transcript): Running on Claude Code Max plan means frontier model quality without per-token API costs. The Forge already does this. A personal version would lean into this harder with longer-running autonomous projects.

4. **Self-marketing capability** (from transcript): Mike's agent can be told "go get clients" as its first project. This requires the orchestrator + domain system + a marketing domain file. Not relevant for Voltage Forge but relevant for a personal Fiverr-style agent.

5. **Payment processing** (from transcript): Mike mentioned giving the agent a wallet. This is Phase 5+ territory for any version. Requires human-in-the-loop approval for all transactions.

These notes are for Jake's reference only. No implementation planned for Voltage Forge.
