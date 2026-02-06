# Console Log Capture Workflow

This workflow describes how to use Chrome DevTools MCP to capture console messages, monitor JavaScript errors, and debug runtime issues.

## Overview

The Runtime and Log domains of Chrome DevTools Protocol provide access to console output, JavaScript exceptions, and runtime evaluation. This workflow covers capturing and analyzing console output for debugging.

## Prerequisites

1. Chrome running with remote debugging enabled
2. Chrome DevTools MCP server connected
3. Target page loaded in browser

## Workflow Steps

### Step 1: Enable Runtime Domain

Enable the Runtime domain to receive console messages:

```
Action: Enable runtime monitoring
CDP Domain: Runtime
Method: Runtime.enable
```

This enables:
- Console API calls (log, warn, error, etc.)
- JavaScript exceptions
- Runtime evaluation

### Step 2: Enable Log Domain (Optional)

For additional log entries beyond console API:

```
Action: Enable log monitoring
CDP Domain: Log
Method: Log.enable
```

This captures:
- Browser-level logs
- Security warnings
- Deprecation notices

### Step 3: Capture Console Messages

Console messages are received as events with these properties:

**Message Structure:**
- `type`: Message type (log, warning, error, debug, info)
- `text`: Message content
- `url`: Source file URL
- `line`: Line number in source
- `column`: Column number
- `stackTrace`: Call stack (for errors)
- `timestamp`: When message was logged

### Step 4: Filter and Analyze

Filter console output by:

**By Type:**
```
Filter: type = "error"
Purpose: Find only error messages
```

**By Source:**
```
Filter: url contains "app.js"
Purpose: Messages from specific file
```

**By Content:**
```
Filter: text contains "failed"
Purpose: Find failure-related messages
```

### Step 5: Handle Exceptions

JavaScript exceptions provide detailed information:

**Exception Data:**
- Exception text/message
- Line and column number
- Full stack trace
- Source URL
- Whether exception was caught

## Common Use Cases

### Use Case 1: Debug JavaScript Errors

**Scenario:** Application throwing unexpected errors

**Workflow:**
1. Enable Runtime domain
2. Navigate to or interact with the application
3. Capture exception events
4. Analyze:
   - Error message
   - Stack trace
   - Source location
   - Triggering action

**Analysis Steps:**
1. Read error message for cause
2. Examine stack trace for call sequence
3. Identify source file and line number
4. Determine what user action triggered error

### Use Case 2: Monitor Application Logging

**Scenario:** Track application state through console.log

**Workflow:**
1. Enable Runtime domain
2. Perform application actions
3. Capture all console.log messages
4. Analyze log sequence for:
   - Expected log messages appearing
   - Order of operations
   - Variable values logged
   - Missing expected logs

**Useful For:**
- Verifying code execution paths
- Checking variable values
- Understanding timing of operations
- Finding where code stops executing

### Use Case 3: Find Deprecation Warnings

**Scenario:** Application using deprecated APIs

**Workflow:**
1. Enable Runtime and Log domains
2. Load and interact with application
3. Filter for warning messages
4. Identify deprecated API usage:
   - Browser API deprecations
   - Library/framework warnings
   - Security warnings

**Common Warnings:**
- `console.warn` from frameworks
- Browser deprecation notices
- Mixed content warnings
- Insecure form warnings

### Use Case 4: Track Async Operations

**Scenario:** Debug async/await or Promise issues

**Workflow:**
1. Enable Runtime domain with async stack traces
2. Trigger async operations
3. Capture console output and exceptions
4. Analyze:
   - Promise rejection messages
   - Unhandled rejection warnings
   - Async stack traces

**Key Information:**
- Where promise was created
- What caused rejection
- Whether rejection was handled
- Full async call stack

### Use Case 5: Security Issue Detection

**Scenario:** Find security-related console warnings

**Workflow:**
1. Enable Runtime and Log domains
2. Load application
3. Filter for security-related messages:
   - Mixed content warnings
   - CORS errors
   - CSP violations
   - Insecure connection warnings

**Security Indicators:**
- "Mixed Content" messages
- "Blocked by CORS" errors
- "Content Security Policy" violations
- Certificate warnings

## Advanced Techniques

### Runtime Evaluation

Execute JavaScript and capture output:

```
Method: Runtime.evaluate
Input: JavaScript expression
Output: Return value and any console output
```

**Use Cases:**
- Query application state
- Trigger specific code paths
- Test JavaScript snippets
- Access variables and objects

