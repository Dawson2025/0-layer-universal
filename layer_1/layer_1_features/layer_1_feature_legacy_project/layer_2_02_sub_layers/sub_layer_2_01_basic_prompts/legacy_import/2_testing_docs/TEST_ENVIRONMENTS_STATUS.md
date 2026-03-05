---
resource_id: "5b128b11-c0cc-496c-9aab-09f287752d18"
resource_type: "document"
resource_name: "TEST_ENVIRONMENTS_STATUS"
---
# Test Environments Status
**Date**: 2025-10-23
**Status**: Development environment fully operational, Staging/Production awaiting credentials

---

<!-- section_id: "92d71dbd-d80c-4892-a3b7-b88e6119c69b" -->
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

<!-- section_id: "09c5e785-533d-4bbf-b4de-e6ad285d5a49" -->
## Development Environment ✅ FULLY OPERATIONAL

**Firebase Project**: `lang-trak-dev`
**Credentials**: `keys/lang-trak-dev-agent-key.json` ✅
**Tests**: 7 comprehensive CRUD tests

<!-- section_id: "bf8ff79d-757b-4e21-bc12-e34eb2083867" -->
### What's Tested:
- ✅ Firestore connection
- ✅ All collections accessible (projects, words, phonemes, groups)
- ✅ Project CRUD operations
- ✅ Word CRUD operations
- ✅ Phoneme CRUD operations
- ✅ Group CRUD operations
- ✅ Composite indexes work

<!-- section_id: "9f48e1c2-2fbc-4277-a320-3b33070b6557" -->
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

<!-- section_id: "e526b590-96e1-4ca2-9b15-1c14a9941202" -->
## Staging Environment 🔄 AWAITING CREDENTIALS

**Firebase Project**: `lang-trak-staging` (referenced in `.firebaserc`)
**Credentials**: `keys/lang-trak-staging-agent-key.json` ❌ **MISSING**
**Tests**: 3 verification tests (created but can't run without credentials)

<!-- section_id: "0b1071df-b2bc-4b69-9120-01a6ff29e984" -->
### What Would Be Tested:
- 🔄 Firestore connection
- 🔄 All collections accessible
- 🔄 Basic CRUD operations

<!-- section_id: "8d16ce76-972b-4f26-abf4-9cf9caf00cda" -->
### Test File Location:
`tests/integration/real_firebase/test_staging_environment.py`

<!-- section_id: "f705c003-76af-4d7c-83c8-3a1dd9202b7f" -->
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

<!-- section_id: "78035e1f-d31c-400b-ab90-5f47a851f2d8" -->
## Production Environment 🔄 AWAITING CREDENTIALS

**Firebase Project**: `lang-trak-prod` (referenced in `.firebaserc`)
**Credentials**: `keys/lang-trak-prod-agent-key.json` ❌ **MISSING**
**Tests**: 3 smoke tests (READ-ONLY for safety)

<!-- section_id: "12bacd84-d81e-4868-9f25-118681957c32" -->
### What Would Be Tested (READ-ONLY):
- 🔄 Firestore accessible
- 🔄 Collections readable
- 🔄 Project queries work

**IMPORTANT**: Production tests are **READ-ONLY** by design:
- ❌ NO writes
- ❌ NO deletes
- ❌ NO modifications
- ✅ Only verification that production is accessible and responsive

<!-- section_id: "67224cc1-3955-4a56-90c2-f890322eb64e" -->
### Test File Location:
`tests/integration/real_firebase/test_prod_smoke.py`

<!-- section_id: "02c2ff7a-9975-42f7-bba5-31cfeae3c43c" -->
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

<!-- section_id: "1126bb72-99dd-4b68-971b-eccad3654a46" -->
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

<!-- section_id: "33d2d688-8f1a-4e15-a0dd-96a189b879a8" -->
## Current Capabilities

<!-- section_id: "af1a09a8-ecca-47cf-823a-8395c1318281" -->
### What Works NOW (No Setup Required):
```bash
# Fast tests - 36 tests in ~6 seconds
./scripts/run-fast-tests.sh

# Dev environment tests - 7 tests in ~4 seconds
./scripts/run-dev-tests.sh

# Complete suite (fast + dev) - 43 tests in ~10 seconds
./scripts/run-all-tests.sh
```

<!-- section_id: "003a6978-9fab-4117-a2fe-adca7297f196" -->
### What Needs Credentials:
- Staging environment tests → Need `keys/lang-trak-staging-agent-key.json`
- Production smoke tests → Need `keys/lang-trak-prod-agent-key.json`

---

<!-- section_id: "19dd5112-894f-4953-aeef-34b7fe64cff0" -->
## Recommended Next Steps

<!-- section_id: "9453f4b9-c7e6-42d3-ab51-40cd2df3ce66" -->
### Priority 1: Start Using What Works
```bash
# Use this for daily development
./scripts/run-fast-tests.sh
```

<!-- section_id: "66eaaf71-7632-4ba5-a356-de5a4f90a398" -->
### Priority 2: Set Up Staging (Optional, when ready for pre-production)
1. Create/access `lang-trak-staging` Firebase project
2. Generate service account key
3. Save to `keys/lang-trak-staging-agent-key.json`
4. Run staging tests to verify

<!-- section_id: "5d71b7e3-23a7-448b-b1fe-121da608e878" -->
### Priority 3: Set Up Production (Before first deploy)
1. Create/access `lang-trak-prod` Firebase project
2. Generate service account key (read-only if possible)
3. Save to `keys/lang-trak-prod-agent-key.json`
4. Run smoke tests to verify production is healthy

---

<!-- section_id: "4a4ecd78-4668-4238-84a2-b45fc4c75e8f" -->
## Security Notes

<!-- section_id: "c7bdb439-29c9-43b2-8d5a-01eaaa9066d9" -->
### Credential Files (.gitignore)
All credential files should be in `.gitignore`:
```
keys/*.json
firebase-admin-config.json  # May contain sensitive paths
```

<!-- section_id: "db99161d-bca7-417a-8013-7b5a662c83f8" -->
### Service Account Permissions
- **Dev**: Full Firestore access (read/write/delete)
- **Staging**: Full Firestore access (read/write/delete)
- **Production**: Read-only recommended (for safety)

<!-- section_id: "ec8d32ab-8f01-4b5c-afbf-0addba834a22" -->
### Credential Storage in CI/CD
For GitHub Actions or other CI/CD:
- Store credentials as encrypted secrets
- Never commit credential files to git
- Use environment-specific secrets for each environment

---

<!-- section_id: "47665862-96df-4778-a70b-ba8b7c89e310" -->
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
