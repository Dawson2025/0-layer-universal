---
resource_id: "1ddc7f5c-c3fd-47bf-a52c-39214fdb3595"
resource_type: "readme
document"
resource_name: "README"
---
# Configure Firebase Authorized Domains (CI)

This repository includes a GitHub Actions workflow `.github/workflows/update-auth-domains.yml`
that runs `scripts/configure-auth-domains.py` using a Google Cloud service account. Use this
if you prefer updating authorized domains from CI rather than running the script locally.

<!-- section_id: "2f25e86f-5754-4ec1-9bf3-21d85c352e1c" -->
## Overview

- The workflow is manual (workflow_dispatch) and accepts `projects`, `domains`, and `dry_run` inputs.
- It authenticates to Google Cloud using a service account key stored in the repository secrets.

<!-- section_id: "9bfb3d6b-67af-4b32-a034-24d1759c52f3" -->
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

<!-- section_id: "a80ed01f-ac47-45bb-bc84-1393b4148597" -->
## Add the key to GitHub Secrets

1. Open your GitHub repo -> Settings -> Secrets -> Actions -> New repository secret
2. Name the secret `FIREBASE_SA_KEY`
3. Paste the entire contents of `firebase-domain-updater-key.json` into the secret value

<!-- section_id: "3ecc41b6-2841-4e94-8b95-727930e29af6" -->
## Run the workflow

Go to the repository Actions tab, select "Update Firebase Authorized Domains", click "Run workflow",
enter the `projects` and `domains` inputs, and set `dry_run` to `false` to apply changes.

<!-- section_id: "55e5f466-c56f-4517-a8f1-ed8ee5b21abd" -->
## Notes
- The service account needs the ability to call the Identity Toolkit Admin API. `roles/editor`
  is a quick option. For production, consider a custom role that only includes the minimal
  methods required.
- Do NOT commit the service account key file to the repo. Use GitHub Secrets only.
