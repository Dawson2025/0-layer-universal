---
resource_id: "4911acc1-64e6-4dc2-a53d-f3ba8a899b76"
resource_type: "document"
resource_name: "context_retrieval_workflow"
---
# Context Retrieval Workflow

This document describes the workflow for retrieving documentation context using the Context7 MCP server.

<!-- section_id: "d9fb8b30-5f27-46d3-a59e-2d4a5588d8c5" -->
## Overview

The context retrieval workflow fetches comprehensive documentation for a specific library once you have its Context7-compatible identifier. This is the primary workflow for getting up-to-date library documentation into your AI agent's context.

<!-- section_id: "0d6eb71c-54b0-4e90-b6bd-fc504c2dfbc9" -->
## Prerequisites

- Context7 MCP server configured and running
- Valid `CONTEXT7_API_KEY` set
- Known Context7 library ID (from search workflow)

<!-- section_id: "859bdc6d-720b-46e1-a30d-8d5026e8a91e" -->
## Workflow Steps

<!-- section_id: "0481719e-7399-4f60-81cc-c69c8f4e6049" -->
### Step 1: Identify Documentation Needs

Before retrieving context, determine:
- **Target library**: Which library documentation is needed
- **Specific topic**: Is there a particular aspect (hooks, routing, configuration)?
- **Token budget**: How much context can the agent handle?

<!-- section_id: "ee5f8921-fd90-4292-a12a-241c776e397f" -->
### Step 2: Obtain Library ID

If you don't have the Context7 library ID, first use the [Context Search Workflow](./context_search_workflow.md):

```
Tool: resolve-library-id
Input: { "libraryName": "react" }
Output: "/facebook/react" (example)
```

<!-- section_id: "7fd6a260-fcee-4122-9e32-90c04d1340b8" -->
### Step 3: Retrieve Documentation

Use the `get-library-docs` tool with the library ID:

**Basic Retrieval:**
```
Tool: get-library-docs
Input: {
  "context7CompatibleLibraryID": "/facebook/react"
}
```

**Topic-Focused Retrieval:**
```
Tool: get-library-docs
Input: {
  "context7CompatibleLibraryID": "/facebook/react",
  "topic": "hooks"
}
```

**Token-Limited Retrieval:**
```
Tool: get-library-docs
Input: {
  "context7CompatibleLibraryID": "/facebook/react",
  "topic": "useState",
  "tokens": 5000
}
```

<!-- section_id: "ba533d3f-a1ea-4dde-9b7b-c4055700f690" -->
### Step 4: Process Retrieved Context

The returned documentation typically includes:
- API reference information
- Code examples
- Usage guidelines
- Common patterns

**Structure of Response:**
```
{
  "documentation": "...",
  "examples": [...],
  "version": "18.2.0",
  "source": "official"
}
```

<!-- section_id: "b14ad67a-ab22-4845-ae62-9a808c1a97a5" -->
### Step 5: Apply Context to Task

Use the retrieved documentation to:
- Answer user questions accurately
- Generate correct code examples
- Provide version-specific guidance
- Reference official best practices

<!-- section_id: "d736dfc9-5840-4a3c-a55e-e1fe279bf7cc" -->
## Best Practices

<!-- section_id: "3771b3b4-8724-47f1-83f6-6a2e5d685cc5" -->
### 1. Use Topic Filtering

Always specify a topic when possible to:
- Reduce token usage
- Get more relevant documentation
- Faster response times

```
// Better
{ "topic": "useEffect" }

// Broader (more tokens)
{ "topic": "hooks" }

// Broadest (maximum tokens)
{ }  // No topic
```

<!-- section_id: "40062f09-7c95-4246-b26b-014aac2651ca" -->
### 2. Manage Token Budget

Consider the context window limits:
- Default: 10,000 tokens
- For focused queries: 5,000 tokens
- For comprehensive coverage: 15,000+ tokens

