---
resource_id: "8eb98add-22c4-47c3-8ed3-1ff8759c7b0c"
resource_type: "document"
resource_name: "fact-checking-workflow"
---
# Fact-Checking Workflow

## Overview

This protocol defines a rigorous methodology for verifying claims, validating information, and assessing source reliability using the Tavily MCP server. It provides structured approaches for confirming accuracy of technical documentation, user-provided information, and web content.

## When to Use

- Verifying technical claims before implementation
- Confirming accuracy of documentation
- Validating user-provided specifications
- Cross-referencing conflicting information
- Assessing credibility of sources
- Checking current status of deprecated features

## Core Principles

### The Three-Source Rule

No fact should be considered verified unless confirmed by at least three independent, authoritative sources.

### Source Independence

Sources must be genuinely independent:
- Different organizations/authors
- Not citing each other
- Different methodologies or perspectives

### Recency Verification

Information accuracy depends on timeliness:
- Technical facts: Verify within last 12 months
- API/Library info: Verify within last 6 months
- Security info: Verify within last 30 days

## Verification Workflow

### Phase 1: Claim Identification

Break down the information to verify into discrete, testable claims:

```markdown
Original Statement:
"React 18 introduced automatic batching and concurrent rendering,
making it 30% faster than React 17"

Discrete Claims:
1. React 18 introduced automatic batching
2. React 18 introduced concurrent rendering
3. React 18 is 30% faster than React 17
```

### Phase 2: Initial Verification Search

For each claim, conduct an initial search:

```
Tool: tavily_search
Parameters:
  query: "[claim as searchable phrase]"
  search_depth: basic
  max_results: 5
  include_answer: true
```

### Phase 3: Source Authority Assessment

Evaluate each source found:

```markdown
## Source Evaluation Criteria

| Criterion | Questions to Ask |
|-----------|------------------|
| Authority | Is this an official source? Expert author? |
| Currency | When was this published? Still accurate? |
| Accuracy | Can claims be verified elsewhere? |
| Purpose | Is there bias? Commercial interest? |
| Coverage | Is information complete or partial? |
```

### Phase 4: Cross-Verification

Search for the same information using different approaches:

```
Search 1: Direct claim search
  Query: "[exact claim]"

Search 2: Official documentation
  Query: "[topic] official documentation"
  include_domains: [official sites]

Search 3: Counter-claim search
  Query: "[claim] not true myth"

Search 4: Expert discussion
  Query: "[claim] explanation analysis"
```

### Phase 5: Conflict Resolution

When sources conflict:

1. **Identify the conflict type**
   - Factual disagreement
   - Outdated vs. current information
   - Different contexts or scopes
   - Misinterpretation or nuance

2. **Weight sources by authority**
   - Official documentation > third-party
   - Primary sources > secondary sources
   - Recent > older (for technical content)

3. **Search for resolution**
   ```
   Query: "[conflicting topic] clarification explanation"
   Query: "[topic] common misconception"
   ```

### Phase 6: Verification Report

Document findings in structured format:

```markdown
# Verification Report

## Claim: [Statement being verified]

## Verdict: [VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / FALSE]

## Evidence

### Supporting Sources
1. [Source 1]: [URL] - [Key quote or summary]
2. [Source 2]: [URL] - [Key quote or summary]
3. [Source 3]: [URL] - [Key quote or summary]

### Contradicting Sources (if any)
1. [Source]: [URL] - [Contradiction explanation]

## Confidence Level: [HIGH / MEDIUM / LOW]

## Notes
[Any caveats, context, or nuances]

## Verification Date: [Date]
```

## Verification Patterns

### Pattern: Technical Claim Verification

```
Step 1: Search official documentation
  Query: "[technology] [feature] documentation"
  include_domains: [official docs site]

Step 2: Search community confirmation
  Query: "[technology] [feature] example"
  include_domains: [github.com, stackoverflow.com]

Step 3: Search for known issues
  Query: "[technology] [feature] issue bug"

Step 4: Check version-specific accuracy
  Query: "[technology] [version] [feature]"
```

### Pattern: Version/Deprecation Verification

```
Step 1: Official changelog
  Query: "[technology] changelog release notes [version]"

Step 2: Deprecation notices
  Query: "[technology] [feature] deprecated"

Step 3: Migration guides
  Query: "[technology] [feature] migration upgrade"

Step 4: Current status
  Query: "[technology] [feature] [current year]"
```

### Pattern: Performance Claim Verification

```
Step 1: Official benchmarks
  Query: "[technology] official benchmark performance"

Step 2: Independent benchmarks
  Query: "[technology] benchmark comparison"
  exclude_domains: [technology's official site]

Step 3: Methodology review
  Query: "[technology] benchmark methodology"

Step 4: Real-world validation
  Query: "[technology] production performance"
```

### Pattern: Security Claim Verification

```
Step 1: Official security advisories
  Query: "[technology] security advisory CVE"
  include_domains: [official sites, cve.mitre.org]

Step 2: Security research
  Query: "[technology] security analysis"
  include_domains: [security blogs, research sites]

Step 3: Patch status
  Query: "[technology] [vulnerability] patch fix"

Step 4: Current threat status
  Query: "[technology] security [current year]"
  days: 30 (use news search)
```

