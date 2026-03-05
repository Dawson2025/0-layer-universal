#!/bin/bash
# resource_id: "4e13973b-1702-46d1-bf00-7cc951debbfd"
# resource_type: "script"
# resource_name: "test-system-tts"
# test-system-tts.sh — Automated tests for Phase 2 System TTS integration
# Tests Speech Dispatcher + Piper integration, scripts, and configuration

PASS=0
FAIL=0
TOTAL=0

test_result() {
    TOTAL=$((TOTAL + 1))
    if [ "$1" -eq 0 ]; then
        PASS=$((PASS + 1))
        echo "  PASS: $2"
    else
        FAIL=$((FAIL + 1))
        echo "  FAIL: $2 — $3"
    fi
}

echo "=== System TTS Phase 2 Tests ==="
echo ""

# --- Component Tests ---
echo "--- Component Availability ---"

piper --help >/dev/null 2>&1
test_result $? "Piper binary available" "piper not found in PATH"

[ -f "/home/dawson/.local/share/piper-voices/en_US-amy-medium.onnx" ]
test_result $? "Amy voice model present" "ONNX file missing"

which paplay >/dev/null 2>&1
test_result $? "paplay (PulseAudio) available" "paplay not found"

which spd-say >/dev/null 2>&1
test_result $? "spd-say available" "spd-say not found"

[ -f "/usr/lib/speech-dispatcher-modules/sd_generic" ]
test_result $? "sd_generic module binary present" "sd_generic not found"

# --- Configuration Tests ---
echo ""
echo "--- Configuration ---"

[ -f "/home/dawson/.config/speech-dispatcher/speechd.conf" ]
test_result $? "User-local speechd.conf exists" "Missing ~/.config/speech-dispatcher/speechd.conf"

[ -f "/home/dawson/.config/speech-dispatcher/modules/piper-generic.conf" ]
test_result $? "Piper module config exists" "Missing piper-generic.conf"

grep -q 'DefaultModule piper-generic' ~/.config/speech-dispatcher/speechd.conf 2>/dev/null
test_result $? "DefaultModule set to piper-generic" "DefaultModule not set correctly"

grep -q 'AddModule "piper-generic"' ~/.config/speech-dispatcher/speechd.conf 2>/dev/null
test_result $? "piper-generic AddModule registered" "AddModule line missing"

grep -q 'AddModule "espeak-ng"' ~/.config/speech-dispatcher/speechd.conf 2>/dev/null
test_result $? "espeak-ng AddModule registered (fallback)" "espeak-ng not registered"

# --- Module Loading Tests ---
echo ""
echo "--- Speech Dispatcher Module Loading ---"

MODULES=$(spd-say -O 2>&1)
echo "$MODULES" | grep -q "piper-generic"
test_result $? "piper-generic module loaded in speechd" "Module not loaded"

echo "$MODULES" | grep -q "espeak-ng"
test_result $? "espeak-ng module loaded in speechd" "Fallback module not loaded"

# --- Module Config Validation ---
echo ""
echo "--- Piper Module Config Validation ---"

LOGFILE="/run/user/$(id -u)/speech-dispatcher/log/piper-generic.log"
if [ -f "$LOGFILE" ]; then
    ERRORS=$(cat "$LOGFILE" | grep -c "Missing argument\|Error\|error")
    [ "$ERRORS" -eq 0 ]
    test_result $? "No errors in piper-generic.log" "$ERRORS error(s) found"
else
    test_result 0 "No piper-generic.log (clean start)"
fi

grep -q 'GenericExecuteSynth' ~/.config/speech-dispatcher/modules/piper-generic.conf 2>/dev/null
test_result $? "GenericExecuteSynth defined" "Missing synthesis command"

grep -q 'DefaultVoice' ~/.config/speech-dispatcher/modules/piper-generic.conf 2>/dev/null
test_result $? "DefaultVoice defined" "Missing default voice"

grep -q 'paplay' ~/.config/speech-dispatcher/modules/piper-generic.conf 2>/dev/null
test_result $? "Uses paplay (PulseAudio) for output" "Not using paplay"

# --- Audio Output Tests (silent — just checks exit codes) ---
echo ""
echo "--- Audio Pipeline Tests ---"

echo "test" | piper --model /home/dawson/.local/share/piper-voices/en_US-amy-medium.onnx --output-raw 2>/dev/null | head -c 1000 > /dev/null
test_result $? "Piper produces raw audio output" "Piper pipeline failed"

spd-say -w "test" 2>/dev/null
test_result $? "spd-say with Piper (default) succeeds" "spd-say default failed"

spd-say -w -o espeak-ng "test" 2>/dev/null
test_result $? "spd-say with espeak-ng fallback succeeds" "spd-say espeak-ng failed"

# --- Script Tests ---
echo ""
echo "--- Script Tests ---"

[ -x "/home/dawson/.local/bin/speak" ]
test_result $? "speak script is executable" "Not executable"

[ -x "/home/dawson/.local/bin/speak-selection" ]
test_result $? "speak-selection script is executable" "Not executable"

grep -q 'paplay' /home/dawson/.local/bin/speak 2>/dev/null
test_result $? "speak uses paplay" "Still using aplay"

grep -q 'paplay' /home/dawson/.local/bin/speak-selection 2>/dev/null
test_result $? "speak-selection uses paplay" "Still using aplay"

grep -q 'paplay' /home/dawson/.claude/hooks/tts-response.sh 2>/dev/null
test_result $? "tts-response.sh hook uses paplay" "Still using aplay"

# --- Orca Readiness ---
echo ""
echo "--- Orca Readiness ---"

which orca >/dev/null 2>&1
test_result $? "Orca binary available" "orca not found"

ORCA_VER=$(orca --version 2>&1)
echo "$ORCA_VER" | grep -qE "^[0-9]+\."
test_result $? "Orca version: $ORCA_VER" "Could not get Orca version"

# --- Keepalive Timer ---
echo ""
echo "--- GSD Keepalive ---"

systemctl --user is-active gsd-keepalive.timer >/dev/null 2>&1
test_result $? "gsd-keepalive.timer is active" "Timer not active"

pgrep -x gsd-media-keys >/dev/null 2>&1
test_result $? "gsd-media-keys is running" "Not running — keyboard shortcuts may fail"

pgrep -x gsd-power >/dev/null 2>&1
test_result $? "gsd-power is running" "Not running — brightness buttons may fail"

# --- Summary ---
echo ""
echo "=== Results: $PASS/$TOTAL passed, $FAIL failed ==="
[ "$FAIL" -eq 0 ] && echo "All tests passed!" || echo "Some tests failed — review above."
exit $FAIL
