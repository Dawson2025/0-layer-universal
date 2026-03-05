---
resource_id: "f6ae8ef5-efa1-486c-ac41-b6cb2614228b"
resource_type: "knowledge"
resource_name: "PHASE_4_UNREAL_GPU_GUIDE"
---
# Phase 4: Unreal Engine & GPU Access from Phone

**Date:** 2026-01-10
**Status:** Planning Phase
**Prerequisites:** Phases 1-3 complete (VPS relay, Tailscale, AI agents)

<!-- section_id: "50484c05-562a-4cb9-bdd1-5313b619c789" -->
## Goal

Access Unreal Engine 3D environment and gaming from your phone without requiring your laptop to be on.

<!-- section_id: "5a094494-ad70-405c-9084-64bba79a0ac1" -->
## The Challenge

- Oracle Cloud Free Tier VPS = No GPU (CPU-only ARM processors)
- Unreal Engine requires GPU for 3D rendering
- Solution: Cloud GPU instance or laptop streaming

<!-- section_id: "d7c0ad8e-6b24-46f8-9982-da909fb549cf" -->
## Decision Matrix

<!-- section_id: "58f80bf9-3af4-46e9-bcd1-43046219b702" -->
### Quick Recommendations

| Your Usage Pattern | Best Solution | Monthly Cost |
|-------------------|---------------|--------------|
| Rarely use Unreal (< 10 hrs/mo) | Paperspace on-demand | $5-10 |
| Weekly sessions (20-40 hrs/mo) | Paperspace or Shadow PC | $15-40 |
| Daily Unreal work (50-100 hrs/mo) | Shadow PC subscription | $30-50 |
| Have laptop, occasional mobile | Laptop + Moonlight | $0 |
| Laptop + cloud backup | Laptop + Paperspace | $0-20 |

<!-- section_id: "bba6b492-4a3d-4b89-95db-186168037a44" -->
## Solution 1: Free Laptop Streaming ($0/month)

<!-- section_id: "053f0374-c1dd-44fc-ad2e-771c0a56acda" -->
### When to Use
- You have access to your Windows laptop
- Laptop can be left on or remotely woken
- Budget is primary concern
- Acceptable latency on your network

<!-- section_id: "09cbf0a7-e357-42e2-af5a-6ca9897070bc" -->
### Setup Guide

#### Step 1: Install Sunshine on Windows Laptop
```bash
# Download from: https://github.com/LizardByte/Sunshine/releases
# Install Sunshine (NVENC encoder if you have NVIDIA GPU)
# Configure in Sunshine web UI (https://localhost:47990)
```

#### Step 2: Install Moonlight on Phone
- iOS: https://apps.apple.com/app/moonlight-game-streaming/id1000551566
- Android: https://play.google.com/store/apps/details?id=com.limelight

#### Step 3: Configure Tailscale Connection
```bash
# On Windows laptop:
tailscale up

# Note your Tailscale IP (e.g., 100.x.x.x)
tailscale ip -4
```

#### Step 4: Connect from Phone
1. Open Moonlight app
2. Add PC manually using Tailscale IP
3. Pair with laptop (enter PIN)
4. Launch Unreal Engine
5. Stream at 1080p/60fps or higher

<!-- section_id: "5fbb676e-e6d7-4b57-83e0-a9cd3c563bb1" -->
### Performance Tuning
- **Codec:** H.265 (better quality) or H.264 (better compatibility)
- **Bitrate:** 10-30 Mbps for 1080p, 50-80 Mbps for 4K
- **Resolution:** 1920x1080 or 1280x720 on phone
- **FPS:** 30-60 fps

<!-- section_id: "2c81083c-f6a6-4db6-b8a4-c1566ac87a91" -->
### Pros
- $0 cost
- Full GPU power of your laptop
- Low latency on same network
- Complete control over environment

<!-- section_id: "05cfca26-3a52-46f1-963d-9e23d82c2e5a" -->
### Cons
- Laptop must be on
- Requires good upload speed from home
- Network dependent
- Power consumption (~50-100W)

---

