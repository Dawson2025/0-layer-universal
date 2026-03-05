---
resource_id: "62636e60-68cb-4df1-af7f-3d3f6b0fa586"
resource_type: "document"
resource_name: "README_TESTING"
---
# Testing Guide

✅ **Status**: Comprehensive testing strategy implemented and verified (2025-10-23)

<!-- section_id: "263110a1-33d9-407f-a6d3-f1ac910fb808" -->
## Quick Start

<!-- section_id: "fc7209aa-b305-4fc4-a8ec-46c4ec7625e8" -->
### Daily Development ⭐ **Recommended**
```bash
# Run fast tests (~2 seconds)
./scripts/run-fast-tests.sh
```
**What it runs**: 22 unit tests + 7 emulator integration tests
**Speed**: 7.5x faster than target!

<!-- section_id: "ff58d173-6605-4d0b-a73c-ef63aa3182a2" -->
### Weekly / Pre-Deploy
```bash
# Test against real dev Firebase (~4 seconds)
./scripts/run-dev-tests.sh
```
**What it runs**: 7 real Firebase dev environment tests
**Verifies**: Actual lang-trak-dev Firebase project works correctly

<!-- section_id: "d093c159-47ba-452a-a927-322d37b5d3d4" -->
### Complete Test Suite
```bash
# Everything (~6 seconds)
./scripts/run-all-tests.sh
```
**What it runs**: Fast tests + Real Firebase dev tests
**Total**: 36 tests (22 unit + 7 emulator + 7 real Firebase)

<!-- section_id: "9e5b3fd0-147d-45d7-a1d0-1f015c2c569b" -->
## Test Structure

- `tests/unit/` - Fast unit tests (mocked)
- `tests/integration/emulator/` - Fast integration tests (Firebase Emulator)
- `tests/integration/real_firebase/` - Real Firebase environment tests

<!-- section_id: "021283dc-6377-47a7-a559-4f723ed14e8f" -->
## More Information

See `docs/0_context/layer_2_features/layer_2_feature_2.14_2_workflow_feature_2_testing/2.02_sub_layers/sub_layer_2.02_feature_knowledge/TESTING_WORKFLOW_GUIDE.md` for complete documentation.

<!-- section_id: "51f47d62-9b80-4a6e-bbfc-968e42171aac" -->
## Test Execution Times

| Test Type | Target | Actual | Performance | When to Run |
|-----------|--------|--------|-------------|-------------|
| Fast Tests (Unit + Emulator) | 15s | **~2s** | ✅ 7.5x faster | Every commit |
| Dev Environment Tests | 1m | **~4s** | ✅ 15x faster | Weekly |
| Complete Suite | 2m | **~6s** | ✅ 20x faster | Pre-deploy |

**All tests verified and passing!**
