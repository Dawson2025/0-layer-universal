# Static vs Dynamic Context

## Summary

Context is classified along two independent dimensions: timing (when it enters the model's working memory) and ownership (who controls it). These dimensions are orthogonal, producing a 2x2 matrix.

Static context (CLAUDE.md chain, MCP schemas, skill listings, auto memory) is loaded on every API call -- roughly 7,500 tokens per call regardless of relevance. Dynamic context (.0agnostic/ reads, .gab.jsonld queries, skill content) only costs tokens when explicitly invoked. This asymmetry makes static context a multiplicative cost (tokens x API calls) while dynamic context is a one-time cost per read.

The ownership dimension separates fixed context (controlled by Claude Code runtime -- system prompt preamble, loading order, tool formats) from configurable context (controlled by the project author -- CLAUDE.md content, .0agnostic/ resources, MCP servers). The biggest optimization lever is the static+configurable quadrant: keep CLAUDE.md lean (identity + triggers + pointers) and push detail into .0agnostic/ for on-demand loading. Target a dynamic-to-static ratio of 5:1 or higher.

## Key Concepts

- **Static**: Loaded every API call automatically; constant token cost per call
- **Dynamic**: Loaded only when agent invokes; pay-per-use token cost
- **Fixed**: Controlled by Claude Code runtime (cannot modify)
- **Configurable**: Controlled by project author (can optimize)
- **Target ratio**: Dynamic content should be 5-10x the size of static content
- **Budget**: ~7,500 tokens per API call for all static context combined

## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Full dimensions doc | `.0agnostic/01_knowledge/static_dynamic_context.md` | 2x2 matrix, flow diagram, token budgets |
| Optimization strategies | `.0agnostic/01_knowledge/chain_optimization_strategies.md` | 6 strategies for reducing static cost |
| Stage 02 research | `layer_2_99_stages/stage_2_02_research/outputs/by_topic/architecture/` | Original research |
| Default view diagram | `layer_3_group/.../chain_visualization/diagrams/current/context_chain/default_view.md` | Configurable context only |
