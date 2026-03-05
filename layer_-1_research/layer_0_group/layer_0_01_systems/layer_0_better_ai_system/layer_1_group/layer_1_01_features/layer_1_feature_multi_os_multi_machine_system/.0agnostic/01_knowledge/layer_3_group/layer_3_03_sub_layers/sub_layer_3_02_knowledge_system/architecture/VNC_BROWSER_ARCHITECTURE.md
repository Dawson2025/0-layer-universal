---
resource_id: "36a1d0aa-9d9c-4f7d-a0e8-d8b4379c5f59"
resource_type: "knowledge"
resource_name: "VNC_BROWSER_ARCHITECTURE"
---
# VNC Browser Automation Architecture

**Date:** 2026-01-10
**Status:** Planning Phase

<!-- section_id: "fa7965b5-2186-41cd-b3f9-ef2ffb1d7ee9" -->
## Overview

This document describes the Visual Browser Control system that will run on the Oracle Cloud VPS, allowing mobile viewing and interaction with AI-controlled browser automation.

<!-- section_id: "d9e5cd35-c6e5-414a-a207-7606a11c236f" -->
## Architecture Components

<!-- section_id: "522d1bc8-8aa6-4cd4-91d5-0bb40b1253b2" -->
### 1. VPS Environment (Oracle Cloud Free Tier)
- **Hardware:** 4 ARM CPUs, 24GB RAM, 200GB storage
- **OS:** Ubuntu 22.04 or 24.04 LTS (ARM64)
- **Cost:** $0/month (permanent free tier)

<!-- section_id: "e72b23f5-7c71-405a-81c9-45c81913942d" -->
### 2. Desktop Environment
- **Option A:** XFCE (Lightweight, ~200MB RAM)
- **Option B:** LXDE (Ultra-lightweight, ~150MB RAM)
- **Recommendation:** XFCE for better VNC compatibility

<!-- section_id: "ceacb7c5-5b94-4ef9-a9b7-c62df09da8e9" -->
### 3. VNC Server
- **Software:** TigerVNC or x11vnc
- **Configuration:**
  - Password-protected access
  - Tunneled through Tailscale (encrypted)
  - Display resolution: 1920x1080 or 1280x720
  - Color depth: 24-bit

<!-- section_id: "40395270-5a11-4e3a-b677-e8f9852cef85" -->
### 4. Browser Setup
- **Primary:** Chromium (ARM-compatible)
- **Fallback:** Firefox ESR
- **MCP Integration:** Claude in Chrome extension or headless Chrome + Puppeteer

<!-- section_id: "339aa7ad-b72f-4689-9b47-60f3c1e404bb" -->
### 5. Mobile Access
- **VNC Client:** VNC Viewer (RealVNC) or Jump Desktop
- **Network:** Tailscale VPN (zero-trust, encrypted)
- **Interaction:** Full touch control, keyboard, mouse

<!-- section_id: "d0c9e9dd-5474-45e0-a5ff-2545b8418251" -->
## Workflow

<!-- section_id: "b34be883-fa70-466d-940b-6b784c013101" -->
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

<!-- section_id: "b0cc93e3-d897-407e-8c10-4524ac83d3b4" -->
### User Experience
1. **Launch:** AI agent starts browser automation task on VPS
2. **View:** User opens VNC viewer on phone, sees live browser session
3. **Interact:** User can take over manually if needed
4. **Monitor:** Watch AI complete tasks in real-time
5. **Results:** Code/data syncs back to laptop via Syncthing

<!-- section_id: "2dc7d5a7-d456-4852-bc8b-498d4aecccf9" -->
## Use Cases

<!-- section_id: "38ad02c9-25d3-416e-893a-5183879d7f04" -->
### Development & Testing
- Watch AI debug web applications
- See AI interact with development tools
- Monitor automated testing workflows

