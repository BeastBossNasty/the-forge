# THE FORGE -- Operating Instructions

The Forge is an AI-powered operating system for managing ad campaigns and executing tasks autonomously. It is built for a single user (Jake) who interacts entirely in plain English. Claude Code is the builder, operator, and learner. Every interaction happens through slash commands, vault reads/writes, and MCP integrations. Never ask Jake to edit code, debug, or read logs.

---

## Vault Location and Structure

All knowledge lives in `vault/` as plain markdown files. Claude Code reads and writes them using built-in file tools (Read, Write, Grep, Glob). No Obsidian dependency yet, but all structural decisions are Obsidian-compatible from day one.

```
vault/
  _agency/          Agency-wide playbooks, lessons, and team info
  _clients/         Per-client knowledge (one folder per client)
    _sandbox/       Test client for dry runs
    truniagen/      TruNiagen (ChromaDex)
    bella-luna/     Bella Luna Toys
  _forge/           Forge self-improvement data
  _templates/       Templates for new notes and new clients
```

Each client folder contains: `benchmarks/`, `brand/`, `decisions/`, `lessons/`, `anomalies/`, `pipeline/`, `projects/`, `tickets/`, `meetings/`, `snapshots/`, `stakeholders/`, and an `_INDEX.md`.

---

## Working with Clients

- When a command specifies a client name, look in `vault/_clients/[client-name]/`
- If no client is specified, ask which client
- Always check the client's vault for context before giving recommendations
- Check `_agency/playbooks/` for relevant best practices
- Check `_agency/lessons/` for cross-client learnings
- Use `_clients/_sandbox/` for dry runs before touching a real client
- Use `_templates/client/` when creating a new client folder via `scripts/bootstrap_client.sh`
- Keep client data isolated in the correct folder. Never cross-contaminate.

---

## Vault Schema

### Frontmatter (Required on Every Note)

Every markdown file in the vault (except `_INDEX.md` files) must have this YAML frontmatter:

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

---

## Auto-Save Rules

Skills that pull live data should write findings back to the vault.

**Auto-save (no human approval needed):**
- Anomalies: any metric outside the client's acceptable range -> `anomalies/` (check for existing notes first to prevent duplicates on repeated runs)
- Snapshots: periodic performance data captures -> `snapshots/` (NOT `benchmarks/` -- that folder holds KPI targets only)

**Never auto-save (requires human judgment):**
- Decisions
- Lessons
- Validated decisions being converted to lessons

When a decision outcome becomes clear (validated or failed), flag it in the output for Jake to act on. Do not auto-convert.

---

## MCP Servers & API Access

**Gmail MCP:** Connected to `voltage.the.forge@gmail.com` (Forge dedicated inbox). Used by `/check-inbox` for email intake and task routing.

**Meta Ads API:** Credentials in `.env`. Long-lived token (expires 2026-05-07). Covers all 5 client ad accounts:
- TruNiagen: act_196113284341625
- Bella Luna: act_551906995157520
- Bowling.com: act_1935937429809554
- GGB: act_646330722224163
- HABA: act_941543396233578

**Nexus MCP (Obsidian):** Connected via `.mcp.json`. The Nexus plugin runs inside Obsidian and gives Claude Code semantic search, graph traversal, and structured queries over the vault. Prefer Nexus tools over raw file reads when available. Obsidian must be running for Nexus to work.

**Future additions:**
- Google Ads MCP: when API credentials are provisioned
- Browser MCP: when Chrome automation is needed

---

## Rubric Engine & 4D Scoring

Every client has a rubric in `benchmarks/performance-benchmarks.md` defining tier thresholds, hard stops, and scaling constraints. See `vault/_agency/playbooks/rubric-engine.md` for the full playbook.

### 4D Decision Scoring (Automatic)
Decisions are automatically scored using 4-dimensional signal weighting:
1. **Temporal decay:** Recent signals weighted more (half-life 15-30 days)
2. **Contextual lift:** Decisions in similar conditions get boosted (seasonal + state similarity)
3. **Outcome trust:** Improved decisions boosted 1.2x, worsened penalized 0.7x
4. **Category success:** High-success categories boosted 1.15x

This runs automatically during `/briefing`, `/weekly-report`, and `/performance-review`. No manual trigger needed. Scoring results are appended to decision notes.

### Ruleset Analysis
`/analyze-rulesets [client]` compares rubric thresholds against scored decision outcomes and suggests adjustments. Also runs automatically during `/self-improve`.

### Client Quick Reference

| Client | Model | Healthy | Caution | Floor |
|--------|-------|---------|---------|-------|
| TruNiagen | LTV Conservative | Adj ROAS >= 1.5x | >= 1.2x | < 1.2x |
| Bella Luna | Momentum (gradient) | ROAS >= 10x | >= 5x | < 5x |
| Bowling | CPA-focused | ROAS >= 15x | >= 12x | < 12x |
| GGB | Standard E-com | ROAS >= 4x | >= 2x | < 2x |
| HABA | Conservative | ROAS >= 4x | >= 2x | < 2x |

---

## Quality Rules

