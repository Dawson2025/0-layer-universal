---
resource_id: "9f8d16be-a329-4263-85d3-2dd2d6ee9242"
resource_type: "document"
resource_name: "integration-plan"
---
﻿# Cloud Integration & Credential Plan

This document describes how the ClearSign / Assignment Time project manages Google Cloud, Firebase, and Canvas credentials across development, testing, and production environments.

<!-- section_id: "51d2dd7a-e3a8-4fdc-848d-317dc318ba95" -->
## Goals
- Keep API keys and secrets out of source control.
- Ensure each environment has isolated credentials and Firestore data sets.
- Make it easy for contributors to spin up a local environment without touching production resources.

<!-- section_id: "63dea748-e238-44f8-8989-ca0fe3146d43" -->
## Implementation Steps


<!-- section_id: "6c57e3b7-682a-4e2b-9d70-62d537d21a4d" -->
### 1. Project & Resource Setup
- Create three distinct Google Cloud and Firebase projects: `assignment-time-dev`, `assignment-time-test`, and `assignment-time`.
- Link each Firebase project to its own native Firestore database so no environment shares data.
- After the projects exist, update `.firebaserc` to map the aliases used by local tooling and CI:

```json
{
  "projects": {
    "dev": "assignment-time-dev",
    "test": "assignment-time-test",
    "prod": "assignment-time"
  }
}
```

<!-- section_id: "ba583bd6-2151-44f4-9ed1-7923a7fb98f8" -->
### 2. Credential Handling
- **Development**: Every contributor runs `gcloud auth application-default login`; confirm the ADC file is present and keep `.env.local` git-ignored with only non-sensitive dev secrets.
- **Testing**: In the testing project, create a dedicated service account with the roles `Cloud Functions Invoker`, `Secret Manager Secret Accessor`, and `Datastore User`. Store its key in your CI secret manager, inject it at runtime via `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/testing-service-account.json"`, and delete it after tests.
- **Production**: Prefer workload identity by attaching the production service account directly to Cloud Functions, Cloud Run, or Compute Engine. If a key must exist, store it in Secret Manager and load it only at runtime.

<!-- section_id: "068c1438-900c-442e-b693-43b9f3a885f5" -->
### 3. Canvas & External API Keys
- Create environment-specific secrets such as `CANVAS_API_KEY` in Secret Manager (`gcloud secrets create CANVAS_API_KEY --replication-policy automatic --project=<PROJECT_ID>`).
- Grant only the required service accounts `roles/secretmanager.secretAccessor`.
- For local development, load the key from `.env.local` or export it before running emulators (`export CANVAS_API_KEY=your-key`).

<!-- section_id: "79f4c754-c85d-47b3-9905-a126899a5db2" -->
### 4. Firestore Configuration & Data Hygiene
- Never point different environments at the same Firestore instance; verify scripts and emulators reference the correct project.
- Seed and clean test data using project-aware scripts, and periodically query collections to detect unintended cross-environment writes.

<!-- section_id: "06965f53-a0c9-43fe-81a0-4ab1a523f901" -->
### 5. CI/CD Pipeline Hygiene
- Testing pipelines download the testing service account key on the runner, set `GOOGLE_APPLICATION_CREDENTIALS`, run integration tests, then remove the file.
- Production deployments use the attached service account or fetch the production key from Secret Manager during the build/deploy window only.
- Use `firebase use <alias>` or `GOOGLE_CLOUD_PROJECT` environment variables to ensure commands target the right project.

<!-- section_id: "2cf51011-560f-4330-abbb-5a26de48cae6" -->
### 6. Security & Audit
- Enable and review IAM audit logs for all projects; ensure you can trace access to service accounts and secrets.
- Set organization policies to restrict service account key creation.
- Document and schedule rotations for secrets and service accounts; verify IAM bindings per environment on a regular cadence.

