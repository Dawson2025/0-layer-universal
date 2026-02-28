# Testing Guide

✅ **Status**: Comprehensive testing strategy implemented and verified (2025-10-23)

## Quick Start

### Daily Development ⭐ **Recommended**
```bash
# Run fast tests (~2 seconds)
./scripts/run-fast-tests.sh
```
**What it runs**: 22 unit tests + 7 emulator integration tests
**Speed**: 7.5x faster than target!

### Weekly / Pre-Deploy
```bash
# Test against real dev Firebase (~4 seconds)
./scripts/run-dev-tests.sh
```
**What it runs**: 7 real Firebase dev environment tests
**Verifies**: Actual lang-trak-dev Firebase project works correctly

### Complete Test Suite
```bash
# Everything (~6 seconds)
./scripts/run-all-tests.sh
```
**What it runs**: Fast tests + Real Firebase dev tests
**Total**: 36 tests (22 unit + 7 emulator + 7 real Firebase)

## Test Structure

- `tests/unit/` - Fast unit tests (mocked)
- `tests/integration/emulator/` - Fast integration tests (Firebase Emulator)
- `tests/integration/real_firebase/` - Real Firebase environment tests

## More Information

See `docs/0_context/layer_2_features/layer_2_feature_2.14_2_workflow_feature_2_testing/2.02_sub_layers/sub_layer_2.02_feature_knowledge/TESTING_WORKFLOW_GUIDE.md` for complete documentation.

## Test Execution Times

| Test Type | Target | Actual | Performance | When to Run |
|-----------|--------|--------|-------------|-------------|
| Fast Tests (Unit + Emulator) | 15s | **~2s** | ✅ 7.5x faster | Every commit |
| Dev Environment Tests | 1m | **~4s** | ✅ 15x faster | Weekly |
| Complete Suite | 2m | **~6s** | ✅ 20x faster | Pre-deploy |

**All tests verified and passing!**
