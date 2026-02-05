# Fixes Applied: Yoga Pro 9 Speaker I2C Configuration

## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

## Date
2026-01-26

## Fix 1: Blacklist TAS2781 Kernel Driver

### Problem

The `snd_hda_scodec_tas2781_i2c` kernel driver was resetting our I2C configuration:
- Audio worked immediately after running bypass script
- Within seconds, audio reverted to weak/thin state
- Driver was reinitializing amplifier with default settings

### Diagnosis

```bash
lsmod | grep -i tas
# Output showed snd_hda_scodec_tas2781_i2c loaded
```

### Fix

Created driver blacklist file:

```bash
sudo tee /etc/modprobe.d/disable-tas2781-driver.conf << 'EOF'
blacklist snd_hda_scodec_tas2781_i2c
EOF
```

### Verification

```bash
# After reboot, driver should not be loaded
lsmod | grep snd_hda_scodec_tas2781_i2c
# Should return nothing
```

### Result

Driver blacklisted. Requires reboot to take effect permanently.

---

## Fix 2: Immediate Driver Removal (Without Reboot)

### Problem

User needed audio working immediately, couldn't wait for reboot.

### Fix

Unloaded driver from running kernel:

```bash
sudo rmmod snd_hda_scodec_tas2781_i2c
```

Then re-ran the bypass script:

```bash
sudo /usr/local/bin/2pa-byps.sh
```

### Verification

```bash
lsmod | grep -i tas
# Only library modules remain:
# snd_soc_tas2781_fmwlib
# snd_soc_tas2781_comlib
# (these don't interfere with I2C settings)
```

### Result

Audio working immediately. User confirmed: "It's working better. Much better."

---

## Summary of All Fixes

| Fix | Problem | Solution | Status |
|-----|---------|----------|--------|
| 1 | Driver resets I2C config | Blacklist driver | Applied (needs reboot) |
| 2 | Need immediate fix | rmmod driver | Applied |

---

## Files Modified/Created

| File | Action | Purpose |
|------|--------|---------|
| `/etc/modprobe.d/disable-tas2781-driver.conf` | Created | Blacklist TAS2781 driver |
| `/usr/local/bin/2pa-byps.sh` | Created | I2C bypass script |
| `/etc/systemd/system/yoga-16imh9-speakers.service` | Created | Run script at boot/resume |

---

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
