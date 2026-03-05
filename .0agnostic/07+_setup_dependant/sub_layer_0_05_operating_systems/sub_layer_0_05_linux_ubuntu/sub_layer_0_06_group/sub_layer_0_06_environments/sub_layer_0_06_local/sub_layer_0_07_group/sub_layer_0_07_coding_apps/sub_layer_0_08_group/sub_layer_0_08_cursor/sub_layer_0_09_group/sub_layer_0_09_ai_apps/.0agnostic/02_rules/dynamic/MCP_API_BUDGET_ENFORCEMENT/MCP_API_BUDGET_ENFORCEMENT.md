---
resource_id: "1eaa3212-fe34-433e-bef3-a0cdcefc9fcd"
resource_type: "rule"
resource_name: "MCP_API_BUDGET_ENFORCEMENT"
---
# MCP API Budget Enforcement Rule

**Type**: Dynamic (triggered by scenario)
**Importance**: 1 (High)
**Scope**: All AI agents using paid MCP API tools

<!-- section_id: "65081705-23c0-41fa-90ad-e7c418658af4" -->
## Rule

Before calling any paid MCP API tool, check current month's spending in `memory/mcp_api_usage.md`:

1. **Green (< 80%)**: Proceed. Log after call.
2. **Yellow (80-99%)**: Inform user of budget status before proceeding. Log after call.
3. **Red (>= 100%)**: Ask user for explicit confirmation before proceeding. Suggest alternatives (e.g., browser-based search, cached results, skip this query). Log after call.

After every paid MCP call, update the usage log immediately.

<!-- section_id: "137632dc-e91f-4587-979f-dca521dbfbe9" -->
## Trigger Conditions

- About to call any tool matching: `perplexity_*`, `tavily_*`, or any tool listed in `budget_config.json` services
- User asks about API spending or budget status

<!-- section_id: "72a0e384-da94-4961-926a-46ca46101e23" -->
## Paid MCP Tools (Current)

- `mcp__perplexity__perplexity_ask`
- `mcp__perplexity__perplexity_search`
- `mcp__perplexity__perplexity_reason`
- `mcp__perplexity__perplexity_research`
- `mcp__tavily__tavily_search` (if exceeding free tier)
- `mcp__tavily__tavily_extract` (if exceeding free tier)

<!-- section_id: "e7f01f46-d37d-41a5-92d4-dd79a275f8e5" -->
## Rationale

API-only approach should stay under $20/month (Pro subscription cost) to remain cost-effective. Tracking and enforcement ensures we know when the API approach stops being the better deal.

<!-- section_id: "fd749c61-61b0-4988-8f95-044243afcb80" -->
## Related

- Protocol: `mcp_api_cost_tracking_protocol.md`
- Config: `budget_config.json` at MCP servers parent level
- Billing: https://www.perplexity.ai/account/api/billing
