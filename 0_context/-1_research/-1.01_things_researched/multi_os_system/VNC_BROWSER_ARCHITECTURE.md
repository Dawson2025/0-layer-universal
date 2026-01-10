# VNC Browser Automation Architecture

**Date:** 2026-01-10
**Status:** Planning Phase

## Overview

This document describes the Visual Browser Control system that will run on the Oracle Cloud VPS, allowing mobile viewing and interaction with AI-controlled browser automation.

## Architecture Components

### 1. VPS Environment (Oracle Cloud Free Tier)
- **Hardware:** 4 ARM CPUs, 24GB RAM, 200GB storage
- **OS:** Ubuntu 22.04 or 24.04 LTS (ARM64)
- **Cost:** $0/month (permanent free tier)

### 2. Desktop Environment
- **Option A:** XFCE (Lightweight, ~200MB RAM)
- **Option B:** LXDE (Ultra-lightweight, ~150MB RAM)
- **Recommendation:** XFCE for better VNC compatibility

### 3. VNC Server
- **Software:** TigerVNC or x11vnc
- **Configuration:**
  - Password-protected access
  - Tunneled through Tailscale (encrypted)
  - Display resolution: 1920x1080 or 1280x720
  - Color depth: 24-bit

### 4. Browser Setup
- **Primary:** Chromium (ARM-compatible)
- **Fallback:** Firefox ESR
- **MCP Integration:** Claude in Chrome extension or headless Chrome + Puppeteer

### 5. Mobile Access
- **VNC Client:** VNC Viewer (RealVNC) or Jump Desktop
- **Network:** Tailscale VPN (zero-trust, encrypted)
- **Interaction:** Full touch control, keyboard, mouse

## Workflow

### AI-Controlled Browsing
```
Phone (VNC Viewer)
    ↓ (via Tailscale)
VPS Running:
  - VNC Server
  - Desktop Environment
  - Chrome Browser ← AI Agent controls via MCP
  - AI Agent (Claude Code, etc.)
    ↓ reads/writes
  - ~/dawson-workspace (synced)
```

### User Experience
1. **Launch:** AI agent starts browser automation task on VPS
2. **View:** User opens VNC viewer on phone, sees live browser session
3. **Interact:** User can take over manually if needed
4. **Monitor:** Watch AI complete tasks in real-time
5. **Results:** Code/data syncs back to laptop via Syncthing

## Use Cases

### Development & Testing
- Watch AI debug web applications
- See AI interact with development tools
- Monitor automated testing workflows

### Browser Automation
- Social media management
- Data scraping with visual verification
- Form filling and submission
- Multi-step web workflows

### Research & Learning
- AI navigates documentation
- Live code demonstrations
- Interactive tutorials

## Resource Estimates

### Per Browser Instance
- **Memory:** 500MB - 1GB RAM
- **CPU:** 10-30% of single core
- **Storage:** ~500MB (browser + cache)

### Concurrent Capacity (24GB RAM)
- **Conservative:** 5-8 browsers + desktop
- **Optimal:** 3-4 browsers for comfortable use
- **Max:** 15+ browsers (tight, no headroom)

## Security Considerations

### VNC Access
- Never expose VNC directly to internet
- Always tunnel through Tailscale
- Use strong VNC password
- Consider VNC encryption (if not using Tailscale)

### Browser Isolation
- Run browsers in separate user accounts (optional)
- Use browser profiles for different tasks
- Clear cache/cookies between sessions

### Data Privacy
- Synced workspace contains code, not credentials
- Use environment variables for secrets
- Never save passwords in browser

## Performance Optimization

### ARM Architecture Notes
- Oracle Free Tier uses ARM CPUs (Ampere Altra)
- Chromium ARM builds perform well
- VNC encoding: Tight encoding for mobile networks
- Color depth: 16-bit for slower connections

### Network Optimization
- Tailscale provides automatic route optimization
- VNC compression settings: Medium to High
- Screen resolution: Lower for better mobile experience

## Implementation Checklist

