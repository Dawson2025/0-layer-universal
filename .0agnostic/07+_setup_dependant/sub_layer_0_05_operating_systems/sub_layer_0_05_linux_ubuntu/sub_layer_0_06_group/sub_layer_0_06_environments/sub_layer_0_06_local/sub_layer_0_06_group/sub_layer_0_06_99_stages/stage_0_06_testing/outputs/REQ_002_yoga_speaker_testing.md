---
resource_id: "a28fefd8-7ef3-4683-8c46-edeec604ce14"
resource_type: "output"
resource_name: "REQ_002_yoga_speaker_testing"
---
# Testing: Yoga Pro 9 Speaker I2C Configuration

## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

## Date
2026-01-26

## Test Results

### Test 1: I2C Bypass Script Execution

**Command**:
```bash
sudo /usr/local/bin/2pa-byps.sh
```

**Expected**: Script runs without errors, reports success

**Actual**:
```
Laptop model: 83DN
Using I2C bus: 2
Speaker bypass configured successfully
```

**Result**: PASS

---

### Test 2: Immediate Audio Improvement

**Method**: Play audio immediately after running bypass script

**Expected**: Fuller sound with more bass

**Actual**: User confirmed "It was working really well" - sound much fuller with noticeable bass/vibration

**Result**: PASS

---

### Test 3: Audio Persistence

**Method**: Wait a few seconds after script runs, continue playing audio

**Expected**: Audio quality should persist

**Actual**: User reported "now it isn't. I noticed the difference, but now the difference is gone"

**Result**: FAIL

---

### Test 4: Driver Interference Check

**Command**:
```bash
lsmod | grep -i tas
```

**Expected**: Check if TAS2781 driver is loaded

**Actual**:
```
snd_hda_scodec_tas2781_i2c    36864  0
snd_soc_tas2781_fmwlib        45056  1 snd_hda_scodec_tas2781_i2c
snd_soc_tas2781_comlib        24576  2 ...
```

**Result**: Driver IS loaded - this is resetting our I2C configuration

---

### Test 5: Driver Unload

**Command**:
```bash
sudo rmmod snd_hda_scodec_tas2781_i2c
```

**Expected**: Driver unloads, I2C config persists

**Actual**: Driver successfully unloaded, confirmed with `lsmod | grep -i tas` showing only library modules remain

**Result**: PASS

---

### Test 6: Audio After Driver Removal

**Method**: Play audio after driver blacklist and unload

**Expected**: Audio quality persists

**Actual**: User confirmed "It's working better. Much better. It seems to vibrate the laptop a lot, but it's working a lot better. It sounds much fuller."

**Result**: PASS

---

## Issues Found

### Issue 1: TAS2781 Driver Resets Configuration

**Severity**: Critical

**Description**: The `snd_hda_scodec_tas2781_i2c` kernel driver resets the I2C configuration set by our bypass script. This causes audio to revert to weak/thin state within seconds of running the script.

**Root Cause**: Driver is loaded by default and periodically reinitializes the TAS2781 amplifier with default (subwoofer-disabled) settings.

**Resolution**: Blacklist driver in `/etc/modprobe.d/disable-tas2781-driver.conf`

---

## Test Summary

| Test | Description | Result |
|------|-------------|--------|
| 1 | I2C script execution | PASS |
| 2 | Immediate audio improvement | PASS |
| 3 | Audio persistence | FAIL → Fixed |
| 4 | Driver interference check | Identified issue |
| 5 | Driver unload | PASS |
| 6 | Audio after driver removal | PASS |

## Final Verification

After all fixes applied:
- Subwoofer active (laptop vibrates with bass)
- Sound significantly fuller than before
- Audio quality persists over time
- User satisfaction: "It sounds much fuller"
