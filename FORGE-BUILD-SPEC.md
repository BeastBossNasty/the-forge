# THE FORGE — Complete Build Spec

## Read This Entire Document Before Writing Any Code

This document is the single source of truth for The Forge. Read it top to bottom, internalize the architecture, then build Phase 1 in the order specified. Do not skip sections. Do not make assumptions. If something is ambiguous, flag it — do not guess.

---

## What Is The Forge

The Forge is an AI-powered operating system for managing ad campaigns and executing tasks autonomously. It is built for a single user (Jake) who has zero coding knowledge. Jake is the strategist and tester. Claude Code is the builder, operator, and learner. Jake will never edit code, debug, or read logs. Every interaction happens in plain English.

The Forge has five layers, built in phases:

```
Layer 5: SELF-IMPROVEMENT (Phase 3)
    Continuous background: self-research, skill acquisition, memory optimization
    ↑
Layer 4: INTAKE & ROUTING (Phase 2)
    Gmail polling → task classification → planning → ticket creation
    ↑
Layer 3: EXECUTION ENGINE (Phase 1)
    Slash commands → skill selection → MCP calls → quality checks → delivery
    ↑
Layer 2: MEMORY — the vault (Phase 1)
    Clients, playbooks, lessons, decisions, benchmarks, skills archive
    ↑
Layer 1: FOUNDATION (Phase 1)
    Project folder, CLAUDE.md, .claude/ config, MCP connections
```

This build spec covers Phase 1. Phases 2-3 are documented here for architectural awareness — build decisions in Phase 1 must not block future phases.

---

## Architecture Decisions (Locked)

### Plain Markdown First, Obsidian Later

The vault starts as plain markdown files. Claude Code reads and writes them using built-in file tools (Read, Write, Grep, Glob). No Obsidian dependency. No Nexus MCP dependency.

**However**, every structural decision must be Obsidian-compatible from day one:
- All internal references use `[[wikilink]]` syntax even though nothing resolves them yet
- All notes use standardized YAML frontmatter (see schema below)
- Folder structure matches what Obsidian expects
- File naming follows `YYYY-MM-DD-short-description.md` for dated notes

When the time comes to upgrade, the process is: install Obsidian, point it at `vault/`, install the Nexus (Claudesidian) plugin, update `.mcp.json` to add the Nexus server, and update `CLAUDE.md` to prefer Nexus MCP tools over raw file reads. Nothing gets rebuilt or migrated.

### Token Arbitrage

The Forge runs on Claude Code with a Claude Max subscription. Flat monthly cost, not per-token API calls. This means Opus 4.6 with a 1M context window at no marginal cost per task. All execution happens through Claude Code, not the Anthropic API. This is the same strategy the reference implementation uses.

### Codex CLI as Second Opinion (Phase 1.5)

OpenAI's Codex CLI will be added as a pre-commit reviewer. This uses a competing AI model to catch mistakes Claude makes. It requires either a ChatGPT subscription or OpenAI API key. Not needed for Phase 1 — add it once the foundation is working. When added, it runs via a PreCommit hook: `codex review --uncommitted`.

### Security Principles

- Never hallucinate metrics. Only report what you can actually see in a platform or file.
- Never auto-save decisions or lessons. Those require human judgment. Auto-save is limited to anomalies (metrics outside acceptable range) and snapshots (periodic data captures).
- Client data stays isolated in the correct client folder. Never cross-contaminate.
- Downloaded MCPs and skills must be scanned before use (check GitHub stars, recent activity, known issues). Do not blindly install packages.
- When in doubt, ask Jake. He would rather be asked than have something go wrong silently.

---

## Folder Structure

Build this exactly. Do not add, rename, or reorganize folders.

