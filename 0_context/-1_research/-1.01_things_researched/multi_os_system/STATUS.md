# Status: Multi-OS Workspace Sync

## System Health (2026-01-10)

| Device | Status | Sync Mode | Notes |
| :--- | :--- | :--- | :--- |
| **WSL** | 🟢 Running | Send & Receive | Canonical source |
| **Windows** | 🟢 Running | Send & Receive | Connected to WSL |
| **Ubuntu** | ⏸️ **Dual Boot** | Send & Receive | **Offline (Expected)** |
| **Hetzner VPS** | 🚧 **Provisioning** | Send & Receive | **CPX11, 2GB RAM, $4.15/mo** |

## ⚠️ Architecture Constraints Identified

**The Ubuntu system is a Dual Boot installation on the same hardware.**

1.  **Direct Sync is Impossible:** Windows and Ubuntu are never running at the same time. They cannot "connect" to each other.
2.  **"Disconnected" Status is Normal:** When you are in Windows, Ubuntu is off. When you are in Ubuntu, Windows is off.

## How to Sync in Dual Boot

To keep these systems in sync, you need an **Intermediary Device** (Store-and-Forward).

**Required: A 3rd "Always On" Device**
- **Option A:** A Smartphone (Android/iOS) running Syncthing.
- **Option B:** A VPS or Home Server (Raspberry Pi).
- **Option C:** A NAS.

**Workflow:**
1.  **Windows/WSL** runs -> Syncs changes to **Phone/Server**.
2.  *Reboot to Ubuntu.*
3.  **Ubuntu** runs -> Syncs changes **from Phone/Server**.

## Immediate Action (IN PROGRESS - 2026-01-10)

**Initial Attempt:** Oracle Cloud Free Tier VPS
- **Status:** ❌ Signup blocked by fraud prevention system
- **Issue:** Automated rejection despite meeting all requirements
- **Support:** Ticket submitted (48-hour response time)

**Current Solution:** Hetzner Cloud CPX11
- **Cost:** €3.79/month (~$4.15 USD)
- **Specs:** 2 vCPUs, 2GB RAM, 40GB SSD, Ubuntu 22.04
- **Status:** Provisioning now
- **Next:** Install Syncthing and connect Windows/Ubuntu
- **Migration Path:** Can move to Oracle later if account approved

## Recent Log
- **2026-01-10:** Oracle Cloud signup rejected by fraud prevention. Pivoting to Hetzner CPX11.
- **2026-01-10:** Submitted Oracle support ticket. Will migrate from Hetzner if approved.
- **2026-01-10:** Selected Oracle Cloud Free Tier VPS as relay solution. Account signup attempted.
- **2026-01-10:** Expanded vision to include VNC desktop + browser automation for mobile viewing.
- **2026-01-09:** Identified system as Dual Boot. Ceased network scanning for Ubuntu IP.
- **2026-01-09:** Windows Syncthing service fixed.

## Next Steps
1.  Complete Oracle Cloud account signup and verification.
2.  Provision Ubuntu ARM VPS instance.
3.  Install Syncthing on VPS and configure relay.
4.  Connect Windows/WSL and Ubuntu to VPS.
5.  Test dual-boot sync workflow.
