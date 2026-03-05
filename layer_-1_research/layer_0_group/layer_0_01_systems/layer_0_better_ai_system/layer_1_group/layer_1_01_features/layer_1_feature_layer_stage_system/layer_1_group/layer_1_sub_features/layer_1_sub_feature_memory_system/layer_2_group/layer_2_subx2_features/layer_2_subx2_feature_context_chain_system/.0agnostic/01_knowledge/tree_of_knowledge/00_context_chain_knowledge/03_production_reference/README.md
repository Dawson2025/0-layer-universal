---
resource_id: "0db828f8-1a2f-4dc8-a953-1e383ae7921a"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Branch: Production Reference

<!-- section_id: "02b879bf-3170-4d34-8e5a-2b3ff18e8b55" -->
## Purpose

Summaries of how the production system works, pointing to original locations. These are NOT copies of production docs -- they are concise overviews with references to where the real content lives.

<!-- section_id: "56639939-997e-411d-a21d-7df949780667" -->
## Topics

| File | Topic | Summary |
|------|-------|---------|
| `gab_system.md` | GAB/AALang agent system | How GAB agents drive context loading, agent patterns, mode/actor structure |
| `context_system.md` | Production context system | How context actually works -- agnostic system, CLAUDE.md cascade, loading |
| `rules_overview.md` | Production rules system | What rules exist, where they live, how they are organized |

<!-- section_id: "f53d1eed-1af1-4dda-bd9d-c99f0139e643" -->
## Important

These files summarize and reference the production system. The actual production implementations live in `layer_0/` -- always refer to those for the authoritative versions.
