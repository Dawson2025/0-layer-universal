# AutoGen Agent Context

## Identity
Stages container for the audio sub-feature.
- **Parent**: `../../0AGNOSTIC.md` (layer_1_sub_feature_audio)

## Stages

| Stage | Name | Purpose |
|-------|------|---------|
| 00 | Stage Registry | Stage metadata and proposals |
| 01 | Request Gathering | Clarify TTS/audio requirements |
| 02 | Research | Investigate TTS tools, APIs, integration patterns |
| 03 | Instructions | Define constraints and guidelines |
| 04 | Design | Architecture for audio integration |
| 05 | Planning | Break into implementation tasks |
| 06 | Development | Build TTS integration |
| 07 | Testing | Verify audio output quality and reliability |
| 08 | Criticism | Review and identify gaps |
| 09 | Fixing | Address issues from criticism |
| 10 | Current Product | Working TTS integration |
| 11 | Archives | Historical records |

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
