# Need: Three-Tier Architecture — User Stories

## Actors

- **Agent**: AI agent (Claude, Gemini, Cursor, etc.) working in the layer-stage system
- **Developer**: Human maintaining the system (Dawson)

---

### US-1: Agent regains competence after compaction
**As an** agent whose context was just compacted,
**I want to** read Tier 1 (pointers) then Tier 2 (distilled knowledge) and be competent,
**So that** I don't need to re-read all stage outputs to continue working.

**Acceptance**: Agent reads ~260 lines (not ~5,000) and can answer domain questions correctly.

---

### US-2: Agent knows where to find details
**As an** agent that needs a specific detail (e.g., STDP timing window),
**I want** the knowledge file to tell me exactly which stage output file and section has the full explanation,
**So that** I load one targeted file instead of searching across all outputs.

**Acceptance**: Every knowledge file claim has a "See [file] Section [X]" reference.

---

### US-3: Developer knows what goes where
**As the** developer creating new content,
**I want** clear rules for what belongs in 0AGNOSTIC.md vs .0agnostic/knowledge/ vs stage outputs,
**So that** I don't accidentally put detailed content in static context or duplicate content across tiers.

**Acceptance**: Tier boundary rules are documented with examples and anti-patterns.

---

### US-4: New entity follows the pattern
**As the** developer creating a new entity,
**I want** a knowledge file template,
**So that** every entity's knowledge files have consistent structure.

**Acceptance**: Template exists, includes required sections (summary, references, version).
