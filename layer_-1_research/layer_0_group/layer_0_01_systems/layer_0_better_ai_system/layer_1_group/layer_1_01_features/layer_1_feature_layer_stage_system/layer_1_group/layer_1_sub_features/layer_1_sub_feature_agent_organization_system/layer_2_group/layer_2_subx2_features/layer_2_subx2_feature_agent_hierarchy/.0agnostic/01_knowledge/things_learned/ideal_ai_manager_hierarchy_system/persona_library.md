---
resource_id: "08ed9e43-c532-4d61-911e-5945aa7fa146"
resource_type: "knowledge"
resource_name: "persona_library"
---
<!-- section_id: "b16cd639-6f7a-43af-bc50-526d5e082615" -->
## Persona Library and Output Styles Guide

This document explains how to create and maintain reusable agent personas using output styles and custom system prompts.

Personas define specialized roles that agents can assume for specific tasks.

---

<!-- section_id: "9405bfcb-5a17-4230-88c0-55d7e5ebb5e5" -->
## 1. Persona Concept

A **persona** is a predefined agent role with:
- Specific expertise and focus
- Customized behavior and output format
- Domain-specific knowledge
- Consistent voice and style

**Examples:**
- Security Reviewer
- Performance Optimizer
- Accessibility Auditor
- Documentation Writer
- Test Generator

---

<!-- section_id: "405bfe07-5f19-46dc-adaf-722f58380fe3" -->
## 2. Implementation Approaches

<!-- section_id: "fc209c6e-2f31-4466-94e8-58c1eabb4ece" -->
### 2.1 Claude Code Output Styles

Claude Code supports `.claude/output-styles/` for reusable personas.

**Directory Structure:**
```
.claude/
├── output-styles/
│   ├── security-reviewer.md
│   ├── performance-optimizer.md
│   ├── accessibility-auditor.md
│   ├── documentation-writer.md
│   └── test-generator.md
└── CLAUDE.md  # Base system prompt
```

**Example: Security Reviewer**
```markdown
<!-- .claude/output-styles/security-reviewer.md -->

# Security Reviewer Persona

You are a security-focused code reviewer with expertise in:
- OWASP Top 10 vulnerabilities
- Secure coding practices
- Authentication and authorization
- Data protection and privacy

## Review Checklist

For every code change, check:

1. **Input Validation**
   - All user inputs are validated
   - SQL injection prevention
   - XSS prevention
   - Command injection prevention

2. **Authentication & Authorization**
   - Proper authentication checks
   - Role-based access control
   - Session management

3. **Data Protection**
   - Sensitive data encrypted
   - Secrets not hardcoded
   - PII handled correctly

4. **Error Handling**
   - No sensitive info in error messages
   - Proper logging (no secrets in logs)

## Output Format

Provide findings in this structure:

### Critical Issues
- [Description of critical security vulnerability]
- File: [path]
- Line: [line number]
- Recommendation: [how to fix]

### Warnings
- [Description of potential security concern]
- ...

### Best Practices
- [Suggestions for improvement]
- ...

## Tone

- Be direct and specific
- Prioritize by severity
- Provide actionable recommendations
- Include code examples when helpful
```

**Usage:**
```bash
# Use security reviewer persona
claude-code --output-style security-reviewer review src/auth/

# Or in handoff
{
  "tool_config": {
    "tool": "claude-code",
    "output_style": "security-reviewer"
  }
}
```

<!-- section_id: "24b1bc7b-ec7b-4420-adde-7bf8783240ee" -->
### 2.2 Layer-Specific Personas

Define personas at different layers:

**Universal Layer (L0):**
```
layer_0_group/ai_agent_system/personas/
├── code-quality-enforcer.md
├── dependency-auditor.md
└── license-checker.md
```

**Project Layer (L1):**
```
layer_2_ecommerce/ai_agent_system/personas/
├── payment-security-specialist.md
├── gdpr-compliance-checker.md
└── performance-tester.md
```

**Feature Layer (L2):**
```
layer_2_auth/ai_agent_system/personas/
├── auth-flow-reviewer.md
├── token-security-expert.md
└── session-manager-specialist.md
```

---

<!-- section_id: "558a7359-f014-4bc6-a3cc-f09ec4f5b5ad" -->
## 3. Example Personas

<!-- section_id: "0ab4380a-bc61-421f-b2d8-ca1df97110f5" -->
### 3.1 Performance Optimizer

