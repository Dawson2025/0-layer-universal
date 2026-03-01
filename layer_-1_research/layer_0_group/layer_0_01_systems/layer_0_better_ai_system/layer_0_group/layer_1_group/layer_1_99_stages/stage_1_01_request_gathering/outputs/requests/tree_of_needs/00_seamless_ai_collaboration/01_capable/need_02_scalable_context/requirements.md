# Need: Scalable Context

**Branch**: [01_capable](../)
**Question**: "Does it still work when the project grows 10x?"

---

## Definition

System works for small and large projects without context explosion.
- Delegation distributes cognitive load across agents
- Progressive disclosure loads details on demand
- Referenced resources keep prompts small

---

## Why This Matters

- Projects grow over time
- More code, more docs, more history
- Context windows don't grow with projects
- System must scale without degradation

---

## Requirements

### Agent Delegation (from request_03)
- MUST support manager-worker agent hierarchy
- MUST define Manager agent responsibilities
- MUST define Worker agent responsibilities
- MUST define Specialist agent types (research, code, review, etc.)
- MUST allow managers to delegate to specialized workers
- MUST enable workers to have focused, scoped context
- MUST transfer minimal state in handoffs (not full context)

### Delegation Decision Matrix (from request_03)
- MUST provide criteria for when to delegate vs execute directly
- MUST specify maximum hierarchy depth
- MUST define task complexity thresholds for delegation
- SHOULD include cost/benefit considerations (token usage)

### Agent Persona Library (from request_03)
- MUST provide persona templates for common agent types
- MUST include context loading instructions per persona
- SHOULD support custom persona creation

### Distributed Cognitive Load
- MUST NOT require one agent to hold everything
- MUST allow multiple agents with different specialties
- MUST support parallel work by independent agents
- SHOULD enable agents to spawn sub-agents as needed

### Context Budgeting
- MUST keep base system prompts small
- MUST load details progressively as needed
- MUST summarize large contexts intelligently (from request_04)
- MUST preserve critical information during compression
- SHOULD indicate when context is getting large

---

## Acceptance Criteria

- [ ] Manager agents can delegate to worker agents
- [ ] Agent roles are documented with examples
- [ ] Delegation matrix covers common scenarios
- [ ] At least 5 persona templates exist
- [ ] Each agent loads only context relevant to its task
- [ ] Handoffs transfer minimal state, not full context
- [ ] System works with 10x more content without breaking
- [ ] Base prompts stay small regardless of project size

---

## Integrated From

- request_03: REQ-03-F01, REQ-03-F02, REQ-03-F03
- request_04: REQ-04-F03 (context compression)
