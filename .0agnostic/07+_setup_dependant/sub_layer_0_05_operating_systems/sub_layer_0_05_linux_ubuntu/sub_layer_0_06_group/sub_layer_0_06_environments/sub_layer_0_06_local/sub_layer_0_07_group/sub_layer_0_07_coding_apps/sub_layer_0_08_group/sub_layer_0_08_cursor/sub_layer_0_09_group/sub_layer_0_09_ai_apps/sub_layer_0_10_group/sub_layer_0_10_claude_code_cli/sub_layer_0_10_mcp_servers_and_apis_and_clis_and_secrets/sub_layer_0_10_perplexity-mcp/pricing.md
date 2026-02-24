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

| MCP Tool | Model | Est. cost/query |
|----------|-------|----------------|
| `perplexity_ask` | Sonar | ~$0.007 |
| `perplexity_search` | Sonar Pro | ~$0.015 |
| `perplexity_reason` | Sonar Reasoning Pro | ~$0.015 |
| `perplexity_research` | Sonar Deep Research | ~$0.15 |

Formula: Total cost = token costs + request fee (by search context size)

## Subscription Comparison

| Factor | API | Pro ($20/mo) |
|--------|-----|-------------|
| Monthly cost | Variable | $20 flat |
| Breakeven (with $5 credit) | ~860 searches/mo | -- |
| Deep Research | Pay per use | ~20/month |
| Unlimited basic | No | Yes |
