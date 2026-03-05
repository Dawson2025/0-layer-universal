---
resource_id: "7e63e24a-2aa6-4b35-836f-199061147349"
resource_type: "rule"
resource_name: "2_4_cache_rules_for_performance"
---
# 2.4: Cache Rules for Performance

<!-- section_id: "97eba2d2-4c92-4088-9188-f6f235a2cb6b" -->
## Requirement

Cache extracted and validated rules to avoid re-parsing on every initialization.

<!-- section_id: "053a237c-573c-4d24-9dd7-64d6fb01cccb" -->
## Acceptance Criteria

- [ ] Extracted rules are stored in cache (e.g., ~/.claude/.critical_rules_cache)
- [ ] Cache includes timestamp/hash of source files
- [ ] Cache is automatically invalidated when CLAUDE.md files change
- [ ] Caching provides measurable performance improvement
- [ ] Cache invalidation is automatic (no manual clearing needed)
- [ ] Stale cache is handled gracefully

<!-- section_id: "b53762a1-df35-45fb-bd3d-9f2de0b50209" -->
## Cache Storage

- **Location**: ~/.claude/.critical_rules_cache or similar
- **Format**: JSON with rule definitions and metadata
- **Contents**: Parsed rules, timestamps, file hashes

<!-- section_id: "424f0e0d-c2d0-45f5-8070-1b6bb5027fca" -->
## Owner Stage

- **Design**: Stage 0_05_design (cache architecture)
- **Development**: Stage 0_06_development (implement)
- **Testing**: Stage 0_07_testing (verify cache behavior)

<!-- section_id: "5870543a-43d5-4bf8-bce3-62568ab94cd2" -->
## Dependencies

- Requires: 2.3 (rules are validated)
- Enables: 2.5 (versioning works with cached rules)

<!-- section_id: "97443dbd-e6d0-45ca-8f43-9937164f3302" -->
## Navigation

- **Parent need**: `PARENT_NEED_P2.md`
- **Previous sibling**: `2_3_validate_rule_syntax.md`
- **Next sibling**: `2_5_support_rule_versioning.md`