### Phase 3A: Desktop + VNC Setup
- [ ] Install XFCE desktop environment
- [ ] Install TigerVNC server
- [ ] Configure VNC password and security
- [ ] Test VNC connection via Tailscale
- [ ] Optimize VNC settings for mobile

### Phase 3B: Browser Setup
- [ ] Install Chromium browser
- [ ] Install Chrome extensions (Claude in Chrome)
- [ ] Configure browser profiles
- [ ] Test MCP server integration
- [ ] Verify browser automation works

### Phase 3C: AI Agent Deployment
- [ ] Install Claude Code CLI
- [ ] Install other AI agents/tools
- [ ] Configure agents to use synced workspace
- [ ] Test agent browser control
- [ ] Verify VNC viewing during automation

### Phase 3D: Mobile Client Setup
- [ ] Install VNC Viewer on phone
- [ ] Configure Tailscale connection
- [ ] Test mobile VNC access
- [ ] Optimize display settings
- [ ] Test interactive control

## Future Enhancements

### Potential Additions
- **noVNC:** Web-based access (no app required)
- **Clipboard sharing:** Copy/paste between phone and VPS
- **Audio forwarding:** Hear browser audio on phone
- **Recording:** Capture AI automation sessions
- **Multi-user:** Share VNC session with collaborators

### Scaling Options
- **Dedicated GPU Instance:** For heavy browser workloads
- **Container-based browsers:** Docker isolation per task
- **Horizontal scaling:** Multiple VPS instances

## Phase 4: Unreal Engine & Gaming Access

### Requirements
Accessing Unreal Engine 3D environment and gaming from phone requires GPU capabilities, which Oracle Free Tier does not provide.

### Option A: Stream from Local Laptop (Recommended for start)
When your laptop is powered on:
- **Software:** Moonlight + Sunshine, or Steam Link
- **Network:** Via Tailscale for secure access
- **Workflow:** Phone → Tailscale → Laptop GPU
- **Cost:** $0 (uses existing laptop hardware)
- **Limitation:** Laptop must be powered on and online

### Option B: Cloud GPU Instance (Future upgrade)
For always-available gaming/Unreal access:
- **Provider:** AWS EC2 G4/G5, GCP with T4/A100, or Paperspace
- **Cost:** $0.50-2.00/hour ($15-60/mo if always on)
- **Specs:** NVIDIA GPU (T4 or better)
- **Use Case:** Professional game dev work, always-on access

### Option C: Hybrid Approach (Best of both)
- **Lightweight tasks:** Use Oracle Free VPS (code, browsers, agents)
- **GPU tasks:** Stream from laptop when home
- **Professional work:** Rent cloud GPU hourly as needed
- **Cost:** Minimal, pay only when GPU needed

## Cost Analysis

| Component | Cost | Notes |
|-----------|------|-------|
| VPS (Oracle Free Tier) | $0/mo | Permanent free |
| Tailscale | $0/mo | Free tier (1 user, 100 devices) |
| VNC Viewer App | $0 | Free apps available |
| **Total** | **$0/mo** | Zero ongoing cost |

## Comparison to Alternatives

### vs. Cloud Desktop (Windows 365, AWS WorkSpaces)
- **Cost:** $20-40/mo vs. $0/mo
- **Flexibility:** Less vs. Full control
- **ARM Support:** Limited vs. Native

### vs. Dedicated Browser Automation Services
- **Cost:** $50-200/mo vs. $0/mo
- **AI Integration:** Complex vs. Direct
- **Customization:** Limited vs. Unlimited

### vs. Local Phone Apps
- **Power:** Phone limited vs. VPS 24GB RAM
- **Persistence:** Requires phone on vs. Always available
- **Syncing:** Complex vs. Built-in (Syncthing)

## References

- Oracle Cloud Free Tier: https://www.oracle.com/cloud/free/
- TigerVNC Documentation: https://tigervnc.org/
- Tailscale Setup Guide: https://tailscale.com/kb/
- Claude in Chrome: https://github.com/anthropics/claude-in-chrome
