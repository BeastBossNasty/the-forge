---
name: regression-test
description: Run all skills against the sandbox client to verify they still work correctly. Catches regressions from structural changes or skill updates.
---

# Regression Test

## Purpose
Periodically run every skill against the sandbox client to verify they still produce correct output. Catches regressions before they affect real clients.

## Steps

1. **Pre-flight check:**
   - Verify sandbox client data exists and is intact
   - Read `vault/_clients/_sandbox/_INDEX.md` to confirm structure
   - Note the current state of sandbox data (decisions, tickets, anomalies) for comparison

2. **Run each skill against sandbox:**

   a. **Briefing** (`_sandbox`):
      - Should produce a performance snapshot, flag the CPA anomaly, note the overdue decision review, list open tickets
      - Pass criteria: mentions benchmarks, references the anomaly, identifies overdue items

   b. **Reflect** (`_sandbox`):
      - Should identify overdue reviews, patterns, gaps
      - Pass criteria: catches the overdue budget scale decision, flags the active anomaly

   c. **Check Tickets** (`_sandbox`):
      - Should find the open UGC creative refresh ticket
      - Pass criteria: correctly identifies open tickets, notes acceptance criteria status

   d. **Weekly Report** (`_sandbox`):
      - Should produce a weekly summary referencing benchmarks
      - Pass criteria: references benchmarks, notes no live data available, identifies decision outcomes

   e. **Save Decision** (`_sandbox`):
      - Test with a mock decision: "Test decision for regression testing"
      - Pass criteria: creates a properly formatted decision note with frontmatter
      - Cleanup: delete the test decision note after verification

   f. **Create Ticket** (`_sandbox`):
      - Test with a mock ticket: "Test ticket for regression testing"
      - Pass criteria: creates a properly formatted ticket with frontmatter and acceptance criteria
      - Cleanup: delete the test ticket after verification

   g. **Performance Review** (`_sandbox`):
      - Should produce a deep dive referencing benchmarks
      - Pass criteria: references benchmarks, notes no live data, identifies decision outcomes

   h. **Check Inbox:**
      - Verify the send script works: send a test email to voltage.the.forge@gmail.com
      - Pass criteria: email sends without error

3. **Grade each skill:**
   - PASS: produced correct output matching pass criteria
   - PARTIAL: produced output but missed some criteria
   - FAIL: errored out or produced incorrect/empty output

4. **Cleanup:**
   - Delete any test notes created during the run
   - Verify sandbox data is in the same state as before the test

5. **Log results:**
   - Save to `vault/_forge/learnings/YYYY-MM-DD-regression-test.md`

## Output Format

### Regression Test Results

| Skill | Status | Notes |
|-------|--------|-------|
| briefing | PASS/PARTIAL/FAIL | [details] |
| reflect | PASS/PARTIAL/FAIL | [details] |
| check-tickets | PASS/PARTIAL/FAIL | [details] |
| weekly-report | PASS/PARTIAL/FAIL | [details] |
| save-decision | PASS/PARTIAL/FAIL | [details] |
| create-ticket | PASS/PARTIAL/FAIL | [details] |
| performance-review | PASS/PARTIAL/FAIL | [details] |
| check-inbox (send) | PASS/PARTIAL/FAIL | [details] |

### Overall: [X/8 passing]

### Issues Found
List any regressions or problems discovered.

### Recommendations
Fixes needed for failing skills.

## Rules
- Always clean up test data after the run. The sandbox should be in the same state before and after.
- Never run regression tests against real client data.
- Log all results, even if everything passes.
- If a skill fails, do not attempt to fix it during the test run. Log it and move on.
