---
name: capability-sprint
description: Search for, evaluate, download, security-scan, and archive new MCP servers, skills, and tools to expand The Forge's capabilities.
---

# Capability Sprint

## Purpose
Stock The Forge's arsenal. Find new MCPs, skills, plugins, and tools that could expand what The Forge can do. Download, scan for security, test, and archive them.

## Steps

1. **Identify capability gaps:**
   - Read `vault/_forge/improvement-queue/` for requested capabilities
   - Read `vault/_forge/capability-log/` for what's already been evaluated
   - Read recent processing logs for tasks that failed or couldn't be completed
   - Determine what new tools would have the highest impact

2. **Search for tools:**
   - Search GitHub for relevant MCP servers, Claude Code skills, and plugins
   - Search for tools matching identified gaps (e.g., Meta Ads MCP, Google Ads MCP, data processing tools)
   - Check Claude Code community resources for shared skills
   - Use web search to find recently published tools

3. **Security scan each candidate:**
   - Check GitHub stars, forks, and recent activity (minimum: 10+ stars, updated within 6 months)
   - Check for known issues or security advisories
   - Review the README and source code for red flags (obfuscated code, suspicious network calls, credential harvesting)
   - Check the license for compatibility
   - If anything looks suspicious, skip it and log why

4. **Test in sandbox:**
   - Install the tool in a test configuration
   - Run it against the sandbox client data
   - Verify it produces expected output
   - Check for side effects (unexpected file writes, network calls)

5. **Archive approved tools:**
   - Save tool metadata to `vault/_forge/skills-archive/` as `tool-name.md`:
     ```
     ---
     type: snapshot
     date: YYYY-MM-DD
     status: [approved | rejected | needs-review]
     source: forge-research
     tags: [capability, mcp/skill/plugin, category]
     ---
     # [Tool Name]
     **Source:** [GitHub URL]
     **Type:** [MCP server | skill | plugin | script]
     **Purpose:** [What it does]
     **Stars:** [count] | **Last updated:** [date]
     **Security scan:** [pass | fail | flagged]
     **Test result:** [pass | fail | partial]
     **Notes:** [Any relevant context]
     ```
   - If approved, add installation instructions to the archive entry
   - Update `vault/_forge/capability-log/` with what was evaluated

6. **Log the sprint:**
   - Save summary to `vault/_forge/learnings/YYYY-MM-DD-capability-sprint.md`

## Output Format

### Tools Evaluated
| Tool | Type | Stars | Security | Test | Status |
|------|------|-------|----------|------|--------|
| [name] | [MCP/skill/plugin] | [count] | [pass/fail] | [pass/fail] | [approved/rejected] |

### Newly Archived
List of tools added to the skills archive with brief descriptions.

### Gaps Remaining
Capabilities still needed that no good tool was found for.

### Recommendations
Tools that need Jake's approval before installation (e.g., tools requiring API keys or elevated permissions).

## Rules
- Never install a tool without scanning it first.
- Minimum threshold: 10+ GitHub stars, updated within 6 months, no security flags.
- Always test against sandbox before approving for production use.
- Never auto-install tools that require API keys or credentials. Flag those for Jake.
- Log everything: what was evaluated, why it was approved or rejected.
- Check `vault/_forge/skills-archive/` before evaluating to avoid re-scanning known tools.
