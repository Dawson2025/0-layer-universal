---
resource_id: "b599b0b0-f04d-461e-9f84-d5622b7886c9"
resource_type: "document"
resource_name: "gnome_session_troubleshooting"
---
# GNOME Session Troubleshooting

This document outlines the steps taken to resolve a broken GNOME desktop session where critical services were not running, leading to issues with media keys, brightness control, and application launching.

<!-- section_id: "65dc3b18-0973-4ab7-a0d2-d5a0de94cfd8" -->
## Symptoms

- Volume and brightness keys not working.
- Applications like Files (Nautilus) and Terminal failing to launch.
- GNOME settings daemons (gsd-*) not running.
- `gnome-session` process not running.

<!-- section_id: "03f90192-d242-41e9-854c-b1ea0deec689" -->
## Diagnosis

The root cause was a fundamentally broken GNOME session. The `gnome-session` manager was not starting correctly, which prevented all other necessary settings and desktop daemons from initializing. This can happen due to incorrect session selection at login or a corrupted user session state.

<!-- section_id: "153d2b74-0273-47f8-a11e-ce25065d9398" -->
## Resolution Steps

1.  **Correct Session Selection**: The primary fix was to ensure the correct session is selected at the login screen.
    - Log out from the current session.
    - At the login screen, click the gear icon.
    - Select "Ubuntu" or "Ubuntu on Xorg".
    - Log in.

2.  **Manual Daemon Startup (Temporary Fix)**: Before discovering the session issue, we manually started the required daemons. This is a temporary solution but useful for diagnostics.
    ```bash
    DISPLAY=:0 /usr/libexec/gsd-media-keys &
    DISPLAY=:0 /usr/libexec/gsd-power &
    DISPLAY=:0 /usr/libexec/gsd-xsettings &
    DISPLAY=:0 /usr/libexec/gsd-color &
    DISPLAY=:0 /usr/libexec/gsd-keyboard &
    DISPLAY=:0 /usr/libexec/gsd-housekeeping &
    ```

3.  **Application Launching via DBus**: We also manually launched applications using `dbus-send` to confirm that the underlying services were becoming available.
    ```bash
    # Launch Files (Nautilus)
    DISPLAY=:0 dbus-send --session --type=method_call --dest=org.gnome.Nautilus /org/gnome/Nautilus org.freedesktop.Application.Activate "array:string:"

    # Launch Terminal
    DISPLAY=:0 gnome-terminal &
    ```

<!-- section_id: "5ff894e9-5d9c-497d-9a10-a7b2bcc9f81b" -->
## Permanent Fix

The permanent solution is to always ensure the correct GNOME session is selected at login. If the session becomes corrupted again, the first step should be to log out and re-select the "Ubuntu" session.