<!-- section_id: "e90bce65-fec8-4d0a-a307-ae7b13601b81" -->
## Solution 2: Cloud GPU Instances (Always Available)

<!-- section_id: "4af01e28-c985-4db0-875b-023d36bfc656" -->
### Option A: Paperspace (Best for On-Demand)

**Recommended for:** Occasional to regular Unreal users

#### Pricing
- **M4000 GPU:** $0.51/hour (good for Unreal Editor)
- **P4000 GPU:** $0.78/hour (better performance)
- **RTX 4000:** $0.82/hour (ray tracing)
- **RTX 5000:** $1.10/hour (heavy projects)

#### Real Cost Examples
| Monthly Usage | GPU Type | Monthly Cost |
|---------------|----------|--------------|
| 10 hours | M4000 | $5.10 |
| 30 hours | M4000 | $15.30 |
| 50 hours | M4000 | $25.50 |
| 100 hours | M4000 | $51.00 |
| 100 hours | RTX 4000 | $82.00 |

#### Setup Guide
1. Sign up: https://www.paperspace.com/
2. Create Machine > Core plan
3. Select GPU tier (start with M4000)
4. Choose Ubuntu or Windows
5. Install Unreal Engine
6. Use built-in streaming or install Parsec
7. Stop machine when done (hourly billing)

#### Workflow
```bash
# Start machine via web dashboard or API
# Connect via Parsec or web console
# Work on Unreal project
# Stop machine when finished
# Only pay for hours used
```

#### Pros
- Pay only when using
- No monthly commitment
- Multiple GPU options
- Built-in streaming
- Easy scaling

#### Cons
- Hourly cost adds up for heavy use
- Need to remember to stop instances
- Storage costs when machine is off

---

<!-- section_id: "f42b3db4-0eba-4a9c-a54c-246443362d52" -->
### Option B: Shadow PC (Best for Daily Use)

**Recommended for:** Daily Unreal users, want simplicity

#### Pricing
- **Subscription:** $29.99-49.99/month
- **Usage:** Unlimited hours
- **GPU:** GTX 1080 equivalent or better (varies by tier)

#### Setup Guide
1. Sign up: https://shadow.tech/
2. Choose subscription tier
3. Download Shadow app on phone
4. Install Unreal Engine in Shadow PC
5. Stream from anywhere

#### Workflow
- Open Shadow app on phone
- Instant access to Windows PC
- Use like local machine
- Close when done (no hourly charges)

#### Pros
- Flat monthly rate
- Unlimited usage
- Optimized streaming
- Simplest setup
- No server management

#### Cons
- Pay even if not using
- Less control than VPS
- Fixed hardware specs
- Subscription commitment

---

<!-- section_id: "52861587-15f9-4ff9-8a06-52f53df7b254" -->
### Option C: AWS EC2 (Best for Enterprise)

**Recommended for:** AWS users, professional workflows

#### Pricing
- **g4dn.xlarge:** $0.526/hour (~$380/mo always-on)
- **g4dn.2xlarge:** $0.752/hour (more CPU/RAM)
- **Spot instances:** ~$0.16/hour (70% cheaper, can be terminated)

#### Setup Guide
```bash
# 1. Launch EC2 instance
aws ec2 run-instances \
  --instance-type g4dn.xlarge \
  --image-id ami-xxxx \
  --key-name your-key

# 2. Install NVIDIA drivers
sudo apt update
sudo apt install nvidia-driver-525

# 3. Install desktop environment
sudo apt install ubuntu-desktop

# 4. Install VNC or Parsec for streaming

# 5. Install Unreal Engine

# 6. Stop when done
aws ec2 stop-instances --instance-ids i-xxxxx
```

#### Cost Optimization
- **Stop when not using:** $0/hour when stopped (only pay for storage)
- **Use Spot instances:** 70% cheaper for non-critical work
- **Schedule auto-stop:** Lambda function to stop after hours

#### Pros
- Enterprise reliability
- AWS ecosystem integration
- Flexible scaling
- Stop/start to save money

#### Cons
- Most expensive option
- Requires AWS knowledge
- Manual streaming setup
- Complex for beginners

---

