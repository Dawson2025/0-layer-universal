# Inotify - Linux File Watching System

## What is Inotify?

Inotify is a Linux kernel subsystem that monitors filesystem events. Applications use it to watch files and directories for changes (creation, modification, deletion, etc.).

## Key Concepts

### Watches vs Instances
- **Watch**: Monitors a single file or directory
- **Instance**: A file descriptor opened by a process for inotify operations
- Each process can have multiple instances, each with multiple watches

### System Limits

| Parameter | Default | Location |
|-----------|---------|----------|
| `max_user_watches` | 65,536 | `/proc/sys/fs/inotify/max_user_watches` |
| `max_user_instances` | 128 | `/proc/sys/fs/inotify/max_user_instances` |

### Memory Usage
- Each watch consumes ~160-1000 bytes of kernel memory
- At 1M watches: ~160MB-1GB RAM dedicated to file watching

## Common Consumers

| Application Type | Inotify Usage |
|-----------------|---------------|
| IDEs (VS Code, Cursor, IntelliJ) | Heavy - watches all project files, node_modules |
| Electron apps | Heavy - each app runs Chromium + Node.js |
| Node.js hot-reload | Moderate - watches source files |
| File managers | Light - watches current directory |
| Desktop environments | Moderate - portals, settings daemons |

## Symptoms of Exhaustion

When inotify limits are exhausted:
- Applications fail to start
- "No space left on device" errors (misleading - not disk space)
- Desktop services fail (media keys, file dialogs)
- IDE file watching breaks
- System enters "degraded" state

## Diagnostic Commands

```bash
# Check current limits
cat /proc/sys/fs/inotify/max_user_watches
cat /proc/sys/fs/inotify/max_user_instances

# Find processes using inotify
find /proc/*/fd -lname anon_inode:inotify 2>/dev/null | \
  cut -d/ -f3 | xargs -I '{}' -- ps --no-headers -o comm -p '{}' 2>/dev/null | \
  sort | uniq -c | sort -rn

# Check systemd user session status
systemctl --user is-system-running
systemctl --user --failed
```

## Related Documentation
- [Ubuntu Desktop](../sub_layer_02_ubuntu_desktop/)
- [System Services](../sub_layer_03_system_services/)
