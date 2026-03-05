---
resource_id: "f4e168ba-0beb-47b8-b657-315fcc1aec06"
resource_type: "document"
resource_name: "web-research-workflow"
---
# Web Research Workflow

<!-- section_id: "17cab94a-c977-4f01-a050-6852b521d2fb" -->
## Overview

This protocol defines a structured approach for conducting comprehensive web research using the Tavily MCP server. It provides a systematic methodology for gathering, validating, and synthesizing information from web sources.

<!-- section_id: "3d054a2f-25a0-4c74-94ba-175e44222956" -->
## When to Use

- Deep-dive research on technical topics
- Competitive analysis and market research
- Documentation gathering for development decisions
- Learning about new technologies or frameworks
- Gathering requirements or specifications

<!-- section_id: "6d1c8d20-73ca-4038-951b-1423d656c99d" -->
## Workflow Steps

<!-- section_id: "0e95b52d-950e-491c-9500-559f3cce3c81" -->
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

<!-- section_id: "6a06efad-f51a-43ac-943b-78a4de41326b" -->
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

<!-- section_id: "fe604f03-4dae-45a3-bb86-c9b372316bc0" -->
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

<!-- section_id: "c5a473ac-8947-48e9-8018-4cb9002f6f13" -->
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

<!-- section_id: "d0693c41-e16c-451e-9d84-37780a915004" -->
### Phase 5: Fill Knowledge Gaps

Identify and address gaps:

1. Review collected information
2. List unanswered questions
3. Execute targeted searches for each gap
4. Document areas where information is unavailable

<!-- section_id: "d85d805d-3807-498e-a1c5-0fe632e06253" -->
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

<!-- section_id: "e04f9bdc-7acf-413e-bc9c-a17c87233762" -->
## Search Strategy Patterns

<!-- section_id: "da62877d-aeac-4b37-b5ac-25557a1940da" -->
### Pattern: Technology Comparison

```
Search 1: "[Technology A] vs [Technology B] comparison"
Search 2: "[Technology A] pros cons"
Search 3: "[Technology B] pros cons"
Search 4: "[Technology A] production use cases"
Search 5: "[Technology B] production use cases"
```

<!-- section_id: "c67656ea-f216-4864-b76c-7b359d0630b3" -->
### Pattern: Best Practices Research

```
Search 1: "[topic] best practices [year]"
Search 2: "[topic] common mistakes"
Search 3: "[topic] security considerations"
Search 4: "[topic] performance optimization"
Search 5: "[topic] official documentation"
```

<!-- section_id: "3aad244b-400e-439e-b8a2-121fb8806767" -->
### Pattern: Problem-Solution Research

```
Search 1: "[problem description] solution"
Search 2: "[error message or symptom]"
Search 3: "[problem] workaround"
Search 4: "[problem] root cause"
Search 5: "[problem] prevention"
```

<!-- section_id: "2e5bee16-16f3-429d-ab3a-85a09a277449" -->
### Pattern: Learning New Technology

```
Search 1: "[technology] getting started tutorial"
Search 2: "[technology] core concepts"
Search 3: "[technology] common patterns"
Search 4: "[technology] real world examples"
Search 5: "[technology] official documentation"
```

<!-- section_id: "e22f382c-b8f6-4821-a5ce-9b4f61164fc1" -->
## Domain Filtering Strategies

<!-- section_id: "15776d1e-746b-40b4-a5f7-a9f30d235c95" -->
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

<!-- section_id: "e9804dce-2fc2-4b85-b870-12cbcae17bfb" -->
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

<!-- section_id: "3b47b787-3d88-486f-9a79-1a9523fb3741" -->
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

<!-- section_id: "557d324a-e3b7-4a01-90cd-c710b02938b6" -->
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

<!-- section_id: "a04d9819-982e-4637-ab42-25db09963f92" -->
## Quality Checklist

Before concluding research, verify:

- [ ] Primary question has been answered
- [ ] Multiple authoritative sources confirm key findings
- [ ] Information is current (check publication dates)
- [ ] Conflicting information has been addressed
- [ ] Knowledge gaps have been documented
- [ ] Sources are properly cited
- [ ] Findings are organized and accessible

<!-- section_id: "64031161-c31a-4158-abcd-ce454d0c30a2" -->
## Rate Limit Considerations

To avoid rate limiting during extended research:

1. **Batch Similar Queries**: Group related searches
2. **Start Broad, Then Narrow**: Reduces total search count
3. **Cache Results**: Don't repeat identical searches
4. **Use Basic Depth First**: Only use advanced when needed

<!-- section_id: "03fe4edc-c2e7-421f-bc7b-c861d8d81613" -->
## Integration with Other Tools

<!-- section_id: "acec3110-f4af-4163-b950-0821db312882" -->
### Combining with Browser MCP

For sources requiring detailed reading:
1. Use Tavily to identify relevant URLs
2. Use Browser MCP to navigate and extract detailed content
3. Return to Tavily for follow-up searches

<!-- section_id: "709ca1b3-5bc6-4671-97f1-6746df049840" -->
### Combining with File Tools

For persisting research:
1. Create research document with findings
2. Save source URLs for reference
3. Export structured data for later use

<!-- section_id: "093a6e15-0680-4fd4-8c51-a4a96fbd1744" -->
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

<!-- section_id: "b3520fa4-39e6-434b-b368-334e2e0bbfee" -->
## Troubleshooting Research Workflows

| Issue | Solution |
|-------|----------|
| Too many irrelevant results | Add domain filters, use more specific terms |
| Outdated information | Add year to query, use news search |
| Conflicting information | Search for meta-analyses, check source dates |
| Missing specific details | Use advanced depth, include raw content |
| Rate limit reached | Batch remaining queries, prioritize critical gaps |
