---
type: preferences
date: 2026-03-18
status: active
source: manual
tags: [access-control, multi-user, config]
---

# Access Control Configuration

## User Roles

### Admin
- Full access to all vault data and all commands
- Can modify access control settings
- Can approve escalated tasks
- Can modify client data directly

### Operator
- Can run read-only commands (briefing, reflect, check-tickets, weekly-report, performance-review)
- Can view client data but not modify decisions or lessons
- Cannot approve escalated tasks
- Cannot modify access control settings

### Viewer
- Can view reports only
- No command access
- No vault write access

## Current Users

| User | Email | Role | Clients |
|------|-------|------|---------|
| Jake Brown | jakeb11@gmail.com | admin | all |

## Adding Users

To add a new user:
1. Add their entry to the table above with role and permitted clients
2. Add their email to `vault/_forge/inbox-config.md` authorized senders (if they should be able to email tasks)
3. Set their client access (specific clients or "all")

## Client Isolation Rules

- Users with specific client access can only see/modify data in their assigned client folders
- Agency-wide playbooks and lessons are readable by all roles
- Team member profiles in `_agency/team/` are readable by all roles
- The `_forge/` folder is admin-only
- The `_sandbox/` client is accessible by all roles (for testing)

## Future: Remote Vault Access

When Obsidian + Nexus MCP is set up:
- Multiple users can access the vault simultaneously via Obsidian Sync or a shared drive
- Access controls will be enforced at the MCP layer
- Each user's Claude Code session will respect their role permissions
