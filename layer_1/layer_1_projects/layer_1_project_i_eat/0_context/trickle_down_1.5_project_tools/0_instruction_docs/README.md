---
resource_id: "07067ea8-c5a3-4574-98f5-78096804b49f"
resource_type: "readme
document"
resource_name: "README"
---
# Configure Firebase Authorized Domains (CI)

This repository includes a GitHub Actions workflow `.github/workflows/update-auth-domains.yml`
that runs `scripts/configure-auth-domains.py` using a Google Cloud service account. Use this
if you prefer updating authorized domains from CI rather than running the script locally.

<!-- section_id: "43107d8e-f7a5-41b7-b513-cddd89c330a7" -->
## Overview

- The workflow is manual (workflow_dispatch) and accepts `projects`, `domains`, and `dry_run` inputs.
- It authenticates to Google Cloud using a service account key stored in the repository secrets.

<!-- section_id: "93fbbdf8-3bb4-4b7d-a39f-b5d69329a814" -->
## Create a service account (least-privilege steps)

Run these locally using `gcloud` (replace `PROJECT` with one of your cloud project IDs):

```bash
# Create service account
gcloud iam service-accounts create firebase-domain-updater \
  --display-name="Firebase Domain Updater"

# Replace PROJECT with a project that will be used to run the workflow (this can be any
# project where you have permission to grant roles; it does not have to be the same
# project(s) you're updating but often is).
PROJECT=lang-trak-dev

# Grant Editor role (or a narrower custom role that includes Identity Toolkit admin methods)
gcloud projects add-iam-policy-binding "$PROJECT" \
  --member="serviceAccount:firebase-domain-updater@$PROJECT.iam.gserviceaccount.com" \
  --role="roles/editor"

# Create and download the key (keep it private)
gcloud iam service-accounts keys create firebase-domain-updater-key.json \
  --iam-account="firebase-domain-updater@$PROJECT.iam.gserviceaccount.com"
```

<!-- section_id: "4cb2079e-ea65-458a-9638-1853db32d80e" -->
## Add the key to GitHub Secrets

1. Open your GitHub repo -> Settings -> Secrets -> Actions -> New repository secret
2. Name the secret `FIREBASE_SA_KEY`
3. Paste the entire contents of `firebase-domain-updater-key.json` into the secret value

<!-- section_id: "acaa2f24-18c6-4ee4-8c8f-3f34fb445c47" -->
## Run the workflow

Go to the repository Actions tab, select "Update Firebase Authorized Domains", click "Run workflow",
enter the `projects` and `domains` inputs, and set `dry_run` to `false` to apply changes.

<!-- section_id: "a0ff0323-aedd-4871-836e-dd541797807a" -->
## Notes
- The service account needs the ability to call the Identity Toolkit Admin API. `roles/editor`
  is a quick option. For production, consider a custom role that only includes the minimal
  methods required.
- Do NOT commit the service account key file to the repo. Use GitHub Secrets only.
