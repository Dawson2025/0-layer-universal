---
resource_id: "1555c827-b738-40d8-8308-0698443a076c"
resource_type: "rule"
resource_name: "multi_agent_sync"
---
# Multi-Agent Sync Rules

<!-- section_id: "aed367d5-e3aa-43c5-98de-61877f4cf2df" -->
## Rule: Lock Before Writing

Before modifying any shared output:

1. **Check for existing lock**: `.locks/[scope]_[agent].lock`
2. **If locked**: Wait or work on different file
3. **If unlocked**: Acquire lock before writing
4. **After writing**: Release lock

<!-- section_id: "2cd20d6a-6951-446b-96a8-08bfa7efd48e" -->
## Lock File Format

```
.locks/[scope]_[agent_id].lock
```

Content:
```json
{
  "agent_id": "agent_name",
  "timestamp": "2026-01-30T14:25:00Z",
  "scope": "outputs_research",
  "ttl_minutes": 5
}
```

<!-- section_id: "34a36014-a826-4645-956a-91d779a35d2f" -->
## Lock Lifecycle

```
1. ACQUIRE
   Create .locks/scope_agentid.lock with metadata

2. WORK
   Modify files within locked scope

3. RELEASE
   Delete .locks/scope_agentid.lock

4. TIMEOUT
   If lock older than TTL (5 min), consider stale
   Clean up stale locks before acquiring
```

<!-- section_id: "0240b8e0-6983-47b1-9818-53c3dc0f1357" -->
## Atomic Writes

Never write directly to final file:

```bash
# WRONG
echo "content" > final_file.md

# RIGHT
echo "content" > final_file.md.tmp
mv final_file.md.tmp final_file.md
```

The `mv` command is atomic - no partial writes.

<!-- section_id: "593dbeca-e262-40db-98fc-43c27bb77765" -->
## Change Detection

After modifying files, log the change:

```
echo "$(date -Iseconds) | $AGENT_ID | $PATH | MODIFIED | $BEFORE_HASH → $AFTER_HASH" >> divergence.log
```

<!-- section_id: "aca1834e-1929-4b21-a019-a039224ce3b8" -->
## Conflict Resolution

If two agents modified same file:
1. Compare timestamps
2. Keep version with later timestamp (last-write-wins)
3. Log conflict to conflicts.log
4. Notify affected agents

