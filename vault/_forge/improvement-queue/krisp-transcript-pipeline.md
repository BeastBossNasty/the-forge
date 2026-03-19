---
type: project
date: 2026-03-18
status: open
source: manual
importance: high
tags: [krisp, transcripts, meetings, pipeline, phase-next]
---

# Krisp Transcript Pipeline -- Path 3 (API Integration)

## Objective
Auto-ingest every Voltage client call transcript from Krisp via API. Store as searchable vault context. Build a living verbal history per client that AMs can query conversationally and The Forge can reference for briefings, decisions, and pattern detection.

## Architecture

```
Krisp API --> Scheduled Task (daily poll) --> Transcript Processor Skill
    |
    v
vault/_clients/[client]/meetings/
    YYYY-MM-DD-call-topic.md          (structured meeting note)
    YYYY-MM-DD-call-topic-transcript.md  (full raw transcript, searchable)
```

## Phase 1: Krisp API Discovery

### What we need to find out
- Does Krisp have a public API for retrieving transcripts?
- Authentication method (API key, OAuth, etc.)
- Rate limits and data retention policies
- What data is available (full transcript, summary, attendees, duration, timestamps?)
- Can we filter by date range to avoid re-processing old calls?
- Is there a webhook option (push instead of poll)?

### Research tasks
- [ ] Check Krisp developer docs / API documentation
- [ ] Check if Krisp has MCP server or community integrations
- [ ] Check Krisp account settings for API key generation
- [ ] Test API access with a simple curl call
- [ ] Document available endpoints and response format

## Phase 2: Transcript Processor Skill

### New skill: `/process-transcript`

**Input:** Raw Krisp transcript JSON/text
**Processing:**
1. Identify the client from attendee list, calendar context, or conversation content
2. Extract structured data:
   - Attendees (map to vault stakeholders)
   - Duration
   - Key topics discussed
   - Decisions made (trigger `/save-decision` for each)
   - Action items with owners and due dates (offer to create tickets)
   - Client sentiment / concerns raised
   - Follow-up items mentioned
3. Generate two vault files:
   - **Structured meeting note** (frontmatter, key decisions, action items, summary)
   - **Raw transcript** (full text, searchable by Nexus semantic search)
4. Link to related decisions, benchmarks, and previous meetings via wikilinks
5. Update client _INDEX.md with the new meeting

### Auto-classification patterns
The processor needs to figure out which client a call belongs to. Options:
- Match attendee emails against `stakeholders/` directory
- Match calendar event title (if Krisp includes it)
- Match keywords in transcript (company names, product names, account references)
- Fall back to asking Jake if ambiguous

### Frontmatter for meeting notes
```yaml
---
type: meeting
client: [auto-detected]
date: YYYY-MM-DD
time: "HH:MM"
status: active
source: krisp-api
importance: medium
tags: [meeting, krisp, auto-transcribed]
related:
  - "[[previous-meeting]]"
  - "[[relevant-decision]]"
duration: "HH:MM"
attendees: [list]
krisp_meeting_id: [for dedup]
---
```

## Phase 3: Scheduled Polling

### New scheduled task: `krisp-transcript-ingest`
- **Schedule:** Daily at 7:00 AM (before the morning briefing at 7:30)
- **Process:**
  1. Authenticate with Krisp API
  2. Query for transcripts since last poll (store last poll timestamp in `vault/_forge/krisp-config.md`)
  3. For each new transcript:
     a. Check if already processed (dedup by Krisp meeting ID stored in frontmatter)
     b. Run through `/process-transcript`
     c. Log to `vault/_forge/learnings/YYYY-MM-DD-krisp-ingest.md`
  4. Update last poll timestamp

### Credentials
- Store Krisp API key in `.env` (already gitignored)
- Add `KRISP_API_KEY=` placeholder
- Add `KRISP_LAST_POLL=` for tracking

## Phase 4: Searchable Context Layer

### What AMs can ask (via Cowork)
- "What did we discuss with Bella Luna last week?"
- "When did Bowling.com mention wanting video ads?"
- "Show me every time GGB's client brought up holiday planning"
- "What concerns has the TruNiagen team raised in the last 3 months?"
- "Summarize all calls with [stakeholder name]"

### How it works with Nexus
- Nexus indexes both the structured notes and raw transcripts
- Semantic search finds relevant passages even without exact keyword matches
- Graph view shows how calls connect to decisions and outcomes
- The 4D scoring system can cross-reference call context with decision outcomes

### How it feeds The Forge's brain
- `/briefing [client]` includes "In the last call on [date], [stakeholder] mentioned [topic]"
- `/reflect [client]` can detect patterns across calls ("client has mentioned creative fatigue 4 times in 6 weeks")
- `/weekly-report [client]` references call context for decision evaluations
- `/analyze-rulesets` can correlate client feedback from calls with performance data

## Phase 5: Living Verbal History

### Per-client call timeline
Each client's _INDEX.md gets a "Recent Calls" section auto-updated:
```
## Recent Calls
- [[2026-03-18-weekly-status]] -- Discussed Q2 creative refresh, client approved UGC test
- [[2026-03-11-performance-review]] -- Reviewed Feb numbers, client happy with ROAS improvement
- [[2026-03-04-budget-planning]] -- Q2 budget allocation, +20% approved for April
```

### Cross-client intelligence
Agency-level patterns from calls:
- "Multiple clients are asking about video ads this month"
- "Holiday planning discussions typically start in September across all accounts"
- "Clients who see their ROAS data in calls are 3x more likely to approve budget increases"

### Stakeholder profiling
Over time, the system builds implicit profiles:
- Communication style (data-driven vs intuition)
- Decision-making speed (approves quickly vs needs multiple calls)
- Hot-button topics (creative quality, budget efficiency, competitive pressure)
- Relationship health indicators (engagement level, pushback frequency)

## Implementation Order

1. **Research Krisp API** (30 min) -- find out what's available
2. **Build `/process-transcript` skill** (1 hour) -- the core processor
3. **Test with a real transcript** -- manually feed one in to verify output quality
4. **Set up scheduled polling** (30 min) -- daily auto-ingest
5. **Wire into existing skills** -- update briefing, reflect, weekly-report to reference call data
6. **Test the conversational search** -- verify AMs can query call history through Cowork

## Open Questions
- Does Krisp's free/pro plan include API access or is it enterprise only?
- What's the transcript quality? Do we need post-processing for speaker identification?
- Should we store audio files in the vault or just text? (storage implications)
- How far back can we pull historical transcripts? (seeding the vault like we did with Meta data)
- Do we need speaker diarization (who said what) or is a flat transcript sufficient?

## Dependencies
- Krisp API access (may require account upgrade)
- Nexus MCP working (for semantic search over transcripts)
- Obsidian running (for Nexus)
