---
resource_id: "abb584fe-91e6-4c59-afe8-c8570be795f8"
resource_type: "document"
resource_name: "pricing"
---
# Perplexity API Pricing Reference

Last verified: 2026-02-24
Source: https://docs.perplexity.ai/docs/getting-started/pricing

## Token Pricing (per 1M tokens)

| Model | Input | Output | Citation | Search Queries | Reasoning |
|-------|-------|--------|----------|----------------|-----------|
| Sonar | $1 | $1 | -- | -- | -- |
| Sonar Pro | $3 | $15 | -- | -- | -- |
| Sonar Reasoning Pro | $2 | $8 | -- | -- | -- |
| Sonar Deep Research | $2 | $8 | $2 | $5/1K queries | $3 |

## Request Fees (per 1,000 requests)

| Model | Low context | Medium | High |
|-------|------------|--------|------|
| Sonar | $5 | $8 | $12 |
| Sonar Pro | $6 | $10 | $14 |
| Sonar Reasoning Pro | $6 | $10 | $14 |

## Estimated Cost Per Query (for tracking)

Based on actual billing data from 2026-02-25 (real usage, not theoretical):

| MCP Tool | Model | Est. cost/query | Source |
|----------|-------|----------------|--------|
| `perplexity_ask` | Sonar | ~$0.01 | Theoretical (no actual data yet) |
| `perplexity_search` | Sonar Pro | ~$0.05 | Actual: 6 calls = $0.31 (~$0.05/call) |
| `perplexity_reason` | Sonar Reasoning Pro | ~$0.05 | Estimated (similar to sonar-pro) |
| `perplexity_research` | Sonar Deep Research | ~$3.00-$5.00 | Actual: ~$15.66 from few calls |

**WARNING**: Deep research is extremely expensive. A single call can generate millions
of reasoning tokens. The $0.15 initial estimate was 20-30x too low.

Formula: Total cost = token costs + request fee (by search context size)

## Actual Cost Breakdown (from billing page 2026-02-25)

Total spent: $16.12 over ~30 days

| Category | Model | Cost | % |
|----------|-------|------|---|
| Reasoning tokens | deep-research | $11.89 | 73.8% |
| Search queries | deep-research | $1.80 | 11.2% |
| Citation tokens | deep-research | $1.26 | 7.8% |
| Output tokens | all | $0.88 | 5.5% |
| Search API requests | mixed | $0.16 | 1.0% |
| API request fees | sonar-pro | $0.13 | 0.8% |
| Input tokens | all | $0.01 | 0.1% |

**Key insight**: Deep research = 97% of costs. Regular sonar-pro searches are cheap (~$0.05/call).

## Subscription Comparison

| Factor | API | Pro ($20/mo) |
|--------|-----|-------------|
| Monthly cost | Variable | $20 flat |
| Breakeven (sonar-pro only) | ~400 searches/mo | -- |
| Deep Research | $3-5+ per call | ~20/month included |
| Unlimited basic | No | Yes |

**Verdict**: If you use deep research regularly, Pro is much cheaper. If you stick to
sonar-pro/ask/reason, API is cheaper unless you do 400+ searches/month.
