---
resource_id: "9cce22cc-d164-4629-8079-ba705ba7060e"
resource_type: "document"
resource_name: "TESTING_WORKFLOW_GUIDE"
---
# Testing Workflow Guide
*Complete Guide to the Comprehensive Firebase Testing Strategy*

## 🎯 Quick Reference

### Development (Every Commit)
```bash
# Fast tests - run before every commit
./scripts/run-fast-tests.sh

# Or manually:
pytest tests/unit tests/integration/emulator -v
```
**Time**: ~15 seconds
**Cost**: $0

### Dev Environment Verification (Weekly / Before Deploy)
```bash
# Test against real lang-trak-dev Firebase
./scripts/run-dev-tests.sh
```
**Time**: ~1 minute
**Cost**: ~$0.50/month

### Complete Test Suite
```bash
# Everything (fast + dev environment)
./scripts/run-all-tests.sh
```
**Time**: ~2 minutes
**Cost**: ~$3/month

---

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

## 🚀 How to Run Tests

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

## 🔧 Configuration

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

## 🎯 CI/CD Integration

### Pull Request Checks (Required for Merge)
```
✅ Unit tests
✅ Emulator integration tests
Total time: ~15 seconds
```

### Main Branch Merge
```
✅ Fast tests (unit + emulator)
✅ Dev environment verification
Total time: ~2 minutes
```

### Nightly Build
```
✅ All fast tests
✅ Dev environment tests
✅ Staging environment tests
Total time: ~5 minutes
```

### Production Deploy
```
✅ All tests pass on main
✅ Tag release (v1.2.3)
✅ Production smoke tests (read-only)
✅ Deploy to production
```

---

## 📝 Writing New Tests

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

## 🐛 Troubleshooting

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

### Tests fail with "Firebase not available"
```bash
# For emulator tests - ensure FIRESTORE_EMULATOR_HOST is set
export FIRESTORE_EMULATOR_HOST=127.0.0.1:8080

# For real Firebase tests - ensure credentials exist
ls firebase-admin-config.json

# And environment variable is set
export RUN_FIREBASE_INTEGRATION_TESTS=1
```

### Emulator data persists between runs
```bash
# Clear emulator data
firebase emulators:start --import=./empty --export-on-exit=./empty
```

### Tests are slow
```bash
# Make sure you're running emulator tests, not real Firebase
pytest tests/integration/emulator -v  # Fast (emulator)
# NOT:
pytest tests/integration/real_firebase -v  # Slow (real Firebase)
```

---

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

## ✅ Best Practices

### DO
✅ Use emulator for daily development
✅ Run fast tests before every commit
✅ Use cleanup_test_data fixture for real Firebase tests
✅ Mark tests with appropriate markers (@pytest.mark.emulator, etc.)
✅ Keep production smoke tests read-only
✅ Run dev environment tests weekly

### DON'T
❌ Run real Firebase tests on every commit (too slow/expensive)
❌ Write to production in tests (EVER!)
❌ Forget to clean up test data
❌ Skip fast tests to save time
❌ Rely only on emulator (need real environment verification)

---

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
