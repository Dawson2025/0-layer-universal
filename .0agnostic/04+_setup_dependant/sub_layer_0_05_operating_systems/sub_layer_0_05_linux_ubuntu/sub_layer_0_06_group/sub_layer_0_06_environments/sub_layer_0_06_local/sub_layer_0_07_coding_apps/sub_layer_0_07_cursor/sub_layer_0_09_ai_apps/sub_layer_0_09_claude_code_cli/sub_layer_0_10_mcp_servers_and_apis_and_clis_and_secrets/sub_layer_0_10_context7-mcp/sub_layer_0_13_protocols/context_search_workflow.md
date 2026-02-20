# Context Search Workflow

This document describes the workflow for searching and resolving library identifiers using the Context7 MCP server.

## Overview

The context search workflow is the entry point for using Context7. Before retrieving documentation for any library, you must first resolve its name to a Context7-compatible identifier. This workflow handles library discovery and ID resolution.

## Prerequisites

- Context7 MCP server configured and running
- Valid `CONTEXT7_API_KEY` set
- Knowledge of the library/framework you want to search for

## Workflow Steps

### Step 1: Identify Search Intent

Determine what library documentation you need:
- **Framework**: React, Vue, Angular, Next.js, etc.
- **Library**: lodash, axios, prisma, etc.
- **Runtime/Platform**: Node.js, Deno, Bun, etc.
- **Tool**: TypeScript, ESLint, Prettier, etc.

### Step 2: Formulate Search Query

Prepare your search term:
- Use the common name of the library
- Include organization if known
- Try npm package name if standard name fails

**Good Search Terms:**
- `react`
- `next.js`
- `prisma`
- `tailwindcss`
- `express`

**Alternative Search Terms (if primary fails):**
- `@types/react` (for TypeScript types)
- `facebook/react` (with organization)
- `vercel/next.js` (full repo path)

### Step 3: Execute Search

Use the `resolve-library-id` tool:

```
Tool: resolve-library-id
Input: {
  "libraryName": "react"
}
```

### Step 4: Process Results

The tool returns matching libraries with their Context7 IDs:

**Successful Response:**
```json
{
  "matches": [
    {
      "id": "/facebook/react",
      "name": "React",
      "description": "A JavaScript library for building user interfaces",
      "version": "18.2.0"
    }
  ]
}
```

**Multiple Matches:**
When multiple libraries match, select the most relevant:
```json
{
  "matches": [
    { "id": "/facebook/react", "name": "React" },
    { "id": "/preactjs/preact", "name": "Preact" },
    { "id": "/facebook/react-native", "name": "React Native" }
  ]
}
```

### Step 5: Store Library ID

Once resolved, use the library ID for documentation retrieval:
- Store for session use
- Pass to `get-library-docs` tool
- Cache for repeated lookups

## Best Practices

### 1. Start with Simple Names

Try the simplest form first:
```
"react"         // Good starting point
"reactjs"       // If above fails
"facebook/react" // If still not found
```

### 2. Handle Ambiguous Results

When multiple matches are returned:
1. Review all options
2. Select based on user's actual need
3. Confirm with user if unclear

### 3. Cache Resolved IDs

Within a session:
- Store library IDs after first resolution
- Reuse for multiple documentation requests
- Avoid redundant API calls

### 4. Handle Not Found Gracefully

If library is not indexed:
1. Try alternative search terms
2. Check if library is in Context7's coverage
3. Fall back to general knowledge

## Workflow Diagram

```
[User Mentions Library]
         |
         v
[Extract Library Name]
         |
         v
[Call resolve-library-id]
         |
         v
[Results Found?] --No--> [Try Alternative Terms]
         |                        |
        Yes                       v
         |               [Still Not Found?]
         v                        |
[Single Match?] --No--> [Select Best Match]
         |                        |
        Yes                       |
         |<-----------------------+
         v
[Store Library ID]
         |
         v
[Proceed to Retrieval Workflow]
```

## Search Term Strategies

### By Category

**Frontend Frameworks:**
```
react, vue, angular, svelte, solid
```

**Backend Frameworks:**
```
express, fastify, koa, nestjs, hono
```

**Full-Stack Frameworks:**
```
next.js, nuxt, remix, sveltekit
```

**Databases/ORMs:**
```
prisma, drizzle, sequelize, mongoose
```

**CSS/Styling:**
```
tailwindcss, styled-components, emotion
```

**Build Tools:**
```
vite, webpack, esbuild, rollup
```

### By Organization

If library name is common, include organization:
```
vercel/next.js
facebook/react
prisma/prisma
tailwindlabs/tailwindcss
```

### By Package Name

For npm packages with scoped names:
```
@tanstack/react-query
@trpc/server
@auth/core
```

## Example Scenarios

### Scenario 1: Finding React

**User Request:** "I need help with React hooks"

```
resolve-library-id({ libraryName: "react" })
Result: { id: "/facebook/react", ... }
```

### Scenario 2: Finding Next.js

**User Request:** "Show me Next.js 14 features"

```
resolve-library-id({ libraryName: "next.js" })
Result: { id: "/vercel/next.js", ... }
```

### Scenario 3: Ambiguous Search

**User Request:** "I need query library docs"

```
resolve-library-id({ libraryName: "query" })
Results: Multiple matches
- /tanstack/react-query (React Query)
- /trpc/trpc (tRPC)
- /graphql/graphql-js (GraphQL)

Action: Ask user to clarify which query library
```

### Scenario 4: Not Found

**User Request:** "Get docs for my-internal-lib"

```
resolve-library-id({ libraryName: "my-internal-lib" })
Result: No matches

Action: Inform user library is not indexed
- Suggest checking Context7 coverage
- Fall back to other documentation sources
```

## Error Handling

### No Results
```
Error: "No libraries found matching query"
Solution:
1. Try alternative names
2. Check spelling
3. Use more specific terms (org/repo)
```

### API Error
```
Error: "Authentication failed"
Solution: Verify CONTEXT7_API_KEY is set correctly
```

### Rate Limited
```
Error: "Rate limit exceeded"
Solution: Wait before retrying, cache results
```

## Common Library IDs Reference

Quick reference for frequently searched libraries:

| Library | Search Term | Context7 ID |
|---------|-------------|-------------|
| React | react | /facebook/react |
| Next.js | next.js | /vercel/next.js |
| Vue | vue | /vuejs/vue |
| Angular | angular | /angular/angular |
| Svelte | svelte | /sveltejs/svelte |
| Express | express | /expressjs/express |
| Prisma | prisma | /prisma/prisma |
| Tailwind CSS | tailwindcss | /tailwindlabs/tailwindcss |
| TypeScript | typescript | /microsoft/TypeScript |

*Note: IDs may vary. Always use resolve-library-id for accurate current IDs.*

## Related Workflows

- [Context Retrieval Workflow](./context_retrieval_workflow.md) - Getting documentation
- [Context Management Workflow](./context_management_workflow.md) - Managing cached context

---

**Last Updated**: 2026-01-13
**Tool**: `resolve-library-id`
**MCP Server**: Context7
