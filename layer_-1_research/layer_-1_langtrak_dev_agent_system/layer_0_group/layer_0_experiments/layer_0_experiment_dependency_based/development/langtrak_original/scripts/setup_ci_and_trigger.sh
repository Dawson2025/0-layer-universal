#!/usr/bin/env bash
# Interactive helper to create a Google Cloud service account, create a key,
# add it to GitHub Actions secrets as FIREBASE_SA_KEY, and trigger the
# `update-auth-domains.yml` workflow in dry-run mode. Run this locally.

set -euo pipefail

prog() { echo "[setup-ci] $*"; }
err() { echo "[setup-ci] ERROR: $*" >&2; }

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || { err "required command '$1' not found. Please install it and re-run."; exit 1; }
}

require_cmd gcloud
require_cmd gh
require_cmd jq

echo
prog "Welcome — this script will help create a service account, upload its key to GitHub Secrets, and trigger the workflow."
echo "IMPORTANT: Run this locally where you can authenticate with gcloud and gh. Do not paste secrets into chat."
echo

read -rp "GitHub repo (owner/repo) [Dawson2025/lang-trak-in-progress]: " GITHUB_REPO
GITHUB_REPO=${GITHUB_REPO:-Dawson2025/lang-trak-in-progress}

read -rp "Cloud project to host the service account [lang-trak-dev]: " GCLOUD_PROJECT
GCLOUD_PROJECT=${GCLOUD_PROJECT:-lang-trak-dev}

read -rp "Service account id to create [firebase-domain-updater]: " SA_NAME
SA_NAME=${SA_NAME:-firebase-domain-updater}
SA_EMAIL="${SA_NAME}@${GCLOUD_PROJECT}.iam.gserviceaccount.com"

read -rp "Projects to update (space-separated) [lang-trak-dev lang-trak-prod]: " INPUT_PROJECTS
INPUT_PROJECTS=${INPUT_PROJECTS:-"lang-trak-dev lang-trak-prod"}

read -rp "Domains to add (space-separated) [example.com dev.example.com localhost 127.0.0.1]: " INPUT_DOMAINS
INPUT_DOMAINS=${INPUT_DOMAINS:-"example.com dev.example.com localhost 127.0.0.1"}

prog "Checking gcloud authentication..."
if ! gcloud auth print-access-token >/dev/null 2>&1; then
  prog "No active gcloud login — opening browser for 'gcloud auth login'..."
  gcloud auth login || { err "gcloud auth login failed"; exit 1; }
fi

prog "Setting active project to $GCLOUD_PROJECT"
gcloud config set project "$GCLOUD_PROJECT"

prog "Checking GitHub CLI authentication..."
if ! gh auth status >/dev/null 2>&1; then
  prog "No active gh login — running 'gh auth login'..."
  gh auth login || { err "gh auth login failed"; exit 1; }
fi

echo
prog "About to create service account: ${SA_EMAIL} in project ${GCLOUD_PROJECT}"
read -rp "Proceed? (y/N): " confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
  prog "Aborted by user."
  exit 0
fi

prog "Creating service account..."
gcloud iam service-accounts create "$SA_NAME" --display-name="Firebase Domain Updater" || true

prog "Granting roles/editor to the service account on project $GCLOUD_PROJECT (you can change this later)"
gcloud projects add-iam-policy-binding "$GCLOUD_PROJECT" \
  --member="serviceAccount:${SA_EMAIL}" --role="roles/editor" || true

KEY_FILE="firebase-domain-updater-key.json"
if [ -f "$KEY_FILE" ]; then
  prog "A local key file '$KEY_FILE' already exists. It will be overwritten after confirmation."
  read -rp "Overwrite key file? (y/N): " overwrite
  if [[ "$overwrite" != "y" && "$overwrite" != "Y" ]]; then
    err "Please move or remove existing $KEY_FILE and re-run this script.";
    exit 1
  fi
  rm -f "$KEY_FILE"
fi

prog "Creating service account key (will be saved to $KEY_FILE)"
gcloud iam service-accounts keys create "$KEY_FILE" --iam-account="$SA_EMAIL"

if [ ! -f "$KEY_FILE" ]; then
  err "Key file was not created; aborting"
  exit 1
fi

prog "Uploading key as GitHub secret FIREBASE_SA_KEY to repo $GITHUB_REPO"
prog "(the key file will be removed locally after upload)"

# Use gh to set secret from file
gh secret set FIREBASE_SA_KEY --body-file="$KEY_FILE" --repo "$GITHUB_REPO"

prog "Uploaded secret. Cleaning up local key file."
shred -u "$KEY_FILE" || rm -f "$KEY_FILE"

echo
prog "Now I will trigger the workflow in dry-run mode. You can inspect logs in Actions -> Update Firebase Authorized Domains."

echo "Projects: $INPUT_PROJECTS"
echo "Domains:  $INPUT_DOMAINS"

read -rp "Proceed to trigger workflow in dry-run mode? (y/N): " run_confirm
if [[ "$run_confirm" != "y" && "$run_confirm" != "Y" ]]; then
  prog "Skipped triggering workflow. You can trigger it from GitHub Actions UI."
  exit 0
fi

prog "Triggering workflow (dry-run=true)..."
gh workflow run update-auth-domains.yml \
  -f projects="$INPUT_PROJECTS" \
  -f domains="$INPUT_DOMAINS" \
  -f dry_run=true \
  --repo "$GITHUB_REPO"

prog "Workflow triggered. It may take a minute to start. Opening workflow runs page..."
gh run list --workflow=update-auth-domains.yml --repo "$GITHUB_REPO" -L 5

echo
prog "When the run appears, open it in the Actions UI, inspect the 'Run domain updater script' logs, and paste any errors here if you want me to review."

read -rp "After you've reviewed dry-run logs, do you want me to re-trigger with dry_run=false to apply changes? (y/N): " apply_confirm
if [[ "$apply_confirm" != "y" && "$apply_confirm" != "Y" ]]; then
  prog "Done. You can re-run this script or use the Actions UI to apply changes later."
  exit 0
fi

prog "Triggering workflow to apply changes (dry_run=false)..."
gh workflow run update-auth-domains.yml \
  -f projects="$INPUT_PROJECTS" \
  -f domains="$INPUT_DOMAINS" \
  -f dry_run=false \
  --repo "$GITHUB_REPO"

prog "Apply workflow triggered. Use the Actions UI to watch progress. Paste the run URL or logs here when available and I'll verify the changes and run sign-in tests."

exit 0
