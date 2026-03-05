---
resource_id: "17c6b5a7-d2b8-4e7b-b026-3dc554ce7131"
resource_type: "rule"
resource_name: "lean_static_context"
---
# Rule: Lean Static Context

**Status**: MANDATORY
**Applies**: Every entity creation, every CLAUDE.md edit

---

<!-- section_id: "9ea884ad-b5ad-4bd7-8592-0b8f6ed4884d" -->
## Rule

Static context (CLAUDE.md, auto memory) is included in every API call. Keep it minimal. Push detail into dynamic context (.0agnostic/).

1. **Entity CLAUDE.md**: Target 30-80 lines, maximum 150 lines
2. **Container CLAUDE.md**: Target 15-30 lines, maximum 50 lines
3. **0AGNOSTIC.md**: Target 20-50 lines, maximum 100 lines
4. **Auto memory (MEMORY.md)**: Target 50-100 lines, truncated at 200

<!-- section_id: "31862ee5-4c77-4e9e-b9f4-97c88fb2484c" -->
## What Goes Where

| Content | Static (CLAUDE.md) | Dynamic (.0agnostic/) |
|---------|--------------------|-----------------------|
| Identity (3-5 lines) | Yes | No |
| Triggers (5-10 lines) | Yes | No |
| Pointers to resources | Yes (table of paths) | No |
| Detailed rules | No | Yes (rules/) |
| Knowledge documents | No | Yes (knowledge/) |
| Skill content | Listing only | Yes (skills/SKILL.md) |
| Agent constraints | No | Yes (.gab.jsonld) |
| Session history | No | Yes (episodic_memory/) |

<!-- section_id: "092dae71-981b-4b91-bf67-da079aef21e1" -->
## Why

Static context has **multiplicative cost**: tokens x number_of_API_calls. A 1,000-token CLAUDE.md costs 1,000 tokens on every call, regardless of relevance.

Dynamic context has **one-time cost**: tokens x 1 per read.

<!-- section_id: "9c731c37-c2fe-4e74-85f9-9d2f46bb86d0" -->
## Audit

```bash
wc -l CLAUDE.md        # should be <80 for entities, <30 for containers
wc -l 0AGNOSTIC.md     # should be <100
```

<!-- section_id: "da64f810-e122-470c-8d7a-cb43650dc69a" -->
## Related

- Principle: `knowledge/principles/lean_static_context.md`
- Knowledge: `knowledge/static_dynamic_context.md`