```
the-forge/
├── FORGE-BUILD-SPEC.md              ← this file (reference only, do not modify)
├── CLAUDE.md                         ← master operating instructions for Claude Code
├── .claude/
│   ├── agents/
│   │   ├── briefing-agent.md
│   │   └── project-agent.md
│   ├── commands/
│   │   ├── briefing.md
│   │   ├── save-decision.md
│   │   ├── reflect.md
│   │   ├── check-tickets.md
│   │   ├── create-ticket.md
│   │   ├── weekly-report.md
│   │   ├── process-meeting.md
│   │   └── performance-review.md
│   ├── skills/
│   │   ├── daily-briefing/SKILL.md
│   │   ├── save-decision/SKILL.md
│   │   ├── reflect/SKILL.md
│   │   ├── check-tickets/SKILL.md
│   │   ├── create-ticket/SKILL.md
│   │   ├── weekly-report/SKILL.md
│   │   ├── process-meeting/SKILL.md
│   │   └── performance-review/SKILL.md
│   ├── hooks/hooks.json
│   └── settings.local.json
├── .mcp.json                         ← MCP server config (empty/placeholder until configured)
├── vault/
│   ├── _agency/
│   │   ├── _INDEX.md
│   │   ├── playbooks/
│   │   │   ├── meta-ads-playbook.md
│   │   │   ├── google-ads-playbook.md
│   │   │   ├── voltage-brand-voice.md
│   │   │   └── client-onboarding-checklist.md
│   │   ├── lessons/
│   │   │   └── auto-save-findings.md
│   │   └── team/
│   │       ├── _INDEX.md
│   │       ├── jake.md
│   │       ├── john.md
│   │       ├── andrea.md
│   │       ├── lee.md
│   │       ├── mike.md
│   │       ├── chris.md
│   │       └── charlie.md
│   ├── _clients/
│   │   ├── _sandbox/
│   │   │   ├── _INDEX.md
│   │   │   ├── benchmarks/performance-benchmarks.md
│   │   │   ├── brand/
│   │   │   │   ├── brand-voice.md
│   │   │   │   ├── creative-guidelines.md
│   │   │   │   └── target-audiences.md
│   │   │   ├── decisions/
│   │   │   ├── lessons/
│   │   │   ├── anomalies/
│   │   │   ├── pipeline/
│   │   │   │   └── content-calendar.md
│   │   │   ├── projects/
│   │   │   ├── tickets/
│   │   │   ├── meetings/
│   │   │   ├── snapshots/
│   │   │   └── stakeholders/
│   │   ├── truniagen/
│   │   │   ├── _INDEX.md
│   │   │   ├── benchmarks/performance-benchmarks.md
│   │   │   ├── brand/
│   │   │   │   ├── brand-voice.md
│   │   │   │   ├── creative-guidelines.md
│   │   │   │   └── target-audiences.md
│   │   │   ├── decisions/
│   │   │   ├── lessons/
│   │   │   ├── anomalies/
│   │   │   ├── pipeline/
│   │   │   │   └── content-calendar.md
│   │   │   ├── projects/
│   │   │   ├── tickets/
│   │   │   ├── meetings/
│   │   │   ├── snapshots/
│   │   │   └── stakeholders/
│   │   └── bella-luna/
│   │       └── [identical structure to truniagen]
│   ├── _forge/
│   │   ├── _INDEX.md
│   │   ├── skills-archive/
│   │   ├── learnings/
│   │   ├── capability-log/
│   │   └── improvement-queue/
│   └── _templates/
│       ├── _INDEX.md
│       ├── client/
│       │   ├── _INDEX.md
│       │   ├── benchmarks/performance-benchmarks.md
│       │   ├── brand/
│       │   │   ├── brand-voice.md
│       │   │   ├── creative-guidelines.md
│       │   │   └── target-audiences.md
│       │   ├── decisions/decision-template.md
│       │   ├── lessons/lesson-template.md
│       │   ├── anomalies/anomaly-template.md
│       │   ├── pipeline/content-calendar.md
│       │   ├── projects/project-template.md
│       │   ├── tickets/ticket-template.md
│       │   ├── meetings/meeting-template.md
│       │   ├── snapshots/
│       │   └── stakeholders/stakeholder-template.md
│       └── personal/
│           └── preferences.md
└── scripts/
    └── bootstrap_client.sh
```

---

## Vault Schema

### Frontmatter (Required on Every Note)

Every markdown file in the vault (except `_INDEX.md` files) must have this YAML frontmatter block:

