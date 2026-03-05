---
resource_id: "5c552cae-373f-45e1-93d9-56fe4ab037a9"
resource_type: "knowledge"
resource_name: "system_architecture_diagram"
---
# Agent Delegation System — Architecture Diagrams

Comprehensive Mermaid.js diagrams showing how all components of the agent delegation system connect and fit within the greater layer-stage system.

---

<!-- section_id: "a5752550-415f-47e4-aa4e-a8f003f6f5e9" -->
## 1. Entity Hierarchy and Position in the Greater System

Where ADS sits in the layer-stage hierarchy, its children, and the universal artifacts it produces.

```mermaid
graph TB
    ROOT["0_layer_universal<br/>Root Manager"]
    ROOT_AG["Root .0agnostic/<br/>11 Guides, 10 Principles<br/>5 Rules, 1 Protocol"]
    LSS["layer_stage_system<br/>Layer 0 Feature"]
    ADS["agent_delegation_system<br/>Layer 1 - CANONICAL WORKSPACE"]
    S01["Stage 01<br/>Request Gathering<br/>9 requirements"]
    S02["Stage 02<br/>Research<br/>4 formal topics"]
    S04["Stage 04<br/>Design<br/>10 decisions"]
    S06["Stage 06<br/>Development<br/>Universal artifacts"]
    MEM["memory_system<br/>Layer 2<br/>24 research docs"]
    MULTI["multi_agent_system<br/>Layer 2<br/>Scaffolded"]
    CCS["context_chain_system<br/>Layer 3<br/>76 PASS tests<br/>WORKING EXAMPLE"]
    WS_RULE["Workspace Rule<br/>Dynamic rule at root"]

    ROOT --> LSS
    LSS --> ADS
    ADS --> S01
    ADS --> S02
    ADS --> S04
    ADS --> S06
    ADS --> MEM
    ADS --> MULTI
    MEM --> CCS

    S06 -.->|produces| ROOT_AG
    CCS -.->|validates| ROOT_AG
    WS_RULE -.->|routes to| ADS
    ROOT --- ROOT_AG

    style ADS fill:#1a365d,color:#fff,stroke:#2b6cb0
    style ROOT_AG fill:#2d3748,color:#fff
    style CCS fill:#2f855a,color:#fff
    style WS_RULE fill:#c53030,color:#fff
```

---

<!-- section_id: "41929b3c-4396-4a1e-bf25-1b4dea1a2e13" -->
## 2. Research-to-Production Pipeline

How research findings flow through design decisions into universal artifacts.

```mermaid
graph LR
    R1["Research:<br/>Tool Context Cascading<br/>3/4 cascade natively"]
    R2["Research:<br/>Multi-Agent Patterns<br/>CrewAI, LangGraph, AutoGen"]
    R3["Research:<br/>Scope Boundary Traversal<br/>Directional patterns"]
    R4["Research:<br/>Class/Object Patterns<br/>SOLID validated"]

    D1["Design:<br/>Minimal Context Model<br/>Own STATIC + neighbors<br/>+ on-demand"]
    D2["Design:<br/>Directional Scope<br/>Boundaries<br/>3-step process"]
    D3["Design:<br/>Context Propagation<br/>Funnel"]
    D4["Design:<br/>Two-Halves Pattern<br/>STATIC + Current State"]

    A1["Artifact:<br/>11 Stage Guides"]
    A2["Artifact:<br/>10 Principles"]
    A3["Artifact:<br/>Scope Boundary Rule"]
    A4["Artifact:<br/>Stage Report Protocol"]
    A5["Artifact:<br/>Agent Template"]

    R1 -->|validates| D1
    R2 -->|validates| D1
    R3 -->|informs| D2
    R4 -->|validates| D1
    R4 -->|validates| D2

    D1 -->|shapes| A1
    D1 -->|shapes| A5
    D2 -->|produces| A3
    D2 -->|updates| A2
    D3 -->|produces| A4
    D4 -->|produces| A5

    style R1 fill:#2b6cb0,color:#fff
    style R2 fill:#2b6cb0,color:#fff
    style R3 fill:#2b6cb0,color:#fff
    style R4 fill:#2b6cb0,color:#fff
    style D1 fill:#6b46c1,color:#fff
    style D2 fill:#6b46c1,color:#fff
    style D3 fill:#6b46c1,color:#fff
    style D4 fill:#6b46c1,color:#fff
    style A1 fill:#2f855a,color:#fff
    style A2 fill:#2f855a,color:#fff
    style A3 fill:#2f855a,color:#fff
    style A4 fill:#2f855a,color:#fff
    style A5 fill:#2f855a,color:#fff
```

