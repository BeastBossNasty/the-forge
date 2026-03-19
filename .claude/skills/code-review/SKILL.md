---
name: code-review
description: Run Codex CLI as a code quality manager. Audits data accuracy in reports, finds gaps and optimizations in skills/scripts/HTML, and validates any deliverable before it ships.
---

# Code Review (Codex Manager)

## Purpose
Use OpenAI's Codex CLI as a second-opinion code and data quality manager. This skill invokes Codex to review code, reports, and deliverables for bugs, data mismatches, optimizations, and gaps. Can be triggered by command, conversationally, or automatically before shipping any deliverable.

## When to Use
- Before shipping any client report (PDF, HTML, or email)
- After writing or modifying skills, scripts, or config files
- When asked "have Codex check this" or "run a code review"
- As part of the pre-commit hook (already configured in .git/hooks/pre-commit)
- When debugging a failing skill or script

## Modes

### 1. Data Audit Mode (for reports and deliverables)
Verify that all numbers, metrics, and claims in a report match the vault source data.

**Steps:**
1. Read the report file (HTML, PDF script, or markdown)
2. Read the corresponding client vault data:
   - `benchmarks/performance-benchmarks.md`
   - `snapshots/` (all relevant snapshots)
   - `decisions/` (all decisions referenced)
3. Cross-reference every number in the report against vault sources
4. Flag any mismatches, rounding errors, or unsourced claims
5. Check that before/after date ranges are consistent
6. Verify chart data arrays match the narrative text

**Output:** List of verified numbers, flagged mismatches, and confidence level.

### 2. Code Quality Mode (for skills, scripts, HTML)
Review code for bugs, security issues, and optimizations.

**Steps:**
1. Run `codex review --uncommitted` for staged changes, OR
2. Run `codex review` on specific files passed as arguments
3. Parse Codex output for findings
4. Categorize by severity: P1 (must fix), P2 (should fix), P3 (nice to have)
5. For each finding, suggest a specific fix

**Output:** Prioritized list of issues with suggested fixes.

### 3. Gap Analysis Mode (for the overall system)
Review the full project for missing capabilities, incomplete skills, or structural issues.

**Steps:**
1. Read CLAUDE.md for the system's documented capabilities
2. Scan all skill files for completeness
3. Check that every command has a matching skill
4. Check that every skill referenced in other skills exists
5. Look for TODO comments, placeholder content, or stub implementations
6. Compare against the original FORGE-BUILD-SPEC.md for drift

**Output:** Gap report with severity and recommendations.

## How to Invoke

### Via command: `/code-review [target]`
- `/code-review` -- review uncommitted changes (default)
- `/code-review report bella-luna` -- data audit the latest Bella Luna report
- `/code-review gaps` -- run gap analysis on the full system
- `/code-review [filepath]` -- review a specific file

### Conversationally:
- "Have Codex check this"
- "Run a code review on the report"
- "Audit the numbers in the Bella Luna case study"
- "Check for gaps in the system"

### Automatically:
- Pre-commit hook runs Codex on every commit (already configured)
- The generate-report skill should auto-trigger data audit mode before saving

## Integration with Codex CLI

The skill calls Codex CLI directly:
```bash
codex review --uncommitted                    # Default: review staged changes
codex review -- [file1] [file2]               # Review specific files
```

Codex CLI uses GPT-5.4 with xhigh reasoning effort. It runs in read-only sandbox mode and cannot modify files.

## Rules
- Never ship a client deliverable without running data audit mode first.
- Codex findings are advisory, not blocking (unless P1 severity).
- P1 issues must be fixed before delivery. P2 issues should be fixed. P3 is optional.
- Log all review results to `vault/_forge/learnings/YYYY-MM-DD-code-review.md`.
- If Codex flags a data mismatch in a report, verify against the source vault files before changing anything. Codex can be wrong.
- The data audit should check: total revenue, total spend, ROAS calculations, purchase counts, CPA math, date ranges, and percentage changes.