```yaml
---
type: [decision | lesson | benchmark | meeting | brand | anomaly | pipeline | project | ticket | snapshot | playbook | team-member | stakeholder | preferences]
client: [client-slug]           # omit for agency-wide notes
date: YYYY-MM-DD
status: [active | pending-review | archived | open | in-progress | closed]
source: [manual | browser-mcp | meta-review | google-review | meeting-processor | self-improvement | forge-research]
confidence: 0.0-1.0            # omit for agency-wide playbooks/templates
importance: [low | medium | high]  # omit for agency-wide playbooks/templates
tags: [relevant, tags]
related:
  - "[[wikilink]]"
# Optional
time: HH:MM
due: YYYY-MM-DD
assignee: ""
---
```

`_INDEX.md` files are navigation pages and do not need frontmatter. They contain a brief description of the folder's purpose and links to key files within it.

### File Naming

- Dated notes: `YYYY-MM-DD-short-description.md`
- Evergreen reference pages: `descriptive-name.md` (e.g., `brand-voice.md`, `performance-benchmarks.md`)
- Templates: `[type]-template.md`

### Writing Rules

- Be specific, not vague. "CPA increased 15% to $22.50" not "CPA went up."
- Include the reasoning, not just the action. Why was this decision made?
- Compare performance against the client's own benchmarks, not arbitrary numbers.
- Link related notes with `[[wikilinks]]` when relevant. Even though nothing resolves these yet, they create the relationship graph for when Obsidian is added.
- Every decision note must include an expected outcome and a review date in the body.
- Weekly reviews should either validate the decision, convert it into a lesson, or flag it for follow-up.

### Auto-Save Rules

Skills that pull live data should write findings back to the vault:

**Auto-save (no human approval needed):**
- Anomalies: any metric outside the client's acceptable range → `anomalies/` (check for existing notes first to prevent duplicates on repeated runs)
- Snapshots: periodic performance data captures → `snapshots/` (NOT `benchmarks/` — that folder holds KPI targets only)

**Never auto-save (requires human judgment):**
- Decisions
- Lessons
- Validated decisions being converted to lessons

When a decision outcome becomes clear (validated or failed), flag it in the output for Jake to act on. Do not auto-convert.

---

## Client Knowledge (Pre-Populate)

### TrūNiagen

```yaml
# vault/_clients/truniagen/benchmarks/performance-benchmarks.md
---
type: benchmark
client: truniagen
date: 2026-03-18
status: active
source: manual
importance: high
tags: [meta-ads, benchmarks, ltv]
---
```

**Product:** NAD+ supplement (ChromaDex brand TrūNiagen)
**Strategy model:** Conservative LTV-based. Decisions are measured against lifetime customer value, not immediate ROAS.
**ROAS threshold:** 1.5x (adjusted for lifetime value — appears low but accounts for subscription revenue and repeat purchases)
**Campaign structure:** Mix of ABO and CBO campaigns
**Key metrics:**
- Purchases
- Purchase conversion value
- Outbound clicks
- Outbound click rate
- Outbound CPA
- Purchase conversion ROAS
- Spend
- Custom conversion: Subscriptions (unique to TrūNiagen — other clients do not have this)

**LTV adjustment:** TrūNiagen is the only client with an LTV adjustment ruleset. When evaluating performance, raw ROAS understates actual value because it doesn't capture subscription lifetime revenue. Apply the LTV multiplier when comparing against benchmarks.

### Bella Luna Toys

```yaml
# vault/_clients/bella-luna/benchmarks/performance-benchmarks.md
---
type: benchmark
client: bella-luna
date: 2026-03-18
status: active
source: manual
importance: high
tags: [meta-ads, benchmarks, scaling]
---
```

**Product:** Waldorf-style wooden toys
**Strategy model:** Aggressive momentum-based. When performance is strong, scale fast. When it dips, pull back and rotate creative.
**ROAS threshold:** 10x+ (this is not a typo — Bella Luna achieves exceptional blended ROAS)
**Campaign structure:** Clean two-campaign active structure:
1. Consolidated Primary Sales CBO (always-on prospecting)
2. Seasonal Sales ABO (rotates with seasonal product pushes)
**Creative strategy:** Seasonal creative rotation. UGC-style content outperforms polished brand content. Replace creatives when CTR drops 30%+ from peak or frequency exceeds 3x.
**Key insight:** The simplicity of the two-campaign structure is a feature, not a limitation. Consolidation feeds the algorithm more data per campaign, improving optimization.

### Agency-Wide Context