---

<!-- section_id: "71e0cba3-6028-4108-adf4-06aaf4e87f4d" -->
## 3. Consolidation Funnel

How information propagates from stage outputs up to the entity source of truth, and how universal artifacts cascade down to all agents.

```mermaid
graph TB
    subgraph BOTTOM_UP["Bottom-Up Consolidation"]
        OUT["Stage Outputs<br/>outputs/by_topic/<br/>outputs/design_decisions/"]
        ORPT["Output Report<br/>outputs/reports/output_report.md"]
        DOT_AG["Stage .0agnostic/<br/>Structured knowledge and rules"]
        SRPT["Stage Report<br/>.0agnostic/.../stage_report.md<br/>Manager-readable summary"]
        S0AG["Stage 0AGNOSTIC.md<br/>Entry point with status"]

        OUT --> ORPT
        ORPT --> DOT_AG
        DOT_AG --> SRPT
        SRPT --> S0AG
    end

    subgraph ENTITY_LEVEL["Entity Consolidation"]
        STAGES_RPT["stages_report.md<br/>All stage reports combined"]
        CHILD_RPT["child_layers_report.md<br/>All child reports combined"]
        LAYER_RPT["layer_report.md<br/>Entity summary for parent"]
        E0AG["Entity 0AGNOSTIC.md<br/>MOST consolidated<br/>Comes LAST not first"]

        STAGES_RPT --> LAYER_RPT
        CHILD_RPT --> LAYER_RPT
        LAYER_RPT --> E0AG
    end

    subgraph TOP_DOWN["Top-Down Cascade"]
        ROOT_AG["Root .0agnostic/<br/>Universal artifacts"]
        SYNC["agnostic-sync.sh"]
        TOOLS["CLAUDE.md, AGENTS.md<br/>GEMINI.md, OPENAI.md<br/>All agents read these"]

        ROOT_AG --> SYNC
        SYNC --> TOOLS
    end

    S0AG -.->|feeds into| STAGES_RPT
    E0AG -.->|dev stage produces| ROOT_AG

    style OUT fill:#2b6cb0,color:#fff
    style E0AG fill:#1a365d,color:#fff
    style ROOT_AG fill:#2f855a,color:#fff
    style TOOLS fill:#2f855a,color:#fff
```

---

<!-- section_id: "12bc77a8-9c8c-4931-bf0d-c0699c5b6fe8" -->
## 4. Canonical Workspace Pattern

How agents anywhere in the system recognize delegation work and traverse to ADS.

```mermaid
graph TB
    AGENT["Any Agent<br/>Encounters delegation work"]
    RECOGNIZE["Recognize out-of-scope<br/>Delegation keywords detected"]

    TRIGGER_ROOT["Root 0AGNOSTIC.md<br/>Trigger: Modifying<br/>agent delegation"]
    TRIGGER_RULE["Workspace Rule<br/>.0agnostic/02_rules/dynamic/<br/>Keywords and actions"]
    TRIGGER_BACK["Backward Pointers<br/>In Principles and Rules<br/>Canonical Workspace section"]

    PROTOCOL["Update Protocol<br/>7-step workflow<br/>.0agnostic/03_protocols/"]
    SELECT{"Select Stage"}
    S01W["01 Requirements"]
    S02W["02 Research"]
    S04W["04 Design"]
    S06W["06 Development"]
    PROPAGATE["Propagate through<br/>consolidation funnel"]
    RESULT["Updated Universal Artifacts<br/>Root .0agnostic/"]

    AGENT --> RECOGNIZE
    RECOGNIZE -->|Principle 8| TRIGGER_ROOT
    TRIGGER_ROOT --> TRIGGER_RULE
    TRIGGER_RULE -->|traverse to ADS| PROTOCOL
    TRIGGER_BACK -.->|backward pointers| PROTOCOL
    PROTOCOL --> SELECT
    SELECT --> S01W
    SELECT --> S02W
    SELECT --> S04W
    SELECT --> S06W
    S01W --> PROPAGATE
    S02W --> PROPAGATE
    S04W --> PROPAGATE
    S06W --> PROPAGATE
    PROPAGATE --> RESULT
    RESULT -.->|cascade via<br/>agnostic-sync| AGENT

    style AGENT fill:#718096,color:#fff
    style TRIGGER_RULE fill:#c53030,color:#fff
    style PROTOCOL fill:#1a365d,color:#fff
    style RESULT fill:#2f855a,color:#fff
```

