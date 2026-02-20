# Multi-Agent Sync Rules

## Rule: Lock Before Writing

Before modifying any shared output:

1. **Check for existing lock**: `.locks/[scope]_[agent].lock`
2. **If locked**: Wait or work on different file
3. **If unlocked**: Acquire lock before writing
4. **After writing**: Release lock

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

## Change Detection

After modifying files, log the change:

```
echo "$(date -Iseconds) | $AGENT_ID | $PATH | MODIFIED | $BEFORE_HASH → $AFTER_HASH" >> divergence.log
```

## Conflict Resolution

If two agents modified same file:
1. Compare timestamps
2. Keep version with later timestamp (last-write-wins)
3. Log conflict to conflicts.log
4. Notify affected agents

