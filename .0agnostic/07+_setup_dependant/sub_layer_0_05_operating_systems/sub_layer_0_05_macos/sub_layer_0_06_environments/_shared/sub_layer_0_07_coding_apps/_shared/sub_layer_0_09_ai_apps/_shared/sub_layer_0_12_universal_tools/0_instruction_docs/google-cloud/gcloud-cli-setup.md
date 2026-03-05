---
resource_id: "f58643a0-5392-4b31-8faa-269bf9ba1007"
resource_type: "document"
resource_name: "gcloud-cli-setup"
---
# gcloud CLI Setup Guide

<!-- section_id: "7c14ba2e-25f4-433b-b5cf-ba507d5aac6d" -->
## Installation

<!-- section_id: "542e51a0-02b4-43df-a0d9-63a0b8cd1824" -->
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

<!-- section_id: "27c29cf3-857a-4107-a0df-b660ba4da782" -->
### macOS
```bash
# Using Homebrew
brew install --cask google-cloud-sdk
```

<!-- section_id: "d6055c84-8b6d-4351-9bc8-ad483d3c482c" -->
### Windows
Download and run the installer from: https://cloud.google.com/sdk/docs/install

<!-- section_id: "a4a0c2c5-3108-47e1-acef-d6b7272a3e6d" -->
## Authentication

<!-- section_id: "a61f204c-f42d-4c87-945d-8aa9a5745045" -->
### Interactive Login (with browser)
```bash
gcloud auth login
```

<!-- section_id: "37cc9a01-247e-49a9-8174-dd391340226b" -->
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

<!-- section_id: "57f5c0a9-6f0f-44f7-a09c-5d3ef49ec5a9" -->
## Project Configuration

```bash
# List available projects
gcloud projects list

# Set active project
gcloud config set project PROJECT_ID

# View current configuration
gcloud config list
```

<!-- section_id: "da59846e-7de9-4533-96c9-928707663b3b" -->
## Common Issues

<!-- section_id: "3774ca0d-eaa6-4f14-b9d0-55165331babf" -->
### Billing Required
Some GCP services (like Secret Manager) require billing to be enabled:
```
ERROR: This API method requires billing to be enabled.
```

**Solution:** Enable billing at https://console.cloud.google.com/billing

<!-- section_id: "78a9dada-4aa8-4cc4-b41d-506840513f9f" -->
### Multiple Accounts
If you have multiple Google accounts:
```bash
# List accounts
gcloud auth list

# Switch active account
gcloud config set account EMAIL@example.com
```

<!-- section_id: "830c6d0c-ad37-42cf-b293-564ca9f3b1df" -->
## Related
- [Secret Manager Setup](./secret-manager.md)
- [Canvas API Integration](./canvas-api-integration.md)
