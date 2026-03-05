---
resource_id: "15530047-9250-4af6-b144-9edd8cfbc5ad"
resource_type: "output"
resource_name: "REQ-02_chain_depth_for_agent_types"
---
# Chain Depth for Agent Types

**Need**: [Context Chain Support](../README.md)

---

- MUST define the appropriate chain depth for each agent type (how far up the hierarchy to load)
- SHOULD limit manager chain depth to: self + parent + grandparent (3 levels)
- SHOULD limit stage agent chain depth to: self + parent entity (2 levels)
- MUST NOT load the entire chain from root to leaf for every agent -- only what is needed