## Source Authority Rankings

### Tier 1: Primary/Official Sources

```json
{
  "include_domains": [
    "docs.python.org",
    "developer.mozilla.org",
    "nodejs.org",
    "reactjs.org",
    "kubernetes.io",
    "docker.com"
  ]
}
```

Characteristics:
- Official project documentation
- Primary source material
- Direct from maintainers

### Tier 2: Expert/Institutional Sources

```json
{
  "include_domains": [
    "github.com",
    "stackoverflow.com",
    "infoq.com",
    "martinfowler.com",
    "blog.google"
  ]
}
```

Characteristics:
- Recognized experts
- Peer-reviewed or heavily scrutinized
- Technical depth

### Tier 3: Community/Educational Sources

```json
{
  "include_domains": [
    "dev.to",
    "hashnode.com",
    "freecodecamp.org",
    "css-tricks.com"
  ]
}
```

Characteristics:
- Community contributions
- Educational focus
- Variable quality

### Tier 4: General Sources

Use with caution:
- News sites
- General tech blogs
- Social media references

## Red Flags for False Information

### Content Red Flags

| Red Flag | Description |
|----------|-------------|
| No citations | Claims without sources |
| Single source | Only one reference exists |
| Outdated dates | Old information presented as current |
| Extreme claims | "Always", "never", "100%" |
| Contradiction | Conflicts with known facts |

### Source Red Flags

| Red Flag | Description |
|----------|-------------|
| Anonymous author | No accountability |
| Commercial bias | Selling related product |
| No updates | Site not maintained |
| Copied content | Duplicated from elsewhere |
| SEO spam | Keyword-stuffed content |

## Verification Decision Matrix

```
                    Source Authority
                    High    Medium    Low
                   +-------+--------+------+
Evidence    High   | VERIFY| VERIFY | CHECK|
Agreement   Medium | VERIFY| CHECK  | DOUBT|
            Low    | CHECK | DOUBT  | REJECT|
                   +-------+--------+------+

VERIFY: Claim can be considered verified
CHECK: Additional verification needed
DOUBT: Treat with skepticism
REJECT: Do not rely on claim
```

## Common Verification Scenarios

### Scenario: Verifying Library Compatibility

```
Claim: "Library X is compatible with Framework Y version 3.0"

Verification Steps:
1. Check Library X's official compatibility matrix
2. Search for Framework Y 3.0 support in Library X changelog
3. Find GitHub issues or discussions about compatibility
4. Look for working examples or tutorials
5. Check npm/pip dependencies for version constraints

Search Queries:
- "[Library X] [Framework Y] 3.0 compatibility"
- "[Library X] peer dependencies"
- "[Library X] [Framework Y] 3.0 issue"
- "[Library X] supported [Framework Y] versions"
```

### Scenario: Verifying Best Practice Claims

```
Claim: "You should always use X pattern for Y problem"

Verification Steps:
1. Find the origin of this recommendation
2. Search for authoritative sources recommending this
3. Look for counter-arguments or alternatives
4. Check if context matters (when NOT to use)
5. Verify with official style guides or documentation

Search Queries:
- "[X pattern] [Y problem] best practice"
- "[Y problem] recommended approach official"
- "[X pattern] when not to use"
- "[Y problem] alternatives to [X pattern]"
```

### Scenario: Verifying Statistics/Numbers

```
Claim: "Technology X is 50% faster than Y"

Verification Steps:
1. Find the original benchmark source
2. Verify benchmark methodology
3. Check for independent replication
4. Look for conflicting benchmarks
5. Understand test conditions and limitations

Search Queries:
- "[Technology X] vs [Technology Y] benchmark"
- "[Technology X] performance claim methodology"
- "[Technology X] speed independent test"
- "[original claim source] benchmark criticism"
```

## Output Templates

### Quick Verification Summary

```markdown
## Claim: [Statement]
## Status: [VERIFIED/UNVERIFIED/FALSE]
## Confidence: [HIGH/MEDIUM/LOW]
## Key Source: [Most authoritative URL]
## Verified: [Date]
```

### Detailed Verification Report

```markdown
# Fact-Check Report

## Subject
[Topic or claim being investigated]

## Claims Analyzed
1. [Claim 1] - [VERIFIED/UNVERIFIED/FALSE]
2. [Claim 2] - [VERIFIED/UNVERIFIED/FALSE]

## Methodology
- Sources consulted: [Number]
- Search depth: [Basic/Advanced]
- Time period: [Date range]

## Findings

### Claim 1: [Statement]
**Verdict:** [VERDICT]
**Evidence:**
- [Source 1]: [Summary]
- [Source 2]: [Summary]
**Confidence:** [Level]

### Claim 2: [Statement]
...

## Overall Assessment
[Summary of verification findings]

## Caveats
[Any limitations or uncertainties]

## Sources
[Full list of URLs consulted]
```

## Troubleshooting Verification

| Issue | Solution |
|-------|----------|
| No sources found | Rephrase claim, broaden search |
| All sources point to same origin | Look for independent verification |
| Sources conflict | Weight by authority, check dates |
| Information seems outdated | Add year to search, use news search |
| Official docs unclear | Search for explanatory articles |
| Claim too specific | Break into smaller verifiable parts |
