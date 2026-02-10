# Multi-OS Workspace Sync Plan + Implementation

## Plan Summary

Goal: Create a **Hybrid AI Development Ecosystem** that combines the raw performance of a local laptop (Dual Boot) with the accessibility and orchestration power of a Remote AI Hub.

### Core Architecture: "The Hybrid Mesh"

This architecture solves the Dual Boot sync problem *and* enables the "Phone/Agent Access" vision simultaneously.

1.  **Local Nodes (High Performance):**
    *   **Windows 11 (Host):** Runs Unreal Engine, Games, Adobe Suite.
    *   **Native Ubuntu (Dual Boot):** Runs heavyweight Code, Docker, AI Model Training.
    *   *Constraint:* Never online at the same time.

2.  **Remote Hub (High Availability):**
    *   **Cloud VPS:** Oracle Cloud Free Tier (4 ARM CPUs, 24GB RAM, 200GB storage) - $0/mo permanent free tier.
    *   **Role 1 (Sync Bridge):** Acts as the Store-and-Forward relay. Windows pushes here; Ubuntu pulls from here.
    *   **Role 2 (Agent Backend):** Hosts the Voice/Video AI agents and CLI tools.
    *   **Role 3 (Mobile Access):** SSH/VNC into *this* server from your phone to trigger agents or edit code.
    *   **Role 4 (Visual Browser Control):** VNC desktop environment allows viewing and controlling AI-driven browser automation from phone.

3.  **The Sync Fabric:**
    *   **Syncthing:** Maintains an identical copy of `~/dawson-workspace` on Windows, Ubuntu, and the VPS.
    *   **Result:** Edit on Laptop (Local speed) -> Syncs to VPS -> Accessible on Phone immediately.

## Implementation Roadmap

### Phase 1: The Cloud Relay (Fixing Dual Boot)
*   **Action:** Provision Oracle Cloud Free Tier VPS (ARM-based Ubuntu).
*   **Setup:** Install Syncthing on VPS.
*   **Connect:** Link Windows and Ubuntu to the VPS.
*   **Result:** Seamless switching between Windows and Ubuntu with zero ongoing cost.

### Phase 2: Remote Access (Mobile)
*   **Network:** Install Tailscale on VPS, Laptop, and Phone.
*   **Access:** Use Blink Shell (Phone) to SSH into the VPS.
*   **Result:** Full CLI access to your workspace from anywhere.

### Phase 3: AI Agent Integration + Visual Browser Control
*   **Desktop Environment:** Install lightweight desktop (XFCE/LXDE) on VPS.
*   **VNC Server:** Set up TigerVNC for remote desktop access.
*   **Browser Automation:** Install Chrome/Chromium for AI-controlled browsing via MCP servers.
*   **Deploy Agents:** Install your CLI Agents (Claude Code, etc.) on the VPS.
*   **Voice/Video:** Set up the WebRTC/LiveKit backend on the VPS.
*   **Control:** Agents running on the VPS can:
    - Read/write the synced files (effectively "coding on your laptop" remotely)
    - Control browsers via MCP
    - Execute tasks visible through VNC from your phone
*   **Mobile View:** Full interactive browser control from phone via VNC viewer app.

### Phase 4: 3D Integration (Unreal)
*   **Local:** Run Unreal Engine on your Laptop (using local GPU).
*   **Remote:** For phone access, use the VPS to proxy commands to your Laptop (when running) or deploy a dedicated GPU node later.

## Immediate Next Step (IN PROGRESS - 2026-01-10)
To unblock the Dual Boot sync, we are provisioning the **Phase 1 Relay**.

**Initial Attempt:** Oracle Cloud Free Tier VPS
*   **Status:** ❌ Signup blocked by fraud prevention
*   **Issue:** Oracle's automated system rejected signup despite meeting all requirements
*   **Action:** Support ticket submitted (48-hour response time)
*   **Decision:** Proceed with Hetzner while waiting for Oracle resolution

**Current Solution:** Hetzner Cloud CPX11
*   **Cost:** €3.79/mo (~$4.15 USD)
*   **Specs:** 2 vCPUs, 2GB RAM, 40GB SSD
*   **Advantage:** Instant provisioning, reliable, sufficient for Phases 1-3
*   **Migration Path:** Can migrate to Oracle later if account approved
*   **Status:** Provisioning now

---

## Current System Status (2026-01-10)

| Environment | OS | Status | Notes |
| :--- | :--- | :--- | :--- |
| **WSL2** | Ubuntu 24.04 | ✅ Running | Connected to Windows |
| **Windows** | Windows 11 | ✅ Running | Connected to WSL |
| **Ubuntu** | Desktop | ⏸️ Offline | **Waiting for Relay** |
| **Remote Hub** | Oracle Cloud ARM Ubuntu | 🚧 Provisioning | **Free Tier, 24GB RAM** |

## Documentation
- Detailed Status: `SYNC_STATUS_2026-01-09.md`
- Research Results: `1 I am a software engineer looking for the optimal.md`
- Vision: `Architecture_Remote_AI_Hub.md` (To Be Created)
