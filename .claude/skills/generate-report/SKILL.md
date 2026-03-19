---
name: generate-report
description: Generate a client-facing performance report as a standalone HTML file. Pulls vault data, formats it professionally, and outputs a shareable report.
---

# Generate Report

## Purpose
Create a polished, client-facing performance report that can be shared externally. Outputs a standalone HTML file with professional formatting.

## Steps

1. Identify the client from the command argument. If not provided, ask which client.
2. Determine report period (default: last 7 days). Accept custom date ranges if specified.
3. Read client vault:
   - `benchmarks/performance-benchmarks.md` for KPI context
   - `decisions/` for recent decisions and their outcomes
   - `anomalies/` for flagged issues
   - `snapshots/` for historical performance data
   - `brand/brand-voice.md` for client-appropriate tone
   - `pipeline/content-calendar.md` for upcoming work context
4. Pull platform data if available (via MCP or Browser MCP)
5. Generate the report content:
   - Executive summary (2-3 sentences)
   - Performance metrics table with trend indicators
   - Key wins and challenges
   - Strategic actions taken and their results
   - Upcoming priorities
   - Recommendations
6. Output as a standalone HTML file to `vault/_clients/[client]/reports/`
   - Filename: `YYYY-MM-DD-[period]-report.html`
   - Professional styling (clean, modern, Voltage branding)
   - Print-friendly layout
   - No external dependencies (all CSS inline)

## Report HTML Template Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>[Client] Performance Report - [Date Range]</title>
  <style>
    /* Clean, professional styling */
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 800px; margin: 0 auto; padding: 40px; color: #1a1a1a; }
    h1 { color: #111; border-bottom: 3px solid #111; padding-bottom: 12px; }
    h2 { color: #333; margin-top: 32px; }
    .metric-table { width: 100%; border-collapse: collapse; margin: 16px 0; }
    .metric-table th, .metric-table td { padding: 10px 14px; text-align: left; border-bottom: 1px solid #e0e0e0; }
    .metric-table th { background: #f5f5f5; font-weight: 600; }
    .up { color: #16a34a; }
    .down { color: #dc2626; }
    .neutral { color: #737373; }
    .highlight { background: #f0fdf4; padding: 16px; border-left: 4px solid #16a34a; margin: 16px 0; }
    .warning { background: #fef2f2; padding: 16px; border-left: 4px solid #dc2626; margin: 16px 0; }
    .footer { margin-top: 48px; padding-top: 16px; border-top: 1px solid #e0e0e0; color: #737373; font-size: 14px; }
    @media print { body { padding: 20px; } }
  </style>
</head>
<body>
  <!-- Report content generated dynamically -->
</body>
</html>
```

## Output Format (Console)

### Report Generated
- File: `vault/_clients/[client]/reports/YYYY-MM-DD-weekly-report.html`
- Period: [date range]
- Sections: executive summary, metrics, wins, challenges, actions, recommendations

### Data Sources
- Vault data: [list what was read]
- Live data: [available/unavailable]

## Rules
- Follow the client's brand voice when writing the report.
- Follow Voltage brand voice for internal sections.
- No em dashes anywhere in the report.
- Be specific with numbers. Never approximate when you have exact data.
- If live data is unavailable, clearly state "Data from vault records" at the top.
- Never hallucinate metrics. If a number isn't in the vault or live data, don't include it.
- Create the `reports/` directory if it doesn't exist.
- Reports are standalone HTML. No external CSS, JS, or image dependencies.