1. Don't hallucinate metrics. Only report what you can actually see in a platform or file.
2. If you can't access something, say so plainly. Never invent data.
3. When saving decisions, always include what was decided, the reasoning, expected outcome, and a review date.
4. Keep client data isolated in the correct client folder. Never cross-contaminate.
5. Compare against client benchmarks, not arbitrary numbers.
6. Never auto-save decisions or lessons. Those require human judgment.
7. Downloaded MCPs and skills must be scanned before use (check GitHub stars, recent activity, known issues).
8. When in doubt, ask Jake. He would rather be asked than have something go wrong silently.

---

## Security Principles

- Client data stays isolated in the correct client folder
- Never hallucinate metrics
- Never auto-save decisions or lessons
- Downloaded MCPs and skills must be scanned before use
- When in doubt, ask Jake

## Email Intake (Phase 2)

**Inbox:** voltage.the.forge@gmail.com
**Command:** `/check-inbox` (manual) + scheduled polling every 15 minutes
**Config:** `vault/_forge/inbox-config.md`

### How It Works
1. Poll inbox for unread emails
2. Verify sender is authorized (Jake only, for now)
3. Classify the task and match to a skill
4. Route based on tier:
   - **Auto-execute:** Read-only skills (briefing, reflect, check-tickets, weekly-report, performance-review) run immediately, draft reply with results
   - **Approval required:** Write skills (save-decision, create-ticket, process-meeting) create a pending ticket, draft reply asking for approval
   - **Escalate:** Live platform changes, money, credentials, or ambiguous requests create a high-priority ticket and flag for Jake
5. All replies are sent directly via `scripts/send_email.py`. No drafts.

### Processing Log
Daily log saved to `vault/_forge/learnings/YYYY-MM-DD-inbox-processing.md`

---

## Brand Voice (All Voltage Content)

- No em dashes -- ever, anywhere, for any reason
- Plain English over jargon
- Confident and direct, not hedging or disclaimering
- Boutique expertise + tech-forward positioning

---

## Self-Improvement (Phase 3)

The Forge improves itself continuously. Scheduled daily at 6am on weekdays.

**Commands:**
- `/self-improve` -- Review vault health, identify failure patterns, propose structural changes
- `/capability-sprint` -- Search for new MCPs, skills, and tools. Security-scan and archive.
- `/regression-test` -- Run all skills against the sandbox client to catch regressions

**How it works:**
1. Self-improve: audit vault health, review processing logs, identify patterns, propose fixes
2. Regression test: run every skill against sandbox, grade results, flag failures
3. Capability sprint: search for new tools, security-scan (min 10+ GitHub stars, updated within 6 months), test in sandbox, archive approved tools

**Storage:**
- `vault/_forge/skills-archive/` -- evaluated tools with security scan results
- `vault/_forge/learnings/` -- processing logs, improvement reports, test results
- `vault/_forge/capability-log/` -- capability evaluation history
- `vault/_forge/improvement-queue/` -- proposed changes awaiting review

**Rules:**
- Never install tools without security scanning first
- Never modify client data during self-improvement (vault health fixes are limited to frontmatter and indexes)
- Proposals for structural changes go to improvement-queue, not directly implemented
- Always clean up test data after regression tests

---

## Team & Advanced Features (Phase 4)

**Commands:**
- `/generate-report [client]` -- Create a client-facing HTML performance report
- `/budget-check [client] [project/ticket]` -- Check project budget status before executing
- `/human-handoff` -- Create a structured handoff when human intervention is needed

### Client-Facing Reports
Generate standalone HTML reports for sharing with clients. Professional styling, Voltage branding, print-friendly. Saved to `vault/_clients/[client]/reports/`.

### Budget-Aware Execution
Projects and tickets can have optional budget fields in frontmatter (`budget_hours`, `budget_dollars`, etc.). Before costly operations, check spend against allocation. Green/Yellow/Red status system. Red blocks execution until Jake approves.

### Multi-User Access Control
Config: `vault/_forge/access-control.md`
Roles: admin (full access), operator (read-only commands), viewer (reports only).
Client isolation enforced per user. Currently Jake-only. Adding users requires updating access-control.md and inbox-config.md.

### Human-in-the-Loop Handoff
When The Forge hits a step requiring human action (platform login, visual review, payment, etc.), it creates a structured handoff ticket, sends Jake an email notification, and pauses. The ticket includes step-by-step instructions and context. `/check-tickets` handles resume after the human step is done.

---

## Codex Review (Active)

Codex CLI is installed and runs `codex review --uncommitted` as a git pre-commit hook. This uses OpenAI's GPT model as a second opinion to catch mistakes before commits.

---

## Future: Obsidian Upgrade

The vault is designed to be Obsidian-compatible from day one. All internal references use `[[wikilink]]` syntax. All notes use standardized YAML frontmatter. The upgrade path is: install Obsidian, point it at `vault/`, install the Nexus (Claudesidian) plugin, update `.mcp.json`, and update this file. Nothing gets rebuilt or migrated. Full details in `FORGE-BUILD-SPEC.md`.
