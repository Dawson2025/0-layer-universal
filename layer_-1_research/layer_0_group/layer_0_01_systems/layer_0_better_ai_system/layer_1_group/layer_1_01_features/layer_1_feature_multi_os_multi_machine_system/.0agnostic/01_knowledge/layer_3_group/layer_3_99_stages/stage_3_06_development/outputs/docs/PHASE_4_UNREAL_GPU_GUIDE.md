---
resource_id: "f6ae8ef5-efa1-486c-ac41-b6cb2614228b"
resource_type: "knowledge"
resource_name: "PHASE_4_UNREAL_GPU_GUIDE"
---
# Phase 4: Unreal Engine & GPU Access from Phone

**Date:** 2026-01-10
**Status:** Planning Phase
**Prerequisites:** Phases 1-3 complete (VPS relay, Tailscale, AI agents)

## Goal

Access Unreal Engine 3D environment and gaming from your phone without requiring your laptop to be on.

## The Challenge

- Oracle Cloud Free Tier VPS = No GPU (CPU-only ARM processors)
- Unreal Engine requires GPU for 3D rendering
- Solution: Cloud GPU instance or laptop streaming

## Decision Matrix

### Quick Recommendations

| Your Usage Pattern | Best Solution | Monthly Cost |
|-------------------|---------------|--------------|
| Rarely use Unreal (< 10 hrs/mo) | Paperspace on-demand | $5-10 |
| Weekly sessions (20-40 hrs/mo) | Paperspace or Shadow PC | $15-40 |
| Daily Unreal work (50-100 hrs/mo) | Shadow PC subscription | $30-50 |
| Have laptop, occasional mobile | Laptop + Moonlight | $0 |
| Laptop + cloud backup | Laptop + Paperspace | $0-20 |

## Solution 1: Free Laptop Streaming ($0/month)

### When to Use
- You have access to your Windows laptop
- Laptop can be left on or remotely woken
- Budget is primary concern
- Acceptable latency on your network

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

### Performance Tuning
- **Codec:** H.265 (better quality) or H.264 (better compatibility)
- **Bitrate:** 10-30 Mbps for 1080p, 50-80 Mbps for 4K
- **Resolution:** 1920x1080 or 1280x720 on phone
- **FPS:** 30-60 fps

### Pros
- $0 cost
- Full GPU power of your laptop
- Low latency on same network
- Complete control over environment

### Cons
- Laptop must be on
- Requires good upload speed from home
- Network dependent
- Power consumption (~50-100W)

---

## Solution 2: Cloud GPU Instances (Always Available)

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

## Solution 3: Hybrid Model (RECOMMENDED)

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

### Why This Works Best

1. **Cost optimized:** Only pay for GPU when needed
2. **Always accessible:** Oracle VPS available 24/7 for code
3. **Flexible:** Choose GPU tier based on task
4. **Scalable:** Add more GPU time as needed

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

## Implementation Checklist

### Phase 4A: Free Laptop Streaming (Do First)
- [ ] Install Tailscale on Windows laptop
- [ ] Install Sunshine on Windows laptop
- [ ] Configure Sunshine encoder settings
- [ ] Install Moonlight on phone
- [ ] Test streaming Unreal Engine
- [ ] Optimize bitrate and resolution
- [ ] Set up Wake-on-LAN (optional)

### Phase 4B: Cloud GPU Setup (When Needed)
- [ ] Evaluate usage patterns (10, 30, 100 hrs/mo?)
- [ ] Choose provider (Paperspace/Shadow/AWS)
- [ ] Create account and provision instance
- [ ] Install Unreal Engine on cloud instance
- [ ] Configure streaming (Parsec/Moonlight)
- [ ] Test from phone
- [ ] Set up auto-stop scripts (if applicable)

### Phase 4C: Optimization
- [ ] Test latency on WiFi vs 4G/5G
- [ ] Configure Bluetooth controller
- [ ] Set up project sync with VPS
- [ ] Create workflow documentation
- [ ] Monitor costs and usage

---

## Network Requirements

### For Laptop Streaming
- **Home Upload Speed:** 10+ Mbps (25+ Mbps recommended)
- **Phone Download:** 10+ Mbps for 1080p
- **Latency:** < 50ms for good experience

### For Cloud GPU Streaming
- **Download (phone):** 10-25+ Mbps
- **Upload (from cloud):** Usually 100+ Mbps (not a concern)
- **Latency:** 30-100ms depending on location

### Testing Your Connection
```bash
# Test upload speed from laptop
speedtest-cli

# Test latency to cloud
ping -c 10 <cloud-provider-ip>
```

---

## Controller Options

### Bluetooth Controllers
- Xbox Wireless Controller
- PlayStation DualShock/DualSense
- 8BitDo Pro 2

### Phone Mount Controllers
- Backbone One (lightning/USB-C)
- Razer Kishi V2
- GameSir X2

### Touch Controls
- Works for basic navigation
- Not ideal for complex Unreal work
- Better with stylus for precision

---

## Troubleshooting

### High Latency
- Switch to 5GHz WiFi or ethernet
- Reduce streaming resolution
- Use H.264 instead of H.265
- Check for background downloads

### Poor Video Quality
- Increase bitrate (20-50 Mbps)
- Use wired connection
- Reduce resolution on phone
- Check GPU encoding (NVENC/QuickSync)

### Disconnections
- Verify Tailscale is connected
- Check firewall settings
- Ensure laptop isn't sleeping
- Use static Tailscale IP

---

## Cost Tracking

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

## References

- Moonlight + Sunshine: https://github.com/LizardByte/Sunshine
- Paperspace: https://www.paperspace.com/
- Shadow PC: https://shadow.tech/
- AWS EC2 GPU: https://aws.amazon.com/ec2/instance-types/g4/
- Maximum Labs: https://maximum.com/
- Tailscale Setup: https://tailscale.com/kb/
