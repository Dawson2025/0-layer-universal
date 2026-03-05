---
resource_id: "366c25f6-3bf8-4cda-8b5c-970a6a1077c6"
resource_type: "knowledge"
resource_name: "SYNCTHING_ALTERNATIVES_RESEARCH"
---
# Syncthing Alternatives Research

**Date:** 2026-01-11
**Question:** Is Syncthing the best platform for dual-boot Windows/Ubuntu sync via VPS relay, or are there better alternatives?

<!-- section_id: "28be3979-f580-4158-96e4-9171ad55483f" -->
## Executive Summary

**Answer:** Syncthing remains the best choice for dual-boot VPS relay scenarios. While several compelling alternatives exist (Resilio Sync, Seafile, Rclone, Nextcloud), Syncthing is purpose-built for P2P relay use cases and offers the best balance of features, privacy, and performance for this specific scenario.

---

<!-- section_id: "bef13a63-4c17-4501-8d9e-77bfa02732df" -->
## Research Methodology

- Analyzed Reddit discussions, HackerNews, Stack Overflow, tech blogs (2024-2026)
- Reviewed recent tool releases and community sentiment
- Compared performance benchmarks and real-world usage
- Evaluated suitability specifically for dual-boot + VPS relay architecture

---

<!-- section_id: "10b30c53-62ae-42e8-aa76-1bf2da41b35e" -->
## Top Alternatives to Syncthing

<!-- section_id: "301cd2a0-d214-4fb0-a9c8-fb28b245fdcc" -->
### 1. Resilio Sync (Most Common Alternative)

**Type:** Proprietary BitTorrent-based P2P sync

**Performance Benchmarks (2025):**
- 2-4x faster than Syncthing
- 99.6% success rate across 2,847 file transfers
- 240 MB/s sustained on gigabit connections
- 4.2 min for 10GB transfer

**Pros:**
- Faster out-of-the-box (better default tuning)
- Mature, reliable relay support
- Excellent for large files
- Native apps for all platforms

**Cons:**
- Proprietary (closed source)
- Freemium model limits features
- Less community control
- Privacy concerns with proprietary protocol

**Dual-Boot Suitability:** 9/10
**Best For:** Performance-critical scenarios where speed matters most

---

<!-- section_id: "d5a40dda-431e-4615-a6e8-8d3f40a1473b" -->
### 2. Seafile (Fastest Server-Based)

**Type:** Self-hosted file sync server with block-based syncing

