# Context Management Workflow

This document describes the workflow for managing, caching, and optimizing context retrieved from the Context7 MCP server.

## Overview

The context management workflow ensures efficient use of Context7 API resources by implementing caching strategies, version tracking, and intelligent context refresh policies. This workflow operates alongside the search and retrieval workflows to optimize overall performance.

## Prerequisites

- Context7 MCP server configured and running
- Understanding of search and retrieval workflows
- Knowledge of token budget constraints

## Core Concepts

### Context Lifecycle

1. **Discovery**: Library ID resolved via search
2. **Retrieval**: Documentation fetched from API
3. **Caching**: Context stored for session reuse
4. **Application**: Context used to answer queries
5. **Refresh**: Outdated context updated as needed

### Context States

| State | Description | Action |
|-------|-------------|--------|
| Fresh | Recently fetched, current version | Use directly |
| Cached | Previously fetched, same session | Use if version matches |
| Stale | Old version or long-lived | Consider refresh |
| Missing | Not yet retrieved | Fetch from API |

## Workflow Steps

### Step 1: Check Context Cache

Before making API calls, check if context already exists:

**Cache Check Criteria:**
- Same library ID requested
- Same or compatible topic
- Token limit not exceeded by cached content
- Version requirements satisfied

### Step 2: Evaluate Freshness

Determine if cached context is still valid:

**Freshness Indicators:**
- Time since last fetch
- Library version changes
- Topic scope changes
- User-specified version requirements

**Decision Matrix:**

| Scenario | Cached Version | Needed Version | Action |
|----------|----------------|----------------|--------|
| Same library, same topic | 18.2.0 | Any | Use cache |
| Same library, different topic | 18.2.0 | Any | Fetch new |
| Same library, new version | 18.2.0 | 19.0.0 | Fetch new |
| Different library | N/A | N/A | Fetch new |

### Step 3: Fetch or Reuse

Based on evaluation:

**Reuse Cached Context:**
```
// No API call needed
context = cachedContext[libraryId]
```

**Fetch Fresh Context:**
```
Tool: get-library-docs
Input: { context7CompatibleLibraryID, topic, tokens }
Action: Store result in cache
```

### Step 4: Merge Multiple Contexts

When multiple libraries are needed:

**Sequential Approach:**
```
1. Fetch Library A context
2. Fetch Library B context
3. Combine for response
```

**Token Budget Distribution:**
```
Total Budget: 20,000 tokens
Library A (primary): 12,000 tokens
Library B (secondary): 8,000 tokens
```

### Step 5: Cache Management

Implement cache policies:

**Add to Cache:**
```
cache[libraryId] = {
  content: documentation,
  topic: requestedTopic,
  version: libraryVersion,
  fetchedAt: timestamp,
  tokens: tokenCount
}
```

**Evict from Cache:**
- Oldest entries first
- Least recently used
- When total tokens exceed limit

## Best Practices

### 1. Session-Level Caching

Within a single session:
- Store library IDs after resolution
- Cache documentation by library + topic
- Reuse cached content for follow-up questions

**Example Session Cache:**
```
sessionCache = {
  libraryIds: {
    "react": "/facebook/react",
    "next.js": "/vercel/next.js"
  },
  documentation: {
    "/facebook/react:hooks": { content, version, tokens },
    "/vercel/next.js:routing": { content, version, tokens }
  }
}
```

### 2. Token Budget Management

Track and manage token usage:

**Budget Tracking:**
```
totalBudget = 30000
usedTokens = 0

for each contextRequest:
  if usedTokens + request.tokens > totalBudget:
    evictOldestContext()
  fetchContext(request)
  usedTokens += actualTokensUsed
```

**Optimization Strategies:**
- Use topic filtering to reduce token usage
- Request smaller token limits for simple queries
- Evict unused contexts proactively

### 3. Version-Aware Caching

Track library versions:

**Version Checking:**
```
if cachedContext.version != requiredVersion:
  refreshContext()
```

