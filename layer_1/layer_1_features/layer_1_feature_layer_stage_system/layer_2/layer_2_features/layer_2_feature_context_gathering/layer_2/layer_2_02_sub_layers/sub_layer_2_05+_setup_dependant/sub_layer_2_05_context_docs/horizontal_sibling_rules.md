---
resource_id: "7e5d483e-5582-4cd4-b081-9ea172116280"
resource_type: "document"
resource_name: "horizontal_sibling_rules"
---
# Horizontal Sibling Rules

<!-- section_id: "cc5dea46-2e17-408a-95fc-55f95ab6f074" -->
## Conditions for Inclusion
1. Sibling is RELATED (shares dependencies, has cross-references)
2. Relationship is TASK-RELEVANT (affects current work)

<!-- section_id: "7ea50908-da9a-4637-abd1-ebc156eb97d2" -->
## Examples
| Scenario | Include? | Why |
|----------|----------|-----|
| Working on auth, user feature exists | Yes | Auth uses user |
| Working on math, science exists | No | Not related |
| Working on feature, shared utility exists | Yes | Uses it |

<!-- section_id: "c0bc9d73-5874-4bac-8d9a-e6fe86c360d5" -->
## The Two-Condition Test

<!-- section_id: "597b7eab-5b1b-4974-bd83-9bcb184e0902" -->
### Condition 1: Is the Sibling RELATED?
A sibling is related if:
- It shares dependencies with current entity
- It has explicit cross-references
- It provides utilities/services used by current entity
- It consumes outputs from current entity
- It is mentioned in current entity's documentation

<!-- section_id: "c7356b3f-0643-4e4c-bb69-8a4b89f416d5" -->
### Condition 2: Is the Relationship RELEVANT to Current Task?
The relationship is relevant if:
- Current task involves the shared functionality
- Current task modifies interfaces between entities
- Current task requires understanding sibling behavior
- Current task affects sibling's dependencies

<!-- section_id: "0c70103a-1be6-4b1b-8fc7-86b282d8810a" -->
## Decision Matrix

```
                    RELATED?
                    Yes         No
RELEVANT?   Yes     INCLUDE     EXCLUDE
            No      EXCLUDE     EXCLUDE
```

Both conditions must be true for inclusion.

<!-- section_id: "389d8520-1c0a-4455-9141-856d7cf1670d" -->
## Examples in Detail

<!-- section_id: "bcd50c36-4e8f-4a77-bb99-8fff22ee223d" -->
### Example 1: Auth Feature Working on Login
- **Current**: auth feature
- **Sibling**: user feature
- **Task**: Implement login endpoint
- **Related?**: Yes (auth validates users)
- **Relevant?**: Yes (login needs user data)
- **Decision**: INCLUDE

<!-- section_id: "94a2f639-40c2-4e8b-b01c-d587b149f511" -->
### Example 2: Auth Feature Working on Token Refresh
- **Current**: auth feature
- **Sibling**: payment feature
- **Task**: Implement token refresh
- **Related?**: No (no direct relationship)
- **Relevant?**: No (token refresh doesn't involve payments)
- **Decision**: EXCLUDE

<!-- section_id: "0b8ff49f-3d9e-4901-a7d3-7a8bd0513429" -->
### Example 3: API Feature Adding Endpoint
- **Current**: api feature
- **Sibling**: database feature
- **Task**: Add new endpoint
- **Related?**: Yes (API uses database)
- **Relevant?**: Yes (endpoint queries database)
- **Decision**: INCLUDE

<!-- section_id: "08a7c373-8f8b-4d93-80fb-dc88fbbccf88" -->
### Example 4: UI Feature Styling Button
- **Current**: ui feature
- **Sibling**: api feature
- **Task**: Change button color
- **Related?**: Yes (UI calls API)
- **Relevant?**: No (styling doesn't affect API)
- **Decision**: EXCLUDE

<!-- section_id: "7e64f35a-4f19-4f0d-be40-042d85f55e86" -->
## Avoiding Context Pollution

Including unrelated siblings causes:
1. **Token Waste** - Consuming context window with irrelevant info
2. **Confusion** - AI may conflate unrelated concepts
3. **Slower Processing** - More context to process
4. **Wrong Decisions** - Irrelevant context may mislead

<!-- section_id: "e6afe3dc-a2c8-4316-9d8f-4adbc278d82f" -->
## Implementation Hints

When checking for relationships, look for:
- Import statements referencing sibling
- Shared configuration files
- Common interfaces or types
- Documentation cross-references
- Dependency declarations