**Performance Benchmarks (2025):**
- 6 min for 11GB folder (vs Nextcloud's 17 min)
- Lowest RAM usage (~200 MB)
- Ranked #1 by Slant community for self-hosted storage

**Pros:**
- Blazing fast sync speeds
- Efficient block-level sync
- Clean web interface
- Low resource usage
- Can access files via web from anywhere

**Cons:**
- Requires full server setup (not just relay)
- Centralized architecture (single point of failure)
- Less feature-rich than Nextcloud
- Smaller community than Syncthing/Nextcloud

**Dual-Boot Suitability:** 8/10
**Best For:** Speed priority + wanting web access to files

---

<!-- section_id: "af93a84e-3bde-40a7-a702-da3dad046e9a" -->
### 3. Rclone (Scheduled Sync)

**Type:** Command-line periodic sync tool

**Performance Benchmarks (2025):**
- 4x faster than rsync (Jeff Geerling testing)
- Supports 70+ cloud backends
- Multi-threaded transfers

**Pros:**
- Simple, lightweight
- Great for scheduled backups
- Minimal VPS resources
- Highly reliable
- Excellent documentation

**Cons:**
- **No real-time sync** (scheduled/manual only)
- CLI only (no GUI)
- Manual conflict resolution
- Requires scheduling setup (cron)

**Dual-Boot Suitability:** 6/10
**Best For:** Scheduled sync acceptable, simplicity priority

**Common Pattern:** Many developers use Rclone **alongside** Syncthing
- Syncthing for real-time device sync
- Rclone for periodic backup to cloud storage

---

<!-- section_id: "8682179d-73c1-4534-ad36-5a5895290c8e" -->
### 4. Nextcloud (Full-Featured Suite)

**Type:** Complete collaboration platform with file sync

**Deployment Stats:**
- 400,000+ installations worldwide
- Very large community
- Active development

**Performance:**
- 17 min for 11GB folder (slower than Seafile/Syncthing)
- Resource-heavy on VPS

**Pros:**
- Full collaboration suite (office apps, calendar, contacts)
- Web access from anywhere
- Huge community and ecosystem
- Excellent documentation
- Most feature-complete

**Cons:**
- Slower sync than alternatives
- High resource usage
- Over-engineered for simple file sync
- Complexity overhead

**Dual-Boot Suitability:** 7/10
**Best For:** Want full collaboration suite, not just sync

---

<!-- section_id: "016536ea-55ad-46c9-82df-5b5cc704b00d" -->
### 5. FreeFileSync + RealTimeSync

**Type:** Open-source GUI sync tool with optional real-time monitoring

**Latest Release:** v14.6 (December 2025)

**Pros:**
- User-friendly GUI
- Reliable, actively maintained
- Good documentation
- Transparent operation
- Excellent for scheduled tasks

**Cons:**
- No built-in network relay support
- RealTimeSync less sophisticated than true P2P
- Windows-centric development
- Limited for dual-boot scenarios

**Dual-Boot Suitability:** 5/10
**Best For:** GUI users, Windows-heavy environments

---

<!-- section_id: "2c324393-7e61-463b-a3fb-768e8b63a446" -->
### 6. Unison

**Type:** Mature two-way sync tool (since early 2000s)

**Pros:**
- Mature, reliable
- Good conflict handling
- Cross-platform (Windows, macOS, Linux, BSD)

**Cons:**
- Minimal maintenance (2.5 developers, 0.1 FTE)
- Aging codebase
- Limited recent updates
- Small community

**Dual-Boot Suitability:** 6/10
**Best For:** Traditional two-way sync, academic use

---

<!-- section_id: "ab22fabe-6d3d-48ad-8154-80608ed49583" -->
## Feature Comparison Matrix

| Feature | Syncthing | Resilio Sync | Seafile | Nextcloud | Rclone | FreeFileSync |
|---------|-----------|--------------|---------|-----------|--------|--------------|
| **Real-time Sync** | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ (RealTimeSync) |
| **Bidirectional** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **VPS Relay Support** | ✓ (built-in) | ✓ | Server required | Server required | ✓ | ✗ |
| **Open Source** | ✓ (MPL v2) | ✗ | ✓ (GPL/Commercial) | ✓ (AGPL) | ✓ (MIT) | ✓ (GPL v3) |
| **Encryption in Transit** | ✓ (TLS 1.3) | ✓ | ✓ | ✓ | ✓ | ✗ |
| **Encryption at Rest** | ✗ (external) | ✓ | ✓ (AES-256) | ✓ | Backend-dependent | ✗ |
| **Cross-Platform** | Excellent | Excellent | Excellent | Excellent | Excellent | Excellent |
| **GUI** | Web-based | Native/Web | Web | Web | CLI only | Native GUI |
| **Block-level Sync** | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| **Mobile Support** | Limited iOS | Excellent | Excellent | Excellent | N/A | N/A |
| **Privacy** | Excellent | Good | Excellent | Excellent | Excellent | Excellent |

---

<!-- section_id: "800ea635-77a3-40df-8955-1b52b7fc109d" -->
## Performance Comparison

**Speed Rankings (Based on 2025 Testing):**

1. **Resilio Sync**: 4.2 min for 10GB transfer
2. **Seafile**: 6 min for 11GB folder
3. **Syncthing**: Variable (configuration-dependent)
4. **Nextcloud**: 17 min for 11GB folder
5. **FreeFileSync**: On-demand only
6. **Rclone**: 4x faster than rsync (for scheduled sync)

**Network Efficiency:**
- **Syncthing 2.0**: Multiple connections by default (1 metadata + 2 data streams)
- **Resilio Sync**: "2-10x improvement with P2P tech"
- **Rclone**: Multi-threaded, parallel transfers

---

<!-- section_id: "2a2e5c87-9dc0-429f-a0c5-17caf05a72dd" -->
## Community Support Comparison

| Tool | GitHub Stars | Development | Community | Documentation |
|------|--------------|-------------|-----------|---------------|
| Syncthing | 60k+ | Very Active | Large | Excellent |
| Nextcloud | 25k+ | Very Active | Very Large | Excellent |
| Rclone | 45k+ | Very Active | Large | Excellent |
| Seafile | 11k+ | Active | Medium | Good |
| FreeFileSync | N/A | Active | Medium | Good |
| Unison | 4k+ | Minimal | Small | Good |
| Resilio Sync | Proprietary | Active | Medium | Good |

---

<!-- section_id: "06a88a88-22fb-4779-8653-7c8f010b04f9" -->
## What Developers Actually Use (2024-2026)

<!-- section_id: "0f90a81d-69f2-46af-9869-eebaad0a5be7" -->
### Primary Choices from Community Data:

**1. Syncthing** - Dominant for personal/small team use
- "For 2-5 devices in a household or small team, Syncthing's zero-maintenance approach often wins"
- Privacy-conscious developers prefer it
- Zero server requirement appeals to self-hosters

**2. Resilio Sync** - Performance-critical scenarios
- "Can't beat the speed when you need it"
- Popular in business environments
- Used when performance > open source priority

**3. Rclone** - Cloud backup/multi-cloud scenarios
- Often used complementary to Syncthing
- Common pattern: "Syncthing for device sync + Rclone for cloud backup"

**4. Seafile** - Self-hosted with speed priority
- "Seafile stands out for anyone who values speed, reliability, and a rich feature set"
- Popular in academic/research environments

**5. Nextcloud** - Team collaboration
- Dominates self-hosted collaboration space
- Used when you need more than just file sync

---

<!-- section_id: "e2c1daaf-9173-402f-a628-fc7f40c9eb04" -->
## Syncthing Recent Developments (2024-2025)

<!-- section_id: "a7ddab5f-79a7-4809-8934-02df6eb82bdb" -->
### Syncthing 2.0 Release (August 2025)

**Major Changes:**
- Database migration to SQLite (more reliable)
- Multiple connections by default
- 6-month deleted file retention policy

**Positive:**
- Better database reliability
- Improved performance for many users

**Controversial:**
- Removed rolling hash detection
  - Now downloads entire file on change (vs just changed blocks)
  - Impacts large files on slow connections
- Platform support dropped for some systems (due to SQLite compilation)

**Community Reaction:**
- Generally positive for stability improvements
- Some performance concerns with rolling hash removal
- "Expect some rough edges and keep a sense of adventure"

<!-- section_id: "7ac92267-3327-4244-bb13-116ce5a61b60" -->
### Android App Discontinued (December 2024)

**Issue:** Official Android app removed from Google Play Store due to policy changes

**Solution:** Community fork "Syncthing-Fork" continues development on F-Droid
- Active maintenance
- Additional improvements over official version

**Impact:** Desktop usage unaffected, iOS still limited

---

<!-- section_id: "c84d616b-259b-43e2-82b4-3c55ddb18a30" -->
## Reported Issues with Syncthing (2025)

Based on community discussions:

**Performance Issues:**
- "Files or folders inexplicably reporting as out of sync or 99% syncing stuck"
- "Devices dropping their connection and not regaining it until they restart"
- "Difficulty saturating LAN connections with default settings"

**Workarounds:**
- Manual performance tuning often needed
- Adjust connection limits, scan intervals
- Use multiple data connections (default in v2.0)

**V2.0 Specific:**
- Rolling hash removal means entire file re-download on change
- Some users report increased bandwidth usage for large files

---

<!-- section_id: "f42658df-f837-458b-a613-a685c8803a76" -->
## Dual-Boot Specific Considerations

<!-- section_id: "ad81b7e0-79e0-4ad7-b555-b43758545c9c" -->
### Challenge:
"Windows and Linux are installed on the same system, you can't run both OSes at the same time, making it impossible for Syncthing to sync between these devices"

<!-- section_id: "41b4e485-0304-4099-b710-f5a5f5e9329f" -->
### Solutions Ranked:

**1. VPS Relay with Syncthing** (Recommended) ⭐
- Set up private Syncthing relay on VPS
- Windows syncs to VPS when booted
- Ubuntu syncs to VPS when booted
- VPS acts as "always-on" intermediary
- Official support via `syncthing-relaysrv`

**2. VPS Server (Seafile/Nextcloud)**
- VPS runs full sync server
- Both OSes sync to VPS as central server
- Web access bonus
- Higher resource usage

**3. Shared NTFS Partition** (Not Recommended)
- Direct shared storage between OSes
- No sync needed
- Risk of file system corruption
- NTFS limitations on Linux

**4. Scheduled Sync (Rclone)**
- Manual or scheduled syncs to VPS
- Simpler setup
- No real-time sync
- Requires discipline to run

---

<!-- section_id: "c008501a-e530-4ab3-94ec-c0fd4b14e736" -->
## Suitability for Dual-Boot + VPS Relay

| Tool | Score | Reasoning |
|------|-------|-----------|
| **Syncthing** | 9/10 | Purpose-built for P2P relay, official relay server support |
| **Resilio Sync** | 9/10 | Excellent relay support, faster, but proprietary |
| **Seafile** | 8/10 | Fast and reliable, but requires full server setup |
| **Nextcloud** | 7/10 | Works well, but overkill for simple sync |
| **Rclone** | 6/10 | No real-time sync, manual scheduling |
| **Unison** | 6/10 | Works but minimal maintenance, aging |
| **FreeFileSync** | 5/10 | Limited network relay support |

---

<!-- section_id: "234b0aec-5e85-4c41-acbd-82d3bd3e32c0" -->
## Recommendation for Our Setup

<!-- section_id: "6f70f953-ca09-4778-8698-b508e801eb18" -->
### **Stick with Syncthing** ✅

**Reasons:**

1. **Purpose-Built for This Use Case**
   - Official VPS relay support (`syncthing-relaysrv`)
   - Designed for devices that aren't always online
   - Perfect for dual-boot scenario

2. **Already Implemented**
   - Windows/WSL already configured
   - VPS relay set up and working
   - 59% sync complete (as of 2026-01-11 23:46 PST)

3. **Open Source & Privacy**
   - No proprietary lock-in
   - Community control
   - End-to-end encryption

4. **Zero Additional Cost**
   - Only VPS cost (which we need anyway)
   - No cloud storage fees
   - No subscription required

5. **Proven & Popular**
   - Most common choice for this scenario
   - 60k+ GitHub stars
   - Large, active community

6. **Future-Proof**
   - Active development (v2.0 released Aug 2025)
   - Strong community support
   - Regular updates

<!-- section_id: "c2b531f5-2467-43d3-ad23-bc0cedb5cfef" -->
### When to Consider Alternatives:

**Switch to Resilio Sync if:**
- Speed becomes critical (need 2-4x faster)
- Willing to use proprietary software
- Budget for Pro features

**Switch to Seafile if:**
- Need web access to files from anywhere
- Want fastest server-based solution
- Centralized architecture is acceptable

**Add Rclone if:**
- Want periodic backup to cloud storage
- Complement Syncthing (not replace)
- Simple cloud backup needed

**Switch to Nextcloud if:**
- Need full collaboration suite
- Want office apps, calendar, contacts
- Team collaboration required

---

<!-- section_id: "20d71649-7c11-4251-b29c-8700fc72a6e6" -->
## iOS Considerations

<!-- section_id: "f25eeaf2-f56b-4a50-9428-8034476bcdd8" -->
### Syncthing on iOS: Very Limited ❌

**Problem:** Apple restrictions prevent background sync
- **Möbius Sync** exists but only works when app is open
- Not practical for real-time sync

<!-- section_id: "debb0324-0bf3-4b0b-9e15-c38dd776453a" -->
### Better Alternatives for iOS:

**1. SSH/SFTP to VPS** (Recommended)
- Apps: Blink Shell ($20), Termius (free tier)
- Access synced workspace directly on VPS
- Full terminal access

**2. VNC Desktop** (From Phase 3 Plan)
- Apps: VNC Viewer (free), Jump Desktop ($15)
- Full graphical desktop on VPS
- Visual file management

**3. Code-Server** (VS Code in Browser)
- Run VS Code on VPS
- Access via Safari on iPhone
- Full IDE experience

**4. Working Copy** (Git Client)
- For git repos specifically
- $20 for push access
- Excellent for code projects

<!-- section_id: "dc249ab9-422a-485b-aba9-5e02a3845b64" -->
### Android: Full Support ✅
- Official Syncthing-Fork app works perfectly
- Background sync supported
- True real-time sync to phone

---

<!-- section_id: "97f434fb-0cb0-48c8-9c38-d8ded36841eb" -->
## Technical Comparison: Architecture Types

<!-- section_id: "c8257268-9a2d-4d15-b5e7-8528ced03694" -->
### P2P Relay (Syncthing, Resilio Sync)
**How it works:**
```
Windows ←→ VPS Relay ←→ Ubuntu
```

**Pros:**
- No central server needed
- VPS just relays connections
- Lowest VPS resource usage
- Most privacy-preserving

**Cons:**
- No web access to files
- Requires all devices have client installed

<!-- section_id: "fd82c269-9157-44a8-a966-81f50a393a00" -->
### Client-Server (Seafile, Nextcloud)
**How it works:**
```
Windows → VPS Server ← Ubuntu
```

**Pros:**
- Web access from anywhere
- Central management
- Easier troubleshooting

**Cons:**
- Higher VPS resource usage
- Single point of failure
- More complex setup

<!-- section_id: "18133c15-0bb8-440c-a2a4-2c0a92a65e0a" -->
### Scheduled Sync (Rclone, FreeFileSync)
**How it works:**
```
Windows → (manual/cron) → VPS → (manual/cron) → Ubuntu
```

**Pros:**
- Simplest setup
- Lowest resource usage
- Full control over when sync happens

**Cons:**
- Not real-time
- Requires discipline
- Manual conflict resolution

---

<!-- section_id: "5e6b4e96-d130-4a8f-8ab2-92d068e97980" -->
## Migration Paths (If Needed Later)

<!-- section_id: "a1fce3e3-3e67-4f9e-bf08-8b40c436f358" -->
### From Syncthing → Resilio Sync
**Difficulty:** Easy
**Time:** 1-2 hours
**Steps:**
1. Install Resilio Sync on all devices
2. Share folder with VPS relay
3. Wait for initial sync
4. Disable Syncthing
**Data Loss Risk:** Low (both use P2P architecture)

<!-- section_id: "1d27ab25-1fcb-416b-abd5-285692844de3" -->
### From Syncthing → Seafile
**Difficulty:** Medium
**Time:** 3-4 hours
**Steps:**
1. Install Seafile server on VPS
2. Install Seafile clients on Windows/Ubuntu
3. Upload workspace to Seafile
4. Disable Syncthing
**Data Loss Risk:** Low (centralized server)

<!-- section_id: "6b8e4dc4-bfbc-469b-9048-83e750574126" -->
### From Syncthing → Nextcloud
**Difficulty:** Medium-High
**Time:** 4-6 hours
**Steps:**
1. Install Nextcloud on VPS (Docker recommended)
2. Install desktop clients
3. Upload workspace
4. Configure sync folders
**Data Loss Risk:** Low (centralized server)

<!-- section_id: "509d415c-d249-480a-be2a-bbdcfd044098" -->
### Adding Rclone (Complementary)
**Difficulty:** Easy
**Time:** 30 min
**Steps:**
1. Install rclone on VPS
2. Configure cloud backend
3. Set up cron job
4. Keep Syncthing running
**Data Loss Risk:** None (additive)

---

<!-- section_id: "cac0d225-9d63-4d59-9098-c79c6f466604" -->
## Cost Comparison (Annual)

| Solution | VPS Cost | Software Cost | Total/Year |
|----------|----------|---------------|------------|
| **Syncthing** | €49 ($54) | $0 | **$54** |
| **Resilio Sync Free** | €49 ($54) | $0 | **$54** |
| **Resilio Sync Pro** | €49 ($54) | $60/year | **$114** |
| **Seafile** | €49 ($54) | $0 | **$54** |
| **Nextcloud** | €49 ($54) | $0 | **$54** |
| **Rclone** | €49 ($54) | $0 | **$54** |
| **Cloud Sync (Dropbox)** | $0 | $120/year | **$120** |

**Note:** Assumes current Hetzner CX23 VPS (€4.09/month)
- Seafile/Nextcloud might need larger VPS for good performance
- Oracle Free Tier would reduce all costs to $0 (if approved)

---

<!-- section_id: "876b2a50-5012-4f32-990e-32392db3ac16" -->
## Security Comparison

| Feature | Syncthing | Resilio Sync | Seafile | Nextcloud | Rclone |
|---------|-----------|--------------|---------|-----------|--------|
| **Encryption in Transit** | TLS 1.3 | TLS | HTTPS | HTTPS | Backend-dependent |
| **Encryption at Rest** | External tool | ✓ Built-in | ✓ AES-256 | ✓ | Backend-dependent |
| **Zero-Knowledge** | ✓ (no server) | ✓ (no server) | ✗ | ✗ | Depends |
| **Open Source Audit** | ✓ | ✗ | ✓ | ✓ | ✓ |
| **Two-Factor Auth** | N/A | GUI password | ✓ | ✓ | N/A |
| **Device Authorization** | ✓ Device IDs | ✓ Keys | ✓ Tokens | ✓ Tokens | ✓ Keys |

---

<!-- section_id: "d8b870b5-112e-40d8-9bd9-792f4af2c7e2" -->
## Performance Tuning Tips for Syncthing

If you experience slow performance:

<!-- section_id: "feef048c-a97d-4bb1-aea6-9e6e18426d67" -->
### 1. Increase Concurrent Connections
```xml
<options>
    <maxConcurrentIncomingRequestKiB>256000</maxConcurrentIncomingRequestKiB>
</options>
```

<!-- section_id: "fb180f03-105d-4312-9323-3a48cf0d8357" -->
### 2. Adjust Scan Interval
```xml
<folder rescanIntervalS="3600">  <!-- Lower for faster detection -->
```

<!-- section_id: "4e810b7e-4960-441b-9453-5f057267307e" -->
### 3. Enable Multiple Connections
```xml
<device numConnections="0">  <!-- 0 = automatic, default in v2.0 -->
```

<!-- section_id: "1d1ae6b2-7e86-4733-baab-921c105923b2" -->
### 4. Optimize for LAN
```xml
<options>
    <limitBandwidthInLan>false</limitBandwidthInLan>
</options>
```

---

<!-- section_id: "c4e33817-2668-400c-80e3-f99873a30ef6" -->
## Conclusion

**For dual-boot Windows/Ubuntu synchronization via VPS relay:**

**Syncthing is the optimal choice** because:
- ✅ Purpose-built for P2P relay scenarios
- ✅ Official relay server support
- ✅ Open source and privacy-respecting
- ✅ Zero additional cost beyond VPS
- ✅ Already implemented and working
- ✅ Large, active community
- ✅ Proven reliability for this use case

**Alternatives are better in specific scenarios:**
- **Resilio Sync** if speed is paramount (2-4x faster)
- **Seafile** if you want web access + speed
- **Nextcloud** if you need full collaboration suite
- **Rclone** if scheduled sync is acceptable

**Recommendation:** Continue with Syncthing as implemented. If performance issues arise, tune first, then consider Resilio Sync as easiest migration path.

---

<!-- section_id: "d8854752-466a-4ca7-b852-873aa2265331" -->
## References

- [AlternativeTo Syncthing Alternatives](https://alternativeto.net/software/syncthing/)
- [Resilio Blog: Syncthing Alternative](https://www.resilio.com/blog/syncthing-alternative)
- [Syncthing Forum: Dual Boot Sync](https://forum.syncthing.net/t/dual-boot-and-sync-same-files/5658)
- [How-To Geek: Linux-Windows Dual Boot File Management](https://www.howtogeek.com/how-i-manage-files-in-my-linux-windows-dual-boot-pc/)
- [Raysync: Syncthing Slow Issue Fixed 2025](https://www.raysync.io/news/syncthing-slow/)
- [Syncthing Forum: 2.0 Release](https://forum.syncthing.net/t/syncthing-2-0-august-2025/24758)
- [Cloudee Reviews: Rclone vs Syncthing](https://cloudeereviews.com/blog/rclone-vs-syncthing/)
- [Jeff Geerling: 4x Faster Network File Sync](https://www.jeffgeerling.com/blog/2025/4x-faster-network-file-sync-rclone-vs-rsync)
- [SSD Nodes: Nextcloud vs Seafile](https://www.ssdnodes.com/blog/nextcloud-vs-seafile-dropbox-alternative/)
- [gHacks: Syncthing Android Discontinuation](https://www.ghacks.net/2024/10/21/syncthing-for-android-is-being-discontinued-but-theres-an-alternative-app-you-can-switch-to/)
- [Resilio Blog: Sync Speed Test](https://www.resilio.com/blog/sync-speed-test-over-16-times-faster-than-the-cloud)
- [FreeFileSync RealTimeSync Documentation](https://freefilesync.org/manual.php?topic=realtimesync)
- [Syncthing Relay Server Documentation](https://docs.syncthing.net/users/strelaysrv.html)
- [Linux.iac: Syncthing 2.0 Launch](https://linuxiac.com/syncthing-2-0-launches-with-major-database-overhaul/)

---

**Document Status:** ✅ Complete
**Last Updated:** 2026-01-11
**Next Review:** When considering migration or if performance issues arise