**Voltage Media:**
- Boutique performance marketing agency, 20+ years operating
- Google Premier Partner (Top 3%)
- Meta Business Partner
- Microsoft Advertising Partner
- Business Portfolio ID: 622383571242852
- Core positioning: boutique expertise combined with technology adoption ahead of competitors
- Team: John (boss/decision-maker), Jake (paid social, organic social, AI infrastructure), Andrea, Lee, Mike, Chris, Charlie

**Brand voice rules (all Voltage content):**
- No em dashes — ever, anywhere, for any reason
- Plain English over jargon
- Confident and direct, not hedging or disclaimering
- Boutique expertise + tech-forward positioning

---

## Skills (Phase 1)

Each skill lives in `.claude/skills/[skill-name]/SKILL.md`. Each has a corresponding command in `.claude/commands/[command-name].md`.

### Skill 1: Daily Briefing

**Command:** `/briefing [client]`
**Purpose:** Morning status update. What happened, what needs attention, what to do today.

**Steps:**
1. Read the client's vault: recent decisions, lessons, benchmarks, anomalies, pipeline, open tickets, active projects
2. Check `_agency/lessons/` for cross-client learnings that may apply
3. If a platform MCP or Browser MCP is available, pull today's performance data
4. Compare current performance against client benchmarks
5. Flag anything outside acceptable ranges
6. Auto-save: anomalies (if any metric is outside range) and snapshots (if live data was pulled). Check for existing anomaly notes before creating duplicates.

**Output format:**
- Performance snapshot: key metrics vs benchmarks
- Recent decisions: what was decided recently and early signals on outcomes
- Flags: anything that needs attention today
- Suggested actions: what to consider doing today
- Saved to vault: list any auto-saved notes

If live data is unavailable, say exactly what is missing. Do not invent metrics.

### Skill 2: Save Decision

**Command:** `/save-decision [client]`
**Purpose:** Log a decision with full context so future reviews can evaluate whether it worked.

**Steps:**
1. Ask Jake to describe the decision (or parse it from the conversation context)
2. Read client benchmarks and recent decisions for context
3. Create a decision note with: what was decided, reasoning, expected outcome, review date
4. Link to related benchmarks, lessons, or previous decisions via `[[wikilinks]]`

**Note format:**
```markdown
---
type: decision
client: [client]
date: YYYY-MM-DD
status: active
source: manual
confidence: [0.0-1.0]
importance: [low | medium | high]
tags: [relevant, tags]
related:
  - "[[related-note]]"
---

# [Short description of decision]

**Decision:** [What was decided]

**Reasoning:**
[Why — reference data, benchmarks, patterns]

**Expected outcome:**
[What should happen if this works]

**Review date:** YYYY-MM-DD

Related: [[links]]
```

### Skill 3: Reflect

**Command:** `/reflect [client]`
**Purpose:** Independent analysis. Not answering a specific question — forming observations about patterns, risks, and opportunities the account manager might not have asked about.

**Steps:**
1. Read the client's full vault: decisions, lessons, anomalies, benchmarks, brand, pipeline, projects, tickets, meetings, stakeholders
2. Check `_agency/lessons/` and `_agency/playbooks/` for relevant cross-client context
3. Analyze holistically. Look for:
   - Overdue reviews: decisions or anomalies past their review date
   - Contradictions: recent decisions that conflict with existing lessons or benchmarks
   - Patterns: recurring themes across decisions (repeated reverts, same issue resurfacing)
   - Stale data: benchmarks, brand docs, or pipeline items not updated in a while
   - Gaps: missing context that would help future briefings (e.g., no benchmarks for a platform being used)
   - Opportunities: things working well that could be doubled down on
   - Risks: upcoming deadlines with unfinished dependencies, projects with no progress
4. Do NOT pull live platform data. This is vault-only analysis.

**Output format:**
- Overdue reviews
- Patterns
- Contradictions and gaps
- Opportunities
- Risks
- Recommendation: the single most important thing to address

Keep it concise and opinionated. This is a second opinion, not a status report. Do not auto-save anything. Present observations only. Jake decides what to act on.

### Skill 4: Check Tickets

**Command:** `/check-tickets [client]`
**Purpose:** Advance all open tickets. Complete work, close finished items, flag blockers.