<!-- section_id: "2944fc6a-011f-4154-bfcf-8d4b62920586" -->
### Option D: Maximum Labs (Best Price/Performance)

**Recommended for:** Budget-conscious, want modern GPUs

#### Pricing
- **RTX 3070:** $0.41/hour (~$300/mo always-on)
- **RTX 4090:** $0.80/hour (top-tier consumer GPU)

#### Setup
Similar to AWS, but with better GPU options at lower cost.

#### Pros
- Best GPU price/performance
- Modern consumer GPUs
- Good for Unreal 5

#### Cons
- Smaller company
- Less infrastructure than AWS
- Fewer regions

---

<!-- section_id: "cc6153c4-e9a0-482c-a8df-140da7c58018" -->
## Solution 3: Hybrid Model (RECOMMENDED)

<!-- section_id: "0261aeab-e1a3-4b34-b65c-a210f71fe966" -->
### Architecture

**Day-to-day work:**
- Oracle Free VPS ($0/mo)
  - Code editing via SSH
  - File sync via Syncthing
  - AI agents
  - Browser automation
  - Light development tasks

**GPU-intensive sessions:**
- Paperspace on-demand or Shadow PC
  - Unreal Engine
  - 3D rendering
  - Gaming
  - GPU-accelerated tasks

<!-- section_id: "227adeb7-5324-4588-8b4f-f101cd822f64" -->
### Why This Works Best

1. **Cost optimized:** Only pay for GPU when needed
2. **Always accessible:** Oracle VPS available 24/7 for code
3. **Flexible:** Choose GPU tier based on task
4. **Scalable:** Add more GPU time as needed

<!-- section_id: "c2f9ed2f-b24a-45e8-9a0e-458cb6d08a50" -->
### Monthly Cost Examples

| Scenario | VPS Cost | GPU Cost | Total |
|----------|----------|----------|-------|
| Light Unreal (10 hrs) | $0 | $5-10 | $5-10 |
| Regular use (30 hrs) | $0 | $15-30 | $15-30 |
| Heavy use (100 hrs) | $0 | Shadow $30 | $30 |
| Professional (200 hrs) | $0 | Shadow $40 | $40 |

**vs. Always-On GPU:** $380-400/month

**Annual Savings:** $3,000-4,500/year

---

<!-- section_id: "442e175d-4136-4b34-94ce-06dd6984ea07" -->
## Implementation Checklist

<!-- section_id: "d06ad071-60ce-4206-ad94-1353f2f1bf5b" -->
### Phase 4A: Free Laptop Streaming (Do First)
- [ ] Install Tailscale on Windows laptop
- [ ] Install Sunshine on Windows laptop
- [ ] Configure Sunshine encoder settings
- [ ] Install Moonlight on phone
- [ ] Test streaming Unreal Engine
- [ ] Optimize bitrate and resolution
- [ ] Set up Wake-on-LAN (optional)

<!-- section_id: "fa62f204-b432-4222-b2d8-930c1ad24226" -->
### Phase 4B: Cloud GPU Setup (When Needed)
- [ ] Evaluate usage patterns (10, 30, 100 hrs/mo?)
- [ ] Choose provider (Paperspace/Shadow/AWS)
- [ ] Create account and provision instance
- [ ] Install Unreal Engine on cloud instance
- [ ] Configure streaming (Parsec/Moonlight)
- [ ] Test from phone
- [ ] Set up auto-stop scripts (if applicable)

<!-- section_id: "7db345a1-953d-48a9-9b4a-c766a21ce757" -->
### Phase 4C: Optimization
- [ ] Test latency on WiFi vs 4G/5G
- [ ] Configure Bluetooth controller
- [ ] Set up project sync with VPS
- [ ] Create workflow documentation
- [ ] Monitor costs and usage

---

<!-- section_id: "c8282c4b-9dab-4fe7-8e33-1aa528892a16" -->
## Network Requirements

<!-- section_id: "28acacfa-12f0-4ade-8a6b-8fa3f754093e" -->
### For Laptop Streaming
- **Home Upload Speed:** 10+ Mbps (25+ Mbps recommended)
- **Phone Download:** 10+ Mbps for 1080p
- **Latency:** < 50ms for good experience