---

<!-- section_id: "f51e51ef-83ad-41f9-913d-38ea08f50a18" -->
## 5. OOP-to-Agent Architecture Mapping

How object-oriented programming concepts map to the agent delegation architecture.

```mermaid
graph LR
    subgraph OOP["OOP Concepts"]
        BC["Base Class"]
        ABC["Abstract Class"]
        CC["Concrete Class"]
        IF["Interface"]
        PRIV["Private Methods"]
        HELPER["Helper / Utility"]
        COMP["Composition"]
        SRP_C["Single Responsibility"]
        FACTORY["Factory Pattern"]
        DI["Dependency Injection"]
    end

    subgraph AGENTS["Agent Architecture"]
        UNIV["Universal Infrastructure<br/>Root .0agnostic/"]
        TEMPLATE["Stage Agent Template<br/>STAGE_AGENT_TEMPLATE.md"]
        STAGE_AG["Stage 0AGNOSTIC.md<br/>Specific methodology"]
        STATIC["STATIC Section<br/>Identity, Triggers, I/O"]
        DYNAMIC["DYNAMIC + Outputs<br/>On-demand only"]
        RULES_P["Rules + Protocols<br/>Reusable across agents"]
        ON_DEMAND["On-Demand Loading<br/>Compose from sources"]
        STAGE_F["Stage Agents<br/>Research / Design / Dev"]
        P8_INST["Principle 8<br/>Spawn agent for scope"]
        MGR_DEL["Manager Delegation<br/>Task + pointer provided"]
    end

    BC --> UNIV
    ABC --> TEMPLATE
    CC --> STAGE_AG
    IF --> STATIC
    PRIV --> DYNAMIC
    HELPER --> RULES_P
    COMP --> ON_DEMAND
    SRP_C --> STAGE_F
    FACTORY --> P8_INST
    DI --> MGR_DEL

    style OOP fill:#6b46c1,color:#fff
    style AGENTS fill:#2b6cb0,color:#fff
```

---

<!-- section_id: "f09020b1-661d-4f4d-931d-b1b64be18b44" -->
## 6. Complete System Overview

The full picture: how research, design, artifacts, validation, and the canonical workspace loop all connect.

```mermaid
graph TB
    NEEDS["Tree of Needs<br/>9 requirements, 3 branches"]
    EXTERNAL["External Research<br/>Frameworks, tools, OOP"]

    RESEARCH["Stage 02: Research<br/>4 Topics"]
    DESIGN["Stage 04: Design<br/>10 Decisions"]
    DEV["Stage 06: Development<br/>Produces artifacts"]

    FUNNEL["Consolidation Funnel<br/>stage outputs to<br/>stage reports to<br/>entity 0AGNOSTIC.md"]
    SYNC["agnostic-sync.sh<br/>Generates tool files"]

    UA["Universal Artifacts<br/>Root .0agnostic/<br/>11 Guides, 10 Principles<br/>5 Rules, 1 Protocol"]

    CCS["context_chain_system<br/>76 PASS tests<br/>All 11 stages populated"]

    WS_RULE["Workspace Rule<br/>Triggers on keywords"]
    WS_PROTO["Update Protocol<br/>7-step workflow"]
    WS_BACK["Backward Pointers<br/>In Principles + Rules"]

    ANY["Any Agent<br/>encounters delegation work"]

    NEEDS --> RESEARCH
    EXTERNAL --> RESEARCH
    RESEARCH --> DESIGN
    DESIGN --> DEV

    DEV -->|produces| UA
    DEV -->|updates| FUNNEL
    FUNNEL --> SYNC

    UA -->|cascade down| CCS
    CCS -->|validates| UA

    ANY -->|Principle 8| WS_RULE
    WS_RULE -->|routes to| WS_PROTO
    WS_PROTO -->|directs to| RESEARCH
    WS_BACK -.->|points from| UA

    style UA fill:#2f855a,color:#fff
    style CCS fill:#2f855a,color:#fff
    style WS_RULE fill:#c53030,color:#fff
    style WS_PROTO fill:#c53030,color:#fff
    style ANY fill:#718096,color:#fff
    style RESEARCH fill:#2b6cb0,color:#fff
    style DESIGN fill:#6b46c1,color:#fff
    style DEV fill:#1a365d,color:#fff
```