### Exception Breakpoints

Set up to pause on exceptions:

```
Method: Debugger.setPauseOnExceptions
Options:
- "all": Pause on all exceptions
- "uncaught": Pause only on uncaught
- "none": Don't pause on exceptions
```

### Console API Interception

Monitor specific console methods:

```
Console Methods:
- console.log() - General logging
- console.warn() - Warnings
- console.error() - Errors
- console.info() - Informational
- console.debug() - Debug info
- console.trace() - Stack trace
- console.assert() - Assertions
- console.table() - Tabular data
- console.group() - Grouped output
- console.time() - Performance timing
```

## Output Examples

### Console Message Event

```json
{
  "type": "log",
  "args": [
    {
      "type": "string",
      "value": "User logged in successfully"
    }
  ],
  "executionContextId": 1,
  "timestamp": 1234567890.123,
  "stackTrace": {
    "callFrames": [
      {
        "functionName": "handleLogin",
        "scriptId": "42",
        "url": "https://example.com/app.js",
        "lineNumber": 156,
        "columnNumber": 8
      }
    ]
  }
}
```

### Exception Event

```json
{
  "exceptionDetails": {
    "exceptionId": 1,
    "text": "Uncaught TypeError: Cannot read property 'name' of undefined",
    "lineNumber": 42,
    "columnNumber": 15,
    "scriptId": "10",
    "url": "https://example.com/app.js",
    "stackTrace": {
      "callFrames": [
        {
          "functionName": "getUserName",
          "scriptId": "10",
          "url": "https://example.com/app.js",
          "lineNumber": 42,
          "columnNumber": 15
        },
        {
          "functionName": "displayProfile",
          "scriptId": "10",
          "url": "https://example.com/app.js",
          "lineNumber": 78,
          "columnNumber": 5
        }
      ]
    },
    "exception": {
      "type": "object",
      "subtype": "error",
      "className": "TypeError",
      "description": "TypeError: Cannot read property 'name' of undefined"
    }
  }
}
```

### Log Entry Event

```json
{
  "entry": {
    "source": "security",
    "level": "warning",
    "text": "Mixed Content: The page was loaded over HTTPS, but requested an insecure resource",
    "timestamp": 1234567890.123,
    "url": "https://example.com/page.html"
  }
}
```

## Message Type Reference

| Type | Description | Severity |
|------|-------------|----------|
| `log` | General console.log output | Info |
| `debug` | console.debug output | Debug |
| `info` | console.info output | Info |
| `warning` | console.warn output | Warning |
| `error` | console.error or exceptions | Error |
| `dir` | console.dir output | Info |
| `dirxml` | console.dirxml output | Info |
| `table` | console.table output | Info |
| `trace` | console.trace output | Info |
| `clear` | console.clear called | Info |
| `startGroup` | console.group started | Info |
| `endGroup` | console.groupEnd called | Info |
| `assert` | console.assert failed | Error |
| `profile` | console.profile | Info |
| `profileEnd` | console.profileEnd | Info |

## Troubleshooting

### Missing Console Messages

**Problem:** Expected console output not appearing

**Solutions:**
1. Ensure Runtime.enable was called before the messages were logged
2. Check if console is being cleared (console.clear)
3. Verify correct execution context is selected
4. Some messages may be filtered by log level

### Incomplete Stack Traces

**Problem:** Stack traces are truncated or missing

**Solutions:**
1. Enable async stack traces: `Debugger.setAsyncCallStackDepth({ maxDepth: 32 })`
2. Source maps may be needed for minified code
3. Native functions don't appear in stack traces

### High Volume of Messages

**Problem:** Too many console messages to process

**Solutions:**
1. Filter by message type (errors only)
2. Filter by source URL
3. Use pattern matching on message text
4. Clear console periodically

### Exception Not Caught

**Problem:** Exceptions happening but not being captured

**Solutions:**
1. Verify Runtime.enable was called
2. Check if exceptions are in different execution context (iframes)
3. Some Promise rejections need `unhandledrejection` event listener
4. Service Worker exceptions are in separate context

---

## Related Workflows

- [Network Inspection Workflow](./network-inspection-workflow.md)
- [DOM Inspection Workflow](./dom-inspection-workflow.md)

---

**Last Updated**: 2025-01-13
**CDP Domains**: Runtime, Log
**Reference**:
- https://chromedevtools.github.io/devtools-protocol/tot/Runtime/
- https://chromedevtools.github.io/devtools-protocol/tot/Log/
