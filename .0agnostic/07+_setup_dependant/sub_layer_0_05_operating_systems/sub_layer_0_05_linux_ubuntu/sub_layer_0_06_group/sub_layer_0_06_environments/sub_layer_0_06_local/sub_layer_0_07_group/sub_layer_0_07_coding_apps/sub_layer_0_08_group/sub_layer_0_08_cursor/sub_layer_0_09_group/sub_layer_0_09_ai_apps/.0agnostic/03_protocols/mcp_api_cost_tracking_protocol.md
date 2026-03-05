---
resource_id: "a1316b96-7b50-48f6-ab2c-f4ab192403c2"
resource_type: "protocol"
resource_name: "mcp_api_cost_tracking_protocol"
---
# MCP API Cost Tracking Protocol

**Purpose**: Track spending on paid MCP APIs to compare against subscription alternatives and enforce budget limits.

<!-- section_id: "26a03515-ba5a-4dcd-b956-dbf37479b929" -->
## When to Use

After EVERY call to a paid MCP API tool (Perplexity, Tavily, etc.).

<!-- section_id: "1d1e05e7-9f58-4727-a0e1-f7ca08eba348" -->
## Workflow

<!-- section_id: "4584bf89-16b2-4e2b-9779-fd382a0e930f" -->
### Before Each Paid MCP Call

1. Read `memory/mcp_api_usage.md` -- check current month's total
2. Compare against budget ($20/month):
   - **Under 80%** --> Proceed normally
   - **80-99%** --> Warn user: "Budget at {X}% (${spent}/${limit}). Proceed?"
   - **100%+** --> Ask user: "Monthly budget reached. Continue anyway?"
3. Make the MCP call

<!-- section_id: "5680cbf0-7f21-46db-aad5-19a9bbbfa00d" -->
### After Each Paid MCP Call

1. Append a row to the current month's table in `memory/mcp_api_usage.md`:
   - Date, Service, Tool, Query summary (10 words max), Est. cost
2. Update the month's running total and budget percentage
3. Update query count breakdown

<!-- section_id: "895a58e5-849d-4df5-960a-bb36a4e32e5d" -->
### At Month End

1. Copy the month's data into a summary block using the monthly summary template
2. Calculate: total spend, query breakdown, comparison vs Pro subscription
3. Start a fresh month table

<!-- section_id: "7ae884f8-a327-490e-b44f-c6f7cf776f7c" -->
## Estimated Costs (Quick Reference — verified from real billing 2026-02-25)

| Tool | Est. cost | Budget impact |
|------|----------|--------------|
| `perplexity_ask` | ~$0.01 | Minimal |
| `perplexity_search` | ~$0.05 | Low |
| `perplexity_reason` | ~$0.05 | Low |
| `perplexity_research` | ~$3-5+ | **HIGH — 15-25% of monthly budget per call** |
| `tavily_search` | ~$0.008 | Minimal (free tier: $0) |

**CRITICAL**: Always prefer `perplexity_ask` or `perplexity_search` over `perplexity_research`.
Only use deep research when the user explicitly requests it or the task genuinely requires it.

<!-- section_id: "142edc88-e626-4e51-af10-8bfc0e00f0f6" -->
## Configuration

Budget config: `sub_layer_0_10_group/sub_layer_0_10_01_tools_and_services/budget_config.json`
Per-service pricing: `sub_layer_0_10_group/sub_layer_0_10_01_tools_and_services/sub_layer_0_11_group/[service]/pricing.md`

<!-- section_id: "8caeada7-999c-4f1b-932a-8cda4a51804e" -->
## Related

- Rule: `.0agnostic/02_rules/dynamic/MCP_API_BUDGET_ENFORCEMENT/`
- Auto-memory: `memory/mcp_api_usage.md`
