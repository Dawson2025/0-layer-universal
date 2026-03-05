---
resource_id: "0db828f8-1a2f-4dc8-a953-1e383ae7921a"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Branch: Production Reference

## Purpose

Summaries of how the production system works, pointing to original locations. These are NOT copies of production docs -- they are concise overviews with references to where the real content lives.

## Topics

| File | Topic | Summary |
|------|-------|---------|
| `gab_system.md` | GAB/AALang agent system | How GAB agents drive context loading, agent patterns, mode/actor structure |
| `context_system.md` | Production context system | How context actually works -- agnostic system, CLAUDE.md cascade, loading |
| `rules_overview.md` | Production rules system | What rules exist, where they live, how they are organized |

## Important

These files summarize and reference the production system. The actual production implementations live in `layer_0/` -- always refer to those for the authoritative versions.
