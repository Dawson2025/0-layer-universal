---
resource_id: "d5caab9e-2b42-4414-beaf-661979a2c732"
resource_type: "output"
resource_name: "US-01_developer_compares_avenues"
---
# US-01: Developer compares avenues on a capability

**Need**: [Avenue Benchmarking](../README.md)

---

**As a** developer choosing between data-based avenues,
**I want** to see ranked benchmark data with real units for each capability,
**So that** I can make an evidence-based technology decision instead of relying on intuition.

### What Happens

1. Developer queries the database for a specific capability (e.g., speed)
2. System returns all avenue types ranked by normalized score
3. Raw values with units are shown alongside normalized scores (e.g., "50ms, score: 95")
4. Developer can compare across capability categories to see full picture

### Acceptance Criteria

- Query returns ranked results with raw value, unit, and normalized score
- Rankings are consistent with the normalization formula
