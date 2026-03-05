---
resource_id: "3d4dd574-aad9-48de-b2d8-86eddce425ca"
resource_type: "document"
resource_name: "TESTING_WORKFLOW_GUIDE"
---
# Testing Workflow Guide
*Complete Guide to the Comprehensive Firebase Testing Strategy*

<!-- section_id: "068763e1-a3a1-41de-a84a-e868a75b903b" -->
## 🎯 Quick Reference

<!-- section_id: "47a7005e-b55e-49a8-af2f-88c912740d6f" -->
### Development (Every Commit)
```bash
# Fast tests - run before every commit
./scripts/run-fast-tests.sh

# Or manually:
pytest tests/unit tests/integration/emulator -v
```
**Time**: ~15 seconds
**Cost**: $0

<!-- section_id: "4de9d519-8dbe-4c09-ab2d-6c42ff466cfd" -->
### Dev Environment Verification (Weekly / Before Deploy)
```bash
# Test against real lang-trak-dev Firebase
./scripts/run-dev-tests.sh
```
**Time**: ~1 minute
**Cost**: ~$0.50/month

<!-- section_id: "12761e85-3344-4904-991e-f03be5b0832c" -->
### Complete Test Suite
```bash
# Everything (fast + dev environment)
./scripts/run-all-tests.sh
```
**Time**: ~2 minutes
**Cost**: ~$3/month

---

<!-- section_id: "f58ec6d9-78bf-4c44-aa66-8db1e90d6478" -->
## 📊 Test Organization

```
tests/
├── unit/                              # Fast, mocked tests
│   └── (your unit tests here)
│
├── integration/
│   ├── emulator/                      # 70% of integration tests ⭐ PRIMARY
│   │   ├── conftest.py                # Auto-starts Firebase Emulator
│   │   ├── test_phoneme_lifecycle.py  # Phoneme CRUD tests
│   │   ├── test_word_lifecycle.py     # Word CRUD tests
│   │   └── test_group_lifecycle.py    # Group CRUD tests
│   │
│   └── real_firebase/                 # 30% - Environment verification
│       ├── conftest.py                # Environment configuration
│       ├── test_dev_environment.py    # Tests for lang-trak-dev
│       ├── test_staging_environment.py # Tests for staging
│       ├── test_prod_smoke.py         # Smoke tests for production
│       └── test_cloud_integration.py  # Original integration tests
```

---

<!-- section_id: "1a78391c-164e-4e7f-8d70-394582a964d3" -->
## 🚀 How to Run Tests

<!-- section_id: "ecff969a-c59c-4d61-b2b2-bc0bc40b1c93" -->
### 1. Fast Tests (Development Loop) ⭐ **Use This Daily**

```bash
# Run fast tests
./scripts/run-fast-tests.sh
```

**What it does**:
1. Runs all unit tests
2. Starts Firebase Emulator
3. Runs integration tests against emulator
4. Stops emulator

**When to use**: Before every commit, during development

<!-- section_id: "e6150b5c-61b0-4256-abc8-f8ee038a53fb" -->
### 2. Dev Environment Tests (Weekly)

```bash
# Confirm you want to test against real Firebase
./scripts/run-dev-tests.sh
```

**What it does**:
1. Connects to **real** lang-trak-dev Firebase project
2. Creates test data
3. Verifies CRUD operations work
4. Cleans up test data

**When to use**: Weekly, before deployments, after Firebase changes

<!-- section_id: "7c63b121-272f-4989-9268-e14d3cf6df32" -->
### 3. Manual Test Runs

#### Run emulator tests only
```bash
# Start emulator manually and run tests
firebase emulators:start --only firestore,auth,storage --project demo-test &
pytest tests/integration/emulator -v -m emulator
```

#### Run specific test file
```bash
# Specific emulator test
pytest tests/integration/emulator/test_phoneme_lifecycle.py -v

# Specific dev environment test
FIREBASE_TEST_ENV=development RUN_FIREBASE_INTEGRATION_TESTS=1 \
  pytest tests/integration/real_firebase/test_dev_environment.py -v
```

