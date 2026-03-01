# Context Priority Rules

**Purpose**: Define how context from different layers is prioritized and how overrides work.

---

## Core Principle: Inheritance with Override

```
Lower layers provide the base.
Higher layers inherit and can override.
```

This is standard inheritance - like classes in programming where child classes inherit from parents but can override methods.

---

## Layer Hierarchy

```
layer_-1 (research)     ← Experimental, inherits layer_0, can override most things
     ↑
layer_0 (universal)     ← Base layer, provides defaults for everything
     ↑
layer_1 (projects)      ← Project-specific, inherits layer_0, can override
     ↑
layer_2+ (features)     ← Deeper nesting, inherits all above, can override
```

**Direction of inheritance**: Higher-numbered layers inherit from lower-numbered layers.

**Direction of override**: Higher-numbered layers can override lower-numbered layers.

---

## Precedence Rules

### Rule 1: Higher Layer Can Override Lower

A rule in layer_1 can override a rule in layer_0.

```markdown
# In layer_0/rules/git_commit_rule.md
Use conventional commit format: type(scope): message

# In layer_1/project_x/CLAUDE.md
@override layer_0/rules/git_commit_rule.md
Use project-specific format: [JIRA-123] message
```

Result: In project_x, use JIRA format. Everywhere else, use conventional commits.

### Rule 2: Later in Chain Overrides Earlier

Within the same layer, files loaded later override files loaded earlier.

```
~/.claude/CLAUDE.md          ← Loaded first
~/project/CLAUDE.md          ← Loaded second, can override
~/project/CLAUDE.local.md    ← Loaded last, highest precedence
```

### Rule 3: CLAUDE.local.md Wins

`CLAUDE.local.md` files are for personal preferences and have highest precedence within their scope.

### Rule 4: Explicit Override Preferred

Use `@override` marker to make overrides explicit and documented.

```markdown
@override ../layer_0/rules/some_rule.md
Reason: This project requires different behavior because [reason].

[New rule content]
```

---

## What CAN Be Overridden

| Category | Can Override? | Notes |
|----------|---------------|-------|
| Coding style rules | Yes | Projects may have different styles |
| Commit message format | Yes | Teams may use different formats |
| Documentation format | Yes | Projects may have different standards |
| Workflow preferences | Yes | Teams work differently |
| Tool preferences | Yes | Different projects, different tools |
| Knowledge references | Yes | Projects have specific knowledge |

---

## What SHOULD NOT Be Overridden (Without Good Reason)

| Category | Override? | Notes |
|----------|-----------|-------|
| Security governance | Rarely | Safety rules exist for protection |
| AI Context Modification Protocol | Rarely | Prevents accidental damage |
| File path linking rule | Rarely | Usability feature |
| Research and sources practice | Rarely | Ensures quality |

These CAN technically be overridden, but doing so requires a documented reason.

---

## Override Syntax

### Explicit Override (Recommended)

```markdown
@override [path/to/original/rule.md]
Reason: [Why this override is needed]

[New content]
```

### Implicit Override (Less Clear)

Simply defining a rule with the same name in a higher layer will override, but this is less clear to future agents and humans.

---

## Conflict Resolution

When the same thing is defined differently in multiple places:

1. **Check layer numbers**: Higher layer wins
2. **Check position in chain**: Later file wins
3. **Check for @override marker**: Explicit override wins
4. **If still unclear**: Ask user

### Example Conflict

```
layer_0/rules/style.md: Use 2-space indentation
layer_1/project/style.md: Use 4-space indentation
```

Resolution: In layer_1/project, use 4-space. In layer_0 contexts, use 2-space.

---

## Recording Overrides

When an override is applied, record it:

```
ctx:ContextLoadingStateActor.overrides += {
  overridingFile: "layer_1/project/CLAUDE.md",
  overriddenFile: "layer_0/rules/git_commit_rule.md",
  what: "commit message format",
  reason: "Project uses JIRA ticket format"
}
```

This creates transparency about what's been overridden.

---

## Scope of Overrides

Overrides only apply within their scope:

| Override Location | Applies To |
|-------------------|------------|
| layer_1/project_a/ | Only project_a and its children |
| layer_1/project_b/ | Only project_b and its children |
| layer_0/ | All layers (but can be overridden) |

An override in project_a does NOT affect project_b.

---

## Related Documentation

- `context_loading_protocol.md` - How context is loaded
- `context_scope_boundaries.md` - What context applies where
- `context_agents/` - Agent implementations
