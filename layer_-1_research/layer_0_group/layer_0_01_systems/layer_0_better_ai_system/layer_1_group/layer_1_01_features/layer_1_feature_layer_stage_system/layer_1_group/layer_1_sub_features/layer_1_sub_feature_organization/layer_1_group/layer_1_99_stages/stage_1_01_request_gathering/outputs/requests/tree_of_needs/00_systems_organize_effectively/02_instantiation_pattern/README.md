---
resource_id: "5e40d7ad-75fb-4601-a5fd-fbeece52af29"
resource_type: "readme_output"
resource_name: "README"
---
# Branch 02: Instantiation Pattern

**Question**: How do systems create per-user or per-context instances?

<!-- section_id: "e689ae24-3966-4e00-8ffb-86b99b6a8e38" -->
## Needs

| # | Need | What It Answers |
|---|------|----------------|
| 01 | [System Features](need_01_system_features/) | How are system-wide capabilities organized? |
| 02 | [System Instantiations](need_02_system_instantiations/) | How are per-user instances created? |
| 03 | [Instance Context](need_03_instance_context/) | What context does each instance carry? |
| 04 | [Feature to Instance Flow](need_04_feature_to_instance_flow/) | How do new features reach instances? |

<!-- section_id: "2ad88460-a37c-42dd-a33a-9d0bf3d6b39f" -->
## Key Insight

Features and instances serve fundamentally different purposes. **Features** are R&D — they add capabilities to the system. **Instances** are operational — they personalize the system for a specific user or context. They need different organizational structures but the same foundational pattern.
