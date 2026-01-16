# Horizontal Sibling Rules

## Conditions for Inclusion
1. Sibling is RELATED (shares dependencies, has cross-references)
2. Relationship is TASK-RELEVANT (affects current work)

## Examples
| Scenario | Include? | Why |
|----------|----------|-----|
| Working on auth, user feature exists | Yes | Auth uses user |
| Working on math, science exists | No | Not related |
| Working on feature, shared utility exists | Yes | Uses it |

## The Two-Condition Test

### Condition 1: Is the Sibling RELATED?
A sibling is related if:
- It shares dependencies with current entity
- It has explicit cross-references
- It provides utilities/services used by current entity
- It consumes outputs from current entity
- It is mentioned in current entity's documentation

### Condition 2: Is the Relationship RELEVANT to Current Task?
The relationship is relevant if:
- Current task involves the shared functionality
- Current task modifies interfaces between entities
- Current task requires understanding sibling behavior
- Current task affects sibling's dependencies

## Decision Matrix

```
                    RELATED?
                    Yes         No
RELEVANT?   Yes     INCLUDE     EXCLUDE
            No      EXCLUDE     EXCLUDE
```

Both conditions must be true for inclusion.

## Examples in Detail

### Example 1: Auth Feature Working on Login
- **Current**: auth feature
- **Sibling**: user feature
- **Task**: Implement login endpoint
- **Related?**: Yes (auth validates users)
- **Relevant?**: Yes (login needs user data)
- **Decision**: INCLUDE

### Example 2: Auth Feature Working on Token Refresh
- **Current**: auth feature
- **Sibling**: payment feature
- **Task**: Implement token refresh
- **Related?**: No (no direct relationship)
- **Relevant?**: No (token refresh doesn't involve payments)
- **Decision**: EXCLUDE

### Example 3: API Feature Adding Endpoint
- **Current**: api feature
- **Sibling**: database feature
- **Task**: Add new endpoint
- **Related?**: Yes (API uses database)
- **Relevant?**: Yes (endpoint queries database)
- **Decision**: INCLUDE

### Example 4: UI Feature Styling Button
- **Current**: ui feature
- **Sibling**: api feature
- **Task**: Change button color
- **Related?**: Yes (UI calls API)
- **Relevant?**: No (styling doesn't affect API)
- **Decision**: EXCLUDE

## Avoiding Context Pollution

Including unrelated siblings causes:
1. **Token Waste** - Consuming context window with irrelevant info
2. **Confusion** - AI may conflate unrelated concepts
3. **Slower Processing** - More context to process
4. **Wrong Decisions** - Irrelevant context may mislead

## Implementation Hints

When checking for relationships, look for:
- Import statements referencing sibling
- Shared configuration files
- Common interfaces or types
- Documentation cross-references
- Dependency declarations
