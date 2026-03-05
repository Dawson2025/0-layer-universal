---
resource_id: "a3d34812-d3cf-4678-be95-d05e1705df8d"
resource_type: "document"
resource_name: "network-inspection-workflow"
---
# Network Request Inspection Workflow

This workflow describes how to use Chrome DevTools MCP to inspect network requests, analyze API responses, and debug network-related issues.

<!-- section_id: "42b0aab3-77d6-420c-af4e-4ffad05e64a6" -->
## Overview

The Network domain of Chrome DevTools Protocol provides comprehensive access to HTTP/HTTPS requests, WebSocket connections, and resource loading. This workflow covers common network inspection scenarios.

<!-- section_id: "9f728f88-1d30-432f-ba7b-991caa590875" -->
## Prerequisites

1. Chrome running with remote debugging enabled
2. Chrome DevTools MCP server connected
3. Target page loaded in browser

<!-- section_id: "491bc526-441c-4539-b7e5-812c103ca6a9" -->
## Workflow Steps

<!-- section_id: "e5c71b30-5b97-41b0-9a70-aec33dea55cb" -->
### Step 1: Enable Network Domain

Before capturing network data, the Network domain must be enabled:

```
Action: Enable network monitoring
CDP Domain: Network
Method: Network.enable
```

This begins capturing all network activity for the target page.

<!-- section_id: "a86164f9-63f8-402d-8a20-c8dd6d0a7717" -->
### Step 2: Capture Network Requests

Once enabled, all network requests are captured. Key information includes:

**Request Data:**
- URL and method (GET, POST, etc.)
- Request headers
- Request body (for POST/PUT)
- Initiator (what triggered the request)
- Timestamp

**Response Data:**
- Status code
- Response headers
- Response body (when requested)
- Timing information
- Resource type

<!-- section_id: "d396ac00-b79d-4119-9f48-281885f85ffb" -->
### Step 3: Filter and Analyze

Common filtering scenarios:

**By URL Pattern:**
```
Filter: requests containing "/api/"
Purpose: Focus on API calls only
```

**By Status Code:**
```
Filter: status >= 400
Purpose: Find failed requests
```

**By Resource Type:**
```
Filter: type = "XHR" or "Fetch"
Purpose: Focus on AJAX/fetch calls
```

**By Method:**
```
Filter: method = "POST"
Purpose: Find form submissions or API mutations
```

<!-- section_id: "02112e15-e1df-4f22-9e27-c40288151227" -->
### Step 4: Inspect Request Details

For each request, inspect:

1. **Request Headers**
   - Authentication tokens
   - Content-Type
   - Custom headers
   - Cookies

2. **Request Body**
   - JSON payloads
   - Form data
   - File uploads

3. **Response Headers**
   - Cache-Control directives
   - Set-Cookie headers
   - Content-Type
   - CORS headers

4. **Response Body**
   - JSON responses
   - HTML content
   - Error messages

<!-- section_id: "4dad09f6-b218-4a85-bacc-ab069c7ac1d3" -->
### Step 5: Analyze Timing

Network timing breakdown:

```
Timing Phases:
- DNS Lookup: Time to resolve domain
- Connection: TCP connection establishment
- SSL: TLS handshake time
- Request Sent: Time to send request
- Waiting (TTFB): Time to first byte
- Content Download: Time to receive response
```

<!-- section_id: "86835102-96f6-46fb-8d55-ea6607ed7a00" -->
## Common Use Cases

<!-- section_id: "fd833432-9773-43b1-a0d4-2f594113437f" -->
### Use Case 1: Debug API Failures

**Scenario:** API calls returning unexpected errors

**Workflow:**
1. Enable network monitoring
2. Reproduce the issue
3. Filter for failed requests (status >= 400)
4. Inspect request to verify correct payload
5. Examine response body for error details
6. Check request headers for authentication issues

**Key Questions:**
- Is the request URL correct?
- Are authentication headers present?
- Is the request body properly formatted?
- What error message does the server return?

<!-- section_id: "69f4c341-828a-4109-9736-c0fce496dfc6" -->
### Use Case 2: Performance Analysis

**Scenario:** Page loads slowly

**Workflow:**
1. Enable network monitoring
2. Navigate to target page
3. Analyze timing for all requests
4. Identify slow requests (high TTFB or download time)
5. Check for large resources
6. Look for sequential vs parallel loading

**Metrics to Check:**
- Total request count
- Total transfer size
- Largest requests
- Slowest requests
- Request waterfall pattern

<!-- section_id: "bd983f13-7eb1-4777-838d-75eb99562907" -->
### Use Case 3: CORS Issue Investigation

**Scenario:** Cross-origin requests failing

**Workflow:**
1. Enable network monitoring
2. Trigger cross-origin request
3. Check preflight OPTIONS request (if present)
4. Examine CORS headers in response:
   - Access-Control-Allow-Origin
   - Access-Control-Allow-Methods
   - Access-Control-Allow-Headers
5. Verify request origin matches allowed origin

