---
resource_id: "b3bf3e24-64af-46a9-8623-6f0b6e6971f0"
resource_type: "document"
resource_name: "gcloud-cli-setup"
---
# gcloud CLI Setup Guide

<!-- section_id: "e0af32c0-1ad0-4702-90d3-7e04e8f3ea85" -->
## Installation

<!-- section_id: "586bd957-6aca-43f1-a30b-45d1fd594681" -->
### Linux/Ubuntu
```bash
# Add Google Cloud SDK repository
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Install
sudo apt-get update && sudo apt-get install google-cloud-cli

# Verify installation
gcloud version
```

<!-- section_id: "88b44175-c642-43a9-87a3-7a56295774de" -->
### macOS
```bash
# Using Homebrew
brew install --cask google-cloud-sdk
```

<!-- section_id: "40965b72-3853-4a4f-b9d4-7e4d4c5eded1" -->
### Windows
Download and run the installer from: https://cloud.google.com/sdk/docs/install

<!-- section_id: "3221b8c2-4f7f-4e96-b74a-4db5c20e629a" -->
## Authentication

<!-- section_id: "913c5efd-fe84-4ada-90bd-fe15712e76fa" -->
### Interactive Login (with browser)
```bash
gcloud auth login
```

<!-- section_id: "67e3406a-f0e9-4912-9ab0-65babe8b627d" -->
### Headless/Remote Login (no browser)
For systems without a browser or when using AI coding assistants:

```bash
# Start auth flow
gcloud auth login --no-launch-browser
```

This outputs a URL. Navigate to it in a browser, complete sign-in, and paste the verification code back.

**Using with browser automation (Claude Code + Playwright/Chrome):**
1. Run `gcloud auth login --no-launch-browser` in a screen session
2. Navigate to the URL in the browser
3. Complete OAuth flow
4. Send the verification code to the screen session

Example with screen:
```bash
# Start gcloud in screen
screen -dmS gcloud_auth bash -c 'gcloud auth login --no-launch-browser 2>&1 | tee /tmp/gcloud_output.txt; sleep 60'

# Wait for URL
sleep 3 && cat /tmp/gcloud_output.txt

# After getting code from browser, send it to screen
screen -S gcloud_auth -X stuff 'VERIFICATION_CODE\n'
```

<!-- section_id: "604a0fcd-3f50-4e52-9aa6-f512962650e4" -->
## Project Configuration

```bash
# List available projects
gcloud projects list

# Set active project
gcloud config set project PROJECT_ID

# View current configuration
gcloud config list
```

<!-- section_id: "90916dd7-b02e-400e-89bc-f74db6cfa80b" -->
## Common Issues

<!-- section_id: "63aea4b6-8be6-48c0-9242-6a4a390932c4" -->
### Billing Required
Some GCP services (like Secret Manager) require billing to be enabled:
```
ERROR: This API method requires billing to be enabled.
```

**Solution:** Enable billing at https://console.cloud.google.com/billing

<!-- section_id: "5b6d5c2d-4083-4006-962f-4ac8b9ef83d5" -->
### Multiple Accounts
If you have multiple Google accounts:
```bash
# List accounts
gcloud auth list

# Switch active account
gcloud config set account EMAIL@example.com
```

<!-- section_id: "0a3bb137-aad6-40a7-84b2-dd5e630ef42f" -->
## Related
- [Secret Manager Setup](./secret-manager.md)
- [Canvas API Integration](./canvas-api-integration.md)
