---
resource_id: "d86c6a1c-cd0a-449a-9ed4-41ee7bfc8d3a"
resource_type: "document"
resource_name: "TEST_ENVIRONMENTS_STATUS"
---
# Test Environments Status
**Date**: 2025-10-23
**Status**: Development environment fully operational, Staging/Production awaiting credentials

---

<!-- section_id: "43c5eba6-7fb3-4483-ad54-642b65e25b5f" -->
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

<!-- section_id: "b48b5668-89f0-4440-832b-e2f9ce82e4b7" -->
## Development Environment ✅ FULLY OPERATIONAL

**Firebase Project**: `lang-trak-dev`
**Credentials**: `keys/lang-trak-dev-agent-key.json` ✅
**Tests**: 7 comprehensive CRUD tests

<!-- section_id: "df3380f4-76e9-4664-b461-05acb3aeb086" -->
### What's Tested:
- ✅ Firestore connection
- ✅ All collections accessible (projects, words, phonemes, groups)
- ✅ Project CRUD operations
- ✅ Word CRUD operations
- ✅ Phoneme CRUD operations
- ✅ Group CRUD operations
- ✅ Composite indexes work

<!-- section_id: "b864b952-d3ac-4417-964e-31974285773c" -->
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

<!-- section_id: "da6ae856-5522-4a9f-9c11-574f81940040" -->
## Staging Environment 🔄 AWAITING CREDENTIALS

**Firebase Project**: `lang-trak-staging` (referenced in `.firebaserc`)
**Credentials**: `keys/lang-trak-staging-agent-key.json` ❌ **MISSING**
**Tests**: 3 verification tests (created but can't run without credentials)

<!-- section_id: "d68811a3-9f6f-4273-81d1-4f622823fd96" -->
### What Would Be Tested:
- 🔄 Firestore connection
- 🔄 All collections accessible
- 🔄 Basic CRUD operations

<!-- section_id: "c4e5524e-9d37-4c2f-af44-4e7fce2d521c" -->
### Test File Location:
`tests/integration/real_firebase/test_staging_environment.py`

<!-- section_id: "14d08c6e-2efc-4671-b9ab-1c5970ee3198" -->
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

<!-- section_id: "ee96e829-77e8-42cd-bd09-24e6d8cf5182" -->
## Production Environment 🔄 AWAITING CREDENTIALS

**Firebase Project**: `lang-trak-prod` (referenced in `.firebaserc`)
**Credentials**: `keys/lang-trak-prod-agent-key.json` ❌ **MISSING**
**Tests**: 3 smoke tests (READ-ONLY for safety)

<!-- section_id: "d8fab5f2-f981-4bd6-baa2-ba4dd3703782" -->
### What Would Be Tested (READ-ONLY):
- 🔄 Firestore accessible
- 🔄 Collections readable
- 🔄 Project queries work

**IMPORTANT**: Production tests are **READ-ONLY** by design:
- ❌ NO writes
- ❌ NO deletes
- ❌ NO modifications
- ✅ Only verification that production is accessible and responsive

<!-- section_id: "c902e1a2-9ddf-4911-af0c-8b0d2d90386f" -->
### Test File Location:
`tests/integration/real_firebase/test_prod_smoke.py`

<!-- section_id: "e95e3c5b-096f-4885-bc6c-6fed633ba330" -->
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

<!-- section_id: "7baa666f-9afa-4619-8679-69d40bc9eb9c" -->
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

<!-- section_id: "87629cb7-b7f6-44ee-8d76-ac9e37039fff" -->
## Current Capabilities

<!-- section_id: "cfa832b4-e3e4-4674-840f-8a66c25b1871" -->
### What Works NOW (No Setup Required):
```bash
# Fast tests - 36 tests in ~6 seconds
./scripts/run-fast-tests.sh

# Dev environment tests - 7 tests in ~4 seconds
./scripts/run-dev-tests.sh

# Complete suite (fast + dev) - 43 tests in ~10 seconds
./scripts/run-all-tests.sh
```

<!-- section_id: "39dba31a-cc0e-4d90-94b4-d3ddd46789ab" -->
### What Needs Credentials:
- Staging environment tests → Need `keys/lang-trak-staging-agent-key.json`
- Production smoke tests → Need `keys/lang-trak-prod-agent-key.json`

---

<!-- section_id: "98717235-9894-4b3a-97c4-e67e1d30a163" -->
## Recommended Next Steps

<!-- section_id: "b952c3e1-0dbe-4c8e-92b3-b807252bd4ee" -->
### Priority 1: Start Using What Works
```bash
# Use this for daily development
./scripts/run-fast-tests.sh
```

<!-- section_id: "15e263c8-0b5f-43f2-9db8-3413eec42c30" -->
### Priority 2: Set Up Staging (Optional, when ready for pre-production)
1. Create/access `lang-trak-staging` Firebase project
2. Generate service account key
3. Save to `keys/lang-trak-staging-agent-key.json`
4. Run staging tests to verify

<!-- section_id: "7cab81db-444b-4b56-8bfa-206f497c7ce5" -->
### Priority 3: Set Up Production (Before first deploy)
1. Create/access `lang-trak-prod` Firebase project
2. Generate service account key (read-only if possible)
3. Save to `keys/lang-trak-prod-agent-key.json`
4. Run smoke tests to verify production is healthy

---

<!-- section_id: "eb6595c9-ddbb-4019-8e10-6621d8dc6b9a" -->
## Security Notes

<!-- section_id: "15718ea2-8668-454f-aa5e-0b86acd5df94" -->
### Credential Files (.gitignore)
All credential files should be in `.gitignore`:
```
keys/*.json
firebase-admin-config.json  # May contain sensitive paths
```

<!-- section_id: "626ab66f-6e25-4cb2-b59f-924c7d72b112" -->
### Service Account Permissions
- **Dev**: Full Firestore access (read/write/delete)
- **Staging**: Full Firestore access (read/write/delete)
- **Production**: Read-only recommended (for safety)

<!-- section_id: "3cf04dd6-2e7d-4dbf-9a66-7372a176ecf7" -->
### Credential Storage in CI/CD
For GitHub Actions or other CI/CD:
- Store credentials as encrypted secrets
- Never commit credential files to git
- Use environment-specific secrets for each environment

---

<!-- section_id: "548774fc-8a3e-431b-b42f-f2d3d1d583aa" -->
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
