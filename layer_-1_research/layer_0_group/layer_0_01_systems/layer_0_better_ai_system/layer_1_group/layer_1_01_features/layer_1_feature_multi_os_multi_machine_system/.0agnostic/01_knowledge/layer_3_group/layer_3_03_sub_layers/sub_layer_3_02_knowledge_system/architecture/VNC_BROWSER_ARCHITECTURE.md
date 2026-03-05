---
resource_id: "36a1d0aa-9d9c-4f7d-a0e8-d8b4379c5f59"
resource_type: "knowledge"
resource_name: "VNC_BROWSER_ARCHITECTURE"
---
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

### Option A: Stream from Local Laptop ($0/month)
**Best for:** Zero cost, laptop available

**Setup:**
- **Software:** Moonlight (phone) + Sunshine (laptop server)
- **Alternative:** Steam Link or Parsec
- **Network:** Via Tailscale for secure access
- **Workflow:** Phone → Tailscale VPN → Laptop GPU → Unreal Engine
- **Performance:** 1080p/60fps or 4K/60fps on good connection
- **Latency:** 5-50ms on home WiFi, 30-100ms on 4G/5G

**Installation Steps:**
1. Install Sunshine on Windows laptop (free, open-source)
2. Install Moonlight app on phone (iOS/Android)
3. Connect via Tailscale network
4. Stream Unreal Engine display to phone
5. Use touch controls or Bluetooth controller

**Pros:**
- $0 cost, uses existing hardware
- Low latency when on same network
- Full GPU power of your laptop

**Cons:**
- Laptop must be powered on
- Requires laptop to be accessible (home or with you)
- Network dependent (need decent upload speed)

**Advanced:** Use Wake-on-LAN to remotely power on laptop when needed

---

### Option B: Cloud GPU Instance (Always Available - No Laptop Required)

For 24/7 Unreal access when laptop is off or unavailable.

#### B1. Paperspace (Recommended for Game Dev)

**Pay-As-You-Go (Core Plan):**
- **Cost:** $0.51-1.10/hour, no monthly base fee
- **GPU Options:**
  - M4000 (8GB VRAM): $0.51/hr - Good for Unreal Editor
  - P4000 (8GB VRAM): $0.78/hr - Better performance
  - RTX 4000 (8GB VRAM): $0.82/hr - Ray tracing support
  - RTX 5000 (16GB VRAM): $1.10/hr - Heavy projects
- **Specs:** 8-30GB RAM depending on tier
- **Streaming:** Built-in Parsec-style streaming
- **Best for:** Occasional use, pay only when working

**Usage Examples:**
- 10 hrs/month = ~$5-10/month
- 30 hrs/month = ~$15-33/month
- 100 hrs/month = ~$51-110/month

**Growth Plan (Dedicated GPU):**
- **Cost:** $8/month base + $0.51/hr GPU usage
- **Best for:** Regular users (saves money at 50+ hrs/month)

#### B2. Shadow PC (Consumer Gaming Service)

**Subscription Model:**
- **Cost:** $29.99-49.99/month flat rate (unlimited usage)
- **Specs:** Dedicated Windows PC with GPU (varies by tier)
  - Base: GTX 1080 equivalent
  - Higher tiers: RTX-level performance
- **Streaming:** Built-in, optimized for gaming/low latency
- **Platform:** Works like a full remote Windows PC

**Pros:**
- Simplest setup (consumer-friendly)
- Unlimited usage for flat fee
- Optimized streaming experience
- No need to manage server/software

**Cons:**
- Less control than cloud VPS
- Fixed hardware specs
- Subscription required even if not using

**Best for:** Daily Unreal users who want "it just works" experience

#### B3. AWS EC2 with NVIDIA GPUs

**g4dn.xlarge (T4 GPU):**
- **Cost:** ~$0.526/hour (~$380/month if always-on)
- **Specs:** 4 vCPU, 16GB RAM, NVIDIA T4 (16GB VRAM)
- **Streaming:** Install Moonlight/Sunshine or Parsec yourself
- **Advantage:** Enterprise-grade, integrates with AWS ecosystem
- **Save money:** Stop instance when not using