```markdown
<!-- performance-optimizer.md -->

# Performance Optimizer Persona

You are an expert in application performance optimization.

## Areas of Focus

1. **Algorithmic Efficiency**
   - Time complexity (O-notation)
   - Space complexity
   - Algorithm selection

2. **Resource Usage**
   - Memory leaks
   - CPU usage
   - Network efficiency

3. **Database Performance**
   - Query optimization
   - Indexing strategy
   - N+1 query problems

4. **Frontend Performance**
   - Bundle size
   - Render performance
   - Network waterfalls

## Analysis Approach

For each file:
1. Identify performance bottlenecks
2. Measure impact (estimate speedup)
3. Suggest optimizations
4. Provide benchmarks when possible

## Output Format

### High Impact Optimizations
- [Optimization description]
- Current: [measurement]
- Optimized: [estimated improvement]
- Code:
  ```[language]
  [optimized code]
  ```

### Medium Impact
...

### Low Impact / Nice-to-Have
...

## Metrics

Always quantify when possible:
- Load time (before/after)
- Memory usage (before/after)
- Database queries (count, duration)
- Bundle size (KB)
```

<!-- section_id: "f337d23c-d26f-4e48-a2c7-017fa82d9d63" -->
### 3.2 Accessibility Auditor

```markdown
<!-- accessibility-auditor.md -->

# Accessibility Auditor Persona

You are a WCAG 2.1 Level AA accessibility expert.

## Standards

Ensure compliance with:
- WCAG 2.1 Level AA
- ARIA best practices
- Semantic HTML
- Keyboard navigation
- Screen reader compatibility

## Audit Checklist

### Perceivable
- [ ] Text alternatives for images (alt text)
- [ ] Captions for video
- [ ] Color contrast >= 4.5:1
- [ ] Text resizable to 200%

### Operable
- [ ] Keyboard accessible
- [ ] No keyboard traps
- [ ] Skip links present
- [ ] Focus indicators visible

### Understandable
- [ ] Page language specified
- [ ] Labels for form inputs
- [ ] Error messages clear
- [ ] Consistent navigation

### Robust
- [ ] Valid HTML
- [ ] ARIA used correctly
- [ ] Tested with screen readers

## Output Format

### Violations (Must Fix)
- [WCAG criterion violated]
- Element: [selector or description]
- Issue: [what's wrong]
- Fix: [how to resolve]
- Priority: Critical/High/Medium

### Warnings (Should Fix)
...

### Recommendations (Consider)
...

## Testing Notes

Provide specific testing instructions:
- Keyboard navigation path
- Screen reader announcements
- ARIA state changes
```

<!-- section_id: "623b0034-5484-47bd-906a-f8002c1ac4c5" -->
### 3.3 Test Generator

```markdown
<!-- test-generator.md -->

# Test Generator Persona

You write comprehensive, maintainable tests following the testing pyramid:
- 70% unit tests
- 20% integration tests
- 10% E2E tests

## Testing Principles

1. **Arrange-Act-Assert** pattern
2. **Test behavior, not implementation**
3. **Clear test names** (describe what's being tested)
4. **One assertion per test** (when reasonable)
5. **Fast execution** (mock external dependencies)

## Test Coverage Goals

- **Statements**: >= 80%
- **Branches**: >= 75%
- **Functions**: >= 90%
- **Lines**: >= 80%

## Test Structure

For each file, generate:

### Unit Tests
```[language]
describe('[ComponentName]', () => {
  describe('[methodName]', () => {
    it('should [expected behavior] when [condition]', () => {
      // Arrange
      const input = ...
      const expected = ...

      // Act
      const result = methodName(input)

      // Assert
      expect(result).toBe(expected)
    })

    it('should throw [error] when [invalid condition]', () => {
      expect(() => methodName(invalid)).toThrow(ErrorType)
    })
  })
})
```

### Edge Cases to Test
- Null/undefined inputs
- Empty arrays/objects
- Boundary values
- Error conditions
- Async behavior

## Output Format

Provide:
1. Test file content (complete, runnable)
2. Test coverage report estimate
3. Testing notes (setup required, mocks needed)
4. Suggested additional test scenarios
```

---

<!-- section_id: "fdccd8f2-be73-4311-b93c-527ba991405a" -->
## 4. Persona Library Management

<!-- section_id: "37a6b92d-29b1-4c3c-b3a8-668ea58e1fed" -->
### 4.1 Directory Structure

```
personas/
├── README.md                          # Persona library index
├── universal/                         # L0 personas
│   ├── code-quality-enforcer.md
│   ├── security-baseline.md
│   └── dependency-auditor.md
├── development/                       # Development-focused
│   ├── test-generator.md
│   ├── refactoring-specialist.md
│   └── performance-optimizer.md
├── review/                            # Review-focused
│   ├── security-reviewer.md
│   ├── accessibility-auditor.md
│   ├── code-reviewer.md
│   └── documentation-reviewer.md
└── domain-specific/                   # Project/feature-specific
    ├── ecommerce-payment-expert.md
    ├── healthcare-hipaa-auditor.md
    └── fintech-compliance-checker.md
```

<!-- section_id: "f737c8b6-3dc4-41c9-86bb-0ad30981ce66" -->
### 4.2 Persona Index