<!-- section_id: "88eacc1e-0e9c-4ceb-ab4f-b9a2921c8ffb" -->
### Browser Automation
- Social media management
- Data scraping with visual verification
- Form filling and submission
- Multi-step web workflows

<!-- section_id: "f6700a90-b24f-4130-a1f1-74590b711fca" -->
### Research & Learning
- AI navigates documentation
- Live code demonstrations
- Interactive tutorials

<!-- section_id: "a7abdce9-451f-43f0-85ec-cbae9a95bdc6" -->
## Resource Estimates

<!-- section_id: "e489f1ad-0c07-443d-a12b-02aa71259687" -->
### Per Browser Instance
- **Memory:** 500MB - 1GB RAM
- **CPU:** 10-30% of single core
- **Storage:** ~500MB (browser + cache)

<!-- section_id: "707a9ddd-ec83-4b4e-9686-326ad2cbfe68" -->
### Concurrent Capacity (24GB RAM)
- **Conservative:** 5-8 browsers + desktop
- **Optimal:** 3-4 browsers for comfortable use
- **Max:** 15+ browsers (tight, no headroom)

<!-- section_id: "a589d4d3-e5df-4d81-a219-a126d329c0cf" -->
## Security Considerations

<!-- section_id: "3f672376-49c4-4e05-b00d-d763b61c8b95" -->
### VNC Access
- Never expose VNC directly to internet
- Always tunnel through Tailscale
- Use strong VNC password
- Consider VNC encryption (if not using Tailscale)

<!-- section_id: "33459c63-bc9d-4f38-9724-6b00c84c607d" -->
### Browser Isolation
- Run browsers in separate user accounts (optional)
- Use browser profiles for different tasks
- Clear cache/cookies between sessions

<!-- section_id: "1a829012-2ef8-471d-acab-72fd54d2d3db" -->
### Data Privacy
- Synced workspace contains code, not credentials
- Use environment variables for secrets
- Never save passwords in browser

<!-- section_id: "400316b1-60c6-40a3-b33e-329add173697" -->
## Performance Optimization

<!-- section_id: "28674c66-e868-4de0-aa6e-f908b7fa755c" -->
### ARM Architecture Notes
- Oracle Free Tier uses ARM CPUs (Ampere Altra)
- Chromium ARM builds perform well
- VNC encoding: Tight encoding for mobile networks
- Color depth: 16-bit for slower connections

<!-- section_id: "4e87a46a-7019-4598-8fab-d6e9f3cc3c0c" -->
### Network Optimization
- Tailscale provides automatic route optimization
- VNC compression settings: Medium to High
- Screen resolution: Lower for better mobile experience

<!-- section_id: "4bd73171-1695-4ec6-83ac-4f7692fbc6de" -->
## Implementation Checklist

<!-- section_id: "e44950bc-eea9-4b8b-b36c-f9cb8c652b08" -->
### Phase 3A: Desktop + VNC Setup
- [ ] Install XFCE desktop environment
- [ ] Install TigerVNC server
- [ ] Configure VNC password and security
- [ ] Test VNC connection via Tailscale
- [ ] Optimize VNC settings for mobile

<!-- section_id: "80487a07-55e4-4ff9-9407-50cae1762ac9" -->
### Phase 3B: Browser Setup
- [ ] Install Chromium browser
- [ ] Install Chrome extensions (Claude in Chrome)
- [ ] Configure browser profiles
- [ ] Test MCP server integration
- [ ] Verify browser automation works

<!-- section_id: "0ecd5f7c-162d-4cb1-8958-4bc17caed400" -->
### Phase 3C: AI Agent Deployment
- [ ] Install Claude Code CLI
- [ ] Install other AI agents/tools
- [ ] Configure agents to use synced workspace
- [ ] Test agent browser control
- [ ] Verify VNC viewing during automation

