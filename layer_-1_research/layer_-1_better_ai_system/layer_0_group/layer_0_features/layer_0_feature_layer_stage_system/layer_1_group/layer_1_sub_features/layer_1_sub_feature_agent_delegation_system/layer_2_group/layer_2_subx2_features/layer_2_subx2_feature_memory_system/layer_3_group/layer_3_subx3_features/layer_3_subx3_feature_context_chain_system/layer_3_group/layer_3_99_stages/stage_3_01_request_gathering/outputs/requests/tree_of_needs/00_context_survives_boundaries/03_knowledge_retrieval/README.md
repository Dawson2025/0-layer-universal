# Branch: Knowledge is RETRIEVABLE

**Parent**: [00_context_survives_boundaries](../)

---

## Core Question

> "How do agents find and load the right context efficiently?"

---

## Description

Even well-organized, well-maintained knowledge is useless if agents can't find it. Currently agents guess which files to read or follow manual pointers. Retrieval should be scored (which context is most relevant?) and validated (is the chain intact?).

The two failure modes:
1. **Manual retrieval** → agent loads wrong files, misses relevant context, wastes tokens on irrelevant content
2. **No validation** → agent follows a reference to a moved/deleted file, gets nothing, loses competence

---

## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_scored_retrieval](./need_01_scored_retrieval/) | "Which context is most relevant right now?" | Rank context by recency × relevance × importance |
| [need_02_chain_validation](./need_02_chain_validation/) | "Is the context chain intact?" | Validate references against knowledge graph |

---

## Key Insight

Retrieval in the brain uses spreading activation — related concepts activate each other based on strength of connection. The knowledge graph provides the connection structure; scored retrieval provides the activation strength. Together they replace manual file selection with principled context loading.
