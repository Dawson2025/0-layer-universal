# MCP API Cost Tracking Protocol

**Purpose**: Track spending on paid MCP APIs to compare against subscription alternatives and enforce budget limits.

## When to Use

After EVERY call to a paid MCP API tool (Perplexity, Tavily, etc.).

## Workflow

### Before Each Paid MCP Call

1. Read `memory/mcp_api_usage.md` -- check current month's total
2. Compare against budget ($20/month):
   - **Under 80%** --> Proceed normally
   - **80-99%** --> Warn user: "Budget at {X}% (${spent}/${limit}). Proceed?"
   - **100%+** --> Ask user: "Monthly budget reached. Continue anyway?"
3. Make the MCP call

### After Each Paid MCP Call

1. Append a row to the current month's table in `memory/mcp_api_usage.md`:
   - Date, Service, Tool, Query summary (10 words max), Est. cost
2. Update the month's running total and budget percentage
3. Update query count breakdown

### At Month End

1. Copy the month's data into a summary block using the monthly summary template
2. Calculate: total spend, query breakdown, comparison vs Pro subscription
3. Start a fresh month table

## Estimated Costs (Quick Reference)

| Tool | Est. cost |
|------|----------|
| `perplexity_ask` | $0.007 |
| `perplexity_search` | $0.015 |
| `perplexity_reason` | $0.015 |
| `perplexity_research` | $0.15 |
| `tavily_search` | $0.008 (free tier: $0) |

## Configuration

Budget config: `.../sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/budget_config.json`
Per-service pricing: Each MCP server's `pricing.md`

## Related

- Rule: `.0agnostic/02_rules/dynamic/MCP_API_BUDGET_ENFORCEMENT/`
- Auto-memory: `memory/mcp_api_usage.md`
