# resource_id: "45144598-7bc0-4fe2-8fa2-ec6a14b1747d"
# resource_type: "knowledge"
# resource_name: "upgrade-orchestrator-gab"
# upgrade-orchestrator-gab.jq — Upgrades a stub orchestrator to full GAB compliance
# Usage: jq -f upgrade-orchestrator-gab.jq <stub.gab.jsonld> > <output.gab.jsonld>
#
# Adds: mode actors, state actors, personas, isolated states, missing fields
# Preserves: existing extends, projectOverrides, inheritance, templateInfo

# Get the prefix used by the LLMAgent (e.g., "orch:")
(."@graph"[] | select(."@type" == "gab:LLMAgent") | ."@id" | split(":")[0]) as $prefix |

# Get the layer number for context
(."@graph"[] | select(."@type" == "gab:LLMAgent") | .layer // 0) as $layer |

# Get the LLMAgent @id
(."@graph"[] | select(."@type" == "gab:LLMAgent") | ."@id") as $agent_id |

# 1. Add missing fields to LLMAgent
.["@graph"] |= map(
  if ."@type" == "gab:LLMAgent" then
    . + {
      "actorNameConsistency": "Actor names must be conserved between different sessions",
      "personaNameConsistency": "Persona human names must be conserved between different sessions (detect user language and use appropriate names)"
    }
  else . end
) |

# 2. Add purpose, constraints, contains, precedes, isolatedState to Modes
.["@graph"] |= map(
  if ."@id" == "orch:ReceiveMode" then . + {
    "purpose": ("Layer " + ($layer | tostring) + " orchestrator: receive incoming tasks from parent or child results"),
    "constraints": ["Check hand_off_documents/incoming/ for tasks", "Validate task is within scope", "Do NOT proceed to DelegationMode until task is parsed"],
    "contains": ["orch:ReceivePersona1", "orch:ReceivePersona2"],
    "isolatedState": "orch:ReceiveModeState",
    "initialMode": true,
    "precedes": ["orch:DelegationMode"]
  }
  elif ."@id" == "orch:DelegationMode" then . + {
    "purpose": ("Layer " + ($layer | tostring) + " orchestrator: decompose tasks and spawn child agents"),
    "constraints": ["Check resource budget before spawning", "Select appropriate agent type for subtasks", "Write task files to hand_off_documents/outgoing/", "Do NOT spawn beyond depth limit"],
    "contains": ["orch:DelegationPersona1", "orch:DelegationPersona2"],
    "isolatedState": "orch:DelegationModeState",
    "precedes": ["orch:MonitoringMode"]
  }
  elif ."@id" == "orch:MonitoringMode" then . + {
    "purpose": ("Layer " + ($layer | tostring) + " orchestrator: track progress of spawned child agents"),
    "constraints": ["Poll status files for child updates", "Detect timeouts and failures", "Handle failed children: retry, reassign, or escalate", "Do NOT proceed to AggregationMode until all children complete or timeout"],
    "contains": ["orch:MonitoringPersona1", "orch:MonitoringPersona2"],
    "isolatedState": "orch:MonitoringModeState",
    "precedes": ["orch:AggregationMode"]
  }
  elif ."@id" == "orch:AggregationMode" then . + {
    "purpose": ("Layer " + ($layer | tostring) + " orchestrator: collect and synthesize results from child agents"),
    "constraints": ["Collect result files from children", "Handle partial results from failed children", "Synthesize unified result", "Build confidence score"],
    "contains": ["orch:AggregationPersona1", "orch:AggregationPersona2"],
    "isolatedState": "orch:AggregationModeState",
    "precedes": ["orch:ReportMode"]
  }
  elif ."@id" == "orch:ReportMode" then . + {
    "purpose": ("Layer " + ($layer | tostring) + " orchestrator: report aggregated results to parent or user"),
    "constraints": ["Write result to hand_off_documents/outgoing/to_above/", "Include audit trail", "Clean up completed artifacts", "Transition back to ReceiveMode"],
    "contains": ["orch:ReportPersona1", "orch:ReportPersona2"],
    "isolatedState": "orch:ReportModeState",
    "precedes": ["orch:ReceiveMode"]
  }
  else . end
) |

# 3. Add 10 Mode Actors
.["@graph"] += [
  {"@id": "orch:ReceiveActor1", "@type": "gab:Actor", "id": "ReceiveActor1", "operatesIn": ["orch:ReceiveMode"], "activeMode": "orch:ReceiveMode", "persona": "orch:ReceivePersona1", "role": "Senior", "sessionConsistent": true},
  {"@id": "orch:ReceiveActor2", "@type": "gab:Actor", "id": "ReceiveActor2", "operatesIn": ["orch:ReceiveMode"], "activeMode": "orch:ReceiveMode", "persona": "orch:ReceivePersona2", "role": "Junior", "sessionConsistent": true},
  {"@id": "orch:DelegationActor1", "@type": "gab:Actor", "id": "DelegationActor1", "operatesIn": ["orch:DelegationMode"], "activeMode": "orch:DelegationMode", "persona": "orch:DelegationPersona1", "role": "Senior", "sessionConsistent": true},
  {"@id": "orch:DelegationActor2", "@type": "gab:Actor", "id": "DelegationActor2", "operatesIn": ["orch:DelegationMode"], "activeMode": "orch:DelegationMode", "persona": "orch:DelegationPersona2", "role": "Junior", "sessionConsistent": true},
  {"@id": "orch:MonitoringActor1", "@type": "gab:Actor", "id": "MonitoringActor1", "operatesIn": ["orch:MonitoringMode"], "activeMode": "orch:MonitoringMode", "persona": "orch:MonitoringPersona1", "role": "Senior", "sessionConsistent": true},
  {"@id": "orch:MonitoringActor2", "@type": "gab:Actor", "id": "MonitoringActor2", "operatesIn": ["orch:MonitoringMode"], "activeMode": "orch:MonitoringMode", "persona": "orch:MonitoringPersona2", "role": "Junior", "sessionConsistent": true},
  {"@id": "orch:AggregationActor1", "@type": "gab:Actor", "id": "AggregationActor1", "operatesIn": ["orch:AggregationMode"], "activeMode": "orch:AggregationMode", "persona": "orch:AggregationPersona1", "role": "Senior", "sessionConsistent": true},
  {"@id": "orch:AggregationActor2", "@type": "gab:Actor", "id": "AggregationActor2", "operatesIn": ["orch:AggregationMode"], "activeMode": "orch:AggregationMode", "persona": "orch:AggregationPersona2", "role": "Junior", "sessionConsistent": true},
  {"@id": "orch:ReportActor1", "@type": "gab:Actor", "id": "ReportActor1", "operatesIn": ["orch:ReportMode"], "activeMode": "orch:ReportMode", "persona": "orch:ReportPersona1", "role": "Senior", "sessionConsistent": true},
  {"@id": "orch:ReportActor2", "@type": "gab:Actor", "id": "ReportActor2", "operatesIn": ["orch:ReportMode"], "activeMode": "orch:ReportMode", "persona": "orch:ReportPersona2", "role": "Junior", "sessionConsistent": true}
] |

# 4. Add 4 more State Actors (stubs have 1: ProjectContextStateActor)
.["@graph"] += [
  {"@id": "orch:LayerStateActor", "@type": "gab:Actor", "id": "LayerStateActor", "operatesIn": ["orch:ReceiveMode", "orch:DelegationMode", "orch:MonitoringMode", "orch:AggregationMode", "orch:ReportMode"], "activeMode": null, "persona": "orch:LayerStatePersona", "role": "StateManager", "sessionConsistent": true, "purpose": "Track current layer position and inheritance chain"},
  {"@id": "orch:ChildRegistryStateActor", "@type": "gab:Actor", "id": "ChildRegistryStateActor", "operatesIn": ["orch:DelegationMode", "orch:MonitoringMode", "orch:AggregationMode", "orch:ReportMode"], "activeMode": null, "persona": "orch:ChildRegistryStatePersona", "role": "StateManager", "sessionConsistent": true, "purpose": "Track all spawned child agents and their status"},
  {"@id": "orch:TaskStateActor", "@type": "gab:Actor", "id": "TaskStateActor", "operatesIn": ["orch:ReceiveMode", "orch:DelegationMode", "orch:MonitoringMode", "orch:AggregationMode", "orch:ReportMode"], "activeMode": null, "persona": "orch:TaskStatePersona", "role": "StateManager", "sessionConsistent": true, "purpose": "Track active tasks and their decomposition"},
  {"@id": "orch:ResourceBudgetStateActor", "@type": "gab:Actor", "id": "ResourceBudgetStateActor", "operatesIn": ["orch:DelegationMode", "orch:MonitoringMode"], "activeMode": null, "persona": "orch:ResourceBudgetStatePersona", "role": "StateManager", "sessionConsistent": true, "purpose": "Enforce resource limits: recursion depth, concurrent agents, timeouts"}
] |

# 5. Add 14 more Personas (stubs have 1: ProjectContextStatePersona)
.["@graph"] += [
  {"@id": "orch:ReceivePersona1", "@type": "gab:Persona", "name": "Senior Task Analyst", "role": "senior", "personality": "Thorough, analytical, ensures completeness before proceeding", "responsibilities": ["Parse incoming task files", "Classify task type and complexity", "Validate scope boundaries", "Determine local vs delegation", "Brief junior on findings"], "mode": "orch:ReceiveMode", "actor": "orch:ReceiveActor1", "canMessage": ["orch:ReceivePersona2", "orch:DelegationPersona1", "user"], "canReceiveFrom": ["user", "orch:ReceivePersona2", "orch:ReportPersona1"], "sessionConsistent": true},
  {"@id": "orch:ReceivePersona2", "@type": "gab:Persona", "name": "Junior Task Analyst", "role": "junior", "personality": "Efficient, detail-oriented, handles routine execution", "responsibilities": ["Validate JSON task format", "Check file integrity", "Log incoming tasks", "Flag anomalies to senior", "Prepare task summary"], "mode": "orch:ReceiveMode", "actor": "orch:ReceiveActor2", "canMessage": ["orch:ReceivePersona1"], "canReceiveFrom": ["orch:ReceivePersona1"], "sessionConsistent": true},
  {"@id": "orch:DelegationPersona1", "@type": "gab:Persona", "name": "Senior Delegation Strategist", "role": "senior", "personality": "Strategic, balances workload and agent capabilities", "responsibilities": ["Decompose complex tasks into subtasks", "Select appropriate agent types", "Check resource budget before spawning", "Design delegation strategy", "Review junior delegation plans", "Handle edge cases"], "mode": "orch:DelegationMode", "actor": "orch:DelegationActor1", "canMessage": ["orch:DelegationPersona2", "orch:MonitoringPersona1", "user"], "canReceiveFrom": ["orch:ReceivePersona1", "orch:DelegationPersona2"], "sessionConsistent": true},
  {"@id": "orch:DelegationPersona2", "@type": "gab:Persona", "name": "Junior Delegation Executor", "role": "junior", "personality": "Precise, follows spawn protocols exactly", "responsibilities": ["Write task files for children", "Execute spawn commands", "Register children in registry", "Verify spawn success", "Report spawn results to senior"], "mode": "orch:DelegationMode", "actor": "orch:DelegationActor2", "canMessage": ["orch:DelegationPersona1"], "canReceiveFrom": ["orch:DelegationPersona1"], "sessionConsistent": true},
  {"@id": "orch:MonitoringPersona1", "@type": "gab:Persona", "name": "Senior Progress Monitor", "role": "senior", "personality": "Vigilant, proactive about detecting issues early", "responsibilities": ["Design monitoring strategy", "Detect timeouts and failures", "Decide retry vs reassign vs escalate", "Track progress metrics", "Brief junior on monitoring priorities"], "mode": "orch:MonitoringMode", "actor": "orch:MonitoringActor1", "canMessage": ["orch:MonitoringPersona2", "orch:AggregationPersona1", "user"], "canReceiveFrom": ["orch:DelegationPersona1", "orch:MonitoringPersona2"], "sessionConsistent": true},
  {"@id": "orch:MonitoringPersona2", "@type": "gab:Persona", "name": "Junior Status Tracker", "role": "junior", "personality": "Diligent, consistent in status checks", "responsibilities": ["Poll child status files", "Log status changes", "Calculate elapsed times", "Flag overdue children", "Report status to senior"], "mode": "orch:MonitoringMode", "actor": "orch:MonitoringActor2", "canMessage": ["orch:MonitoringPersona1"], "canReceiveFrom": ["orch:MonitoringPersona1"], "sessionConsistent": true},
  {"@id": "orch:AggregationPersona1", "@type": "gab:Persona", "name": "Senior Results Synthesizer", "role": "senior", "personality": "Integrative, sees the big picture across results", "responsibilities": ["Design aggregation strategy", "Handle partial results from failures", "Synthesize unified result", "Calculate confidence scores", "Review junior collection work"], "mode": "orch:AggregationMode", "actor": "orch:AggregationActor1", "canMessage": ["orch:AggregationPersona2", "orch:ReportPersona1", "user"], "canReceiveFrom": ["orch:MonitoringPersona1", "orch:AggregationPersona2"], "sessionConsistent": true},
  {"@id": "orch:AggregationPersona2", "@type": "gab:Persona", "name": "Junior Results Collector", "role": "junior", "personality": "Methodical, ensures no results are missed", "responsibilities": ["Collect result files from children", "Parse and validate result JSON", "Organize results by subtask", "Flag missing results", "Report collection status to senior"], "mode": "orch:AggregationMode", "actor": "orch:AggregationActor2", "canMessage": ["orch:AggregationPersona1"], "canReceiveFrom": ["orch:AggregationPersona1"], "sessionConsistent": true},
  {"@id": "orch:ReportPersona1", "@type": "gab:Persona", "name": "Senior Report Generator", "role": "senior", "personality": "Clear communicator, focuses on actionable summaries", "responsibilities": ["Design report structure", "Include task metadata and audit trail", "Calculate final confidence", "Write result to outgoing/to_above/", "Decide if cycle back to ReceiveMode"], "mode": "orch:ReportMode", "actor": "orch:ReportActor1", "canMessage": ["orch:ReportPersona2", "orch:ReceivePersona1", "user"], "canReceiveFrom": ["orch:AggregationPersona1", "orch:ReportPersona2"], "sessionConsistent": true},
  {"@id": "orch:ReportPersona2", "@type": "gab:Persona", "name": "Junior Report Writer", "role": "junior", "personality": "Precise, ensures formatting and completeness", "responsibilities": ["Format result JSON", "Compile audit trail", "Verify all fields present", "Write output files", "Report completion to senior"], "mode": "orch:ReportMode", "actor": "orch:ReportActor2", "canMessage": ["orch:ReportPersona1"], "canReceiveFrom": ["orch:ReportPersona1"], "sessionConsistent": true},
  {"@id": "orch:LayerStatePersona", "@type": "gab:Persona", "name": "Layer State Manager", "role": "StateManager", "personality": "Systematic, tracks layer position and inheritance with precision", "responsibilities": ["Track current layer position", "Maintain inheritance chain", "Resolve layer capabilities"], "mode": null, "actor": "orch:LayerStateActor", "canMessage": [], "canReceiveFrom": [], "sessionConsistent": true},
  {"@id": "orch:ChildRegistryStatePersona", "@type": "gab:Persona", "name": "Child Registry Manager", "role": "StateManager", "personality": "Meticulous, maintains accurate registry of all spawned agents", "responsibilities": ["Register spawned children", "Track child status", "Detect orphaned children"], "mode": null, "actor": "orch:ChildRegistryStateActor", "canMessage": [], "canReceiveFrom": [], "sessionConsistent": true},
  {"@id": "orch:TaskStatePersona", "@type": "gab:Persona", "name": "Task State Manager", "role": "StateManager", "personality": "Organized, tracks task decomposition and progress accurately", "responsibilities": ["Track active tasks", "Maintain decomposition tree", "Update progress metrics"], "mode": null, "actor": "orch:TaskStateActor", "canMessage": [], "canReceiveFrom": [], "sessionConsistent": true},
  {"@id": "orch:ResourceBudgetStatePersona", "@type": "gab:Persona", "name": "Resource Budget Manager", "role": "StateManager", "personality": "Conservative, enforces resource limits and prevents overallocation", "responsibilities": ["Track recursion depth", "Monitor concurrent agents", "Enforce timeout limits"], "mode": null, "actor": "orch:ResourceBudgetStateActor", "canMessage": [], "canReceiveFrom": [], "sessionConsistent": true}
] |

# 6. Add 5 IsolatedStates
.["@graph"] += [
  {"@id": "orch:ReceiveModeState", "@type": "gab:IsolatedState", "mode": "orch:ReceiveMode", "scope": "private to Receive Mode", "includes": ["Incoming task files parsed", "Task type classification", "Source identification", "Scope validation results"], "readableBy": ["orch:ReceivePersona1", "orch:ReceivePersona2"], "unreadableBy": ["orch:DelegationPersona1", "orch:DelegationPersona2", "orch:MonitoringPersona1", "orch:MonitoringPersona2", "orch:AggregationPersona1", "orch:AggregationPersona2", "orch:ReportPersona1", "orch:ReportPersona2"]},
  {"@id": "orch:DelegationModeState", "@type": "gab:IsolatedState", "mode": "orch:DelegationMode", "scope": "private to Delegation Mode", "includes": ["Task decomposition plan", "Agent type selection rationale", "Spawn commands prepared", "Resource budget checks"], "readableBy": ["orch:DelegationPersona1", "orch:DelegationPersona2"], "unreadableBy": ["orch:ReceivePersona1", "orch:ReceivePersona2", "orch:MonitoringPersona1", "orch:MonitoringPersona2", "orch:AggregationPersona1", "orch:AggregationPersona2", "orch:ReportPersona1", "orch:ReportPersona2"]},
  {"@id": "orch:MonitoringModeState", "@type": "gab:IsolatedState", "mode": "orch:MonitoringMode", "scope": "private to Monitoring Mode", "includes": ["Child agent status polls", "Timeout tracking", "Failure detection results", "Retry decisions"], "readableBy": ["orch:MonitoringPersona1", "orch:MonitoringPersona2"], "unreadableBy": ["orch:ReceivePersona1", "orch:ReceivePersona2", "orch:DelegationPersona1", "orch:DelegationPersona2", "orch:AggregationPersona1", "orch:AggregationPersona2", "orch:ReportPersona1", "orch:ReportPersona2"]},
  {"@id": "orch:AggregationModeState", "@type": "gab:IsolatedState", "mode": "orch:AggregationMode", "scope": "private to Aggregation Mode", "includes": ["Child result files collected", "Merge strategy selection", "Partial result handling", "Confidence score calculations"], "readableBy": ["orch:AggregationPersona1", "orch:AggregationPersona2"], "unreadableBy": ["orch:ReceivePersona1", "orch:ReceivePersona2", "orch:DelegationPersona1", "orch:DelegationPersona2", "orch:MonitoringPersona1", "orch:MonitoringPersona2", "orch:ReportPersona1", "orch:ReportPersona2"]},
  {"@id": "orch:ReportModeState", "@type": "gab:IsolatedState", "mode": "orch:ReportMode", "scope": "private to Report Mode", "includes": ["Aggregated result formatting", "Audit trail compilation", "Confidence score summary", "Output file writing"], "readableBy": ["orch:ReportPersona1", "orch:ReportPersona2"], "unreadableBy": ["orch:ReceivePersona1", "orch:ReceivePersona2", "orch:DelegationPersona1", "orch:DelegationPersona2", "orch:MonitoringPersona1", "orch:MonitoringPersona2", "orch:AggregationPersona1", "orch:AggregationPersona2"]}
]
