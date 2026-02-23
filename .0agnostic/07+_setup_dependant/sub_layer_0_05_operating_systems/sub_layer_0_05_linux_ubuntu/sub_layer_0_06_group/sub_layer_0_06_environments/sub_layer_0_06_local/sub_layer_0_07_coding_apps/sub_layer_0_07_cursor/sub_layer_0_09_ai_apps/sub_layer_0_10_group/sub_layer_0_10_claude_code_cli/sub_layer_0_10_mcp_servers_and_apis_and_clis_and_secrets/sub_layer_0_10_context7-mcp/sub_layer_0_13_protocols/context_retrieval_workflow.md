# Context Retrieval Workflow

This document describes the workflow for retrieving documentation context using the Context7 MCP server.

## Overview

The context retrieval workflow fetches comprehensive documentation for a specific library once you have its Context7-compatible identifier. This is the primary workflow for getting up-to-date library documentation into your AI agent's context.

## Prerequisites

- Context7 MCP server configured and running
- Valid `CONTEXT7_API_KEY` set
- Known Context7 library ID (from search workflow)

## Workflow Steps

### Step 1: Identify Documentation Needs

Before retrieving context, determine:
- **Target library**: Which library documentation is needed
- **Specific topic**: Is there a particular aspect (hooks, routing, configuration)?
- **Token budget**: How much context can the agent handle?

### Step 2: Obtain Library ID

If you don't have the Context7 library ID, first use the [Context Search Workflow](./context_search_workflow.md):

```
Tool: resolve-library-id
Input: { "libraryName": "react" }
Output: "/facebook/react" (example)
```

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

### Step 5: Apply Context to Task

Use the retrieved documentation to:
- Answer user questions accurately
- Generate correct code examples
- Provide version-specific guidance
- Reference official best practices

## Best Practices

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

### 3. Cache Common Lookups

For frequently accessed documentation:
- Note the version returned
- Reuse context within the same session
- Only re-fetch if version-specific info is needed

### 4. Handle Errors Gracefully

If retrieval fails:
1. Check API key validity
2. Verify library ID is correct
3. Try reducing token count
4. Fall back to cached or training knowledge

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

## Example Scenarios

### Scenario 1: React Hooks Documentation

**User Request:** "How do I use useCallback in React?"

**Workflow:**
1. Library: React (ID: `/facebook/react`)
2. Topic: `useCallback` or `hooks`
3. Tokens: 5000 (focused query)
4. Call: `get-library-docs({ context7CompatibleLibraryID: "/facebook/react", topic: "useCallback", tokens: 5000 })`

### Scenario 2: Next.js Routing

**User Request:** "Explain Next.js App Router"

**Workflow:**
1. Library: Next.js (ID: `/vercel/next.js`)
2. Topic: `app router` or `routing`
3. Tokens: 10000 (moderate complexity)
4. Call: `get-library-docs({ context7CompatibleLibraryID: "/vercel/next.js", topic: "app router", tokens: 10000 })`

### Scenario 3: General Library Overview

**User Request:** "Give me an overview of Prisma ORM"

**Workflow:**
1. Library: Prisma (ID: `/prisma/prisma`)
2. Topic: None (general overview)
3. Tokens: 15000 (comprehensive)
4. Call: `get-library-docs({ context7CompatibleLibraryID: "/prisma/prisma", tokens: 15000 })`

## Error Handling

### Library Not Found
```
Error: "Library ID not valid"
Solution: Use resolve-library-id to find correct ID
```

### Rate Limited
```
Error: "429 Too Many Requests"
Solution: Wait before retrying, reduce request frequency
```

### Timeout
```
Error: "Request timeout"
Solution: Reduce token count, specify narrower topic
```

## Related Workflows

- [Context Search Workflow](./context_search_workflow.md) - Finding library IDs
- [Context Management Workflow](./context_management_workflow.md) - Managing cached context

---

**Last Updated**: 2026-01-13
**Tool**: `get-library-docs`
**MCP Server**: Context7