**Version Requirements:**
- Explicit: User requests specific version
- Implicit: Latest stable is assumed
- Flexible: Any recent version acceptable

### 4. Graceful Degradation

When API is unavailable:

**Fallback Strategy:**
1. Use cached context if available
2. Use general training knowledge
3. Inform user of limitations
4. Suggest alternative approaches

## Workflow Diagram

```
[Context Request]
        |
        v
[Check Cache]
        |
        v
[Cache Hit?] --Yes--> [Check Freshness]
        |                     |
       No                     v
        |             [Fresh Enough?] --Yes--> [Use Cached]
        v                     |
[Fetch from API]             No
        |                     |
        v<--------------------+
[Store in Cache]
        |
        v
[Return Context]
```

## Cache Policies

### Time-Based Expiration

```
CACHE_TTL = 30 minutes  // Session-appropriate

if (now - cachedContext.fetchedAt) > CACHE_TTL:
  refreshContext()
```

### LRU (Least Recently Used)

```
When cache full:
  evict(leastRecentlyUsed)
  add(newContext)
```

### Token-Based Limits

```
MAX_CACHE_TOKENS = 50000

while (totalCacheTokens > MAX_CACHE_TOKENS):
  evictOldest()
```

## Multi-Library Scenarios

### Scenario 1: Related Libraries

**Request:** "Help me set up React with Next.js"

**Management:**
```
1. Fetch React context (hooks focus)
2. Fetch Next.js context (setup focus)
3. Combine contexts for comprehensive answer
4. Cache both for follow-up questions
```

### Scenario 2: Primary + Supporting

**Request:** "How do I use Prisma with Next.js API routes?"

**Management:**
```
Primary: Prisma (full documentation)
Supporting: Next.js (API routes only)

Token allocation:
- Prisma: 10,000 tokens
- Next.js API routes: 5,000 tokens
```

### Scenario 3: Sequential Questions

**Request 1:** "Explain React hooks"
**Request 2:** "How do I use useEffect?"
**Request 3:** "What about useCallback?"

**Management:**
```
Request 1: Fetch full hooks documentation
Request 2: Reuse cached hooks context
Request 3: Reuse cached hooks context

API calls: 1 (instead of 3)
```

## Error Recovery

### Cache Corruption

```
if cacheIntegrityCheck() fails:
  clearCache()
  refetchActiveContexts()
```

### API Timeout

```
if apiTimeout:
  if cacheExists:
    return cachedContext (with stale warning)
  else:
    return fallbackResponse
```

### Rate Limiting

```
if rateLimited:
  wait(retryAfter)
  if cacheExists:
    useCachedContext()
  retry()
```

## Metrics and Monitoring

### Cache Performance

Track these metrics:
- Cache hit rate
- Average fetch time
- Token utilization
- Eviction frequency

### API Usage

Monitor:
- Requests per session
- Tokens consumed
- Error rates
- Response times

## Integration Points

### With Search Workflow

```
// Search result caching
searchCache[query] = libraryId
// Reuse for similar queries
```

### With Retrieval Workflow

```
// Before retrieval
if hasCachedContext(libraryId, topic):
  return cachedContext
else:
  fetchAndCache(libraryId, topic)
```

## Configuration Options

### Cache Settings

```json
{
  "cache": {
    "enabled": true,
    "maxTokens": 50000,
    "ttlMinutes": 30,
    "evictionPolicy": "lru"
  }
}
```

### Refresh Settings

```json
{
  "refresh": {
    "autoRefresh": false,
    "onVersionMismatch": true,
    "backgroundRefresh": false
  }
}
```

## Related Workflows

- [Context Search Workflow](./context_search_workflow.md) - Finding library IDs
- [Context Retrieval Workflow](./context_retrieval_workflow.md) - Getting documentation

---

**Last Updated**: 2026-01-13
**Scope**: Session management, caching, optimization
**MCP Server**: Context7