**Steps:**
1. Read all files in `vault/_clients/[client]/tickets/`
2. Find every ticket with `status: open` or `status: in-progress`
3. For each ticket, review the acceptance criteria checklist
4. If criteria can be completed now: do the work, check off criteria, add timestamped note
5. If all criteria are checked: set `status: closed`, add completion note
6. If blocked: note why, skip to next
7. If needs human input: flag and move on
8. If a closed ticket produced a learning: write it to `lessons/` and link it
9. Auto-save: overdue ticket anomalies (check for existing notes first to prevent duplicates)

**Output format:**
- Tickets closed
- In progress: what was advanced and what remains
- Blocked: what's stuck and why
- Needs your input: decisions required
- Overdue: tickets past their due date
- Saved to vault: list any auto-saved notes

### Skill 5: Create Ticket

**Command:** `/create-ticket [client]`
**Purpose:** Create a trackable work item with clear acceptance criteria.

**Steps:**
1. Parse the task from conversation context or ask Jake to describe it
2. Create a ticket note with: description, acceptance criteria checklist, priority, due date, assignee (if applicable)
3. Link to related projects, decisions, or pipeline items

### Skill 6: Weekly Report

**Command:** `/weekly-report [client]`
**Purpose:** Weekly performance summary with decision outcome tracking.

**Steps:**
1. Read client vault: benchmarks, decisions from the past 7-14 days, lessons, anomalies
2. Pull platform data if available (7-day vs previous 7-day comparison)
3. Compare against benchmarks
4. Check if recent decisions are playing out as expected
5. Reference agency playbooks for best practices
6. Auto-save: weekly snapshot to `snapshots/`, anomalies if any metric is outside range, flag decision outcomes for Jake to review

**Output format:**
- Overall health: one sentence summary
- Platform breakdown: metrics, trends, what's working, what's not
- Decision outcomes: how recent decisions are performing
- Recommendations: specific, actionable next steps with reasoning
- Saved to vault: list any auto-saved notes

### Skill 7: Process Meeting

**Command:** `/process-meeting [client]`
**Purpose:** Extract structured information from a meeting transcript or notes.

**Steps:**
1. Read the transcript/notes provided
2. Extract: decisions made, action items with owners, key insights, follow-up dates
3. Create a meeting note in `meetings/`
4. For each decision extracted: create a separate decision note in `decisions/`
5. For each action item: optionally create a ticket in `tickets/`
6. Link everything together with `[[wikilinks]]`

### Skill 8: Performance Review

**Command:** `/performance-review [client]`
**Purpose:** Deep dive analysis with campaign-level data.

**Steps:**
1. Read client vault: benchmarks, recent decisions, lessons, anomalies
2. Pull detailed platform data (campaign-level: spend, impressions, clicks, CTR, CPC, conversions, CPA, ROAS)
3. Compare last 7 days vs previous 7 days
4. Compare against benchmarks
5. Check if recent decisions are playing out as expected
6. Reference agency playbooks for best practices
7. Auto-save: anomalies, weekly snapshot, flag decision outcomes

**Output format:**
- Overall health: one sentence summary
- Platform-by-platform breakdown: metrics, trends, what's working, what's not
- Decision outcomes: how recent decisions are performing
- Recommendations: specific, actionable next steps with reasoning
- Saved to vault: list any auto-saved notes

Be specific with numbers. If live data is unavailable, say so plainly.

---

## Agents

### Briefing Agent

```yaml
# .claude/agents/briefing-agent.md
---
name: briefing-agent
description: Specializes in generating client briefings and status summaries. Reads vault data, synthesizes across decisions/meetings/projects, and delivers actionable morning updates.
---
```

**Role:** Generate concise, actionable briefings from vault data.
**Principles:**
1. Actionable: lead with what needs attention today
2. Accurate: reference vault sources, never hallucinate metrics
3. Concise: key points only, no fluff
4. Contextualized: compare against client benchmarks, not arbitrary numbers

**Tools:** File read/write/grep (plain markdown mode), Browser MCP or platform MCPs for live data when available.

### Project Agent

```yaml
# .claude/agents/project-agent.md
---
name: project-agent
description: Autonomously advances project tasks across client accounts. Reads project files, completes actionable tasks, flags blockers, and requests human input when needed.
---
```

