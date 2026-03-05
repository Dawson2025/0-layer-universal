---
resource_id: "676d8b96-ea69-4035-944a-1af187534f25"
resource_type: "knowledge"
resource_name: "horizontal_sibling_rules"
---
# Horizontal Sibling Rules

<!-- section_id: "a6f39f4f-7bd4-4a36-87f6-bfe5ab6b238f" -->
## Conditions for Inclusion
1. Sibling is RELATED (shares dependencies, has cross-references)
2. Relationship is TASK-RELEVANT (affects current work)

<!-- section_id: "f947d10d-f959-4235-88bb-3e69afc46035" -->
## Examples
| Scenario | Include? | Why |
|----------|----------|-----|
| Working on auth, user feature exists | Yes | Auth uses user |
| Working on math, science exists | No | Not related |
| Working on feature, shared utility exists | Yes | Uses it |

<!-- section_id: "cd4c99eb-a953-4628-8164-268a8c9f5b66" -->
## The Two-Condition Test

<!-- section_id: "40b4ed23-aa67-4c61-ab0c-e6c7e15bc4b8" -->
### Condition 1: Is the Sibling RELATED?
A sibling is related if:
- It shares dependencies with current entity
- It has explicit cross-references
- It provides utilities/services used by current entity
- It consumes outputs from current entity
- It is mentioned in current entity's documentation

<!-- section_id: "dfda222b-ad94-479a-8452-22d6d198dc5a" -->
### Condition 2: Is the Relationship RELEVANT to Current Task?
The relationship is relevant if:
- Current task involves the shared functionality
- Current task modifies interfaces between entities
- Current task requires understanding sibling behavior
- Current task affects sibling's dependencies

<!-- section_id: "5f31f2d1-5712-4afb-98b3-563ba6a06024" -->
## Decision Matrix

```
                    RELATED?
                    Yes         No
RELEVANT?   Yes     INCLUDE     EXCLUDE
            No      EXCLUDE     EXCLUDE
```

Both conditions must be true for inclusion.

<!-- section_id: "03122e30-1741-4af5-83d1-8d2214b2697f" -->
## Examples in Detail

<!-- section_id: "323d701a-f718-49ff-846c-2e4f1c1f1878" -->
### Example 1: Auth Feature Working on Login
- **Current**: auth feature
- **Sibling**: user feature
- **Task**: Implement login endpoint
- **Related?**: Yes (auth validates users)
- **Relevant?**: Yes (login needs user data)
- **Decision**: INCLUDE

<!-- section_id: "eb7be134-54bb-4c24-9abd-825804bb6486" -->
### Example 2: Auth Feature Working on Token Refresh
- **Current**: auth feature
- **Sibling**: payment feature
- **Task**: Implement token refresh
- **Related?**: No (no direct relationship)
- **Relevant?**: No (token refresh doesn't involve payments)
- **Decision**: EXCLUDE

<!-- section_id: "6cb7b6d1-be7d-4999-8aa5-d7da23a60c58" -->
### Example 3: API Feature Adding Endpoint
- **Current**: api feature
- **Sibling**: database feature
- **Task**: Add new endpoint
- **Related?**: Yes (API uses database)
- **Relevant?**: Yes (endpoint queries database)
- **Decision**: INCLUDE

<!-- section_id: "eaf10d08-21e8-48b0-94cb-e5374b3cadda" -->
### Example 4: UI Feature Styling Button
- **Current**: ui feature
- **Sibling**: api feature
- **Task**: Change button color
- **Related?**: Yes (UI calls API)
- **Relevant?**: No (styling doesn't affect API)
- **Decision**: EXCLUDE

<!-- section_id: "4a51e67b-fbc8-4856-bef5-51ef48d483a3" -->
## Avoiding Context Pollution

Including unrelated siblings causes:
1. **Token Waste** - Consuming context window with irrelevant info
2. **Confusion** - AI may conflate unrelated concepts
3. **Slower Processing** - More context to process
4. **Wrong Decisions** - Irrelevant context may mislead

<!-- section_id: "8493c5b6-80ee-4b94-a9e7-a3f5f0f97715" -->
## Implementation Hints

When checking for relationships, look for:
- Import statements referencing sibling
- Shared configuration files
- Common interfaces or types
- Documentation cross-references
- Dependency declarations
