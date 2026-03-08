---
resource_id: "61847c71-dea0-49df-a655-a4ff9b3a376a"
resource_type: "readme_output"
resource_name: "README"
---
# Branch: Knowledge LIFECYCLE is Managed

**Parent**: [00_context_survives_boundaries](../)

---

<!-- section_id: "01a66cac-7354-4d4f-9976-86d0ac694c0d" -->
## Core Question

> "How does knowledge move between tiers, and how do we know when it's stale?"

---

<!-- section_id: "e5df535d-5c0b-41e3-ae7e-3a1e62414813" -->
## Description

Organization without maintenance decays. Knowledge must flow from stage outputs (Tier 3) into distilled summaries (Tier 2) at the right moments, and staleness must be detected before agents rely on outdated knowledge.

The two failure modes:
1. **No consolidation** → knowledge files never created, agents always read raw outputs
2. **No staleness detection** → knowledge files created once, never updated, silently wrong

---

<!-- section_id: "458ad3fe-dfad-4f6e-ad2a-21891dbd045e" -->
## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_consolidation_process](./need_01_consolidation_process/) | "When and how are findings distilled?" | Protocol for creating knowledge files from stage outputs |
| [need_02_staleness_detection](./need_02_staleness_detection/) | "How do we know when knowledge is outdated?" | Detect drift between knowledge files and their sources |

---

<!-- section_id: "dc85f794-7a03-4de7-b47f-7e8281594cfc" -->
## Key Insight

Consolidation mirrors the brain's sleep replay mechanism — raw episodes (stage outputs) are compressed and transferred to long-term semantic storage (knowledge files) at natural boundaries (stage transitions). The trigger is the boundary, not a timer.
