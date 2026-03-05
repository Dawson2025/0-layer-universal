---
resource_id: "b0b17b27-f5a4-411b-8a09-de73f346e056"
resource_type: "rule"
resource_name: "context_priority_rules"
---
# Context Priority Rules

**Purpose**: Define how context from different layers is prioritized and how overrides work.

---

<!-- section_id: "d3cd3b41-43aa-492a-9d49-a86055696dee" -->
## Core Principle: Inheritance with Override

```
Lower layers provide the base.
Higher layers inherit and can override.
```

This is standard inheritance - like classes in programming where child classes inherit from parents but can override methods.

---

<!-- section_id: "95f47ed2-4ef4-45a2-bfad-99f6b409fc3a" -->
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

<!-- section_id: "44a3d8b3-1f0e-49ea-968d-1db03028e8a3" -->
## Precedence Rules

<!-- section_id: "126eefd7-5a63-4764-aaba-990e7859bcc3" -->
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

<!-- section_id: "fcee8987-ead7-4f0b-a3ce-301095ea7a3d" -->
### Rule 2: Later in Chain Overrides Earlier

Within the same layer, files loaded later override files loaded earlier.

```
~/.claude/CLAUDE.md          ← Loaded first
~/project/CLAUDE.md          ← Loaded second, can override
~/project/CLAUDE.local.md    ← Loaded last, highest precedence
```

<!-- section_id: "979cf630-05d5-4838-b38b-5556575a676a" -->
### Rule 3: CLAUDE.local.md Wins

`CLAUDE.local.md` files are for personal preferences and have highest precedence within their scope.

<!-- section_id: "549ac31b-1634-4db6-9450-5696e28c8953" -->
### Rule 4: Explicit Override Preferred

Use `@override` marker to make overrides explicit and documented.

```markdown
@override ../layer_0/rules/some_rule.md
Reason: This project requires different behavior because [reason].

[New rule content]
```

---

<!-- section_id: "6601e0ae-b3b1-4073-bd4c-ac5253e1f3a9" -->
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

<!-- section_id: "e08f8546-5da9-460d-985d-02479eb718b1" -->
## What SHOULD NOT Be Overridden (Without Good Reason)

| Category | Override? | Notes |
|----------|-----------|-------|
| Security governance | Rarely | Safety rules exist for protection |
| AI Context Modification Protocol | Rarely | Prevents accidental damage |
| File path linking rule | Rarely | Usability feature |
| Research and sources practice | Rarely | Ensures quality |

These CAN technically be overridden, but doing so requires a documented reason.

---

<!-- section_id: "d9c58d4f-e580-4aee-871d-dbf249adaef5" -->
## Override Syntax

<!-- section_id: "e9bedbc9-8015-4902-bd35-5b9cceeb13a1" -->
### Explicit Override (Recommended)

```markdown
@override [path/to/original/rule.md]
Reason: [Why this override is needed]

[New content]
```

<!-- section_id: "e5cafa49-1f35-4bac-b1c4-7e0db1f3e4d6" -->
### Implicit Override (Less Clear)

Simply defining a rule with the same name in a higher layer will override, but this is less clear to future agents and humans.

---

<!-- section_id: "e31a0dff-5874-418a-bca1-165c3d92d373" -->
## Conflict Resolution

When the same thing is defined differently in multiple places:

1. **Check layer numbers**: Higher layer wins
2. **Check position in chain**: Later file wins
3. **Check for @override marker**: Explicit override wins
4. **If still unclear**: Ask user

<!-- section_id: "4ffc7030-220a-4592-a5d0-8355ae620a7e" -->
### Example Conflict

```
layer_0/rules/style.md: Use 2-space indentation
layer_1/project/style.md: Use 4-space indentation
```

Resolution: In layer_1/project, use 4-space. In layer_0 contexts, use 2-space.

---

<!-- section_id: "35bfc1a2-135e-4cc2-a0b8-8336562d9afa" -->
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

<!-- section_id: "060b75ce-4c32-44ca-838c-8a947c1d5aae" -->
## Scope of Overrides

Overrides only apply within their scope:

| Override Location | Applies To |
|-------------------|------------|
| layer_1/project_a/ | Only project_a and its children |
| layer_1/project_b/ | Only project_b and its children |
| layer_0/ | All layers (but can be overridden) |

An override in project_a does NOT affect project_b.

---

<!-- section_id: "56e10832-8243-4295-898e-8cb3d821d4bd" -->
## Related Documentation

- `context_loading_protocol.md` - How context is loaded
- `context_scope_boundaries.md` - What context applies where
- `context_agents/` - Agent implementations
