# MCP API Budget Enforcement Rule

**Type**: Dynamic (triggered by scenario)
**Importance**: 1 (High)
**Scope**: All AI agents using paid MCP API tools

## Rule

Before calling any paid MCP API tool, check current month's spending in `memory/mcp_api_usage.md`:

1. **Green (< 80%)**: Proceed. Log after call.
2. **Yellow (80-99%)**: Inform user of budget status before proceeding. Log after call.
3. **Red (>= 100%)**: Ask user for explicit confirmation before proceeding. Suggest alternatives (e.g., browser-based search, cached results, skip this query). Log after call.

After every paid MCP call, update the usage log immediately.

## Trigger Conditions

- About to call any tool matching: `perplexity_*`, `tavily_*`, or any tool listed in `budget_config.json` services
- User asks about API spending or budget status

## Paid MCP Tools (Current)

- `mcp__perplexity__perplexity_ask`
- `mcp__perplexity__perplexity_search`
- `mcp__perplexity__perplexity_reason`
- `mcp__perplexity__perplexity_research`
- `mcp__tavily__tavily_search` (if exceeding free tier)
- `mcp__tavily__tavily_extract` (if exceeding free tier)

## Rationale

API-only approach should stay under $20/month (Pro subscription cost) to remain cost-effective. Tracking and enforcement ensures we know when the API approach stops being the better deal.

## Related

- Protocol: `mcp_api_cost_tracking_protocol.md`
- Config: `budget_config.json` at MCP servers parent level
- Billing: https://www.perplexity.ai/account/api/billing
