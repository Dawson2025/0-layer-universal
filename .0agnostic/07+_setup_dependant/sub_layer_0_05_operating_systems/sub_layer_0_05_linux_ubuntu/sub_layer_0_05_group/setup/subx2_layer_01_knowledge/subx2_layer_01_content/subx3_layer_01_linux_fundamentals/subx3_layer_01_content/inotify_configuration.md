---
resource_id: "f0cd1732-0d6d-47d0-bbf3-02540b1a206e"
resource_type: "document"
resource_name: "inotify_configuration"
---
# Inotify Configuration

This document explains how to increase the `inotify` limits on a Linux system. These limits control the maximum number of files your user can watch for changes at once.

Default limits are often too low for modern development workflows, especially when using file watchers in tools like IDEs, build tools, and synchronizers.

<!-- section_id: "15e8e5f3-ec4a-45d0-9a68-c7f24192854e" -->
## Symptoms of Low Limits

- Applications crashing or reporting errors like "Unable to watch for changes" or "Inotify limit reached".
- File synchronization services (like Dropbox or Syncthing) failing to update.
- IDEs failing to detect file changes.

<!-- section_id: "f12ca3bb-bf46-4414-a3ca-fbc674fd0661" -->
## Viewing Current Limits

You can view the current `inotify` limits with the following commands:

```bash
# Maximum number of watches per user
cat /proc/sys/fs/inotify/max_user_watches

# Maximum number of inotify instances per user
cat /proc/sys/fs/inotify/max_user_instances
```

<!-- section_id: "7c5f4212-47b5-4ed1-b892-34586b280ee3" -->
## Temporary Increase

You can increase the limits temporarily (until the next reboot) by writing to the proc files as root:

```bash
sudo sysctl fs.inotify.max_user_watches=524288
sudo sysctl fs.inotify.max_user_instances=512
```

<!-- section_id: "d7c3430a-308a-4782-9d43-c625e47eedd8" -->
## Permanent Fix

To make the changes permanent, you need to create a new sysctl configuration file.

1.  **Create the configuration file**:
    ```bash
    sudo touch /etc/sysctl.d/99-inotify.conf
    ```

2.  **Add the new limits to the file**:
    ```bash
    echo "fs.inotify.max_user_watches=1048576" | sudo tee -a /etc/sysctl.d/99-inotify.conf
    echo "fs.inotify.max_user_instances=512" | sudo tee -a /etc/sysctl.d/99-inotify.conf
    ```

3.  **Apply the changes**:
    ```bash
    sudo sysctl -p /etc/sysctl.d/99-inotify.conf
    ```

This ensures the new, higher limits are applied on every system boot.