---

<!-- section_id: "27d78fbb-d245-4668-9490-564ed9a0575f" -->
## 7. Three-Tier Knowledge Model

How knowledge is structured at each tier, from pointers to full detail.

```mermaid
graph LR
    subgraph TIER1["Tier 1: Pointers"]
        T1A["0AGNOSTIC.md"]
        T1B["Identity + scope"]
        T1C["Navigation refs"]
        T1D["Current status"]
    end

    subgraph TIER2["Tier 2: Distilled"]
        T2A[".0agnostic/"]
        T2B["01_knowledge/"]
        T2C["02_rules/"]
        T2D["03_protocols/"]
    end

    subgraph TIER3["Tier 3: Full"]
        T3A["Stage Outputs"]
        T3B["Research notes"]
        T3C["Design specs"]
        T3D["Test results"]
    end

    TIER1 -->|points to| TIER2
    TIER2 -->|summarizes| TIER3

    MGR["Manager<br/>Reads Tier 1"]
    STG["Stage Agent<br/>Loads Tier 2"]
    WKR["In-Stage Worker<br/>Reads Tier 3"]

    MGR -.-> TIER1
    STG -.-> TIER2
    WKR -.-> TIER3

    style TIER1 fill:#2f855a,color:#fff
    style TIER2 fill:#2b6cb0,color:#fff
    style TIER3 fill:#6b46c1,color:#fff
```

---

<!-- section_id: "39e6e334-90a4-422d-a563-203d64a9bac9" -->
## 8. Agent Context Model

What each agent loads: always, compact neighbors, on-demand, and never.

```mermaid
graph TB
    subgraph ALWAYS["Always Loaded - STATIC"]
        OWN["Own 0AGNOSTIC.md<br/>Identity, methodology<br/>triggers, current status"]
        TOOL_F["Tool file - CLAUDE.md<br/>Auto-generated from<br/>0AGNOSTIC.md STATIC"]
    end

    subgraph COMPACT["Compact Neighbor Interfaces"]
        PAR["Parent STATIC section<br/>Identity + triggers only"]
        SIB["Sibling stage reports<br/>Under 30 lines each"]
        CHD["Child layer reports<br/>Consolidated summaries"]
    end

    subgraph ONDEMAND["On-Demand - DYNAMIC"]
        PAR_K["Parent knowledge/<br/>Specific file only"]
        RULES["Applicable rules<br/>Loaded when triggered"]
        PROTO["Relevant protocols<br/>Loaded when needed"]
        FULL["Full stage outputs<br/>Only when in-stage"]
    end

    subgraph REJECTED["Never Loaded - Rejected"]
        NO1["Full ancestor cascade<br/>Context waste at depth"]
        NO2["All parent knowledge<br/>Overflows context window"]
        NO3["Sibling full outputs<br/>Irrelevant to work"]
    end

    style ALWAYS fill:#2f855a,color:#fff
    style COMPACT fill:#2b6cb0,color:#fff
    style ONDEMAND fill:#6b46c1,color:#fff
    style REJECTED fill:#c53030,color:#fff
```

---

<!-- section_id: "f0752d68-527e-468b-9c0f-6f0fcf2e4ee2" -->
## Diagram Index

| # | Diagram | Shows |
|---|---------|-------|
| 1 | Entity Hierarchy | Where ADS sits, its children, and universal artifact production |
| 2 | Research-to-Production Pipeline | How 4 research topics flow to 10 design decisions flow to universal artifacts |
| 3 | Consolidation Funnel | Bottom-up propagation from stage outputs to entity source of truth |
| 4 | Canonical Workspace Pattern | How agents recognize delegation work and traverse to ADS |
| 5 | OOP-to-Agent Mapping | How class/object patterns map to agent architecture concepts |
| 6 | Complete System Overview | Full picture of all components and their connections |
| 7 | Three-Tier Knowledge | Pointer to Distilled to Full knowledge tiers |
| 8 | Agent Context Model | What each agent loads: always, compact, on-demand, never |