**Role:** Work through project task checklists autonomously.
**Principles:**
1. Autonomous: do everything you can without asking
2. Transparent: always note what you did and why
3. Honest: if you can't do something, say why clearly
4. Thorough: check off tasks only when fully completed

**Tools:** File read/write/grep, bash for scripts and data processing, Browser MCP or platform MCPs for ad platform tasks.

---

## Config Files

### hooks.json

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "A vault write just occurred. If the file is inside vault/ and is not an _INDEX.md, verify it has proper YAML frontmatter per the vault schema in CLAUDE.md: type, client (if client-specific), date, status, source, confidence (if client-specific), importance (if client-specific), tags, related. Fix any missing fields before proceeding."
          }
        ]
      }
    ]
  }
}
```

Note: The PostToolUse matcher targets built-in file write tools for plain markdown mode. When Obsidian + Nexus MCP is added later, add a second matcher for `mcp__nexus__*` tools.

### settings.local.json

```json
{
  "permissions": {
    "allow": [
      "Bash(cd:*)",
      "Bash(cat:*)",
      "Bash(grep:*)",
      "Bash(find:*)",
      "Bash(mkdir:*)",
      "Bash(cp:*)",
      "Read",
      "Write",
      "Edit",
      "Glob"
    ]
  }
}
```

Note: When Codex CLI is added (Phase 1.5), add `"Bash(codex review:*)"` to the allow list. When MCPs are added, add `"enableAllProjectMcpServers": true` and the relevant MCP tool permissions.

### .mcp.json (Placeholder)

```json
{
  "mcpServers": {}
}
```

This is intentionally empty. MCP servers will be added as they are configured:
- Nexus (Claudesidian): when Obsidian is set up
- Google Ads MCP: when API credentials are provisioned
- Meta Ads MCP: when built or found
- Browser MCP: when Chrome automation is needed

---

## Playbooks (Pre-Populate)

### Meta Ads Playbook

Pre-populate `vault/_agency/playbooks/meta-ads-playbook.md` with:

**Campaign structure:**
- Separate prospecting and retargeting into distinct campaigns
- Use CBO for prospecting
- Use ABO for retargeting when you need precise frequency control
- 3-5 ad sets per campaign max — more dilutes learning

**Targeting:**
- Default to broad targeting for prospecting at $100+/day spend
- Only use interest targeting when: launching new product with no pixel data, spend under $50/day, or testing a specific niche hypothesis
- Lookalike audiences: start with 1% purchase LAL, expand to 3-5% when 1% saturates
- Exclude purchasers from prospecting (180-day window)

**Budget scaling:**
- Scale in 10-20% increments, not more
- Wait 3-4 days between scaling moves for the algorithm to restabilize
- If CPA spikes after scaling, wait 48h before reverting — it often corrects

**Creative:**
- Minimum 3 active creatives per ad set to avoid fatigue
- Replace creatives when CTR drops 30%+ from peak or frequency exceeds 3x
- UGC-style consistently outperforms polished brand content for prospecting
- Test one variable at a time (hook, format, CTA) — not multiple

**Retargeting:**
- 1-7 day window: highest intent, highest bids
- 8-30 day window: moderate intent, standard bids
- Watch frequency — above 6x means audience is too small or budget too high
- Dynamic product ads (DPA) for e-commerce clients with 50+ SKUs

**Measurement:**
- Use 7-day click, 1-day view attribution
- Don't trust Meta ROAS at face value — cross-reference with GA4 and backend data
- Check platform vs backend CPA weekly — if gap exceeds 20%, investigate

**Common mistakes:**
- Scaling budget too fast (>30% at once) — kills CPA
- Too many ad sets competing — consolidate
- Not excluding converters from prospecting — wastes spend
- Judging creative performance before 1,000 impressions

### Agency Lesson: Auto-Save Findings

Pre-populate `vault/_agency/lessons/auto-save-findings.md` with the pattern that any skill pulling live data should write noteworthy findings back to the vault. Anomalies to `anomalies/`, snapshots to `snapshots/`. Decisions and lessons stay manual. Check for duplicates before saving on repeated runs.

### Voltage Brand Voice Playbook

Pre-populate `vault/_agency/playbooks/voltage-brand-voice.md` with:
- No em dashes — ever
- Plain English over jargon
- Confident and direct
- Boutique expertise + technology adoption positioning
- Business Portfolio ID: 622383571242852

---

## Templates

### Decision Template

```markdown
---
type: decision
client: [client-name]
date: YYYY-MM-DD
status: active
source: manual
confidence: 0.8
importance: medium
tags: []
related:
  - "[[]]"
