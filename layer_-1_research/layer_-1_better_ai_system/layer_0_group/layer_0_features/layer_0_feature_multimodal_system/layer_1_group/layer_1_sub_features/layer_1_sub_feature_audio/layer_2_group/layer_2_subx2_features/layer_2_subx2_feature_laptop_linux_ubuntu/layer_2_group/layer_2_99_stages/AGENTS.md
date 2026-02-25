# AutoGen Agent Context

## Identity
Stages container for the laptop linux ubuntu platform sub-feature.
- **Parent**: `../../0AGNOSTIC.md` (layer_2_subx2_feature_laptop_linux_ubuntu)

## Stages

| Stage | Name | Purpose |
|-------|------|---------|
| 00 | Stage Registry | Stage metadata and proposals |
| 01 | Request Gathering | Platform-specific TTS requirements |
| 02 | Research | GPU TTS engines, Ubuntu integration, VoiceMode |
| 03 | Instructions | Platform constraints and guidelines |
| 04 | Design | Architecture for GPU-accelerated TTS on Ubuntu |
| 05 | Planning | Implementation task breakdown |
| 06 | Development | Install and configure Kokoro, VoiceMode |
| 07 | Testing | Verify TTS quality, latency, GPU usage |
| 08 | Criticism | Review setup and identify gaps |
| 09 | Fixing | Address issues from testing/criticism |
| 10 | Current Product | Working Kokoro TTS on Ubuntu |
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