```
{ "tokens": 5000 }  // Focused
{ "tokens": 10000 } // Standard
{ "tokens": 20000 } // Comprehensive
```

<!-- section_id: "64be8769-e8fc-4930-941a-94e1de33166d" -->
### 3. Cache Common Lookups

For frequently accessed documentation:
- Note the version returned
- Reuse context within the same session
- Only re-fetch if version-specific info is needed

<!-- section_id: "e54fe33a-7174-4fb7-be92-c85c3661ba46" -->
### 4. Handle Errors Gracefully

If retrieval fails:
1. Check API key validity
2. Verify library ID is correct
3. Try reducing token count
4. Fall back to cached or training knowledge

<!-- section_id: "fcbcf150-9a44-49d6-aa7d-0ba4b9ccfc1a" -->
## Workflow Diagram

```
[User Request]
       |
       v
[Identify Library]
       |
       v
[Have Library ID?] --No--> [Search Workflow]
       |                          |
      Yes                         v
       |                   [Get Library ID]
       |                          |
       v<-------------------------+
[Determine Topic]
       |
       v
[Set Token Limit]
       |
       v
[Call get-library-docs]
       |
       v
[Process Response]
       |
       v
[Apply to User Task]
```

<!-- section_id: "9c1a9abc-2dba-4e47-8df2-8bb99dff4e0d" -->
## Example Scenarios

<!-- section_id: "a6e6254a-e6b2-4af3-ac2b-6f83a5b89b67" -->
### Scenario 1: React Hooks Documentation

**User Request:** "How do I use useCallback in React?"

**Workflow:**
1. Library: React (ID: `/facebook/react`)
2. Topic: `useCallback` or `hooks`
3. Tokens: 5000 (focused query)
4. Call: `get-library-docs({ context7CompatibleLibraryID: "/facebook/react", topic: "useCallback", tokens: 5000 })`

<!-- section_id: "035cf720-9e26-410a-b103-36113c3d7f9b" -->
### Scenario 2: Next.js Routing

**User Request:** "Explain Next.js App Router"

**Workflow:**
1. Library: Next.js (ID: `/vercel/next.js`)
2. Topic: `app router` or `routing`
3. Tokens: 10000 (moderate complexity)
4. Call: `get-library-docs({ context7CompatibleLibraryID: "/vercel/next.js", topic: "app router", tokens: 10000 })`

<!-- section_id: "c92200e6-3420-48c2-b338-3b50faa84f62" -->
### Scenario 3: General Library Overview

**User Request:** "Give me an overview of Prisma ORM"

**Workflow:**
1. Library: Prisma (ID: `/prisma/prisma`)
2. Topic: None (general overview)
3. Tokens: 15000 (comprehensive)
4. Call: `get-library-docs({ context7CompatibleLibraryID: "/prisma/prisma", tokens: 15000 })`

<!-- section_id: "14baa8ff-5db2-4bfe-ae34-96b27c7e2a2c" -->
## Error Handling

<!-- section_id: "219bb3e1-5cd8-482f-96bd-d556cf313c16" -->
### Library Not Found
```
Error: "Library ID not valid"
Solution: Use resolve-library-id to find correct ID
```

<!-- section_id: "ed503e37-b518-4171-a4fd-d434a2aeed89" -->
### Rate Limited
```
Error: "429 Too Many Requests"
Solution: Wait before retrying, reduce request frequency
```

<!-- section_id: "22732e86-1153-4fd0-a3ff-9636b2bba7aa" -->
### Timeout
```
Error: "Request timeout"
Solution: Reduce token count, specify narrower topic
```

<!-- section_id: "7823c4de-c4aa-499b-8993-d3d043017316" -->
## Related Workflows

- [Context Search Workflow](./context_search_workflow.md) - Finding library IDs
- [Context Management Workflow](./context_management_workflow.md) - Managing cached context

---

**Last Updated**: 2026-01-13
**Tool**: `get-library-docs`
**MCP Server**: Context7
