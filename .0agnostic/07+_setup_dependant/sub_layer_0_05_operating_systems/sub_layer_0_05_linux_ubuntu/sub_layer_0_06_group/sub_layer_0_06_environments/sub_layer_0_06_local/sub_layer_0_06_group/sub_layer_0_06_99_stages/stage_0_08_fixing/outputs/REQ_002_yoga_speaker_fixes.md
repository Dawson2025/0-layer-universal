---
resource_id: "ff43095e-76b4-433f-abfd-8c97ea64d2b4"
resource_type: "output"
resource_name: "REQ_002_yoga_speaker_fixes"
---
# Fixes Applied: Yoga Pro 9 Speaker I2C Configuration

<!-- section_id: "d74a2deb-7b5f-48dc-90bc-8e020de89798" -->
## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

<!-- section_id: "b9ccaefd-a714-4d79-a4a7-2c2c257df948" -->
## Date
2026-01-26

<!-- section_id: "fc553e14-d525-4eb2-b2df-f9b764d32ff0" -->
## Fix 1: Blacklist TAS2781 Kernel Driver

<!-- section_id: "fd9ed234-93b4-47e9-a455-c0a5fd1ade98" -->
### Problem

The `snd_hda_scodec_tas2781_i2c` kernel driver was resetting our I2C configuration:
- Audio worked immediately after running bypass script
- Within seconds, audio reverted to weak/thin state
- Driver was reinitializing amplifier with default settings

<!-- section_id: "c37a965f-7114-4120-8b2a-a61c5c480968" -->
### Diagnosis

```bash
lsmod | grep -i tas
# Output showed snd_hda_scodec_tas2781_i2c loaded
```

<!-- section_id: "046d6036-4d67-4523-a314-0bd4940f3abb" -->
### Fix

Created driver blacklist file:

```bash
sudo tee /etc/modprobe.d/disable-tas2781-driver.conf << 'EOF'
blacklist snd_hda_scodec_tas2781_i2c
EOF
```

<!-- section_id: "cc75037f-7f7d-4cac-bfe1-b949dee26867" -->
### Verification

```bash
# After reboot, driver should not be loaded
lsmod | grep snd_hda_scodec_tas2781_i2c
# Should return nothing
```

<!-- section_id: "2f835801-248c-4819-b2b6-49d4c96e9863" -->
### Result

Driver blacklisted. Requires reboot to take effect permanently.

---

<!-- section_id: "bb0db639-4f97-4da4-8f63-e15b5aa28de4" -->
## Fix 2: Immediate Driver Removal (Without Reboot)

<!-- section_id: "d1ede5c3-b8b7-4fe7-b941-484782bbf4c5" -->
### Problem

User needed audio working immediately, couldn't wait for reboot.

<!-- section_id: "81915b25-6006-42bd-a6fa-47f591289781" -->
### Fix

Unloaded driver from running kernel:

```bash
sudo rmmod snd_hda_scodec_tas2781_i2c
```

Then re-ran the bypass script:

```bash
sudo /usr/local/bin/2pa-byps.sh
```

<!-- section_id: "98cad2e6-9061-46cc-b511-0cd3a2f03f96" -->
### Verification

```bash
lsmod | grep -i tas
# Only library modules remain:
# snd_soc_tas2781_fmwlib
# snd_soc_tas2781_comlib
# (these don't interfere with I2C settings)
```

<!-- section_id: "f9865a29-b6e8-4d80-94c6-18bbb6aac6f0" -->
### Result

Audio working immediately. User confirmed: "It's working better. Much better."

---

<!-- section_id: "7d358cb5-172b-4bd0-aa1e-44bae8633207" -->
## Summary of All Fixes

| Fix | Problem | Solution | Status |
|-----|---------|----------|--------|
| 1 | Driver resets I2C config | Blacklist driver | Applied (needs reboot) |
| 2 | Need immediate fix | rmmod driver | Applied |

---

<!-- section_id: "bd1e7484-fe1f-4577-8857-a5249c77612f" -->
## Files Modified/Created

| File | Action | Purpose |
|------|--------|---------|
| `/etc/modprobe.d/disable-tas2781-driver.conf` | Created | Blacklist TAS2781 driver |
| `/usr/local/bin/2pa-byps.sh` | Created | I2C bypass script |
| `/etc/systemd/system/yoga-16imh9-speakers.service` | Created | Run script at boot/resume |

---

<!-- section_id: "acc6e1e7-8ffa-43a5-836d-7213dea67fd0" -->
## Recovery Commands

If audio stops working after a system update or kernel change:

```bash
# 1. Re-blacklist driver if needed
sudo tee /etc/modprobe.d/disable-tas2781-driver.conf << 'EOF'
blacklist snd_hda_scodec_tas2781_i2c
EOF

# 2. Unload driver if currently loaded
sudo rmmod snd_hda_scodec_tas2781_i2c 2>/dev/null

# 3. Re-run bypass script
sudo /usr/local/bin/2pa-byps.sh

# 4. Reload EasyEffects preset
easyeffects --load-preset "Yoga Pro 9i Official"
```
