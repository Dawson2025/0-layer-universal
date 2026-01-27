# Requests: Better AI System

## Organization

Requests are organized as a **Tree of Needs**, branching from a single root.

```
requests/
└── tree_of_needs/                           (DAG structure)
    └── 00_seamless_ai_collaboration/        ← ROOT NEED
        │
        ├── 01_capable/                      "Can AI do the work?"
        │   ├── need_01_persistent_knowledge
        │   ├── need_02_scalable_context
        │   ├── need_03_discoverable
        │   └── need_04_multimodal ⟷         (shared with 05_engaging)
        │
        ├── 02_continuous/                   "Does work keep going?"
        │   ├── need_01_tool_portable
        │   ├── need_02_session_resilient
        │   ├── need_03_failure_recoverable
        │   ├── need_04_evolvable
        │   ├── need_05_cross_platform
        │   ├── need_06_universal_rules_and_cross_device_access
        │   ├── need_07_resilient_system_state
        │   ├── need_08_universal_context_discovery
        │   └── need_09_universal_ai_tool_support
        │
        ├── 03_trustworthy/                  "Can I trust AI?"
        │   ├── need_01_rule_compliant
        │   ├── need_02_predictable
        │   └── need_03_bounded
        │
        ├── 04_observable/                   "Can I see what's happening?"
        │   ├── need_01_transparent
        │   ├── need_02_debuggable
        │   └── need_03_auditable
        │
        └── 05_engaging/                     "Is it enjoyable?"
            └── need_01_multimodal ⟷         (shared with 01_capable)

⟷ = Shared need (belongs to multiple branches)
```

---

## The Five Branches

| Branch | Core Question | Key Needs |
|--------|---------------|-----------|
| **01_capable** | Can AI do the work? | Knowledge, Scale, Discovery, Multimodal ⟷ |
| **02_continuous** | Does work keep going? | Portability, Resilience, Recovery, Evolution, Cross-Platform |
| **03_trustworthy** | Can I trust AI? | Rules, Predictability, Boundaries |
| **04_observable** | Can I see what's happening? | Transparency, Debugging, Auditing |
| **05_engaging** | Is it enjoyable? | Multimodal ⟷ |

⟷ = Shared need (multimodal belongs to both 01_capable and 05_engaging)

---

## Quick Reference

| Need | Key Question | Key Solution |
|------|--------------|--------------|
| **01_capable** | | |
| Persistent Knowledge | How does AI remember? | Hierarchical system prompts + referenced resources |
| Scalable Context | Does it scale? | Agent delegation + progressive disclosure |
| Discoverable | Can AI find things? | Clear hierarchy + self-describing prompts |
| Multimodal ⟷ | Can I speak, listen, see? | Voice I/O (Vibe Typer) + diagrams + rich interaction |
| **02_continuous** | | |
| Tool Portable | Can I switch tools? | Agnostic source of truth + tool derivations |
| Session Resilient | Can I pick up later? | Self-describing system + handoff documents |
| Failure Recoverable | What if something breaks? | Idempotent setup + rollback capability |
| Evolvable | Will it still work as AI evolves? | Modular architecture + forward-compatible formats |
| Cross-Platform | Works on Mac, Linux, Windows? | OS abstraction + config portability |
| Universal Rules & Cross-Device | Rules consistent? Can access remotely? | FHS locations + Syncthing + multi-user access |
| Resilient System State | Survives storage failures? | Multi-tier redundancy + recovery partitions + backups |
| Context Discovery | Can find context anywhere? | Universal discovery protocol + 5-tier storage |
| AI Tool Support | Works with any AI tool? | Unified access API + tool adapters + cross-tool sync |
| **03_trustworthy** | | |
| Rule Compliant | Does AI follow rules? | Rule hierarchies + conflict resolution |
| Predictable | Is behavior consistent? | Version tracking + consistent patterns |
| Bounded | Does AI stay in scope? | Scope definitions + permission model |
| **04_observable** | | |
| Transparent | Can I see AI state? | State inspection + decision visibility |
| Debuggable | Can I diagnose issues? | Validation suite + error messages |
| Auditable | Can I review history? | Change tracking + audit trails |
| **05_engaging** | | |
| Multimodal ⟷ | Can I speak, listen, see? | Voice I/O (Vibe Typer) + diagrams + rich interaction |

---

## Reading Order

1. Start with [tree_of_needs](./tree_of_needs/) overview
2. Read [00_seamless_ai_collaboration](./tree_of_needs/00_seamless_ai_collaboration/) root need
3. Explore each branch as relevant
4. Dive into specific needs for detailed requirements
