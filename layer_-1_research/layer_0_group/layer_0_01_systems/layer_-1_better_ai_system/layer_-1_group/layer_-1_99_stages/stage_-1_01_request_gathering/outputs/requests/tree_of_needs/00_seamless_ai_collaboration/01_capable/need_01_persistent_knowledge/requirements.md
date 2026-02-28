# Need: Persistent Knowledge

**Branch**: [01_capable](../)
**Question**: "How does AI remember without context bloat?"

---

## Definition

AI should "know" the project without loading everything into context every time.
- Knowledge persists across sessions
- Context stays small while knowledge stays large
- AI inherits understanding from its location in the hierarchy

---

## Why This Matters

- AI context windows are limited (tokens)
- Loading everything = slow, expensive, unfocused
- Projects contain more knowledge than fits in context
- AI should inherit understanding from its location

---

## Requirements

### Hierarchical System Prompts
- MUST have system prompt files (CLAUDE.md, AGNOSTIC.md) at every level
- MUST load prompts automatically based on working directory
- MUST cascade/merge prompts from parent to child directories
- MUST keep each prompt focused and scoped (not everything everywhere)
- MUST support hierarchical inheritance (project → layer → stage → component)

### Referenced Resources
- MUST support referencing external resources from system prompts
- MUST have config folders (.claude/, .agnostic/) for extended resources
- MUST support just-in-time loading (load when needed, not upfront)
- MUST support resource types: skills, agents, rules, references
- SHOULD support AI app-specific resource types (hooks, commands, MCP)

### Progressive Disclosure
- MUST use summary in prompt → details in referenced file pattern
- MUST load details on demand, not preemptively
- SHOULD indicate what additional information is available

### Context Rules (from request_06)
- MUST have single authoritative context gathering doc
- MUST define what context to load when
- MUST specify loading order
- MUST define what belongs in agnostic vs specific
- SHOULD minimize token usage

### Memory Persistence (from request_04)
- MUST save key decisions from each session
- MUST save learned patterns and preferences
- MUST save project-specific conventions discovered
- MUST support different memory scopes (session, project, universal)
- SHOULD prioritize what to remember based on importance

### Memory Retrieval (from request_04)
- MUST enable querying past session memories
- MUST support semantic similarity search
- MUST return relevant context for current task
- SHOULD rank results by relevance and recency

---

## Acceptance Criteria

- [ ] Every layer/stage/component has a system prompt file
- [ ] System prompts cascade from parent to child
- [ ] Config folders exist with skills, agents, rules, references
- [ ] Resources loaded on demand, not all upfront
- [ ] AI inherits context from its location in hierarchy
- [ ] Context gathering rules are unified and documented
- [ ] Sessions can save at least 10 key learnings
- [ ] Memory retrieval returns relevant results

---

## Integrated From

- request_04: REQ-04-F00, REQ-04-F00c, REQ-04-F01, REQ-04-F02, REQ-04-F05
- request_06: REQ-06-F01, REQ-06-F02, REQ-06-F04