<!-- section_id: "bfb41ea3-3e8f-4086-8925-b131d27a44be" -->
### 7. Common Traps & Safety Nets
- Git-ignore all key files and `.env.local`; never commit credential material.
- Watch for accidental use of production credentials in non-prod environments.
- Run periodic checks (e.g., `firebase firestore:collections`) to confirm data separation.

<!-- section_id: "f9614a06-5f57-4f20-b82a-05645d6d403f" -->
### 8. Maintaining the System
- Share credential rotation plans and security changes with the team.
- Log significant infrastructure or configuration updates and keep this plan aligned with current architecture.

<!-- section_id: "c45f2d5c-02ff-4f95-b0f7-2ae131a36dc0" -->
## Current Environment Setup Status

- **Projects created**: `assignment-time-dev` and `assignment-time-test` (Firebase enabled) in addition to existing `assignment-time`.
- **Firestore**: Default databases provisioned in `assignment-time-dev` and `assignment-time-test` (location `nam5`).
- **`.firebaserc`**: Aliases configured for `dev`, `test`, and `prod`.
- **Secrets**: `CANVAS_API_KEY` (dev) and `CANVAS_API_KEY_TEST` (test) created with active versions.
- **Testing service account**: `testing-ci@assignment-time-test.iam.gserviceaccount.com` has Cloud Functions Invoker, Secret Manager Secret Accessor, and Datastore User roles. CLI retrieval with its key succeeds.
- **Local dev env**: `functions/.env.local` stub created (git-ignored).
- **Pending**: IAM audit-log rotation reminders plus org policy to restrict service-account key creation.
<!-- section_id: "20e2255b-ef50-4939-a838-255c28712f27" -->
## Environment Overview

| Environment | GCP Project (example)        | Firestore Instance            | Auth Strategy                                        | Primary Use |
|-------------|------------------------------|-------------------------------|------------------------------------------------------|-------------|
| Development | `assignment-time-dev`         | Firestore Native (development) | Application Default Credentials (developer account)  | Local feature work |
| Testing     | `assignment-time-test`        | Firestore Native (testing)    | Dedicated testing service account                    | CI / manual QA |
| Production  | `assignment-time`             | Firestore Native (production) | Production service account attached to runtime infra | Live traffic |

> **Note:** Use separate GCP projects where possible. At minimum, segregate Firestore databases via different Firebase projects.

<!-- section_id: "85535940-1715-4c0b-b825-5537368b466b" -->
## Credential Management

<!-- section_id: "5516dd61-0945-4bf2-9195-bf7f93260d72" -->
### Development
- Authenticate using Application Default Credentials (ADC) tied to the developer's user account.
- Run `gcloud auth application-default login` and follow the browser prompt.
- ADC stores credentials at `%APPDATA%\gcloud\application_default_credentials.json` (Windows) or `~/.config/gcloud/application_default_credentials.json` (macOS/Linux).
- Client libraries and Firebase Admin SDK will automatically detect this credential file while running locally.

<!-- section_id: "4f6d2f67-7ca5-4f21-9952-aec90088db45" -->
### Testing
- Create a **testing service account** in the testing project with the minimal roles (e.g., `Cloud Functions Invoker`, `Secret Manager Secret Accessor`, `Datastore User`).
- Download the service account key JSON and store it in the CI secret store or a secure vault.
- Point the test environment to the key file:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/testing-service-account.json"
  ```
- Never reuse production keys in testing; rotate the testing key if it leaks.

<!-- section_id: "3dd6d9e6-8259-488b-8fa0-465957dc0452" -->
### Production
- Prefer **workload identity**: attach the production service account directly to Cloud Functions, Cloud Run, or Compute Engine.
- If a key file is unavoidable, keep it in Secret Manager and load it at runtime. Set the environment variable only when the key material exists on disk:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/production-service-account.json"
  ```
- Rotate production credentials routinely and audit IAM bindings.

<!-- section_id: "b1bed911-bb99-4d59-9a56-eb24d10050cd" -->
### Quick Reference

