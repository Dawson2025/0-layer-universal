# Testing: Laptop Speaker Audio Enhancement

## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

## Date
2026-01-26

## Test Results

### Test 1: Basic Preset
| Aspect | Result | Notes |
|--------|--------|-------|
| Bass | Minimal improvement | User: "still not very impressed" |
| Clarity | No noticeable change | - |
| Volume | Normal | - |
| Stereo | No change | - |

**Verdict:** FAIL - Insufficient improvement

---

### Test 2: Aggressive Preset
| Aspect | Result | Notes |
|--------|--------|-------|
| Bass | No change | - |
| Clarity | No change | - |
| Overall | Same as before | "still isn't that great" |

**Issue Found:** User asked "Do I need to reboot?"

**Investigation:**
```bash
pactl get-default-sink
# Output: alsa_output...sofhdadsp__sink
```

**Root Cause:** Audio was NOT going through EasyEffects at all!

**Verdict:** FAIL - Configuration error (audio bypass)

---

### Test 3: After Routing Fix
| Aspect | Result | Notes |
|--------|--------|-------|
| Audio Quality | Improved | User: "seems to be better" |
| Volume Buttons | BROKEN | Shows EasyEffects, doesn't change volume |
| Brightness Buttons | BROKEN | Also stopped working |

**Issue Found:**
- Volume buttons controlling EasyEffects sink (at 100%)
- Not controlling hardware speaker volume
- gsd-media-keys/gsd-power crashed again

**Verdict:** PARTIAL - Audio better, but volume control broken

---

### Test 4: After Volume Fix
| Aspect | Result | Notes |
|--------|--------|-------|
| Audio Quality | Good | "sounds a bit better" |
| Volume Buttons | Working | Controls hardware speaker |
| Brightness Buttons | Working | gsd-power restarted |
| vs Windows | Not quite | "isn't quite as good as Windows" |

**Verdict:** PASS (with caveats)

---

## Issues Discovered

### Issue 1: Audio Bypass
- **Symptom:** No audio improvement despite EasyEffects running
- **Cause:** Default sink was hardware, not EasyEffects
- **Detection:** `pactl get-default-sink` showed wrong sink
- **Fix:** `pactl set-default-sink easyeffects_sink`

### Issue 2: Volume Button Conflict
- **Symptom:** Volume buttons show EasyEffects but don't change volume
- **Cause:** GNOME controls default sink volume; EasyEffects sink is virtual at 100%
- **Detection:** `wpctl status` showed easyeffects_sink at vol: 1.00
- **Fix:** Set hardware as default sink while apps still route through EasyEffects

### Issue 3: gsd-* Daemon Crashes
- **Symptom:** Volume/brightness buttons stop working
- **Cause:** Daemons crash and systemd doesn't restart them
- **Detection:** `pgrep gsd-media-keys` returns nothing
- **Fix:** gsd-keepalive.timer (already configured from earlier)

### Issue 4: New Apps May Bypass EasyEffects
- **Symptom:** New applications might go directly to hardware
- **Cause:** Hardware is now default sink for volume control
- **Mitigation:** Existing apps stay routed to EasyEffects; user can manually route new apps
- **Better Fix:** Enable "Process all output streams" in EasyEffects settings

---

## Audio Quality Comparison

| Aspect | Linux (Before) | Linux (After) | Windows (Dolby) |
|--------|---------------|---------------|-----------------|
| Bass | Weak | Improved | Best |
| Stereo Width | Narrow | Wider | Widest |
| Clarity | Decent | Good | Excellent |
| Volume Normalization | None | Yes | Yes |
| Overall | Poor | Acceptable | Best |

**User Assessment:** "sounds a bit better" but "isn't quite as good as Windows"

---

## Recommendations for Further Improvement

1. **Try different presets:** User can switch between installed presets to find best match
2. **JamesDSP:** Lower latency alternative to EasyEffects with ViPER-DDC support
3. **AutoEQ:** Generate measurement-based EQ profile for this specific laptop
4. **Accept limitation:** Proprietary Dolby processing cannot be fully replicated
