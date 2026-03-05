---
resource_id: "a3d34812-d3cf-4678-be95-d05e1705df8d"
resource_type: "document"
resource_name: "network-inspection-workflow"
---
# Network Request Inspection Workflow

This workflow describes how to use Chrome DevTools MCP to inspect network requests, analyze API responses, and debug network-related issues.

## Overview

The Network domain of Chrome DevTools Protocol provides comprehensive access to HTTP/HTTPS requests, WebSocket connections, and resource loading. This workflow covers common network inspection scenarios.

## Prerequisites

1. Chrome running with remote debugging enabled
2. Chrome DevTools MCP server connected
3. Target page loaded in browser

## Workflow Steps

### Step 1: Enable Network Domain

Before capturing network data, the Network domain must be enabled:

```
Action: Enable network monitoring
CDP Domain: Network
Method: Network.enable
```

This begins capturing all network activity for the target page.

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

## Common Use Cases

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

## Advanced Techniques

### Request Interception

Intercept and modify requests before they're sent:

```
Purpose: Modify headers, block requests, or change responses
Use Cases:
- Add authentication headers
- Block tracking requests
- Mock API responses for testing
```

### Response Body Retrieval

Get full response body for analysis:

```
Method: Network.getResponseBody
Input: requestId from captured request
Output: Base64-encoded body (if binary) or plain text
```

### Request Blocking

Block specific URLs or patterns:

```
Purpose: Test behavior when resources fail
Use Cases:
- Block third-party scripts
- Simulate API failures
- Test offline scenarios
```

## Output Examples

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

## Troubleshooting

### Missing Requests

**Problem:** Expected requests not appearing

**Solutions:**
1. Ensure Network.enable was called before requests were made
2. Check if requests are cached (may not appear as network requests)
3. Verify correct target page is selected
4. Service Worker may be intercepting requests

### Empty Response Bodies

**Problem:** Network.getResponseBody returns empty

**Solutions:**
1. Some responses may be streamed and not cached
2. Very large responses may not be captured
3. Binary responses need base64 decoding
4. Check if response was a redirect (3xx status)

### Timing Data Missing

**Problem:** Timing information shows -1 values

**Solutions:**
1. Cached responses don't have timing data
2. Failed requests may have incomplete timing
3. Some timing phases may not apply (e.g., no SSL for HTTP)

---

## Related Workflows

- [Console Log Capture Workflow](./console-log-capture-workflow.md)
- [DOM Inspection Workflow](./dom-inspection-workflow.md)

---

**Last Updated**: 2025-01-13
**CDP Domain**: Network
**Reference**: https://chromedevtools.github.io/devtools-protocol/tot/Network/
