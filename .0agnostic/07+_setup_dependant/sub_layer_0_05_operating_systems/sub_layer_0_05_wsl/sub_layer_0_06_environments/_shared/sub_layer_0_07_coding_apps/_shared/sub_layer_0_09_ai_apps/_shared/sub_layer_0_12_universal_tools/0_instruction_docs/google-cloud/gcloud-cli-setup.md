---
resource_id: "2d74e0c6-91c7-41bf-abf8-f0b333dec3f7"
resource_type: "document"
resource_name: "gcloud-cli-setup"
---
# gcloud CLI Setup Guide

<!-- section_id: "ed9f45e8-ec03-452b-a15a-906829fb9375" -->
## Installation

<!-- section_id: "cc63b9fc-8f34-4376-84a1-d125956fca9f" -->
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

<!-- section_id: "50755a63-e97d-4bba-b03a-825b17e7387b" -->
### macOS
```bash
# Using Homebrew
brew install --cask google-cloud-sdk
```

<!-- section_id: "520bd297-ce74-44a7-802c-ba7c0967b403" -->
### Windows
Download and run the installer from: https://cloud.google.com/sdk/docs/install

<!-- section_id: "7acbe2f9-d2a3-4954-946d-d2685357b8c7" -->
## Authentication

<!-- section_id: "8b589704-c80c-45f9-9a94-c5d0d5d560ec" -->
### Interactive Login (with browser)
```bash
gcloud auth login
```

<!-- section_id: "e77e12ae-4dc0-4a99-a6de-7e7938ffaaca" -->
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

<!-- section_id: "edd6c183-e29f-4fa3-9727-18a8e31daa8e" -->
## Project Configuration

```bash
# List available projects
gcloud projects list

# Set active project
gcloud config set project PROJECT_ID

# View current configuration
gcloud config list
```

<!-- section_id: "e51580ee-6300-4b9c-8004-f41ae1f036df" -->
## Common Issues

<!-- section_id: "63042cea-1d56-4239-bdc8-8f60c813b974" -->
### Billing Required
Some GCP services (like Secret Manager) require billing to be enabled:
```
ERROR: This API method requires billing to be enabled.
```

**Solution:** Enable billing at https://console.cloud.google.com/billing

<!-- section_id: "92b1745e-c9cf-4c25-8d29-18196bad1029" -->
### Multiple Accounts
If you have multiple Google accounts:
```bash
# List accounts
gcloud auth list

# Switch active account
gcloud config set account EMAIL@example.com
```

<!-- section_id: "c588d6c2-4810-4ddf-973a-290fbbcee3ea" -->
## Related
- [Secret Manager Setup](./secret-manager.md)
- [Canvas API Integration](./canvas-api-integration.md)
