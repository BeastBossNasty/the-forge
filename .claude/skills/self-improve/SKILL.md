---
name: self-improve
description: Review The Forge's own operation. Identify failure patterns, stale data, structural gaps, and propose improvements. Runs when no client work is queued.
---

# Self-Improve

## Purpose
Continuous self-improvement loop. Review how The Forge is operating, identify what's broken or could be better, and take action to improve.

## Steps

1. **Review learnings and processing logs:**
   - Read all files in `vault/_forge/learnings/`
   - Look for patterns: repeated failures, common unclassifiable emails, skills that produce poor output
   - Identify recurring issues that need structural fixes

2. **Audit vault health:**
   - Check every client folder for stale data (benchmarks, brand docs, pipeline items not updated in 30+ days)
   - Check for orphaned notes (files with broken wikilinks)
   - Check for missing frontmatter or malformed YAML
   - Check for empty folders that should have content
   - Check for duplicate notes covering the same topic

3. **Review skill effectiveness:**
   - Read `vault/_forge/capability-log/` for skill performance history
   - Identify skills that are frequently matched but produce poor results
   - Identify gaps: task types that come in but have no matching skill

4. **Check improvement queue:**
   - Read `vault/_forge/improvement-queue/` for pending improvements
   - Prioritize by impact and feasibility
   - Execute any improvements that can be done now (fix frontmatter, update stale docs, restructure notes)

5. **Propose structural changes:**
   - If a pattern suggests a new skill is needed, propose it
   - If a skill's classification keywords are too broad or narrow, suggest adjustments
   - If the inbox config needs updating, suggest changes
   - Write proposals to `vault/_forge/improvement-queue/`

6. **Log what was done:**
   - Save a summary to `vault/_forge/learnings/YYYY-MM-DD-self-improvement.md`

## Output Format

### Vault Health
- Stale data: [files not updated in 30+ days]
- Missing frontmatter: [files with issues]
- Empty folders: [folders that need content]
- Broken links: [wikilinks that don't resolve to real files]

### Pattern Analysis
- Recurring issues from processing logs
- Skill gaps identified
- Classification accuracy assessment

### Actions Taken
- Fixes applied (frontmatter corrections, stale data flags, etc.)
- Improvements queued for review

### Proposals
- Structural changes proposed for Jake to review
- New skills or skill modifications suggested

## Rules
- Never modify client decisions or lessons without Jake's approval.
- Can fix frontmatter, update indexes, and flag stale data autonomously.
- Proposals for structural changes go to `improvement-queue/`, not directly implemented.
- Always log what was done and why.
- This skill does not pull live platform data. Vault-only analysis.
