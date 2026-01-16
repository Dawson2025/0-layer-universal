# Cloud Integration & Credential Plan

This document describes how the ClearSign / Assignment Time project manages Google Cloud, Firebase, and Canvas credentials across development, testing, and production environments.

## Goals
- Keep API keys and secrets out of source control.
- Ensure each environment has isolated credentials and Firestore data sets.
- Make it easy for contributors to spin up a local environment without touching production resources.

## Implementation Steps


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

### 2. Credential Handling
- **Development**: Every contributor runs `gcloud auth application-default login`; confirm the ADC file is present and keep `.env.local` git-ignored with only non-sensitive dev secrets.
- **Testing**: In the testing project, create a dedicated service account with the roles `Cloud Functions Invoker`, `Secret Manager Secret Accessor`, and `Datastore User`. Store its key in your CI secret manager, inject it at runtime via `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/testing-service-account.json"`, and delete it after tests.
- **Production**: Prefer workload identity by attaching the production service account directly to Cloud Functions, Cloud Run, or Compute Engine. If a key must exist, store it in Secret Manager and load it only at runtime.

### 3. Canvas & External API Keys
- Create environment-specific secrets such as `CANVAS_API_KEY` in Secret Manager (`gcloud secrets create CANVAS_API_KEY --replication-policy automatic --project=<PROJECT_ID>`).
- Grant only the required service accounts `roles/secretmanager.secretAccessor`.
- For local development, load the key from `.env.local` or export it before running emulators (`export CANVAS_API_KEY=your-key`).

### 4. Firestore Configuration & Data Hygiene
- Never point different environments at the same Firestore instance; verify scripts and emulators reference the correct project.
- Seed and clean test data using project-aware scripts, and periodically query collections to detect unintended cross-environment writes.

### 5. CI/CD Pipeline Hygiene
- Testing pipelines download the testing service account key on the runner, set `GOOGLE_APPLICATION_CREDENTIALS`, run integration tests, then remove the file.
- Production deployments use the attached service account or fetch the production key from Secret Manager during the build/deploy window only.
- Use `firebase use <alias>` or `GOOGLE_CLOUD_PROJECT` environment variables to ensure commands target the right project.

### 6. Security & Audit
- Enable and review IAM audit logs for all projects; ensure you can trace access to service accounts and secrets.
- Set organization policies to restrict service account key creation.
- Document and schedule rotations for secrets and service accounts; verify IAM bindings per environment on a regular cadence.

### 7. Common Traps & Safety Nets
- Git-ignore all key files and `.env.local`; never commit credential material.
- Watch for accidental use of production credentials in non-prod environments.
- Run periodic checks (e.g., `firebase firestore:collections`) to confirm data separation.

### 8. Maintaining the System
- Share credential rotation plans and security changes with the team.
- Log significant infrastructure or configuration updates and keep this plan aligned with current architecture.

## Current Environment Setup Status

- **Projects created**: `assignment-time-dev` and `assignment-time-test` (Firebase enabled) in addition to existing `assignment-time`.
- **Firestore**: Default databases provisioned in `assignment-time-dev` and `assignment-time-test` (location `nam5`).
- **`.firebaserc`**: Aliases configured for `dev`, `test`, and `prod`.
- **Secrets**: `CANVAS_API_KEY` (dev) and `CANVAS_API_KEY_TEST` (test) created with active versions.
- **Testing service account**: `testing-ci@assignment-time-test.iam.gserviceaccount.com` has Cloud Functions Invoker, Secret Manager Secret Accessor, and Datastore User roles. CLI retrieval with its key succeeds.
- **Local dev env**: `functions/.env.local` stub created (git-ignored).
- **Pending**: IAM audit-log rotation reminders plus org policy to restrict service-account key creation.
## Environment Overview

| Environment | GCP Project (example)        | Firestore Instance            | Auth Strategy                                        | Primary Use |
|-------------|------------------------------|-------------------------------|------------------------------------------------------|-------------|
| Development | `assignment-time-dev`         | Firestore Native (development) | Application Default Credentials (developer account)  | Local feature work |
| Testing     | `assignment-time-test`        | Firestore Native (testing)    | Dedicated testing service account                    | CI / manual QA |
| Production  | `assignment-time`             | Firestore Native (production) | Production service account attached to runtime infra | Live traffic |

> **Note:** Use separate GCP projects where possible. At minimum, segregate Firestore databases via different Firebase projects.

## Credential Management

### Development
- Authenticate using Application Default Credentials (ADC) tied to the developer's user account.
- Run `gcloud auth application-default login` and follow the browser prompt.
- ADC stores credentials at `%APPDATA%\gcloud\application_default_credentials.json` (Windows) or `~/.config/gcloud/application_default_credentials.json` (macOS/Linux).
- Client libraries and Firebase Admin SDK will automatically detect this credential file while running locally.

### Testing
- Create a **testing service account** in the testing project with the minimal roles (e.g., `Cloud Functions Invoker`, `Secret Manager Secret Accessor`, `Datastore User`).
- Download the service account key JSON and store it in the CI secret store or a secure vault.
- Point the test environment to the key file:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/testing-service-account.json"
  ```
- Never reuse production keys in testing; rotate the testing key if it leaks.

### Production
- Prefer **workload identity**: attach the production service account directly to Cloud Functions, Cloud Run, or Compute Engine.
- If a key file is unavoidable, keep it in Secret Manager and load it at runtime. Set the environment variable only when the key material exists on disk:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/production-service-account.json"
  ```
- Rotate production credentials routinely and audit IAM bindings.

### Quick Reference

| Environment | Recommended Auth                         | How to Configure |
|-------------|-------------------------------------------|------------------|
| Development | ADC (developer user credentials)          | `gcloud auth application-default login` |
| Testing     | Testing service account key               | `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/testing-service-account.json"` |
| Production  | Attached production service account (preferred) or production key | Attach SA to runtime resource or set `GOOGLE_APPLICATION_CREDENTIALS` if a key is required |

### Security Practices
- Keep service account keys out of Git; use `.gitignore` and secret stores.
- Restrict IAM roles per environment to the minimum needed.
- Track key rotations and revoke unused credentials promptly.

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

## Firestore Configuration

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

### Firestore Rules
- Maintain environment-specific rule files if security requirements differ.
- Enforce read/write restrictions based on authentication claims.
- Use the Firebase emulator during development to validate rule changes before deploying.

### Data Management
- Seed data via scripts (`functions/test-student-course-details.js`) pointing to the correct project/emulator.
- Remember to purge testing data regularly to control costs.

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

## Ready-to-Use Snippets

### `.env.local` (development)
```text
CANVAS_API_KEY=your-dev-key
```

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

## Additional Recommendations
- Enable IAM audit logs on all projects.
- Use organization policies to limit who can create service account keys.
- Document rotation schedules for Canvas API keys and service accounts.
- Keep this document updated whenever environment topology or secret handling changes.
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

### Common Traps to Avoid
- Using production credentials in development or testing.
- Committing API keys or service account JSON files to version control.
- Mixing data between environments when running emulators or scripts.

### Maintaining Security Culture
- Communicate credential rotation schedules and security changes to the team.
- Log configuration updates and keep this plan current as infrastructure evolves.