---

# [Short description]

**Decision:** [What was decided]

**Reasoning:**
[Why — reference data, benchmarks, patterns]

**Expected outcome:**
[What should happen if this works]

**Review date:** YYYY-MM-DD

Related: [[links]]
```

### Ticket Template

```markdown
---
type: ticket
client: [client-name]
date: YYYY-MM-DD
status: open
source: manual
confidence: 0.8
importance: medium
tags: [ticket]
related:
  - "[[]]"
due: YYYY-MM-DD
assignee: ""
---

# [Short title]

## Description
[What needs to be done and why]

## Acceptance Criteria
- [ ] [Criteria 1]
- [ ] [Criteria 2]

## Notes
(Agent adds timestamped notes as work progresses)
```

### Lesson Template

```markdown
---
type: lesson
client: [client-name]
date: YYYY-MM-DD
status: active
source: manual
importance: medium
tags: []
related:
  - "[[]]"
---

# [What was learned]

**Context:** [What happened that led to this learning]

**Lesson:** [The specific, actionable takeaway]

**Applies to:** [Which clients or situations this is relevant for]
```

### Anomaly Template

```markdown
---
type: anomaly
client: [client-name]
date: YYYY-MM-DD
status: active
source: [skill that detected it]
confidence: 0.8
importance: [low | medium | high]
tags: []
related:
  - "[[performance-benchmarks]]"
---

# [Short description of anomaly]

**Detected:** [What metric is outside acceptable range]
**Expected:** [What the benchmark says]
**Actual:** [What was observed]
**Potential cause:** [Initial hypothesis if available]
**Recommended action:** [What to do about it]
```

### Project Template

```markdown
---
type: project
client: [client-name]
date: YYYY-MM-DD
status: open
source: manual
importance: high
tags: []
related:
  - "[[]]"
due: YYYY-MM-DD
---

# [Project name]

## Objective
[What this project aims to achieve]

## Tasks
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

## Notes
(Agent adds timestamped notes as tasks are completed)
```

### Meeting Template

```markdown
---
type: meeting
client: [client-name]
date: YYYY-MM-DD
time: "HH:MM"
status: active
source: meeting-processor
importance: medium
tags: [meeting]
related:
  - "[[]]"
---

# [Meeting title / topic]

## Attendees
[List of attendees]

## Key Decisions
[Decisions made — each should also be saved as a separate decision note]

## Action Items
- [ ] [Action item] — Owner: [name] — Due: [date]

## Notes
[Any other important context or discussion points]
```

### Stakeholder Template

```markdown
---
type: stakeholder
client: [client-name]
date: YYYY-MM-DD
status: active
source: manual
tags: [stakeholder]
---

# [Name]

**Role:** [Their role at the client company]
**Email:** [Email]
**Notes:** [Communication preferences, decision-making style, key concerns]
```

---

## Bootstrap Script

`scripts/bootstrap_client.sh` — creates a new client folder from templates:

```bash
#!/bin/bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: scripts/bootstrap_client.sh <client-slug> \"<Client Name>\"" >&2
  exit 1
fi

client_slug="$1"
shift
client_name="$*"

script_dir="$(cd "$(dirname "$0")" && pwd)"
root_dir="$(cd "$script_dir/.." && pwd)"
template_dir="$root_dir/vault/_templates/client"
target_dir="$root_dir/vault/_clients/$client_slug"

if [[ ! -d "$template_dir" ]]; then
  echo "Template directory not found: $template_dir" >&2
  exit 1
fi

if [[ -e "$target_dir" ]]; then
  echo "Target already exists: $target_dir" >&2
  exit 1
fi

cp -R "$template_dir" "$target_dir"

# Remove template files from the live client folder
find "$target_dir" -type f -name "*-template.md" -delete

# Substitute placeholder names
find "$target_dir" -type f -name "*.md" -exec \
  sed -i "s/\[client-name\]/$client_slug/g; s/\[Client Name\]/$client_name/g" {} +

