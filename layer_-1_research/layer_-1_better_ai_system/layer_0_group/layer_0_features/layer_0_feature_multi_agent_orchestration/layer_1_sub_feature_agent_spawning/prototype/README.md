# Agent Spawning Prototype

**Layer**: -1 (Research)
**Feature**: Multi-Agent Orchestration > Agent Spawning
**Status**: Prototype
**Created**: 2026-02-06

## Overview

This prototype demonstrates basic CLI AI agent spawning with file-based communication using the `hand_off_documents/` pattern from the layer-stage system.

## Files

| File | Purpose |
|------|---------|
| `spawn_agent.sh` | Core spawning script - spawns a single agent with safeguards |
| `test_harness.sh` | Test suite for the spawning prototype |
| `examples/` | Example task files for different scenarios |

## Quick Start

```bash
# Make scripts executable
chmod +x spawn_agent.sh test_harness.sh

# Run tests
./test_harness.sh

# Spawn a simple agent (requires claude CLI installed)
./spawn_agent.sh claude examples/simple_task.json
```

## Spawning Safeguards

The prototype implements the following safeguards from `agent_orchestrator_gab.jsonld`:

| Safeguard | Implementation |
|-----------|----------------|
| **Max Recursion Depth** | Checks `CURRENT_DEPTH >= MAX_DEPTH` before spawning |
| **Concurrent Limit** | `MAX_CONCURRENT` environment variable |
| **Timeout** | `timeout` command wraps agent execution |
| **Status Tracking** | JSON status files in `hand_off_documents/status/` |

## Directory Structure

When an agent is spawned, it creates:

```
hand_off_documents/
├── outgoing/to_below/{child_id}/
│   └── task.json          # Task specification for child
├── incoming/from_below/{child_id}/
│   ├── result.json        # Child's result (written by child)
│   ├── stdout.log         # Child's stdout
│   └── stderr.log         # Child's stderr
└── status/{child_id}.json # Status tracking
```

## Supported Agents

| Agent | Command | Best For |
|-------|---------|----------|
| `claude` | `claude --print "{task}"` | Complex reasoning, multi-file changes |
| `codex` | `codex "{task}"` | Quick fixes, single-file edits |
| `gemini` | `gemini "{task}"` | Research, web search |
| `aider` | `aider --message "{task}"` | Git operations, repo-wide changes |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CURRENT_DEPTH` | 0 | Current recursion depth |
| `MAX_DEPTH` | 5 | Maximum recursion depth |
| `MAX_CONCURRENT` | 3 | Maximum concurrent agents |
| `AGENT_TIMEOUT` | 300 | Timeout per agent (seconds) |

## Task File Format

```json
{
    "taskId": "unique_id",
    "description": "Clear, actionable task description",
    "agentType": "claude|codex|gemini|aider",
    "context": {
        "paths": ["relevant/paths/"],
        "constraints": {}
    },
    "expectedOutput": {
        "format": "json|markdown|code",
        "sections": ["expected", "sections"]
    }
}
```

## Result File Format

```json
{
    "taskId": "from_task",
    "status": "completed|failed",
    "result": {
        "summary": "Brief summary",
        "content": "Full result",
        "confidence": 0.0-1.0
    },
    "metadata": {
        "agentType": "agent_used",
        "depth": 1
    }
}
```

## Next Steps

1. **Parallel Spawning**: Extend to spawn multiple agents concurrently
2. **Monitoring Loop**: Add polling for status updates
3. **Result Aggregation**: Implement aggregation strategies
4. **Full Orchestrator**: Implement the complete 5-mode-15-actor pattern

## Related Files

- Design: `../agent_orchestrator_gab.jsonld`
- Research: `../../docs/01_research_recursive_multi_agent_systems.md`
- Findings: `../../docs/02_research_findings_existing_frameworks.md`

---

*Layer -1 (Research) - Multi-Agent Orchestration Prototype*
