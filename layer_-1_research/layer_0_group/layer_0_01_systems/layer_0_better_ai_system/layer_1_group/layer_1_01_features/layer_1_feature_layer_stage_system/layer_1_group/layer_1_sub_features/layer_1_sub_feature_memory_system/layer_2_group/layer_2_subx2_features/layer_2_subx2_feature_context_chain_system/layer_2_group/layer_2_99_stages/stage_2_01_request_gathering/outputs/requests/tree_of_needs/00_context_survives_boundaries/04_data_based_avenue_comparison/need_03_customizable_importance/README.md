---
resource_id: "ceadad1c-f5ba-493a-a327-7aee3e09e89f"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Customizable Importance Weighting

**Branch**: [04_data_based_avenue_comparison](../)
**Question**: "How do different projects weight what matters to them?"
**Version**: 1.0.0

---

## Definition

A two-layer importance system:
- **General importance**: Base importance scores for each operation across 8 dimensions (frequency, criticality, cost impact, risk score, user impact, SLA requirement, competitive advantage, technical debt)
- **Project-specific importance**: Projects can override base importance for their specific priorities

Combined with operation benchmarks, this produces project-specific weighted scores and final avenue recommendations via a decision matrix.

---

## Why This Matters

- A HighThroughputAPI values speed and scalability; a FinancialLedger values transactions and consistency
- Same benchmark data, different recommendations per project
- Without importance weighting, all operations are treated as equally important (they aren't)
- Importance itself must be measurable (not arbitrary) -- each dimension has units and methodology
- The decision matrix gives a single "best avenue for project X" answer

---

## Acceptance Criteria

- [ ] 8 importance dimensions are defined with units and methodology
- [ ] General (base) importance scores exist for all operations
- [ ] Projects can define their own importance overrides
- [ ] Weighted scores combine performance x importance correctly
- [ ] Decision matrix produces per-project avenue recommendations
- [ ] Hybrid avenue combinations are evaluated (e.g., Vector + KG together)

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Research References

- `proposals/04_design/v5_comprehensive_operations_with_customizable_importance.md` -- importance framework
- `proposals/04_design/v6_consolidated_schema_with_improvements.md` -- decision matrix views
