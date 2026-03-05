---
resource_id: "7e63e24a-2aa6-4b35-836f-199061147349"
resource_type: "rule"
resource_name: "2_4_cache_rules_for_performance"
---
# 2.4: Cache Rules for Performance

## Requirement

Cache extracted and validated rules to avoid re-parsing on every initialization.

## Acceptance Criteria

- [ ] Extracted rules are stored in cache (e.g., ~/.claude/.critical_rules_cache)
- [ ] Cache includes timestamp/hash of source files
- [ ] Cache is automatically invalidated when CLAUDE.md files change
- [ ] Caching provides measurable performance improvement
- [ ] Cache invalidation is automatic (no manual clearing needed)
- [ ] Stale cache is handled gracefully

## Cache Storage

- **Location**: ~/.claude/.critical_rules_cache or similar
- **Format**: JSON with rule definitions and metadata
- **Contents**: Parsed rules, timestamps, file hashes

## Owner Stage

- **Design**: Stage 0_05_design (cache architecture)
- **Development**: Stage 0_06_development (implement)
- **Testing**: Stage 0_07_testing (verify cache behavior)

## Dependencies

- Requires: 2.3 (rules are validated)
- Enables: 2.5 (versioning works with cached rules)

## Navigation

- **Parent need**: `PARENT_NEED_P2.md`
- **Previous sibling**: `2_3_validate_rule_syntax.md`
- **Next sibling**: `2_5_support_rule_versioning.md`
