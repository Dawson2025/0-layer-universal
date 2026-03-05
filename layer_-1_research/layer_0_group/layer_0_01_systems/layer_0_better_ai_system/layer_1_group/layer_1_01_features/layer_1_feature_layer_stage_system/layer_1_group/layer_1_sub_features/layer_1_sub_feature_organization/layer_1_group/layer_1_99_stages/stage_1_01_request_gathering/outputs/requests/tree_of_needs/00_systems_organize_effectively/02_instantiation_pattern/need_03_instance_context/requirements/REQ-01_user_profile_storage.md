---
resource_id: "63fa8056-6db2-4808-a5e8-bc5af6a7422b"
resource_type: "output"
resource_name: "REQ-01_user_profile_storage"
---
# User Profile Storage

**Need**: [Instance Context](../README.md)

---

- MUST store user profile in the instance entity's `0AGNOSTIC.md` or `.0agnostic/01_knowledge/`
- MUST include: user name, role, preferences, access level
- SHOULD support profile updates as the user's situation changes
- SHOULD NOT store sensitive credentials — profile is identity, not authentication