<!-- section_id: "be8a3c16-7e3b-4c60-8660-e7d955ab4212" -->
### For Cloud GPU Streaming
- **Download (phone):** 10-25+ Mbps
- **Upload (from cloud):** Usually 100+ Mbps (not a concern)
- **Latency:** 30-100ms depending on location

<!-- section_id: "4cae82ef-e82c-44ca-a978-6a9176258a1f" -->
### Testing Your Connection
```bash
# Test upload speed from laptop
speedtest-cli

# Test latency to cloud
ping -c 10 <cloud-provider-ip>
```

---

<!-- section_id: "0b7df94e-c753-4770-83be-23dd464d6a4d" -->
## Controller Options

<!-- section_id: "4c8721e3-927f-4c23-9f36-4b077e6f1691" -->
### Bluetooth Controllers
- Xbox Wireless Controller
- PlayStation DualShock/DualSense
- 8BitDo Pro 2

<!-- section_id: "f376c5f3-a609-4acc-a7a9-bec2d0f26120" -->
### Phone Mount Controllers
- Backbone One (lightning/USB-C)
- Razer Kishi V2
- GameSir X2

<!-- section_id: "c8b0af32-6a01-4c1f-8547-2ec056bb8614" -->
### Touch Controls
- Works for basic navigation
- Not ideal for complex Unreal work
- Better with stylus for precision

---

<!-- section_id: "84699a3a-b640-459d-995c-7468fc1b45b6" -->
## Troubleshooting

<!-- section_id: "7fcb684e-a208-4af7-8d89-b8b6e1bf4f14" -->
### High Latency
- Switch to 5GHz WiFi or ethernet
- Reduce streaming resolution
- Use H.264 instead of H.265
- Check for background downloads

<!-- section_id: "f0a59df0-7d6a-4bb0-b0ca-523a9328a164" -->
### Poor Video Quality
- Increase bitrate (20-50 Mbps)
- Use wired connection
- Reduce resolution on phone
- Check GPU encoding (NVENC/QuickSync)

<!-- section_id: "3df9f2ea-6dcd-46f5-b36f-c9ce2c18cda8" -->
### Disconnections
- Verify Tailscale is connected
- Check firewall settings
- Ensure laptop isn't sleeping
- Use static Tailscale IP

---

<!-- section_id: "d36d1223-2bbe-4483-a0e1-2f47ce48b046" -->
## Cost Tracking

<!-- section_id: "2f218754-c2c9-4a80-9ccf-56d1d2dbf124" -->
### Monthly Budget Calculator

```
Laptop Streaming:
  - Electricity (~50W, $0.12/kWh): $___/mo
  - Total: $0-5/mo

Paperspace On-Demand:
  - Hours/month: ____
  - Rate/hour: $0.51
  - Total: $_____/mo

Shadow PC:
  - Subscription: $30-50/mo
  - Total: $30-50/mo

AWS EC2:
  - Hours running: ____
  - Rate: $0.526/hr
  - Total: $_____/mo
  - Storage: $10-20/mo
```

---

<!-- section_id: "b51cbf76-4ce1-42af-8f12-62b361d72cf5" -->
## Next Steps

1. **Immediate:** Test laptop streaming with Moonlight + Sunshine ($0)
2. **Evaluate:** Track how many hours you'd use Unreal monthly
3. **Decide:**
   - < 30 hrs/mo = Paperspace on-demand
   - 50-100 hrs/mo = Shadow PC
   - Have laptop = Stick with free streaming
4. **Implement:** Set up chosen solution
5. **Optimize:** Monitor costs and adjust

---

<!-- section_id: "d571ad82-6fb6-4cdf-ac73-85a6fd15cf43" -->
## References

- Moonlight + Sunshine: https://github.com/LizardByte/Sunshine
- Paperspace: https://www.paperspace.com/
- Shadow PC: https://shadow.tech/
- AWS EC2 GPU: https://aws.amazon.com/ec2/instance-types/g4/
- Maximum Labs: https://maximum.com/
- Tailscale Setup: https://tailscale.com/kb/
