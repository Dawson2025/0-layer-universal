---
resource_id: "94490a1a-e846-46f1-b095-f5084f61a08f"
resource_type: "document"
resource_name: "context_search_workflow"
---
# Context Search Workflow

This document describes the workflow for searching and resolving library identifiers using the Context7 MCP server.

<!-- section_id: "c2ff0d53-9bfc-4652-aa81-7cf524608421" -->
## Overview

The context search workflow is the entry point for using Context7. Before retrieving documentation for any library, you must first resolve its name to a Context7-compatible identifier. This workflow handles library discovery and ID resolution.

<!-- section_id: "d5de3cb6-5557-4957-9f5e-7f97e29fcce1" -->
## Prerequisites

- Context7 MCP server configured and running
- Valid `CONTEXT7_API_KEY` set
- Knowledge of the library/framework you want to search for

<!-- section_id: "08a35f78-8a8a-4f65-a1e6-01cfc2f33636" -->
## Workflow Steps

<!-- section_id: "48074b4b-c6c2-469d-b657-1e146abee6c8" -->
### Step 1: Identify Search Intent

Determine what library documentation you need:
- **Framework**: React, Vue, Angular, Next.js, etc.
- **Library**: lodash, axios, prisma, etc.
- **Runtime/Platform**: Node.js, Deno, Bun, etc.
- **Tool**: TypeScript, ESLint, Prettier, etc.

<!-- section_id: "07e4debf-7046-4893-b6ca-5059b2d9e457" -->
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

<!-- section_id: "133c4d9b-12c0-4e5b-9107-c835c4304224" -->
### Step 3: Execute Search

Use the `resolve-library-id` tool:

```
Tool: resolve-library-id
Input: {
  "libraryName": "react"
}
```

<!-- section_id: "adcbd7b8-2b93-468a-9912-c22272a03a55" -->
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

<!-- section_id: "964ec867-2a03-41e1-b07d-4a88d667a2ac" -->
### Step 5: Store Library ID

Once resolved, use the library ID for documentation retrieval:
- Store for session use
- Pass to `get-library-docs` tool
- Cache for repeated lookups

<!-- section_id: "786e729e-06ae-42ba-9a8c-a0b33c30dc86" -->
## Best Practices

<!-- section_id: "6c16f4aa-390e-41f7-97ed-504f8ba008af" -->
### 1. Start with Simple Names

Try the simplest form first:
```
"react"         // Good starting point
"reactjs"       // If above fails
"facebook/react" // If still not found
```

<!-- section_id: "689d4d25-cf34-407f-a937-eda10cc9fff8" -->
### 2. Handle Ambiguous Results

When multiple matches are returned:
1. Review all options
2. Select based on user's actual need
3. Confirm with user if unclear

<!-- section_id: "3b757175-bbd3-444a-8c12-29a49fab035c" -->
### 3. Cache Resolved IDs

Within a session:
- Store library IDs after first resolution
- Reuse for multiple documentation requests
- Avoid redundant API calls

<!-- section_id: "9334faae-7652-4729-b885-0f794434a26f" -->
### 4. Handle Not Found Gracefully

If library is not indexed:
1. Try alternative search terms
2. Check if library is in Context7's coverage
3. Fall back to general knowledge

<!-- section_id: "22ed4f97-f368-4462-988b-2ded06f93d5f" -->
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

<!-- section_id: "e15df340-a95c-4a15-b3c1-5805ac90b1b2" -->
## Search Term Strategies

<!-- section_id: "45df3d20-01d2-4c20-849b-95fe7d302b6d" -->
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

<!-- section_id: "08f3a537-68aa-48bc-bb70-e05096c7104d" -->
### By Organization

If library name is common, include organization:
```
vercel/next.js
facebook/react
prisma/prisma
tailwindlabs/tailwindcss
```

<!-- section_id: "3d177b8b-724d-4e42-be8e-9f722f3081fa" -->
### By Package Name

For npm packages with scoped names:
```
@tanstack/react-query
@trpc/server
@auth/core
```

<!-- section_id: "62b480df-260a-4a1c-b92e-25111a885d3c" -->
## Example Scenarios

<!-- section_id: "8efac117-3ee8-4a3e-979e-7702159b9947" -->
### Scenario 1: Finding React

**User Request:** "I need help with React hooks"

```
resolve-library-id({ libraryName: "react" })
Result: { id: "/facebook/react", ... }
```

<!-- section_id: "9def5948-ee92-4a0a-84c2-93fde32c9936" -->
### Scenario 2: Finding Next.js

**User Request:** "Show me Next.js 14 features"

```
resolve-library-id({ libraryName: "next.js" })
Result: { id: "/vercel/next.js", ... }
```

<!-- section_id: "a3ed4fb2-2b5e-4b10-adb1-402be2ee647e" -->
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

<!-- section_id: "7e79727b-86b6-49bb-9746-f08dae333baa" -->
### Scenario 4: Not Found

**User Request:** "Get docs for my-internal-lib"

```
resolve-library-id({ libraryName: "my-internal-lib" })
Result: No matches

Action: Inform user library is not indexed
- Suggest checking Context7 coverage
- Fall back to other documentation sources
```

<!-- section_id: "c0e87905-be06-4287-a7ed-dcb0f700b797" -->
## Error Handling

<!-- section_id: "bc668502-0da9-4f8d-8fe7-7a4ef4458a7b" -->
### No Results
```
Error: "No libraries found matching query"
Solution:
1. Try alternative names
2. Check spelling
3. Use more specific terms (org/repo)
```

<!-- section_id: "7458f30f-31f8-411d-8c2a-68e42e6c4bdf" -->
### API Error
```
Error: "Authentication failed"
Solution: Verify CONTEXT7_API_KEY is set correctly
```

<!-- section_id: "c6292d8f-a93b-4057-be8c-33e7503af386" -->
### Rate Limited
```
Error: "Rate limit exceeded"
Solution: Wait before retrying, cache results
```

<!-- section_id: "01d1a83b-9b6a-42a8-a85c-4264dcb43f52" -->
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

<!-- section_id: "5ad99794-ddb7-4858-ae89-036e69eeb381" -->
## Related Workflows

- [Context Retrieval Workflow](./context_retrieval_workflow.md) - Getting documentation
- [Context Management Workflow](./context_management_workflow.md) - Managing cached context

---

**Last Updated**: 2026-01-13
**Tool**: `resolve-library-id`
**MCP Server**: Context7
