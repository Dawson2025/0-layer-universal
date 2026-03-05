---
resource_id: "0b9a32f1-a011-4015-8b3b-bf998d851637"
resource_type: "output"
resource_name: "json_ld_vs_markdown_for_llm_instructions_research"
---
# JSON-LD vs Markdown for LLM Agent Instructions: Research Report

> **Layer**: layer_-1_research | **Stage**: 02_research | **Date**: 2026-02-07

---

## Executive Summary

After reviewing academic papers, empirical benchmarks, blog analyses, and real-world projects, the evidence strongly suggests that **JSON-LD is NOT more effective than markdown for LLM agent instructions**. In fact, it is likely worse across most dimensions that matter: token efficiency, instruction-following accuracy, human maintainability, and practical adoption. JSON-LD has a narrow but real value in a completely different domain: web entity disambiguation and knowledge graph alignment for AI search crawlers. The two use cases should not be conflated.

---

## 1. Is There Research Showing JSON-LD Improves LLM Instruction Following vs Markdown?

**Verdict: No. The research that exists shows the opposite.**

### Key Paper: "Does Prompt Formatting Have Any Impact on LLM Performance?" (arXiv:2411.10541, 2024)

This is the most rigorous direct comparison. Researchers formatted identical prompts into plain text, Markdown, JSON, and YAML and tested across GPT-3.5-turbo, GPT-4-32k, GPT-4-turbo, and GPT-4-1106-preview across six benchmarks.

Findings:
- GPT-3.5-turbo performance varied up to **40%** depending on prompt format (in a code translation task).
- For GPT-4 models, **Markdown achieved 81.2% accuracy** on a reasoning task vs **73.9% for JSON**.
- However, for GPT-3.5, JSON won at 59.7% vs Markdown at 50.0% on the same task.
- **Larger, more capable models are more robust** to format variations and tend to prefer Markdown.
- GPT-4-32k performed extremely poorly with JSON on HumanEval because it generated chain-of-thought in plain text but never produced the actual code.

**JSON-LD was not tested separately in this paper**, but plain JSON (a simpler format) already showed mixed-to-negative results compared to Markdown on modern models.

### Key Paper: "Prompt Engineering for Structured Data" (William & Mary, 2024-2025)

Compared six prompt styles (JSON, YAML, CSV, function-calling APIs, simple prefixes, hybrid CSV/prefix) across ChatGPT-4o, Claude, and Gemini for structured data generation.

Findings:
- Hierarchical formats (JSON, YAML) improved accuracy for structured data generation tasks.
- Lightweight formats (CSV, simple prefixes) reduced token usage and latency.
- **No single format was universally optimal** -- it depends on the task and model.

### Key Paper: KG-LLM-Bench (arXiv:2504.07087, 2025)

This is the **only paper to directly test JSON-LD** as a format for feeding data to LLMs. It compared five textualization strategies for knowledge graphs: Structured JSON, List-of-Edges, Structured YAML, JSON-LD, and RDF Turtle.

Findings:
- **JSON-LD performed worst** with an average accuracy of **0.34** across tasks and models.
- Structured JSON achieved the best average at **0.42**.
- List-of-Edges and YAML were close behind Structured JSON.
- JSON-LD required **over 13,000 tokens** per prompt due to namespace specifications and URIs, vs under 3,000 for List-of-Edges and Structured YAML.
- The @context blocks, @type annotations, and URI expansions that define JSON-LD add massive token overhead without helping LLM comprehension.

**This is direct empirical evidence that JSON-LD hurts LLM performance.**

---

## 2. Do LLMs Handle JSON-LD Better Than Markdown for Agent Behavior?

**Verdict: No. They handle it worse.**

### Why JSON-LD is problematic for LLMs:

1. **Token overhead**: JSON-LD includes `@context`, `@type`, `@id`, `@graph`, URI prefixes, and namespace declarations. These are essential for linked data interoperability but are pure noise to an LLM that processes tokens probabilistically. The KG-LLM-Bench paper showed JSON-LD used 4-5x more tokens than simpler formats for the same information.

2. **Training data mismatch**: LLMs are trained overwhelmingly on natural language text, Markdown documentation, and code. JSON-LD is a niche format that appears relatively rarely in training corpora compared to Markdown or plain JSON. Models have less "experience" with it.

