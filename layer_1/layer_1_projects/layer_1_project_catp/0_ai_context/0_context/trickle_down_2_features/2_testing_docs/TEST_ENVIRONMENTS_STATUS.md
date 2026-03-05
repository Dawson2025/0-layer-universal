---
resource_id: "6568171e-a21e-47d6-9cb0-7db19afee3ee"
resource_type: "document"
resource_name: "TEST_ENVIRONMENTS_STATUS"
---
# Test Environments Status
**Date**: 2025-10-23
**Status**: Development environment fully operational, Staging/Production awaiting credentials

---

<!-- section_id: "0531247e-41bd-4b62-b5c2-71939ac5af59" -->
## Environment Overview

Your application has **4 test environments**:

| Environment | Purpose | Firebase Project | Credentials | Tests | Status |
|-------------|---------|------------------|-------------|-------|--------|
| **Unit Tests** | Fast, mocked | N/A (no Firebase) | N/A | 22 tests | ✅ **READY** |
| **Emulator** | Fast, local Firebase | `demo-test` (local) | N/A | 7 tests | ✅ **READY** |
| **Development** | Real dev Firebase | `lang-trak-dev` | ✅ Available | 7 tests | ✅ **READY** |
| **Staging** | Pre-production testing | `lang-trak-staging` | ❌ Missing | 3 tests | 🔄 **NEEDS CREDENTIALS** |
| **Production** | Production smoke tests | `lang-trak-prod` | ❌ Missing | 3 tests (read-only) | 🔄 **NEEDS CREDENTIALS** |

---

<!-- section_id: "d26cc5a9-db1d-43b0-b902-a86aaba31f8c" -->
## Development Environment ✅ FULLY OPERATIONAL

**Firebase Project**: `lang-trak-dev`
**Credentials**: `keys/lang-trak-dev-agent-key.json` ✅
**Tests**: 7 comprehensive CRUD tests

<!-- section_id: "9d4c396f-e6c6-4066-8684-1c1e89cc7225" -->
### What's Tested:
- ✅ Firestore connection
- ✅ All collections accessible (projects, words, phonemes, groups)
- ✅ Project CRUD operations
- ✅ Word CRUD operations
- ✅ Phoneme CRUD operations
- ✅ Group CRUD operations
- ✅ Composite indexes work

<!-- section_id: "25c6fad0-e510-4af8-8996-ac6e644e1de5" -->
### Run Tests:
```bash
# Via script (recommended)
./scripts/run-dev-tests.sh

# Or manually
FIREBASE_TEST_ENV=development \
RUN_FIREBASE_INTEGRATION_TESTS=1 \
pytest tests/integration/real_firebase/test_dev_environment.py -v
```

**Execution Time**: ~4 seconds
**Last Run**: 2025-10-23 ✅ All passing

---

<!-- section_id: "14add3b5-dda7-4ebc-84ce-f52167cb4571" -->
## Staging Environment 🔄 AWAITING CREDENTIALS

