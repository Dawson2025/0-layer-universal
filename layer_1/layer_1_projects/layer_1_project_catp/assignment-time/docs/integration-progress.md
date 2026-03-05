---
resource_id: "a2d4dac2-f34d-437b-8a36-31ef37a16276"
resource_type: "document"
resource_name: "integration-progress"
---
﻿# Integration Progress

This log captures our tangible progress against the infrastructure blueprint in [docs/integration-plan.md](integration-plan.md).

## Snapshot Summary
- Projects online: `assignment-time`, `assignment-time-dev`, `assignment-time-test`
- Firestore: Default databases created in dev/test (region `nam5`)
- Secrets: `CANVAS_API_KEY` (dev) and `CANVAS_API_KEY_TEST` (test) with active versions
- Service accounts: `testing-ci@assignment-time-test.iam.gserviceaccount.com` provisioned, IAM verified, and secret access tested
- Local configuration: `.firebaserc` aliases (`default`, `dev`, `test`, `prod`) and `functions/.env.local` stub committed to local disk (git-ignored)

## Detailed Status
| Area | Status | Evidence |
| --- | --- | --- |
| Project separation | Completed | `gcloud projects list` shows dev/test IDs; `.firebaserc` updated |
| Firestore setup | Completed | Default databases created in `nam5` via CLI |
| Secret Manager | Completed | `gcloud secrets list` confirms `CANVAS_API_KEY` and `CANVAS_API_KEY_TEST` |
| CI service account | Completed | `testing-ci@assignment-time-test` granted roles and exercised through `gcloud secrets versions access` |
| CI workflow | Completed | `.github/workflows/integration.yml` writes SA key, authenticates, and pulls secrets |
| Canvas key retrieval | Completed | Manual CLI run retrieved `CANVAS_API_KEY_TEST` |
| IAM audit-log reminders | Pending | Not yet defined (integration plan section 6) |
| Org policy (SA key creation limit) | Pending | Requires org-level configuration |

## Next Actions
1. Define and schedule IAM audit-log/key-rotation reminders (integration plan section 6).
2. Apply an organization policy restricting service-account key creation (integration plan section 6).
3. Upload the testing SA key to the CI secret store, delete the local temp file, and enable the workflow.
4. Review audit logs after the first CI run to confirm environment separation behaves as expected.

_Last updated: 2025-10-06 01:19:51_