3. **Semantic overhead without semantic benefit**: JSON-LD's linked data features (URIs, contexts, type coercion) exist to enable machine interoperability across the Semantic Web. LLMs do not process these semantically -- they tokenize them character by character. The `@context` block that maps terms to schema.org URIs does not help an LLM understand meaning any better; the LLM already understands the natural language terms.

4. **Structural complexity**: JSON-LD supports features like `@graph`, `@reverse`, blank nodes, and compact/expanded forms. This complexity can confuse LLMs, leading to parsing failures or misinterpretation. The sitelint.com guide documents numerous common JSON-LD parsing issues (malformed JSON, encoding problems, incorrect nesting).

### What Markdown does well for LLMs:

- Preserves natural language flow that LLMs excel at processing.
- Uses minimal syntactic overhead (headers, bullets, bold).
- Mirrors training data distribution (vast amounts of Markdown in documentation, READMEs, forums).
- Supports hierarchical structure through heading levels.
- Is approximately **15% more token-efficient** than equivalent JSON and **34-38% more efficient** than JSON when representing nested data (ImprovingAgents benchmark).

### What Anthropic, OpenAI, and Google actually recommend:

- **Anthropic** (Claude): Recommends XML tags for structured prompt sections, with Markdown for content.
- **OpenAI** (GPT): System prompts are written in Markdown. The platform natively renders Markdown.
- **Google** (Gemini): Recommends structured prompts with Persona, Task, Context, and Format sections.
- **None of these providers recommend JSON-LD for agent instructions.**

One emerging observation from researcher Anand S.: "XML tags are the best way to structure prompts and separate sections for an LLM. It is the only format that all models from Anthropic, Google and OpenAI encourage."

---

## 3. Projects or Tools Using JSON-LD for LLM Agent Behavior

**Verdict: Almost none for agent behavior. One for agent discovery.**

### LMOS (Language Model Operating System) -- Eclipse Foundation

LMOS is the only real project found that uses JSON-LD in the AI agent ecosystem, and it uses JSON-LD **not for agent instructions/behavior** but for **agent discovery and capability description**. LMOS uses JSON-LD as its standardized format for describing agent and tool metadata, building on the W3C Web of Things (WoT) Thing Description specification. This is about machine-to-machine interoperability for finding agents, not for telling agents how to behave.

### What projects actually use for agent behavior:

| Framework | Format for Agent Config | Notes |
|-----------|------------------------|-------|
| LangChain | Python code + JSON schemas for tools | No JSON-LD |
| AutoGPT | JSON/YAML config | No JSON-LD |
| MetaGPT | Python + YAML | No JSON-LD |
| CrewAI | Python + YAML | No JSON-LD |
| Claude Code (Anthropic) | Markdown (CLAUDE.md files) | No JSON-LD |
| agents.json (Wildcard AI) | JSON (OpenAPI-based) | Explicitly not JSON-LD |
| IBM LLM Agent Framework | Python + formal specs | No JSON-LD |
| AgentFlow | JSON config | No JSON-LD |
| MCP (Anthropic) | JSON-RPC | No JSON-LD |

The industry has converged on Markdown for human-authored instructions, JSON/JSON Schema for machine-parseable tool definitions, and YAML for configuration. JSON-LD is absent from the agent instruction space.

---

## 4. Token Cost Comparison: JSON-LD vs Equivalent Markdown

**Verdict: JSON-LD is dramatically more expensive.**

### Direct measurements:

| Format | Relative Token Cost | Source |
|--------|-------------------|--------|
| Markdown (prose) | Baseline (1.0x) | ImprovingAgents, shshell.com |
| YAML | ~1.1x Markdown | ImprovingAgents benchmark |
| Plain JSON | ~1.5x Markdown | ImprovingAgents (34-38% more tokens) |
| JSON (minified) | ~0.7-0.9x Markdown | curiouslychase.com (context-dependent) |
| XML | ~1.8x Markdown | ImprovingAgents (80% more tokens) |
| JSON-LD | ~3-5x Markdown | KG-LLM-Bench (13,000+ vs 3,000 tokens) |

### Why JSON-LD is especially expensive:

