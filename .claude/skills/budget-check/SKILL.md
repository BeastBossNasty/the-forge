---
name: budget-check
description: Track and enforce project budgets. Check time/resource spend against allocated budgets before executing tasks. Prevent overspend.
---

# Budget Check

## Purpose
Track project and task budgets. Every project can have an allocated budget (time, money, or both). This skill checks current spend against allocation before allowing execution to proceed.

## Budget Configuration

Each project or ticket can have budget fields in its frontmatter:

```yaml
budget_hours: 10          # Total hours allocated
budget_spent_hours: 3.5   # Hours used so far
budget_dollars: 500       # Dollar budget (for ad spend, tool costs, etc.)
budget_spent_dollars: 125 # Dollars spent so far
budget_alert_threshold: 0.8  # Alert at 80% spend (default)
```

## Steps

1. Identify the client and project/ticket from context
2. Read the project or ticket file
3. Check budget fields:
   - If `budget_hours` exists, compare `budget_spent_hours` against it
   - If `budget_dollars` exists, compare `budget_spent_dollars` against it
4. Determine status:
   - **Green:** Under 80% of budget (or threshold) -- proceed normally
   - **Yellow:** Between 80-100% of budget -- warn and ask for confirmation
   - **Red:** Over 100% of budget -- block execution, require Jake's approval
5. If checking before a task execution:
   - Estimate the cost of the task
   - Add estimate to current spend
   - If the total would exceed budget, flag before proceeding
6. After task completion:
   - Update `budget_spent_hours` or `budget_spent_dollars` in the project/ticket file
   - Log the spend to the project notes

## Integration with Other Skills

This skill is called by other skills before executing costly operations:
- Before running ad platform changes (budget_dollars)
- Before starting long-running tasks (budget_hours)
- Before capability-sprint downloads (budget_dollars for any paid tools)

### How to call from another skill:
Check the project/ticket frontmatter for budget fields. If present, verify spend is within limits before proceeding. If budget would be exceeded, stop and notify Jake.

## Output Format

### Budget Status: [Client] - [Project/Ticket]

| Resource | Allocated | Spent | Remaining | Status |
|----------|-----------|-------|-----------|--------|
| Hours | [X] | [Y] | [Z] | GREEN/YELLOW/RED |
| Dollars | [X] | [Y] | [Z] | GREEN/YELLOW/RED |

### Recommendation
[Proceed / Warn / Block -- with reasoning]

## Rules
- Never proceed with a task that would exceed a red budget without Jake's explicit approval.
- Yellow budgets generate a warning but don't block.
- If no budget fields exist on a project/ticket, the skill is a no-op (no budget tracking).
- Budget tracking is opt-in per project. Not every task needs a budget.
- Always update spend after task completion.
- Log all budget checks to the project/ticket notes section.
