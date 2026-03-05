---
resource_id: "61847c71-dea0-49df-a655-a4ff9b3a376a"
resource_type: "readme
output"
resource_name: "README"
---
# Branch: Knowledge LIFECYCLE is Managed

**Parent**: [00_context_survives_boundaries](../)

---

## Core Question

> "How does knowledge move between tiers, and how do we know when it's stale?"

---

## Description

Organization without maintenance decays. Knowledge must flow from stage outputs (Tier 3) into distilled summaries (Tier 2) at the right moments, and staleness must be detected before agents rely on outdated knowledge.

The two failure modes:
1. **No consolidation** → knowledge files never created, agents always read raw outputs
2. **No staleness detection** → knowledge files created once, never updated, silently wrong

---

## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_consolidation_process](./need_01_consolidation_process/) | "When and how are findings distilled?" | Protocol for creating knowledge files from stage outputs |
| [need_02_staleness_detection](./need_02_staleness_detection/) | "How do we know when knowledge is outdated?" | Detect drift between knowledge files and their sources |

---

## Key Insight

Consolidation mirrors the brain's sleep replay mechanism — raw episodes (stage outputs) are compressed and transferred to long-term semantic storage (knowledge files) at natural boundaries (stage transitions). The trigger is the boundary, not a timer.
