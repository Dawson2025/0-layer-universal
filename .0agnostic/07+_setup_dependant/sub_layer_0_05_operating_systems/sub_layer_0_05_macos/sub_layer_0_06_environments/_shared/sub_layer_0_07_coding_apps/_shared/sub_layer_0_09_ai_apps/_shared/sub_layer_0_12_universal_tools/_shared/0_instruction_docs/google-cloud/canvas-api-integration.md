---
resource_id: "c227eee5-9ae8-47b6-a757-658f46bffa22"
resource_type: "document"
resource_name: "canvas-api-integration"
---
# Canvas LMS API Integration

This guide covers integrating with the Canvas LMS API using credentials stored in Google Secret Manager.

<!-- section_id: "c2b2f7f7-dfb5-48f3-9405-42f3ab1fdb46" -->
## Overview

Canvas LMS provides a REST API for accessing course data, assignments, grades, and more. API keys should be stored securely in Google Secret Manager.

<!-- section_id: "5fee75a8-9f8d-4ea5-b72b-92cdb2a5cabb" -->
## Prerequisites

- Canvas LMS account with API access
- Google Cloud project with Secret Manager enabled
- gcloud CLI installed and authenticated

<!-- section_id: "78d18a78-596f-4e8e-90ac-085dd99a2aae" -->
## Generating a Canvas API Token

1. Log into Canvas at your institution's URL
2. Go to **Account** > **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Provide a purpose description and optional expiry
6. Copy the generated token (it won't be shown again)

<!-- section_id: "15874808-31d1-4cb9-ad64-274356f026a0" -->
## Storing the Token in Secret Manager

```bash
# Set your GCP project
gcloud config set project YOUR_PROJECT_ID

# Create the secret
echo -n "YOUR_CANVAS_TOKEN" | gcloud secrets create CANVAS_API_KEY --data-file=-
```

<!-- section_id: "0e659336-fc13-4fa9-a330-8aba17fb188c" -->
## Using the API

<!-- section_id: "98a81f1f-5ddb-4b56-860c-6c6343c5e629" -->
### Quick Test
```bash
# Get the API key
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')

# Test with user profile endpoint
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "https://YOUR_INSTITUTION.instructure.com/api/v1/users/self"
```

<!-- section_id: "795f6e58-69b7-4a19-a429-7f61150f3809" -->
### Common Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/v1/users/self` | Current user profile |
| `/api/v1/courses` | List enrolled courses |
| `/api/v1/courses/:id/assignments` | Course assignments |
| `/api/v1/courses/:id/students` | Course students |

<!-- section_id: "1dd1a27d-cb82-4d43-b935-1f8fcd205552" -->
### Example: List Courses

```bash
CANVAS_API_KEY=$(gcloud secrets versions access latest --secret=CANVAS_API_KEY | tr -d '\n')
BASE_URL="https://byui.instructure.com/api/v1"

wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses?enrollment_state=active" | jq '.[].name'
```

<!-- section_id: "b7465c96-f2bc-41b2-ab5d-7e1a1d7bc07a" -->
### Example: Get Assignments

```bash
COURSE_ID="12345"
wget -qO- --header="Authorization: Bearer $CANVAS_API_KEY" \
  "$BASE_URL/courses/$COURSE_ID/assignments" | jq '.[] | {name, due_at}'
```

<!-- section_id: "f2889f6f-c844-46da-a2ba-d9da70d1f256" -->
## Node.js Integration

```javascript
const { SecretManagerServiceClient } = require('@google-cloud/secret-manager');

async function getCanvasApiKey() {
  const client = new SecretManagerServiceClient();
  const [version] = await client.accessSecretVersion({
    name: 'projects/PROJECT_ID/secrets/CANVAS_API_KEY/versions/latest',
  });
  return version.payload.data.toString();
}

async function fetchCanvasCourses(apiKey, baseUrl) {
  const response = await fetch(`${baseUrl}/courses`, {
    headers: {
      'Authorization': `Bearer ${apiKey}`,
    },
  });
  return response.json();
}

// Usage
const apiKey = await getCanvasApiKey();
const courses = await fetchCanvasCourses(apiKey, 'https://byui.instructure.com/api/v1');
```

<!-- section_id: "75385578-7135-42b5-90f6-27ae252a8d41" -->
## Python Integration

```python
from google.cloud import secretmanager
import requests

def get_canvas_api_key(project_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/CANVAS_API_KEY/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def fetch_courses(api_key, base_url):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(f"{base_url}/courses", headers=headers)
    return response.json()

# Usage
api_key = get_canvas_api_key("assignment-time")
courses = fetch_courses(api_key, "https://byui.instructure.com/api/v1")
```

<!-- section_id: "ba5c0dde-ad8a-49c8-8b72-f9a105c63f9f" -->
## Rate Limiting

Canvas API has rate limits. Check response headers:
- `X-Rate-Limit-Remaining`: Requests remaining
- `X-Request-Cost`: Cost of the request

<!-- section_id: "fb093862-11cc-47aa-a90e-75929c86ca30" -->
## Institution-Specific URLs

| Institution | Base URL |
|-------------|----------|
| BYU-Idaho | `https://byui.instructure.com/api/v1` |
| Generic | `https://YOUR_SCHOOL.instructure.com/api/v1` |

<!-- section_id: "fc0757cd-d9c0-41c0-bf29-2b4078f4a884" -->
## Troubleshooting

<!-- section_id: "9f772655-5aad-4669-9481-96758de3a9bf" -->
### 401 Unauthorized
- Check if token is valid and not expired
- Ensure token has necessary permissions

<!-- section_id: "8e044d48-e879-434c-b9a2-f6cd632b3eb8" -->
### 403 Forbidden
- User may not have access to the requested resource
- Check course enrollment status

<!-- section_id: "834846db-acef-4714-86e5-42391fea2e1a" -->
### curl vs wget
If `curl` fails with exit code 43, use `wget`:
```bash
# Instead of curl
wget -qO- --header="Authorization: Bearer $TOKEN" "URL"
```

<!-- section_id: "f15c7abb-9f15-4740-b468-a0d2b4f2b6e2" -->
## Related Projects

- **catp (Canvas Assignment Time Predictor)**: `/home/dawson/dawson-workspace/code/catp/`
  - Reference implementation using Canvas API with Firebase

<!-- section_id: "7fbc0e75-184c-4b85-9f50-9467fa11ab8b" -->
## Related Documentation
- [gcloud CLI Setup](./gcloud-cli-setup.md)
- [Secret Manager](./secret-manager.md)
- [Canvas API Documentation](https://canvas.instructure.com/doc/api/)
