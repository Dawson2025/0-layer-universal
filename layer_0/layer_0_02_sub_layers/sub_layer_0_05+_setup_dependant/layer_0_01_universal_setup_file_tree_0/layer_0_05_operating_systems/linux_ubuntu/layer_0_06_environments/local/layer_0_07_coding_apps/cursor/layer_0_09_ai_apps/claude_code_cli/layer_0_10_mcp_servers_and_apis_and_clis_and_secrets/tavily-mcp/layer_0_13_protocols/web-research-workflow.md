# Web Research Workflow

## Overview

This protocol defines a structured approach for conducting comprehensive web research using the Tavily MCP server. It provides a systematic methodology for gathering, validating, and synthesizing information from web sources.

## When to Use

- Deep-dive research on technical topics
- Competitive analysis and market research
- Documentation gathering for development decisions
- Learning about new technologies or frameworks
- Gathering requirements or specifications

## Workflow Steps

### Phase 1: Define Research Scope

Before starting searches, clearly define:

1. **Primary Question**: What specific question needs answering?
2. **Scope Boundaries**: What aspects are in/out of scope?
3. **Quality Criteria**: What sources are authoritative?
4. **Deliverable Format**: How should findings be presented?

**Example Scope Definition:**
```
Question: What are the best practices for implementing OAuth 2.0 in Node.js?
In Scope: Security considerations, library options, implementation patterns
Out of Scope: OAuth 1.0, other languages, enterprise SSO solutions
Authoritative Sources: Official docs, security blogs, major tech companies
Deliverable: Summary document with code examples
```

### Phase 2: Initial Broad Search

Execute a broad search to understand the landscape:

```
Tool: tavily_search
Parameters:
  query: "[primary topic] overview guide"
  search_depth: basic
  max_results: 10
  include_answer: true
```

**Purpose:**
- Identify key subtopics
- Discover authoritative sources
- Find common terminology
- Understand current state of knowledge

### Phase 3: Deep-Dive Searches

Based on Phase 2 findings, conduct targeted searches:

```
Tool: tavily_search
Parameters:
  query: "[specific subtopic] [year]"
  search_depth: advanced
  max_results: 5
  include_domains: [authoritative sources from Phase 2]
  include_raw_content: true
```

**Repeat for each identified subtopic.**

### Phase 4: Source Validation

For critical findings, validate across multiple sources:

1. **Cross-Reference**: Search for the same fact from different angles
2. **Check Dates**: Verify information is current
3. **Verify Authority**: Confirm source credibility
4. **Look for Contradictions**: Search for opposing viewpoints

```
Tool: tavily_search
Parameters:
  query: "[specific claim] [alternative phrasing]"
  exclude_domains: [original source domain]
  max_results: 5
```

### Phase 5: Fill Knowledge Gaps

Identify and address gaps:

1. Review collected information
2. List unanswered questions
3. Execute targeted searches for each gap
4. Document areas where information is unavailable

### Phase 6: Synthesize Findings

Compile research into structured output:

```markdown
# Research Summary: [Topic]

## Executive Summary
[Brief overview of key findings]

## Key Findings
1. [Finding 1 with source citations]
2. [Finding 2 with source citations]
...

## Detailed Analysis
[In-depth discussion organized by subtopic]

## Sources
- [Source 1]: [URL]
- [Source 2]: [URL]
...

## Limitations
[Areas where research was inconclusive or information was unavailable]

## Recommendations
[Actionable next steps based on findings]
```

## Search Strategy Patterns

### Pattern: Technology Comparison

```
Search 1: "[Technology A] vs [Technology B] comparison"
Search 2: "[Technology A] pros cons"
Search 3: "[Technology B] pros cons"
Search 4: "[Technology A] production use cases"
Search 5: "[Technology B] production use cases"
```

### Pattern: Best Practices Research

```
Search 1: "[topic] best practices [year]"
Search 2: "[topic] common mistakes"
Search 3: "[topic] security considerations"
Search 4: "[topic] performance optimization"
Search 5: "[topic] official documentation"
```

### Pattern: Problem-Solution Research

```
Search 1: "[problem description] solution"
Search 2: "[error message or symptom]"
Search 3: "[problem] workaround"
Search 4: "[problem] root cause"
Search 5: "[problem] prevention"
```

### Pattern: Learning New Technology

```
Search 1: "[technology] getting started tutorial"
Search 2: "[technology] core concepts"
Search 3: "[technology] common patterns"
Search 4: "[technology] real world examples"
Search 5: "[technology] official documentation"
```

## Domain Filtering Strategies

### Development Research

```json
{
  "include_domains": [
    "github.com",
    "stackoverflow.com",
    "developer.mozilla.org",
    "docs.python.org",
    "nodejs.org",
    "reactjs.org"
  ]
}
```

### Security Research

```json
{
  "include_domains": [
    "owasp.org",
    "nist.gov",
    "cve.mitre.org",
    "security.googleblog.com"
  ]
}
```

### Academic/Technical Research

```json
{
  "include_domains": [
    "arxiv.org",
    "acm.org",
    "ieee.org",
    "research.google"
  ]
}
```

### Exclude Low-Quality Sources

```json
{
  "exclude_domains": [
    "pinterest.com",
    "quora.com",
    "w3schools.com",
    "medium.com"
  ]
}
```

## Quality Checklist

Before concluding research, verify:

- [ ] Primary question has been answered
- [ ] Multiple authoritative sources confirm key findings
- [ ] Information is current (check publication dates)
- [ ] Conflicting information has been addressed
- [ ] Knowledge gaps have been documented
- [ ] Sources are properly cited
- [ ] Findings are organized and accessible

## Rate Limit Considerations

To avoid rate limiting during extended research:

1. **Batch Similar Queries**: Group related searches
2. **Start Broad, Then Narrow**: Reduces total search count
3. **Cache Results**: Don't repeat identical searches
4. **Use Basic Depth First**: Only use advanced when needed

## Integration with Other Tools

### Combining with Browser MCP

For sources requiring detailed reading:
1. Use Tavily to identify relevant URLs
2. Use Browser MCP to navigate and extract detailed content
3. Return to Tavily for follow-up searches

### Combining with File Tools

For persisting research:
1. Create research document with findings
2. Save source URLs for reference
3. Export structured data for later use

## Example Complete Workflow

**Research Question**: "What are the current best practices for containerizing Python applications?"

```
Step 1: Broad Search
  Query: "containerizing Python applications best practices 2024"
  Depth: basic, Results: 10, Include Answer: true

Step 2: Identify Subtopics from Results
  - Base image selection
  - Dependency management
  - Multi-stage builds
  - Security hardening
  - Size optimization

Step 3: Deep-Dive Each Subtopic
  Query 1: "Python Docker base image alpine vs slim comparison"
  Query 2: "Python Docker requirements.txt vs poetry"
  Query 3: "Python Docker multi-stage build example"
  Query 4: "Python Docker security best practices"
  Query 5: "Python Docker image size optimization"

Step 4: Validate Key Findings
  Query: "Python Docker official recommendations"
  Domain: docker.com, python.org

Step 5: Synthesize into Document
  [Create structured summary with citations]
```

## Troubleshooting Research Workflows

| Issue | Solution |
|-------|----------|
| Too many irrelevant results | Add domain filters, use more specific terms |
| Outdated information | Add year to query, use news search |
| Conflicting information | Search for meta-analyses, check source dates |
| Missing specific details | Use advanced depth, include raw content |
| Rate limit reached | Batch remaining queries, prioritize critical gaps |
