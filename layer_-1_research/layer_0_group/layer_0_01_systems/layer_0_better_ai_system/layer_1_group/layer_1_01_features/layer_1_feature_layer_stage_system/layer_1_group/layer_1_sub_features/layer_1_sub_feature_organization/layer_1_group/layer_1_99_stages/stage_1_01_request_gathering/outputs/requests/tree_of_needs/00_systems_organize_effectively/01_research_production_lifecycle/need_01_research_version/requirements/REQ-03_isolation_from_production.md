---
resource_id: "898010ab-bb8f-4bf3-abdd-f81ec2c4f7c3"
resource_type: "output"
resource_name: "REQ-03_isolation_from_production"
---
# Isolation from Production

**Need**: [Research Version](../README.md)

---

- MUST NOT allow research entity changes to automatically propagate to production
- MUST require explicit promotion workflow to move research findings to production
- SHOULD allow research entities to read production content (reference, not modify)
- SHOULD track which research findings have been promoted and which are pending