| Environment | Recommended Auth                         | How to Configure |
|-------------|-------------------------------------------|------------------|
| Development | ADC (developer user credentials)          | `gcloud auth application-default login` |
| Testing     | Testing service account key               | `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/testing-service-account.json"` |
| Production  | Attached production service account (preferred) or production key | Attach SA to runtime resource or set `GOOGLE_APPLICATION_CREDENTIALS` if a key is required |

<!-- section_id: "d1f19e68-727d-4048-874b-2a8e5e354ad4" -->
### Security Practices
- Keep service account keys out of Git; use `.gitignore` and secret stores.
- Restrict IAM roles per environment to the minimum needed.
- Track key rotations and revoke unused credentials promptly.

<!-- section_id: "06fcdc99-e1ea-4c00-8bc8-1000c76c1105" -->
## Canvas API Key Handling

| Environment | Storage Location | How Functions Access It |
|-------------|------------------|--------------------------|
| Development | `.env.local` in `functions/` (git ignored) or `firebase functions:config:set` locally | Loaded via `process.env.CANVAS_API_KEY` or emulator config |
| Testing     | Secret Manager secret `CANVAS_API_KEY_TEST` | Injected via service account permissions |
| Production  | Secret Manager secret `CANVAS_API_KEY`      | Accessed through `Secret Manager Secret Accessor` role |

Steps:
1. Store the API key as a Secret Manager secret in each project (`gcloud secrets create CANVAS_API_KEY --replication-policy automatic`).
2. Grant the environment-specific service account `roles/secretmanager.secretAccessor`.
3. In Cloud Functions, keep `CANVAS_API_KEY` out of `config` files; retrieve it on demand using `@google-cloud/secret-manager` as already implemented.
4. For local development, you may set `CANVAS_API_KEY` in `.env.local` or export it in the shell before running emulators.

<!-- section_id: "5b2007bf-2b7d-4cdb-9491-8bef50c65daf" -->
## Firestore Configuration

<!-- section_id: "85352aac-a6ad-4f81-b6c9-3edc67a941ee" -->
### Project Separation
- Each environment should use its own Firebase project and Firestore instance to prevent accidental data crossover.
- Configure per-environment `.firebaserc` aliases:
  ```json
  {
    "projects": {
      "dev": "assignment-time-dev",
      "test": "assignment-time-test",
      "prod": "assignment-time"
    }
  }
  ```

<!-- section_id: "a772379a-71c6-4039-bde3-a7867b1ca618" -->
### Firestore Rules
- Maintain environment-specific rule files if security requirements differ.
- Enforce read/write restrictions based on authentication claims.
- Use the Firebase emulator during development to validate rule changes before deploying.

<!-- section_id: "805c6626-8446-4943-914c-f86a22219e60" -->
### Data Management
- Seed data via scripts (`functions/test-student-course-details.js`) pointing to the correct project/emulator.
- Remember to purge testing data regularly to control costs.

<!-- section_id: "6088f02e-c18d-4327-80e8-2c280f91c862" -->
## Deployment Workflow

1. **Development:**
   - Run emulators with ADC credentials.
   - Use `.env.local` or environment variables for secrets.

2. **Testing/CI:**
   - Configure pipelines to download the testing service account key at runtime.
   - Set `GOOGLE_APPLICATION_CREDENTIALS` before running integration tests.
   - Target the testing Firebase project using `firebase use test`.

3. **Production:**
   - Deploy via CI pipeline with production service account permissions (no key files stored in the repo).
   - Ensure Cloud Functions are configured to access production secrets.
   - After deploy, verify Firestore writes and secret access.

<!-- section_id: "a0d4e160-0e14-461b-96da-7cec2e810d41" -->
## Ready-to-Use Snippets

<!-- section_id: "8b5351b3-785f-4f2a-9817-6fa688b646e7" -->
### `.env.local` (development)
```text
CANVAS_API_KEY=your-dev-key
```

