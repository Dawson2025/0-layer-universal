---
resource_id: "9ab86f5c-885f-4ed7-b655-1de25bd6853d"
resource_type: "document"
resource_name: "context_management_workflow"
---
# Context Management Workflow

This document describes the workflow for managing, caching, and optimizing context retrieved from the Context7 MCP server.

<!-- section_id: "8b8d48f9-3192-4414-8190-e971c8401030" -->
## Overview

The context management workflow ensures efficient use of Context7 API resources by implementing caching strategies, version tracking, and intelligent context refresh policies. This workflow operates alongside the search and retrieval workflows to optimize overall performance.

<!-- section_id: "472d8614-fb19-4140-a0a6-101557eb3d5b" -->
## Prerequisites

- Context7 MCP server configured and running
- Understanding of search and retrieval workflows
- Knowledge of token budget constraints

<!-- section_id: "15e3206f-1e2b-401c-ac8e-b1285084c53e" -->
## Core Concepts

<!-- section_id: "818153fe-6ed2-4d9b-9293-21b3bd43e27e" -->
### Context Lifecycle

1. **Discovery**: Library ID resolved via search
2. **Retrieval**: Documentation fetched from API
3. **Caching**: Context stored for session reuse
4. **Application**: Context used to answer queries
5. **Refresh**: Outdated context updated as needed

<!-- section_id: "a34ed326-7b64-4a6d-94c9-0529ff16c03d" -->
### Context States

| State | Description | Action |
|-------|-------------|--------|
| Fresh | Recently fetched, current version | Use directly |
| Cached | Previously fetched, same session | Use if version matches |
| Stale | Old version or long-lived | Consider refresh |
| Missing | Not yet retrieved | Fetch from API |

<!-- section_id: "a0d36f15-d32b-41ed-aeab-d8cf3d4034e1" -->
## Workflow Steps

<!-- section_id: "e9bf4e68-225c-4c7b-922b-18149f632d87" -->
### Step 1: Check Context Cache

Before making API calls, check if context already exists:

**Cache Check Criteria:**
- Same library ID requested
- Same or compatible topic
- Token limit not exceeded by cached content
- Version requirements satisfied

<!-- section_id: "bee13d5d-c64e-4a5e-93b6-884f58d57c98" -->
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

<!-- section_id: "9137f18a-341d-4858-b4be-28eabb30755b" -->
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

<!-- section_id: "30ddd3fa-7763-4702-95e3-f6d77b7ba390" -->
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

<!-- section_id: "9738ae25-7ef3-49ee-9d1b-63b2d13aa193" -->
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

<!-- section_id: "25bcf40d-b512-4d35-b8a0-f7f9c171d351" -->
## Best Practices

<!-- section_id: "0826da8f-69e2-40da-8fe1-aee21e6fc0d1" -->
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

<!-- section_id: "91cf109d-132d-42e9-9032-0a2952a04bb0" -->
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

<!-- section_id: "20c3ac5a-4cdd-4655-8c30-83ed438630c7" -->
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

<!-- section_id: "e9969d64-a4fe-4583-bf81-beaf929d2daf" -->
### 4. Graceful Degradation

When API is unavailable:

**Fallback Strategy:**
1. Use cached context if available
2. Use general training knowledge
3. Inform user of limitations
4. Suggest alternative approaches

<!-- section_id: "e08dc8d9-1857-47c6-8c0e-0381e16f928b" -->
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

<!-- section_id: "ce49fdd7-1dac-472a-b941-c05c3eb13a3e" -->
## Cache Policies

<!-- section_id: "510693cc-f0d2-4d9a-b5ea-80a03bdd4d83" -->
### Time-Based Expiration

```
CACHE_TTL = 30 minutes  // Session-appropriate

if (now - cachedContext.fetchedAt) > CACHE_TTL:
  refreshContext()
```

