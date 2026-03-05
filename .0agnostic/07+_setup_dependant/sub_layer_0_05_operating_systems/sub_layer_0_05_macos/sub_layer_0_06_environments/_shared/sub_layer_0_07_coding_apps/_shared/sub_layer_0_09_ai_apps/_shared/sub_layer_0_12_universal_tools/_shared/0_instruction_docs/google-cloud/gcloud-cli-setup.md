---
resource_id: "223ecb3f-3e4b-40a6-b76b-5bae3b2d60ac"
resource_type: "document"
resource_name: "gcloud-cli-setup"
---
# gcloud CLI Setup Guide

<!-- section_id: "5f2f7338-9783-4d97-adb2-c39f7e534987" -->
## Installation

<!-- section_id: "1dde3614-351e-45ca-ae61-ebdd55f76fe3" -->
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

<!-- section_id: "9ec7ff20-ef20-4114-a296-05984c302b1f" -->
### macOS
```bash
# Using Homebrew
brew install --cask google-cloud-sdk
```

<!-- section_id: "4ad9a563-4570-4136-8542-9c30a9754d8b" -->
### Windows
Download and run the installer from: https://cloud.google.com/sdk/docs/install

<!-- section_id: "a3d2fc4e-f8dc-4e54-85e6-636a029a0f4d" -->
## Authentication

<!-- section_id: "5ee4216c-74ef-4195-8660-8bed735c4a17" -->
### Interactive Login (with browser)
```bash
gcloud auth login
```

<!-- section_id: "1e270557-64a9-48b2-ab45-c044999e30a1" -->
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

<!-- section_id: "ff568aa0-9018-49dc-888d-1968c939ebbe" -->
## Project Configuration

```bash
# List available projects
gcloud projects list

# Set active project
gcloud config set project PROJECT_ID

# View current configuration
gcloud config list
```

<!-- section_id: "43406ba4-2baf-4458-a8a5-d07cc8ad6fd6" -->
## Common Issues

<!-- section_id: "3ac0050d-0d4f-4f1a-b938-ff56f2bba459" -->
### Billing Required
Some GCP services (like Secret Manager) require billing to be enabled:
```
ERROR: This API method requires billing to be enabled.
```

**Solution:** Enable billing at https://console.cloud.google.com/billing

<!-- section_id: "b4d4b3df-5d5f-4cf3-aae8-318f58ce4806" -->
### Multiple Accounts
If you have multiple Google accounts:
```bash
# List accounts
gcloud auth list

# Switch active account
gcloud config set account EMAIL@example.com
```

<!-- section_id: "4e49c312-8c5d-41b8-a39a-9c4788832d38" -->
## Related
- [Secret Manager Setup](./secret-manager.md)
- [Canvas API Integration](./canvas-api-integration.md)