#### Run tests by marker
```bash
# All emulator tests
pytest -m emulator -v

# All dev environment tests
pytest -m "real_firebase and dev" -v

# All smoke tests
pytest -m smoke -v
```

---

<!-- section_id: "262579ab-f980-40d1-a799-5daef43b644c" -->
## 🔧 Configuration

<!-- section_id: "15293b82-7195-422c-ad4b-720b215539df" -->
### Firebase Emulator
**Config file**: `firebase.json`
```json
{
  "emulators": {
    "firestore": { "port": 8080 },
    "auth": { "port": 9099 },
    "storage": { "port": 9199 },
    "ui": { "enabled": true, "port": 4000 }
  }
}
```

**Access Emulator UI**: http://localhost:4000 (when emulator running)

<!-- section_id: "ad74ad5c-0218-4622-a1dd-aee345ff7bc5" -->
### Environment Selection
```bash
# Test against dev (default)
export FIREBASE_TEST_ENV=development

# Test against staging
export FIREBASE_TEST_ENV=staging

# Test against production (DANGEROUS!)
export FIREBASE_TEST_ENV=production
export ALLOW_PROD_TESTS=yes_i_know_what_im_doing
```

---

<!-- section_id: "18b2cc92-f8bd-4b7f-b4a2-86442c3b65d0" -->
## 🎯 CI/CD Integration

<!-- section_id: "b251e24a-5445-476e-8a86-48dc1162346c" -->
### Pull Request Checks (Required for Merge)
```
✅ Unit tests
✅ Emulator integration tests
Total time: ~15 seconds
```

<!-- section_id: "188d2a31-6e17-4836-8495-bc356bdb3204" -->
### Main Branch Merge
```
✅ Fast tests (unit + emulator)
✅ Dev environment verification
Total time: ~2 minutes
```

<!-- section_id: "b8f0b25e-e31b-44c2-9547-c878764655c7" -->
### Nightly Build
```
✅ All fast tests
✅ Dev environment tests
✅ Staging environment tests
Total time: ~5 minutes
```

<!-- section_id: "3c2c7583-bf65-4c74-9ea1-8c8eb5eed344" -->
### Production Deploy
```
✅ All tests pass on main
✅ Tag release (v1.2.3)
✅ Production smoke tests (read-only)
✅ Deploy to production
```

---

<!-- section_id: "ea32f017-32a8-4085-abf5-c1bfb826e577" -->
## 📝 Writing New Tests

<!-- section_id: "4165c2fa-d4d1-431e-98e4-a987fc91196d" -->
### For Fast Development (Emulator)

**Create test in**: `tests/integration/emulator/`

```python
import pytest
from services.firebase import firestore_db

@pytest.mark.emulator
class TestMyFeature:
    """Test my feature with Firebase Emulator"""

    def test_something(self):
        # Create test data (emulator auto-cleans)
        project_id = firestore_db.create_project({
            'name': 'Test Project',
            'user_id': 'test-user'
        })

        # Verify it works
        project = firestore_db.get_project(project_id)
        assert project is not None
```

**Advantages**:
- Runs in ~1 second
- No cleanup needed
- Works offline
- Perfect for TDD

<!-- section_id: "1d8ba9c2-0c2d-4fb7-83e7-427eaba211a4" -->
### For Environment Verification (Real Firebase)

**Create test in**: `tests/integration/real_firebase/test_dev_environment.py`

```python
import pytest
from services.firebase import firestore_db

@pytest.mark.real_firebase
@pytest.mark.dev
class TestDevEnvironment:
    """Test against real lang-trak-dev"""

    def test_something(self, cleanup_test_data):
        # Create test data
        project_id = firestore_db.create_project({
            'name': 'Dev Test',
            'user_id': 'dev-user'
        })

        # Track for cleanup
        cleanup_test_data.add_project(project_id)

        # Verify it works
        project = firestore_db.get_project(project_id)
        assert project is not None
```