echo "Created client workspace at $target_dir"
```

---

## CLAUDE.md Spec

The `CLAUDE.md` file is the master operating instruction that Claude Code reads on every session. Write it to include:

1. **What The Forge is** (one paragraph)
2. **Vault location and structure** (folder tree reference)
3. **Working with clients:**
   - When a command specifies a client name, look in `vault/_clients/[client-name]/`
   - If no client is specified, ask which client
   - Always check the client's vault for context before giving recommendations
   - Check `_agency/playbooks/` for relevant best practices
   - Check `_agency/lessons/` for cross-client learnings
   - Use `_clients/_sandbox/` for dry runs before touching a real client
   - Use `_templates/client/` when creating a new client folder via `scripts/bootstrap_client.sh`
4. **Vault schema** (frontmatter format, file naming, writing rules)
5. **Auto-save rules** (what gets auto-saved, what requires human judgment)
6. **MCP servers** (currently none — placeholder for future additions with note about Obsidian/Nexus upgrade path)
7. **Quality rules:**
   - Don't hallucinate metrics
   - If you can't access something, say so
   - When saving decisions, always include what was decided and why
   - Keep client data isolated in the correct folder
   - Compare against client benchmarks, not arbitrary numbers
8. **Future: Codex review** (placeholder section noting that `codex review --uncommitted` will be added as a pre-commit step)
9. **Future: Obsidian upgrade** (note that the vault is designed to be Obsidian-compatible and the upgrade path is documented in FORGE-BUILD-SPEC.md)

---

## Sandbox Client

Pre-populate `vault/_clients/_sandbox/` with realistic fake data so skills can be tested without touching real clients. Include:
- A fake brand voice and target audience
- Performance benchmarks with specific numbers
- At least one decision with a review date that has already passed (to test `/reflect` catching overdue reviews)
- At least one anomaly
- At least one open ticket with acceptance criteria
- A content calendar with upcoming items

Make it a fictional DTC brand — something like a premium coffee subscription or a skincare brand. Give it a name. Make the numbers realistic enough to test against but obviously fake.

---

## Build Order

Execute in this exact sequence:

1. Create the full folder structure (all directories, empty folders included)
2. Write `CLAUDE.md`
3. Write all template files in `vault/_templates/`
4. Write the bootstrap script
5. Write all agency-level content (`_agency/playbooks/`, `_agency/lessons/`, `_agency/team/`)
6. Write TrūNiagen vault content (benchmarks, brand, _INDEX)
7. Write Bella Luna vault content (benchmarks, brand, _INDEX)
8. Write the sandbox client with fake data
9. Write `vault/_forge/_INDEX.md` and placeholder files
10. Write all 8 skill files in `.claude/skills/`
11. Write all 8 command files in `.claude/commands/`
12. Write both agent files in `.claude/agents/`
13. Write `hooks.json`
14. Write `settings.local.json`
15. Write `.mcp.json`
16. Initialize git repo, create `.gitignore` (exclude `.env`, `node_modules/`, any credentials files), make initial commit
17. Report what was built and confirm everything is in place

---

## What Comes After Phase 1

For architectural awareness only. Do not build these yet.

**Phase 1.5 — Codex CLI Integration:**
Install OpenAI Codex CLI. Add PreCommit hook: `codex review --uncommitted`. Add `"Bash(codex review:*)"` to settings.local.json permissions.

**Phase 2 — Email Intake & Autonomous Execution:**
Gmail polling loop (check dedicated inbox every 15 minutes). Task classification and planning. Gated ticket creation from email content. Execution pipeline with skill matching. Email response system for completed projects. Security/escalation layer for ambiguous or flagged requests.

**Phase 3 — Self-Improvement Loop:**
A continuous background project that runs when no client work is queued. Self-research: find new MCPs, skills, tools. Self-improvement: review learnings, identify failure patterns, propose structural changes. Skill acquisition: download, test, security-scan, and archive new capabilities. Memory optimization: identify stale data, redundant notes, gaps. Capability testing: periodically run skills against sandbox to catch regressions.

**Phase 4 — Team & Advanced Features:**
Multi-user vault access (remote Obsidian via MCP over network). Client-facing auto-generated reports. Budget-aware execution per project. Remote desktop for human-in-the-loop steps.
