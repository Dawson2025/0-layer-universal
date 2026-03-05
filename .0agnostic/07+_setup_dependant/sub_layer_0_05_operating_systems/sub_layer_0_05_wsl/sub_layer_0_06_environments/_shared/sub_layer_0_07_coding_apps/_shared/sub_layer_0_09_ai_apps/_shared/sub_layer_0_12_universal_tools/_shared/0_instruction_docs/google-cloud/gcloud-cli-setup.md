---
resource_id: "cd3a97f6-fb99-4f8f-b571-3e26864a63fb"
resource_type: "document"
resource_name: "gcloud-cli-setup"
---
# gcloud CLI Setup Guide

<!-- section_id: "b89c495e-f9b2-4ba6-8e8e-62207579870a" -->
## Installation

<!-- section_id: "e9f82b29-3ec9-4ff6-84a0-fec4c396940d" -->
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

<!-- section_id: "9734a73a-8641-4291-9475-4df2c4cc93b2" -->
### macOS
```bash
# Using Homebrew
brew install --cask google-cloud-sdk
```

<!-- section_id: "9e737faa-ac21-49be-aaab-fa978a207f59" -->
### Windows
Download and run the installer from: https://cloud.google.com/sdk/docs/install

<!-- section_id: "fc68ad91-1813-496f-b2a5-d8786fce0f78" -->
## Authentication

<!-- section_id: "3d234389-35b3-46d3-94e2-e0115c0556e4" -->
### Interactive Login (with browser)
```bash
gcloud auth login
```

<!-- section_id: "05488449-38f7-43d9-ae19-8f7de329b596" -->
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

<!-- section_id: "88e408d6-658d-4d34-9a68-095b5a7ddc89" -->
## Project Configuration

```bash
# List available projects
gcloud projects list

# Set active project
gcloud config set project PROJECT_ID

# View current configuration
gcloud config list
```

<!-- section_id: "057dc6ca-ca59-4ba3-98d4-f2ebe3c4a77e" -->
## Common Issues

<!-- section_id: "405b2f18-64d5-4b05-82b9-b0fce44f7760" -->
### Billing Required
Some GCP services (like Secret Manager) require billing to be enabled:
```
ERROR: This API method requires billing to be enabled.
```

**Solution:** Enable billing at https://console.cloud.google.com/billing

<!-- section_id: "10f59c76-2e14-4bcf-aba0-b8ea059f56af" -->
### Multiple Accounts
If you have multiple Google accounts:
```bash
# List accounts
gcloud auth list

# Switch active account
gcloud config set account EMAIL@example.com
```

<!-- section_id: "ea65a248-448d-4bca-b64b-123308a08fc6" -->
## Related
- [Secret Manager Setup](./secret-manager.md)
- [Canvas API Integration](./canvas-api-integration.md)