**When to write**:
- Testing Firebase-specific features (security rules, triggers)
- Verifying indexes work
- Testing Cloud Functions
- Integration with other services

---

<!-- section_id: "40d11914-1d4e-4ea6-a9f2-328b5a1ae076" -->
## 🐛 Troubleshooting

<!-- section_id: "9ffdc330-d945-4db0-9197-eaf8ab9067ec" -->
### Emulator won't start
```bash
# Check if ports are in use
lsof -i :8080  # Firestore
lsof -i :9099  # Auth
lsof -i :9199  # Storage

# Kill processes if needed
kill -9 <PID>

# Or use different ports in firebase.json
```

<!-- section_id: "e6040265-00a5-4ee0-a423-efec6f28f05d" -->
### Tests fail with "Firebase not available"
```bash
# For emulator tests - ensure FIRESTORE_EMULATOR_HOST is set
export FIRESTORE_EMULATOR_HOST=127.0.0.1:8080

# For real Firebase tests - ensure credentials exist
ls firebase-admin-config.json

# And environment variable is set
export RUN_FIREBASE_INTEGRATION_TESTS=1
```

<!-- section_id: "9d62a027-984a-4f88-a1fe-8b38314f8f5d" -->
### Emulator data persists between runs
```bash
# Clear emulator data
firebase emulators:start --import=./empty --export-on-exit=./empty
```

<!-- section_id: "03ba0c93-2be7-4c74-a97a-a31869ceed2e" -->
### Tests are slow
```bash
# Make sure you're running emulator tests, not real Firebase
pytest tests/integration/emulator -v  # Fast (emulator)
# NOT:
pytest tests/integration/real_firebase -v  # Slow (real Firebase)
```

---

<!-- section_id: "09dbbe97-b19b-4dd6-bdf4-a98819ca34cb" -->
## 📊 Performance Benchmarks

| Test Type | Count | Duration | When to Run |
|-----------|-------|----------|-------------|
| Unit Tests | 1000+ | 5s | Every commit |
| Emulator Integration | 200+ | 10s | Every commit |
| **Total Fast Tests** | **1200+** | **15s** | **Every commit** |
| Dev Environment | 30 | 1m | Weekly, pre-deploy |
| Staging Environment | 30 | 1m | Main branch |
| Prod Smoke | 10 | 30s | Pre-production deploy |

---

<!-- section_id: "bf480a72-dd8d-4563-94dd-ae60cca304dd" -->
## ✅ Best Practices

<!-- section_id: "940fc9fa-b71c-4dd3-9b2d-f659c17b8e92" -->
### DO
✅ Use emulator for daily development
✅ Run fast tests before every commit
✅ Use cleanup_test_data fixture for real Firebase tests
✅ Mark tests with appropriate markers (@pytest.mark.emulator, etc.)
✅ Keep production smoke tests read-only
✅ Run dev environment tests weekly

<!-- section_id: "cabdd296-7959-4cc4-8ac8-b321f1aa3cd8" -->
### DON'T
❌ Run real Firebase tests on every commit (too slow/expensive)
❌ Write to production in tests (EVER!)
❌ Forget to clean up test data
❌ Skip fast tests to save time
❌ Rely only on emulator (need real environment verification)

---

<!-- section_id: "d8a18596-0dbc-4f1f-b5ec-933059758181" -->
## 🎯 Summary

**The Strategy**:
1. **Daily**: Use emulator tests (fast, free, offline)
2. **Weekly**: Run dev environment tests (verify real Firebase)
3. **Pre-deploy**: Run complete suite (everything)
4. **Production**: Only smoke tests (read-only, minimal)

**The Result**:
- 🚀 Fast development (15 second test runs)
- ✅ Production confidence (real environment verification)
- 💰 Low cost (~$3/month vs $50+)
- 🎯 Complete coverage (both emulator and real Firebase)

---

**Questions? Check**: `docs/0_context/trickle_down_2_features/0_instruction_docs/ComprehensiveFirebaseTestingStrategy.md`