<!-- section_id: "429bdaa2-d345-4f8a-9277-61ae1dde81df" -->
### LRU (Least Recently Used)

```
When cache full:
  evict(leastRecentlyUsed)
  add(newContext)
```

<!-- section_id: "4c724f6d-62cf-4901-9433-18733fdf2691" -->
### Token-Based Limits

```
MAX_CACHE_TOKENS = 50000

while (totalCacheTokens > MAX_CACHE_TOKENS):
  evictOldest()
```

<!-- section_id: "6b0e0c2f-a05a-43c1-b764-214463965289" -->
## Multi-Library Scenarios

<!-- section_id: "d90a37bb-2dbf-4542-a509-9fa223849dca" -->
### Scenario 1: Related Libraries

**Request:** "Help me set up React with Next.js"

**Management:**
```
1. Fetch React context (hooks focus)
2. Fetch Next.js context (setup focus)
3. Combine contexts for comprehensive answer
4. Cache both for follow-up questions
```

<!-- section_id: "a353b921-6c82-4f12-b396-2370812b8817" -->
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

<!-- section_id: "0cd00ac5-13fc-4731-8e5e-6fca34c6cc14" -->
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

<!-- section_id: "ec110060-2e61-4cf1-b84a-ab6b3a896f70" -->
## Error Recovery

<!-- section_id: "4223b27a-7929-4ad2-8c2f-fb96db8ac0a8" -->
### Cache Corruption

```
if cacheIntegrityCheck() fails:
  clearCache()
  refetchActiveContexts()
```

<!-- section_id: "74ebbb72-8c9b-495a-a0d2-0dfe7f2e348e" -->
### API Timeout

```
if apiTimeout:
  if cacheExists:
    return cachedContext (with stale warning)
  else:
    return fallbackResponse
```

<!-- section_id: "36184118-6694-4032-8316-a594bdf8593b" -->
### Rate Limiting

```
if rateLimited:
  wait(retryAfter)
  if cacheExists:
    useCachedContext()
  retry()
```

<!-- section_id: "ce09d5ff-9dab-43b0-bd14-22e65c8ebc91" -->
## Metrics and Monitoring

<!-- section_id: "c37e1d93-cd70-4401-b421-1d95223f37d7" -->
### Cache Performance

Track these metrics:
- Cache hit rate
- Average fetch time
- Token utilization
- Eviction frequency

<!-- section_id: "8f1cb7c0-30f0-4299-b334-86bfb6e35d6f" -->
### API Usage

Monitor:
- Requests per session
- Tokens consumed
- Error rates
- Response times

<!-- section_id: "9e7964a1-2d8c-42f4-be1d-aff152afa5af" -->
## Integration Points

<!-- section_id: "dff2556d-fb06-4dc3-a7c5-f34c8e6b7cd9" -->
### With Search Workflow

```
// Search result caching
searchCache[query] = libraryId
// Reuse for similar queries
```

<!-- section_id: "1c026acc-6e4d-46dc-b8b4-b237675ce305" -->
### With Retrieval Workflow

```
// Before retrieval
if hasCachedContext(libraryId, topic):
  return cachedContext
else:
  fetchAndCache(libraryId, topic)
```

<!-- section_id: "d7f5b37b-09b6-4ae7-8d6c-ea14d8b06c7d" -->
## Configuration Options

<!-- section_id: "548aaf77-778d-4c96-a913-e976638e8cda" -->
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

<!-- section_id: "cc693dbf-7056-491e-805f-cedfda8874d0" -->
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

<!-- section_id: "b5529574-5792-4abb-8939-0bb21d63b436" -->
## Related Workflows

- [Context Search Workflow](./context_search_workflow.md) - Finding library IDs
- [Context Retrieval Workflow](./context_retrieval_workflow.md) - Getting documentation

---

**Last Updated**: 2026-01-13
**Scope**: Session management, caching, optimization
**MCP Server**: Context7
