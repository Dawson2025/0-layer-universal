# gcloud CLI Setup Guide

## Installation

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

### macOS
```bash
# Using Homebrew
brew install --cask google-cloud-sdk
```

### Windows
Download and run the installer from: https://cloud.google.com/sdk/docs/install

## Authentication

### Interactive Login (with browser)
```bash
gcloud auth login
```

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

## Project Configuration

```bash
# List available projects
gcloud projects list

# Set active project
gcloud config set project PROJECT_ID

# View current configuration
gcloud config list
```

## Common Issues

### Billing Required
Some GCP services (like Secret Manager) require billing to be enabled:
```
ERROR: This API method requires billing to be enabled.
```

**Solution:** Enable billing at https://console.cloud.google.com/billing

### Multiple Accounts
If you have multiple Google accounts:
```bash
# List accounts
gcloud auth list

# Switch active account
gcloud config set account EMAIL@example.com
```

## Related
- [Secret Manager Setup](./secret-manager.md)
- [Canvas API Integration](./canvas-api-integration.md)