**Firebase Project**: `lang-trak-staging` (referenced in `.firebaserc`)
**Credentials**: `keys/lang-trak-staging-agent-key.json` ❌ **MISSING**
**Tests**: 3 verification tests (created but can't run without credentials)

<!-- section_id: "dc6da309-d108-4898-b5d0-59405ac0b99a" -->
### What Would Be Tested:
- 🔄 Firestore connection
- 🔄 All collections accessible
- 🔄 Basic CRUD operations

<!-- section_id: "e16b5f42-48c1-4add-89e9-f597d529a2aa" -->
### Test File Location:
`tests/integration/real_firebase/test_staging_environment.py`

<!-- section_id: "40fc3174-31d8-40a4-ab2d-9f88ccee7c6e" -->
### How to Enable:

#### Option 1: Create New Staging Project
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create new project named `lang-trak-staging`
3. Enable Firestore, Authentication, Storage
4. Create service account:
   - Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Save as `keys/lang-trak-staging-agent-key.json`

#### Option 2: Use Existing Staging Project
If `lang-trak-staging` already exists:
1. Go to Firebase Console → Project Settings → Service Accounts
2. Generate new private key
3. Save as `keys/lang-trak-staging-agent-key.json`

#### Then Run Tests:
```bash
FIREBASE_TEST_ENV=staging \
RUN_FIREBASE_INTEGRATION_TESTS=1 \
pytest tests/integration/real_firebase/test_staging_environment.py -v
```

---

<!-- section_id: "2378a6cb-520d-4b24-ae32-7ff34d820194" -->
## Production Environment 🔄 AWAITING CREDENTIALS

**Firebase Project**: `lang-trak-prod` (referenced in `.firebaserc`)
**Credentials**: `keys/lang-trak-prod-agent-key.json` ❌ **MISSING**
**Tests**: 3 smoke tests (READ-ONLY for safety)

<!-- section_id: "8aec41f4-f18e-4246-b268-9178a00ff9e9" -->
### What Would Be Tested (READ-ONLY):
- 🔄 Firestore accessible
- 🔄 Collections readable
- 🔄 Project queries work

**IMPORTANT**: Production tests are **READ-ONLY** by design:
- ❌ NO writes
- ❌ NO deletes
- ❌ NO modifications
- ✅ Only verification that production is accessible and responsive

<!-- section_id: "e06e051a-699a-4a56-8e87-2b79d034830d" -->
### Test File Location:
`tests/integration/real_firebase/test_prod_smoke.py`

<!-- section_id: "35572f7c-a52f-4e55-8f95-a34e6213b97d" -->
### How to Enable:

#### Option 1: Create New Production Project
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create new project named `lang-trak-prod`
3. Enable Firestore, Authentication, Storage
4. Configure production settings (security rules, indexes, etc.)
5. Create service account:
   - Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Save as `keys/lang-trak-prod-agent-key.json`

#### Option 2: Use Existing Production Project
If `lang-trak-prod` already exists:
1. Go to Firebase Console → Project Settings → Service Accounts
2. Generate new private key (read-only if possible)
3. Save as `keys/lang-trak-prod-agent-key.json`

#### Then Run Tests (with safety confirmation):
```bash
FIREBASE_TEST_ENV=production \
ALLOW_PROD_TESTS=yes_i_know_what_im_doing \
RUN_FIREBASE_INTEGRATION_TESTS=1 \
pytest tests/integration/real_firebase/test_prod_smoke.py -v
```

**Note**: The `ALLOW_PROD_TESTS` flag is required to prevent accidental production test runs.

---

<!-- section_id: "d0c5a62d-3b95-400a-843d-f21854554181" -->
## "Testing Environment" Clarification

You mentioned "testing environment" - this typically refers to one of:

1. **Local Testing** (Emulator) - ✅ Already working
   - Runs completely offline
   - No real Firebase project needed
   - Perfect for rapid development

2. **Development Environment** (`lang-trak-dev`) - ✅ Already working
   - Real Firebase project for testing features
   - Can write/delete/modify data freely
   - This is your primary "testing" environment

3. **Staging Environment** (`lang-trak-staging`) - 🔄 Needs credentials
   - Pre-production environment
   - Tests deployment process
   - Mirrors production configuration

If you meant a different "testing" environment, please clarify and I can add it to the configuration.

---

<!-- section_id: "235fb924-5fe7-46f5-bb85-9614abf411bf" -->
## Current Capabilities

<!-- section_id: "a7cd7a6b-bc2a-498c-b16b-ffbbbd4156ef" -->
### What Works NOW (No Setup Required):
```bash
# Fast tests - 36 tests in ~6 seconds
./scripts/run-fast-tests.sh

# Dev environment tests - 7 tests in ~4 seconds
./scripts/run-dev-tests.sh

# Complete suite (fast + dev) - 43 tests in ~10 seconds
./scripts/run-all-tests.sh
```

<!-- section_id: "925c6f65-f6d6-4071-ae98-72aebda64257" -->
### What Needs Credentials:
- Staging environment tests → Need `keys/lang-trak-staging-agent-key.json`
- Production smoke tests → Need `keys/lang-trak-prod-agent-key.json`

---

<!-- section_id: "d38da58c-24d6-4108-b864-4639283542be" -->
## Recommended Next Steps

<!-- section_id: "c602b7a7-2ea8-4f2f-9a21-2753702e2d9b" -->
### Priority 1: Start Using What Works
```bash
# Use this for daily development
./scripts/run-fast-tests.sh
```

<!-- section_id: "e6aa5b3e-a9bc-4104-879a-b1295c3a9090" -->
### Priority 2: Set Up Staging (Optional, when ready for pre-production)
1. Create/access `lang-trak-staging` Firebase project
2. Generate service account key
3. Save to `keys/lang-trak-staging-agent-key.json`
4. Run staging tests to verify

<!-- section_id: "7d530f3d-c4f4-4227-babd-90876b8a7298" -->
### Priority 3: Set Up Production (Before first deploy)
1. Create/access `lang-trak-prod` Firebase project
2. Generate service account key (read-only if possible)
3. Save to `keys/lang-trak-prod-agent-key.json`
4. Run smoke tests to verify production is healthy

---

<!-- section_id: "50c78ded-bfd6-4dc3-82c8-06f64055c98b" -->
## Security Notes

<!-- section_id: "2fbaf8b9-277a-4fff-89cb-2312655e8f18" -->
### Credential Files (.gitignore)
All credential files should be in `.gitignore`:
```
keys/*.json
firebase-admin-config.json  # May contain sensitive paths
```

<!-- section_id: "a32ba71d-1ff3-4aa4-a4ef-820566a45e5e" -->
### Service Account Permissions
- **Dev**: Full Firestore access (read/write/delete)
- **Staging**: Full Firestore access (read/write/delete)
- **Production**: Read-only recommended (for safety)

<!-- section_id: "bc61365b-6a1c-427d-90a3-e188302558fb" -->
### Credential Storage in CI/CD
For GitHub Actions or other CI/CD:
- Store credentials as encrypted secrets
- Never commit credential files to git
- Use environment-specific secrets for each environment

---

<!-- section_id: "7993e909-5bea-4461-8afa-898a4a1d0d07" -->
## Summary

**Fully Working**:
- ✅ Unit tests (22 tests)
- ✅ Emulator integration tests (7 tests)
- ✅ Development environment tests (7 tests)
- ✅ **Total: 36 tests running in ~6 seconds**

**Awaiting Setup**:
- 🔄 Staging environment tests (3 tests) - needs credentials
- 🔄 Production smoke tests (3 tests) - needs credentials

**You can start using the comprehensive testing strategy RIGHT NOW** with the development environment. Staging and production can be added when you're ready to deploy.
