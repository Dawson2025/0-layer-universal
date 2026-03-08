---
resource_id: "ceadad1c-f5ba-493a-a327-7aee3e09e89f"
resource_type: "readme_output"
resource_name: "README"
---
# Need: Customizable Importance Weighting

**Branch**: [04_data_based_avenue_comparison](../)
**Question**: "How do different projects weight what matters to them?"
**Version**: 1.0.0

---

<!-- section_id: "05251798-e857-4081-90aa-80ab60337b37" -->
## Definition

A two-layer importance system:
- **General importance**: Base importance scores for each operation across 8 dimensions (frequency, criticality, cost impact, risk score, user impact, SLA requirement, competitive advantage, technical debt)
- **Project-specific importance**: Projects can override base importance for their specific priorities

Combined with operation benchmarks, this produces project-specific weighted scores and final avenue recommendations via a decision matrix.

---

<!-- section_id: "e886c0b5-74a8-43e0-a389-6ea783dcbba7" -->
## Why This Matters

- A HighThroughputAPI values speed and scalability; a FinancialLedger values transactions and consistency
- Same benchmark data, different recommendations per project
- Without importance weighting, all operations are treated as equally important (they aren't)
- Importance itself must be measurable (not arbitrary) -- each dimension has units and methodology
- The decision matrix gives a single "best avenue for project X" answer

---

<!-- section_id: "975a0cf8-54bd-4105-81b2-aaeb3709231e" -->
## Acceptance Criteria

- [ ] 8 importance dimensions are defined with units and methodology
- [ ] General (base) importance scores exist for all operations
- [ ] Projects can define their own importance overrides
- [ ] Weighted scores combine performance x importance correctly
- [ ] Decision matrix produces per-project avenue recommendations
- [ ] Hybrid avenue combinations are evaluated (e.g., Vector + KG together)

---

<!-- section_id: "1cfe41be-7250-4941-a1ed-ca84b9fb39fa" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

<!-- section_id: "0e6aa51a-82f5-4232-a072-1be7feda3c5a" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "4ce1792c-43e7-46b1-be8b-77095863fc71" -->
## Research References

- `proposals/04_design/v5_comprehensive_operations_with_customizable_importance.md` -- importance framework
- `proposals/04_design/v6_consolidated_schema_with_improvements.md` -- decision matrix views
