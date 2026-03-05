---
resource_id: "4d5f3ee7-0e0d-445d-8e53-e0d6d0635b44"
resource_type: "output"
resource_name: "REQ-02_instance_upgrade_protocol"
---
# Instance Upgrade Protocol

**Need**: [Feature to Instance Flow](../README.md)

---

- SHOULD define a protocol for upgrading existing instances to new template versions
- SHOULD preserve all instance-specific context during upgrade
- SHOULD validate that the upgrade doesn't break instance functionality
- MAY support selective feature adoption (instance opts into specific features)
