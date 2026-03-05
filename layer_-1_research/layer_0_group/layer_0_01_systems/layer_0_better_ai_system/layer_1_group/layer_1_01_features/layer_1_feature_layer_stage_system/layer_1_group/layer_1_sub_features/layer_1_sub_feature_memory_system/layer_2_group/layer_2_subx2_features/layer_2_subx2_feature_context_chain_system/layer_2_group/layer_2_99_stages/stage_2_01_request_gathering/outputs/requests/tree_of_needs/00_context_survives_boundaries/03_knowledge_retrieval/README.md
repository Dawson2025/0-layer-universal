---
resource_id: "69443c2f-55d4-456a-b7a2-bf1fa05beaa1"
resource_type: "readme
output"
resource_name: "README"
---
# Branch: Knowledge is RETRIEVABLE

**Parent**: [00_context_survives_boundaries](../)

---

<!-- section_id: "5bc63fa0-cc24-407f-9a11-02b8f76cc97b" -->
## Core Question

> "How do agents find and load the right context efficiently?"

---

<!-- section_id: "3b12a5b4-dbee-49c7-bffa-210b8252098b" -->
## Description

Even well-organized, well-maintained knowledge is useless if agents can't find it. Currently agents guess which files to read or follow manual pointers. Retrieval should be scored (which context is most relevant?) and validated (is the chain intact?).

The two failure modes:
1. **Manual retrieval** → agent loads wrong files, misses relevant context, wastes tokens on irrelevant content
2. **No validation** → agent follows a reference to a moved/deleted file, gets nothing, loses competence

---

<!-- section_id: "bdb70ea8-6da1-49a1-83ca-12f6e60bf6f9" -->
## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_scored_retrieval](./need_01_scored_retrieval/) | "Which context is most relevant right now?" | Rank context by recency × relevance × importance |
| [need_02_chain_validation](./need_02_chain_validation/) | "Is the context chain intact?" | Validate references against knowledge graph |
| [need_03_auto_discovery](./need_03_auto_discovery/) | "Will agents find critical protocols without being told?" | Auto-discovery of update protocols and propagation chain |

---

<!-- section_id: "2fd1484e-5e6d-499d-9d8a-f7ae3d75e621" -->
## Key Insight

Retrieval in the brain uses spreading activation — related concepts activate each other based on strength of connection. The knowledge graph provides the connection structure; scored retrieval provides the activation strength. Together they replace manual file selection with principled context loading.