<!-- section_id: "3deefce5-5835-4a0f-b1cf-b93287543563" -->
### GitHub Actions CI Example
```yaml
steps:
  - name: Download Service Account Key
    run: echo "${{ secrets.TESTING_SERVICE_ACCOUNT_KEY }}" > /tmp/testing-sa.json
  - name: Set Credentials
    run: export GOOGLE_APPLICATION_CREDENTIALS="/tmp/testing-sa.json"
  - name: Run Tests
    run: npm test
  - name: Clean Up
    run: rm /tmp/testing-sa.json
```

<!-- section_id: "5e0d8975-e4d1-436a-a495-a22b2d8134e6" -->
### Firebase Functions Secret Access Example
```javascript
const { SecretManagerServiceClient } = require('@google-cloud/secret-manager');
const secretClient = new SecretManagerServiceClient();

async function getCanvasApiKey(projectId) {
  const name = `projects/${projectId}/secrets/CANVAS_API_KEY/versions/latest`;
  const [version] = await secretClient.accessSecretVersion({ name });
  return version.payload.data.toString();
}
```

<!-- section_id: "42eee6f8-464b-4bee-91c3-59f3e150e1db" -->
## Additional Recommendations
- Enable IAM audit logs on all projects.
- Use organization policies to limit who can create service account keys.
- Document rotation schedules for Canvas API keys and service accounts.
- Keep this document updated whenever environment topology or secret handling changes.
<!-- section_id: "90b0cba8-5ec4-4806-9941-37c977f13e25" -->
## Operational Checklist

1. **Project & Resource Separation**
   - Create isolated GCP/Firebase projects for dev, test, and prod; avoid shared Firestore instances or IAM bindings.
   - Verify `.firebaserc` aliases and CI configuration point to the correct project for each environment.

2. **Credential Handling**
   - _Development_: Ensure all contributors run `gcloud auth application-default login` and confirm the ADC path; keep `.env.local` git-ignored.
   - _Testing_: Provision a least-privilege testing service account, store its key in a secure CI vault, inject it only at runtime, and remove it after tests.
   - _Production_: Prefer workload identity (attach the service account to Cloud Functions/Run/Compute Engine). If a key is required, load it from Secret Manager instead of storing it on disk.

3. **Canvas & External API Keys**
   - Store per-environment API keys (e.g., `CANVAS_API_KEY`) in Secret Manager.
   - Grant `roles/secretmanager.secretAccessor` only to the service accounts that need each secret.

4. **Firestore Data Separation**
   - Run seed scripts and tests against the correct project/emulator context.
   - Periodically query collections in each project to catch unintended cross-environment writes.

5. **Emulator Usage & Safety Nets**
   - Require developers to use the Firebase and Cloud Functions emulators locally before pushing changes.
   - Validate Firestore security rules in the emulator prior to staging/production deploys.

6. **Key Rotation & IAM Auditing**
   - Schedule regular service account key and API secret rotations; document the rotation workflow.
   - Enable Cloud Audit Logs and review access events for service accounts and Secret Manager.
   - Restrict who can create service account keys via organization policy.

7. **Deployment Pipeline Hygiene**
   - Configure CI/CD to inject secrets securely at runtime; never commit key material.
   - Ensure the production service account cannot reach dev/test resources.
   - Post-deploy, verify Firestore and Secret Manager access paths and roll back on failure.

<!-- section_id: "7322d51d-259a-44ba-869b-9b1cddde1462" -->
### Common Traps to Avoid
- Using production credentials in development or testing.
- Committing API keys or service account JSON files to version control.
- Mixing data between environments when running emulators or scripts.

<!-- section_id: "e7e4ba93-daa1-48e5-8e95-3d3b062cabb5" -->
### Maintaining Security Culture
- Communicate credential rotation schedules and security changes to the team.
- Log configuration updates and keep this plan current as infrastructure evolves.