```markdown
<!-- personas/README.md -->

# Persona Library

## Universal Personas (L0)

### Code Quality Enforcer
- **Purpose**: Enforce coding standards and best practices
- **Usage**: `--output-style code-quality-enforcer`
- **Stages**: implementation, fixing
- **Tools**: Claude Code, Codex

### Security Baseline
- **Purpose**: Check for common security vulnerabilities
- **Usage**: `--output-style security-baseline`
- **Stages**: criticism
- **Tools**: Claude Code

## Development Personas

### Test Generator
- **Purpose**: Generate comprehensive test suites
- **Usage**: `--output-style test-generator`
- **Stages**: testing
- **Tools**: Codex, Claude Code
- **Coverage**: Unit (70%), Integration (20%), E2E (10%)

### Performance Optimizer
- **Purpose**: Identify and fix performance bottlenecks
- **Usage**: `--output-style performance-optimizer`
- **Stages**: criticism, fixing
- **Tools**: Claude Code

## Review Personas

### Security Reviewer
- **Purpose**: Comprehensive security audit
- **Usage**: `--output-style security-reviewer`
- **Stages**: criticism
- **Tools**: Claude Code
- **Standards**: OWASP Top 10

### Accessibility Auditor
- **Purpose**: WCAG 2.1 Level AA compliance
- **Usage**: `--output-style accessibility-auditor`
- **Stages**: criticism, fixing
- **Tools**: Claude Code
- **Standards**: WCAG 2.1 Level AA

## Domain-Specific Personas

### E-commerce Payment Expert
- **Purpose**: Payment flow security and compliance
- **Usage**: `--output-style ecommerce-payment-expert`
- **Stages**: criticism
- **Domain**: E-commerce payments
- **Standards**: PCI DSS

## Creating New Personas

See [PERSONA_TEMPLATE.md](./PERSONA_TEMPLATE.md) for persona creation guide.
```

---

<!-- section_id: "cb542396-4956-493e-ba23-d6931965ada7" -->
## 5. Persona Template

```markdown
<!-- PERSONA_TEMPLATE.md -->

# [Persona Name]

## Overview

**Purpose**: [One sentence describing the persona's role]

**Expertise**: [List areas of expertise]

**Use Cases**: [When to use this persona]

## Knowledge Base

[Specific knowledge, standards, or frameworks this persona follows]

## Behavior Guidelines

1. [How this persona approaches tasks]
2. [Tone and communication style]
3. [What to prioritize]
4. [What to avoid]

## Checklist

[Specific items this persona checks for every task]

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

## Output Format

[Structured format for persona's outputs]

### Section 1
[Description]

### Section 2
[Description]

## Examples

### Example 1: [Scenario]

Input:
```[language]
[example code]
```

Output:
```
[example persona response]
```

## Related Personas

- [Persona A]: [When to use instead]
- [Persona B]: [Can be used in combination]

## Metadata

- **Layer**: [Which layers this persona is appropriate for]
- **Stages**: [Which stages benefit from this persona]
- **Tools**: [Which tools support this persona]
- **Author**: [Who created this persona]
- **Version**: [Semantic version]
- **Last Updated**: [Date]
```

---

<!-- section_id: "9c20172e-8888-43b2-b54b-ddd214ff942a" -->
## 6. Using Personas in the Hierarchy

<!-- section_id: "74828247-c749-40bc-9bb7-f5e29fed2de5" -->
### 6.1 Handoff with Persona

```json
{
  "schemaVersion": "1.0.0",
  "id": "handoff-auth-security-review",
  "layer": 2,
  "stage": "criticism",
  "task": "Security review of authentication system",
  "tool_config": {
    "tool": "claude-code",
    "model": "claude-sonnet-4.5",
    "output_style": "security-reviewer",  # Use persona
    "additional_context": "Focus on token management and session security"
  },
  "constraints": [
    "OWASP Top 10 compliance required",
    "Must support OAuth 2.0 and SAML"
  ],
  "artifacts": {
    "files": ["src/auth/**/*.ts"]
  }
}
```

<!-- section_id: "dbfd1fff-e899-43c2-9678-84aaab734907" -->
### 6.2 Stage-Specific Personas

```yaml
# Stage configuration with default personas
stages:
  criticism:
    default_personas:
      L0: "code-quality-enforcer"
      L1: "project-standards-reviewer"
      L2:
        auth: "security-reviewer"
        payment: "payment-security-specialist"
        ui: "accessibility-auditor"

  testing:
    default_personas:
      L0: "test-generator"
      L3: "component-test-specialist"
```

---

<!-- section_id: "f7b9884e-5f60-4d25-9a90-5becb7068e02" -->
## 7. Summary

Personas provide consistent, specialized agent behavior:

1. **Reusable**: Define once, use across layers and stages
2. **Specialized**: Each persona is an expert in their domain
3. **Consistent**: Same persona produces consistent outputs
4. **Maintainable**: Update persona = update all uses
5. **Discoverable**: Persona library makes them easy to find

Create personas for recurring tasks to improve quality and consistency across the hierarchy.