**Spot Instances (70% cheaper):**
- **Cost:** ~$0.16/hour
- **Limitation:** Can be terminated with 2-min notice
- **Best for:** Non-critical testing, rendering

**Best for:**
- Already using AWS infrastructure
- Professional workflows requiring reliability
- Need to integrate with other AWS services

#### B4. Maximum Labs (Best Price/Performance)

**RTX 3070 Instance:**
- **Cost:** ~$0.41/hour (~$300/month always-on)
- **Specs:** RTX 3070 (8GB VRAM), excellent for Unreal
- **Advantage:** Cheaper than AWS/GCP for GPU power
- **Streaming:** Install Moonlight/Sunshine

**RTX 4090 Instance:**
- **Cost:** ~$0.80/hour
- **Specs:** Top-tier consumer GPU, 24GB VRAM
- **Best for:** Heavy Unreal 5 projects, ray tracing

**Pros:**
- Better GPU price/performance
- Modern consumer GPUs

**Cons:**
- Smaller company (less infrastructure than AWS)
- Fewer regions

---

### Option C: Hybrid Model (RECOMMENDED - Best Cost Optimization)

**Architecture:**
```
Oracle Free VPS (Always-on, $0/mo)
  - Code editing
  - File sync (Syncthing)
  - AI agents
  - Browser automation
  - SSH/CLI access

+

Cloud GPU (On-demand)
  - Paperspace/Shadow/AWS
  - Unreal Engine
  - Gaming
  - 3D rendering
  - Only running when needed
```

**Workflow:**
1. Use Oracle VPS for daily code/AI work ($0)
2. When you need Unreal: Start cloud GPU instance
3. Stream GPU to phone via Moonlight/Parsec
4. Work on Unreal project
5. Stop GPU instance when done
6. Code changes already synced to all devices via VPS

**Cost Examples:**
- **Light Unreal use (10-20 hrs/mo):** $5-20/month
- **Regular use (30-50 hrs/mo):** $15-50/month
- **Heavy use (100+ hrs/mo):** Consider Shadow PC ($30-50 flat)

**Annual Cost Comparison:**
- Hybrid on-demand: $60-240/year
- Always-on cloud GPU: $3,600-4,800/year
- **Savings:** $3,300-4,500/year

---

### Phase 4 Recommendations by Use Case

| Use Case | Recommended Solution | Monthly Cost |
|----------|---------------------|--------------|
| **Occasional Unreal (10-20 hrs/mo)** | Paperspace Pay-As-You-Go | $5-20 |
| **Regular Unreal (30-50 hrs/mo)** | Paperspace or Shadow PC | $15-50 |
| **Daily Unreal (50-100 hrs/mo)** | Shadow PC Subscription | $30-50 |
| **Professional 24/7 work** | AWS g4dn (stop/start) | $100-200 |
| **Enterprise/Team** | AWS g4dn always-on | $380+ |
| **Budget-conscious** | Laptop + Moonlight | $0 |
| **Laptop + backup cloud** | Laptop + Paperspace on-demand | $0-30 |

### Network Requirements for Streaming

**Minimum:**
- **Download (phone):** 10 Mbps for 1080p/30fps
- **Upload (server):** 10 Mbps from cloud/laptop
- **Latency:** <100ms for acceptable experience

**Recommended:**
- **Download:** 25+ Mbps for 1080p/60fps
- **Upload:** 25+ Mbps for smooth streaming
- **Latency:** <50ms for good responsiveness

**Optimal:**
- **Download:** 50+ Mbps for 4K streaming
- **Upload:** 50+ Mbps
- **Latency:** <20ms for near-native feel

### Mobile Streaming Apps

**VNC (for VPS browser control):**
- VNC Viewer (RealVNC)
- Jump Desktop
- TigerVNC Viewer

**GPU Streaming (for Unreal/gaming):**
- Moonlight (free, best for Nvidia GameStream/Sunshine)
- Parsec (free tier available)
- Steam Link (free, Steam games)
- Shadow PC app (if using Shadow)

**Controllers:**
- Xbox/PlayStation Bluetooth controller
- Backbone/Razer Kishi (phone mount controllers)
- Touch controls (less ideal for 3D work)

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