A simple agent instruction like "You are a helpful assistant that searches the web" in Markdown is a single line. In JSON-LD:

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareAgent",
  "name": "WebSearchAssistant",
  "description": "You are a helpful assistant that searches the web",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://example.com/search?q={query}"
  }
}
```

The `@context`, `@type`, structural braces, quotes, and key names all consume tokens without adding any information the LLM could not derive from the natural language description. At scale (thousands of tokens of agent instructions), this overhead becomes prohibitive.

### Specific benchmark data:

- **shshell.com Token Benchmarks**: For a simple 2-user dataset, JSON uses 50 tokens, YAML uses 35 tokens, Markdown table uses 70 tokens. JSON-LD would add @context overhead on top of JSON's 50, pushing to 80-100+ tokens.
- **YAML vs JSON blog (tashif.codes)**: A comprehensive tiktoken analysis showed JSON at 13,869 tokens, YAML at 12,333 (11.1% reduction), Markdown at 11,612 (16.3% reduction) for the same production data. JSON-LD would be substantially higher than JSON due to namespace overhead.
- **Minification caveat**: One analysis (curiouslychase.com) showed that minified JSON (41 tokens) beat YAML (133 tokens) for the same data. However, JSON-LD cannot be meaningfully minified because its `@context` blocks and URI strings are irreducible.

---

## 5. Does JSON-LD's Graph/Linked-Data Structure Help LLMs Understand Relationships?

**Verdict: No, not for in-context processing. Yes, for pre-processing pipelines.**

### For in-context (prompt) processing:

LLMs do not traverse graph structures. They process linear sequences of tokens. JSON-LD's graph model (nodes connected by typed edges with URI identifiers) is invisible to the LLM's attention mechanism. The LLM sees `"@id": "http://example.com/agent/1"` as a sequence of tokens, not as a graph node identifier.

The KG-LLM-Bench paper directly tested this: when knowledge graphs were represented as JSON-LD (preserving the full linked data structure) vs as simple structured JSON or even flat lists of edges, **the simpler formats performed better**. The graph structure of JSON-LD actively hurt performance because it added token noise without helping the LLM reason about relationships.

### For pre-processing / RAG pipelines:

There is evidence that JSON-LD helps **outside** the LLM context window:

- **iunera Benchmark (2025)**: Adding JSON-LD labels to web content improved vector search accuracy by helping AI disambiguate terms (e.g., distinguishing "bug fix" in software from "insect repellent" in biology). This is a pre-processing/embedding benefit, not an in-context benefit.
- **Ranktracker analysis**: JSON-LD helps LLMs at the web crawling/indexing stage by providing semantic scaffolding for embeddings and knowledge graph alignment. This is about web content consumption, not prompt engineering.

### Key distinction:

JSON-LD's value for AI is in **data preparation** (structuring web content for AI crawlers and search engines) -- not in **prompt content** (telling an LLM agent how to behave).

---

## 6. Known Issues with LLMs Parsing or Following JSON-LD

**Verdict: Multiple significant issues documented.**

1. **Token bloat**: As documented above, 3-5x overhead vs simpler formats.

2. **@context confusion**: LLMs may try to interpret `@context` URLs as actionable links rather than namespace declarations, or may hallucinate incorrect context mappings.

3. **Format fragility**: JSON-LD has multiple valid representations (compact, expanded, flattened, framed). LLMs may generate inconsistent forms, leading to downstream parsing failures.

4. **Encoding issues**: JSON-LD embedded in HTML requires careful character escaping. LLMs generating JSON-LD frequently produce invalid output with unescaped quotes, incorrect Unicode, or malformed URIs.

5. **Lazy generation**: The arXiv:2411.10541 paper found that GPT-4-32k, when given JSON-formatted prompts, would generate chain-of-thought reasoning in plain text but fail to produce the actual structured output. This "laziness" effect is likely worse with JSON-LD's additional structural requirements.

6. **Not all agents parse JSON-LD**: Even the agentnet.bearblog.dev guide (which advocates for JSON-LD in agent systems) warns: "While JSON-LD gives you structure, not all agents parse it out-of-the-box. LLM-based agents may need explicit schema alignment, fine-tuning, or grounding. Structure is necessary -- but not always sufficient."

7. **Reasoning degradation**: Research by Castillo (2025) found that forcing LLMs to use structured formats can hurt reasoning because it makes the model "think in code rather than logic." JSON-LD, being the most structurally constrained format, would be most susceptible to this effect.

---

## 7. Comparison with Other Structured Formats

### Format Rankings for LLM Agent Instructions

Based on the aggregated research:

| Format | Accuracy (Modern LLMs) | Token Efficiency | Human Maintainability | Agent Framework Adoption | Overall Rating |
|--------|----------------------|-----------------|----------------------|------------------------|----------------|
| **Markdown** | High | Best | Excellent | Very High (Claude, docs) | Best overall |
| **YAML** | Highest (per ImprovingAgents) | Very Good (~10% more than MD) | Good | High (configs) | Best for structured data |
| **XML** | Good (Claude prefers for sections) | Poor (80% more than MD) | Moderate | Moderate (Anthropic) | Good for section boundaries |
| **Plain JSON** | Model-dependent | Moderate | Moderate | High (tool schemas) | Good for machine parsing |
| **Minified JSON** | Unknown (untested) | Very Good | Poor | Low | Cost-optimized niche |
| **JSON-LD** | Worst (per KG-LLM-Bench) | Worst (3-5x more than MD) | Poor | Nearly Zero | Not recommended |
| **TOON** | Good (per tensorlake.ai) | Excellent (70-75% less than JSON) | Good | Emerging | Promising for data payloads |
| **CSV** | Good for flat data | Best for tabular | Moderate | Low | Niche (tabular data) |

### Key findings by model family:

- **GPT-5 Nano / Gemini 2.5 Flash Lite**: YAML performed best. JSON performed poorly. Markdown was most token-efficient.
- **Llama 3.2 3B**: Showed little format sensitivity. JSON performed slightly best.
- **GPT-4 / GPT-4-turbo**: More robust to format variations. Markdown slightly preferred for reasoning.
- **Claude models**: Structured JSON outperformed on knowledge graph tasks. XML recommended by Anthropic for prompt sectioning.

### The emerging consensus:

The practical recommendation across multiple independent analyses is a **hybrid approach**:
- **Markdown** for instructions, context, and narrative content (token-efficient, human-readable, aligns with training data)
- **YAML** for structured configuration and data (token-efficient, good accuracy)
- **JSON Schema** for tool definitions and output validation (strict, machine-parseable)
- **XML tags** for prompt section boundaries when needed (all major providers support this)

---

## Conclusions

1. **JSON-LD is not appropriate for LLM agent instructions.** It is the worst-performing format in the only benchmark that directly tested it (KG-LLM-Bench), and it has 3-5x the token cost of alternatives.

2. **JSON-LD's strengths are in web SEO and knowledge graph alignment**, not in prompt engineering. Its linked data features help AI crawlers disambiguate entities during web indexing -- a completely different use case from defining agent behavior.

3. **Markdown is the best general-purpose format** for LLM agent instructions due to its token efficiency, alignment with training data, human readability, and strong performance across models.

4. **YAML is the best format for structured data** fed to LLMs, offering the best accuracy-to-cost ratio in recent benchmarks.

5. **No major AI agent framework uses JSON-LD** for agent behavior definition. The sole exception (LMOS) uses JSON-LD only for agent discovery metadata, not for instructions.

6. **The "graph structure helps LLMs understand relationships" claim is false** for in-context processing. LLMs process linear token sequences, and the graph overhead actively degrades performance.

7. **If you need structured, machine-parseable agent definitions**, plain JSON with JSON Schema validation is strictly superior to JSON-LD for LLM consumption. It provides the same structural rigor without the linked data overhead.

---

## Sources

### Academic Papers
- [Does Prompt Formatting Have Any Impact on LLM Performance? (arXiv:2411.10541)](https://arxiv.org/html/2411.10541v1/)
- [Prompt Engineering for Structured Data (William & Mary)](https://www.cs.wm.edu/~dcschmidt/PDF/Optimizing_Prompt_Styles_for_Structured_Data_Generation_in_LLM.pdf)
- [KG-LLM-Bench: Knowledge Graph Textualization for LLMs (arXiv:2504.07087)](https://arxiv.org/html/2504.07087v1)
- [A Survey of AI Agent Protocols (arXiv:2504.16736)](https://arxiv.org/html/2504.16736v1)
- [IBM: Formally Specifying the High-Level Behavior of LLM-Based Agents](https://github.com/IBM/llm-agent-framework)

### Benchmarks and Empirical Studies
- [Which Nested Data Format Do LLMs Understand Best? (ImprovingAgents)](https://www.improvingagents.com/blog/best-nested-data-format/)
- [JSON vs. YAML vs. Markdown: Token Benchmarks (shshell.com)](https://shshell.com/blog/token-efficiency-module-13-lesson-2-format-comparison)
- [YAML vs JSON for LLM Token Efficiency: The Minification Truth](https://curiouslychase.com/posts/yaml-vs-json-for-llm-token-efficiency-the-minification-truth/)
- [YAML Over JSON in LLM Applications (BlogOS)](https://blog.tashif.codes/blog/JSON-YAML-LLM)

### Industry Analysis and Blog Posts
- [Markdown vs. XML in LLM Prompts: A Comparative Analysis](https://www.robertodiasduarte.com.br/en/markdown-vs-xml-em-prompts-para-llms-uma-analise-comparativa/)
- [Marking Up the Prompt: How Markdown Formatting Influences LLM Responses (NeuralBuddies)](https://www.neuralbuddies.com/p/marking-up-the-prompt-how-markdown-formatting-influences-llm-responses)
- [Supercharge AI Prompts with Markdown for Better Results (Tenacity)](https://tenacity.io/snippets/supercharge-ai-prompts-with-markdown-for-better-results/)
- [Boosting AI Performance: LLM-Friendly Content in Markdown (Webex Developer)](https://developer.webex.com/blog/boosting-ai-performance-the-power-of-llm-friendly-content-in-markdown)
- [Cracking the Code: JSON or XML for Better Prompts (NexAI Labs)](https://www.nexailabs.com/blog/cracking-the-code-json-or-xml-for-better-prompts)
- [AI Prompts: Ditch JSON -- Use Markdown & Plain Text (Bachynski)](https://www.bachynski.blog/2025/11/ai-prompts-ditch-json-use-markdown.html)
- [Markdown vs JSON: Choosing the Right Format for LLM Prompts (WebcrawlerAPI)](https://webcrawlerapi.com/blog/markdown-vs-json-choosing-the-right-format-for-llm-prompts)

### JSON-LD for AI/SEO (Different Use Case)
- [The Comparative Effectiveness of llms.txt and JSON-LD in LLM Optimization](https://www.benallymarketing.com/post/the-comparative-effectiveness-of-llm-txt-and-json-ld-in-large-language-model-optimization)
- [Using JSON-LD to Strengthen LLM Understanding (Ranktracker)](https://www.ranktracker.com/blog/json-ld-strengthen-llm-understanding/)
- [JSON-LD Masterclass: Implementing Schema for AI Agents (Jasmine Directory)](https://www.jasminedirectory.com/blog/json-ld-masterclass-implementing-schema-for-ai-agents/)
- [How AI Engines Read Your JSON-LD, Schema, and Entities (WebTrek)](https://webtrek.io/blog/how-ai-engines-read-your-json-ld-schema-and-entities)
- [Do LLMs use JSON-LD beyond FAQPage and HowTo types? (Brandlight)](https://sat.brandlight.ai/articles/do-llms-use-json-ld-beyond-faqpage-and-howto-types)

### Agent Frameworks and Protocols
- [LMOS Protocol Documentation (Eclipse Foundation)](https://eclipse.dev/lmos/docs/lmos_protocol/introduction/)
- [agents.json Specification (Wildcard AI)](https://github.com/wild-card-ai/agents-json)
- [LLM-Based Agent Frameworks (EmergentMind)](https://www.emergentmind.com/topics/llm-based-agent-frameworks)
- [Structured Knowledge in a Lightweight Format (AgentNet)](https://agentnet.bearblog.dev/structured-knowledge-in-a-lightweight-format/)

### Token-Optimized Formats (Emerging)
- [TOON vs JSON: A Token-Optimized Data Format (Tensorlake)](https://tensorlake.ai/blog/toon-vs-json)
- [TOON vs JSON vs YAML vs CSV for LLM Applications](https://www.piotr-sikora.com/blog/2025-11-29-toon-format-comparison-csv-json-yaml)
- [Why JSON Is Inefficient for LLMs vs TOON and YAML (Scalevise)](https://scalevise.com/resources/json-vs-toon-yaml-llm-context-efficiency/)

### Standards
- [JSON-LD 1.1 W3C Specification](https://www.w3.org/TR/json-ld11/)
- [OpenAI Community: Markdown is 15% More Token Efficient Than JSON](https://community.openai.com/t/markdown-is-15-more-token-efficient-than-json/841742)