<!-- section_id: "c7220982-9004-433a-9766-5ad7468f8c54" -->
### Phase 3D: Mobile Client Setup
- [ ] Install VNC Viewer on phone
- [ ] Configure Tailscale connection
- [ ] Test mobile VNC access
- [ ] Optimize display settings
- [ ] Test interactive control

<!-- section_id: "9fcbb911-a546-4a7b-b4a2-05f228255266" -->
## Future Enhancements

<!-- section_id: "ef989b9c-04a2-408e-8619-342b085e08e3" -->
### Potential Additions
- **noVNC:** Web-based access (no app required)
- **Clipboard sharing:** Copy/paste between phone and VPS
- **Audio forwarding:** Hear browser audio on phone
- **Recording:** Capture AI automation sessions
- **Multi-user:** Share VNC session with collaborators

<!-- section_id: "f945c026-2119-45a2-8f3d-d2016bf3a123" -->
### Scaling Options
- **Dedicated GPU Instance:** For heavy browser workloads
- **Container-based browsers:** Docker isolation per task
- **Horizontal scaling:** Multiple VPS instances

<!-- section_id: "7d655d00-cf2a-40e1-ad55-ac45644c7c51" -->
## Phase 4: Unreal Engine & Gaming Access

<!-- section_id: "69782a47-6e38-4631-9345-cb02fcbacded" -->
### Requirements
Accessing Unreal Engine 3D environment and gaming from phone requires GPU capabilities, which Oracle Free Tier does not provide.

<!-- section_id: "94f80866-54e3-4ebc-8e17-7e906362986e" -->
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

<!-- section_id: "d0044d61-d7be-45a2-ad31-af4b91e4ca90" -->
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

<!-- section_id: "544cf9f2-136c-4f49-ae8b-b73b3731ebd2" -->
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

<!-- section_id: "e4ca2d5e-20e7-463f-b664-f57399e30b4b" -->
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

<!-- section_id: "91f9db20-b69d-4d2f-933c-b637c8017725" -->
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

<!-- section_id: "a4e871b2-81b8-4ee9-b9ca-4a60413e09ff" -->
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

<!-- section_id: "5e27b3c7-d46c-45c7-a14d-b56cc0e911ab" -->
## Cost Analysis

| Component | Cost | Notes |
|-----------|------|-------|
| VPS (Oracle Free Tier) | $0/mo | Permanent free |
| Tailscale | $0/mo | Free tier (1 user, 100 devices) |
| VNC Viewer App | $0 | Free apps available |
| **Total** | **$0/mo** | Zero ongoing cost |

<!-- section_id: "a60860f5-aad9-4027-b894-e0ee243d07ff" -->
## Comparison to Alternatives

<!-- section_id: "979f7f9a-7ea6-4e61-898c-246807667ce4" -->
### vs. Cloud Desktop (Windows 365, AWS WorkSpaces)
- **Cost:** $20-40/mo vs. $0/mo
- **Flexibility:** Less vs. Full control
- **ARM Support:** Limited vs. Native

<!-- section_id: "9ab1ee43-c189-4023-95fd-0276506b0968" -->
### vs. Dedicated Browser Automation Services
- **Cost:** $50-200/mo vs. $0/mo
- **AI Integration:** Complex vs. Direct
- **Customization:** Limited vs. Unlimited

<!-- section_id: "2f41dba0-b095-4956-97e4-fc9845709fa1" -->
### vs. Local Phone Apps
- **Power:** Phone limited vs. VPS 24GB RAM
- **Persistence:** Requires phone on vs. Always available
- **Syncing:** Complex vs. Built-in (Syncthing)

<!-- section_id: "a06cf925-3476-4b0f-b96a-5b9164f317ca" -->
## References

- Oracle Cloud Free Tier: https://www.oracle.com/cloud/free/
- TigerVNC Documentation: https://tigervnc.org/
- Tailscale Setup Guide: https://tailscale.com/kb/
- Claude in Chrome: https://github.com/anthropics/claude-in-chrome