**Common CORS Issues:**
- Missing Access-Control-Allow-Origin header
- Origin not in allowed list
- Preflight request fails
- Credentials mode mismatch

<!-- section_id: "87c22fc3-4441-4f33-9562-8fa198af5a56" -->
### Use Case 4: Authentication Flow Debugging

**Scenario:** Login or authentication not working

**Workflow:**
1. Enable network monitoring
2. Clear cookies/session
3. Perform authentication flow
4. Track requests in sequence:
   - Login request
   - Token/session response
   - Subsequent authenticated requests
5. Verify tokens are stored and sent correctly

**Check Points:**
- Login request payload correct?
- Response contains token/session?
- Token stored in cookie/localStorage?
- Subsequent requests include token?

<!-- section_id: "13aa824c-1f4d-4e57-b3a1-a2ddc53c06bb" -->
### Use Case 5: WebSocket Monitoring

**Scenario:** Real-time data not updating

**Workflow:**
1. Enable network monitoring
2. Connect to page with WebSocket
3. Monitor WebSocket frames:
   - Connection establishment
   - Message frames (sent/received)
   - Close frames
4. Analyze message content and timing

**WebSocket Checks:**
- Connection successful?
- Messages being sent?
- Messages being received?
- Connection staying open?

<!-- section_id: "261fd534-cdf0-49b2-a73f-640a0de2f662" -->
## Advanced Techniques

<!-- section_id: "8b6f457f-2ce4-4b1e-8388-f6a91a02b0f1" -->
### Request Interception

Intercept and modify requests before they're sent:

```
Purpose: Modify headers, block requests, or change responses
Use Cases:
- Add authentication headers
- Block tracking requests
- Mock API responses for testing
```

<!-- section_id: "148dd8f1-1a95-4729-ba52-8d9f5223225f" -->
### Response Body Retrieval

Get full response body for analysis:

```
Method: Network.getResponseBody
Input: requestId from captured request
Output: Base64-encoded body (if binary) or plain text
```

<!-- section_id: "4fcfaa9d-7cf3-4f12-8666-0a0b1d4a356d" -->
### Request Blocking

Block specific URLs or patterns:

```
Purpose: Test behavior when resources fail
Use Cases:
- Block third-party scripts
- Simulate API failures
- Test offline scenarios
```

<!-- section_id: "3cfe0bf2-61cd-45d0-8fe1-29f5374194a3" -->
## Output Examples

<!-- section_id: "e29f8a1e-c201-4435-8ed6-f677f6e45d26" -->
### Captured Request Object

```json
{
  "requestId": "1234.5",
  "url": "https://api.example.com/users",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer token123",
    "Accept": "application/json"
  },
  "timestamp": 1234567890.123,
  "type": "XHR",
  "initiator": {
    "type": "script",
    "url": "https://example.com/app.js",
    "lineNumber": 42
  }
}
```

<!-- section_id: "aec05a1d-28ae-4033-af20-9f461bfc95ec" -->
### Response Object

```json
{
  "requestId": "1234.5",
  "status": 200,
  "statusText": "OK",
  "headers": {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
  },
  "mimeType": "application/json",
  "timing": {
    "dnsStart": 0,
    "dnsEnd": 10,
    "connectStart": 10,
    "connectEnd": 50,
    "sslStart": 20,
    "sslEnd": 50,
    "sendStart": 50,
    "sendEnd": 51,
    "receiveHeadersEnd": 150
  }
}
```

<!-- section_id: "a0f1052f-9753-4c1b-8646-ee8f7f977844" -->
## Troubleshooting

<!-- section_id: "ca76bc33-4201-4f14-b427-1f36b97562a4" -->
### Missing Requests

**Problem:** Expected requests not appearing

**Solutions:**
1. Ensure Network.enable was called before requests were made
2. Check if requests are cached (may not appear as network requests)
3. Verify correct target page is selected
4. Service Worker may be intercepting requests

<!-- section_id: "cca107d5-5e76-4bea-a45a-bb2e37c84c86" -->
### Empty Response Bodies

**Problem:** Network.getResponseBody returns empty

**Solutions:**
1. Some responses may be streamed and not cached
2. Very large responses may not be captured
3. Binary responses need base64 decoding
4. Check if response was a redirect (3xx status)

<!-- section_id: "83330a3a-9728-487a-91a2-107bc0ccfeef" -->
### Timing Data Missing

**Problem:** Timing information shows -1 values

**Solutions:**
1. Cached responses don't have timing data
2. Failed requests may have incomplete timing
3. Some timing phases may not apply (e.g., no SSL for HTTP)

---

<!-- section_id: "563f0bf1-15ec-4b53-9412-3310a64d5556" -->
## Related Workflows

- [Console Log Capture Workflow](./console-log-capture-workflow.md)
- [DOM Inspection Workflow](./dom-inspection-workflow.md)

---

**Last Updated**: 2025-01-13
**CDP Domain**: Network
**Reference**: https://chromedevtools.github.io/devtools-protocol/tot/Network/
