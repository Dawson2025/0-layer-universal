---
resource_id: "84c30b66-41b8-4785-a25a-f205b11ae8b6"
resource_type: "output"
resource_name: "REQ_001_audio_testing"
---
# Testing: Laptop Speaker Audio Enhancement

<!-- section_id: "ae6aed8b-d03c-4aef-8e65-4341ac720acb" -->
## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

<!-- section_id: "e29fbb90-8cdc-4757-8713-ac9c0c876a3a" -->
## Date
2026-01-26

<!-- section_id: "e25d817f-670b-46b3-8862-5def889b01b6" -->
## Test Results

<!-- section_id: "83e9871c-d516-46a9-8642-5939ed163bbf" -->
### Test 1: Basic Preset
| Aspect | Result | Notes |
|--------|--------|-------|
| Bass | Minimal improvement | User: "still not very impressed" |
| Clarity | No noticeable change | - |
| Volume | Normal | - |
| Stereo | No change | - |

**Verdict:** FAIL - Insufficient improvement

---

<!-- section_id: "f47425ad-a02a-46c3-8d48-4c3dd45480a2" -->
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

<!-- section_id: "b27c15f7-1682-48cc-93fa-f2d5c370bd68" -->
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

<!-- section_id: "50e38008-9d88-49e7-a83e-ba93349efcef" -->
### Test 4: After Volume Fix
| Aspect | Result | Notes |
|--------|--------|-------|
| Audio Quality | Good | "sounds a bit better" |
| Volume Buttons | Working | Controls hardware speaker |
| Brightness Buttons | Working | gsd-power restarted |
| vs Windows | Not quite | "isn't quite as good as Windows" |

**Verdict:** PASS (with caveats)

---

<!-- section_id: "e34eed4d-0fa0-44a8-a9f6-e401747c6892" -->
## Issues Discovered

<!-- section_id: "e92f979e-29cb-415f-b8f8-fd817d9868b7" -->
### Issue 1: Audio Bypass
- **Symptom:** No audio improvement despite EasyEffects running
- **Cause:** Default sink was hardware, not EasyEffects
- **Detection:** `pactl get-default-sink` showed wrong sink
- **Fix:** `pactl set-default-sink easyeffects_sink`

<!-- section_id: "b7ae4976-ad2e-418d-839a-2e50cfa2d487" -->
### Issue 2: Volume Button Conflict
- **Symptom:** Volume buttons show EasyEffects but don't change volume
- **Cause:** GNOME controls default sink volume; EasyEffects sink is virtual at 100%
- **Detection:** `wpctl status` showed easyeffects_sink at vol: 1.00
- **Fix:** Set hardware as default sink while apps still route through EasyEffects

<!-- section_id: "1746cd07-8b63-46f7-83fb-7a11f57fa310" -->
### Issue 3: gsd-* Daemon Crashes
- **Symptom:** Volume/brightness buttons stop working
- **Cause:** Daemons crash and systemd doesn't restart them
- **Detection:** `pgrep gsd-media-keys` returns nothing
- **Fix:** gsd-keepalive.timer (already configured from earlier)

<!-- section_id: "3836f2dd-64ab-4947-ab1e-08701bb06c4a" -->
### Issue 4: New Apps May Bypass EasyEffects
- **Symptom:** New applications might go directly to hardware
- **Cause:** Hardware is now default sink for volume control
- **Mitigation:** Existing apps stay routed to EasyEffects; user can manually route new apps
- **Better Fix:** Enable "Process all output streams" in EasyEffects settings

---

<!-- section_id: "ef6b2bcf-ff5e-4d65-92cc-2ab28515877f" -->
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

<!-- section_id: "1f1d8d9b-13ac-43bf-be89-3cc5dc42553e" -->
## Recommendations for Further Improvement

1. **Try different presets:** User can switch between installed presets to find best match
2. **JamesDSP:** Lower latency alternative to EasyEffects with ViPER-DDC support
3. **AutoEQ:** Generate measurement-based EQ profile for this specific laptop
4. **Accept limitation:** Proprietary Dolby processing cannot be fully replicated
