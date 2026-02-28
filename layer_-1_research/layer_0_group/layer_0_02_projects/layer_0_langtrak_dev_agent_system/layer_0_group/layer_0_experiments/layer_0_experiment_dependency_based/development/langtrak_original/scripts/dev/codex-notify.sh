#!/usr/bin/env bash

# Wraps a command (e.g. the Codex CLI) and triggers Windows/WSL notifications,
# speech, and/or sounds whenever the command exits. Intended to run inside WSL.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
START_SERVICES_SCRIPT="${PROJECT_ROOT}/scripts/dev/start_services.sh"

if [ "${CODEX_AUTO_START_SERVICES:-1}" != "0" ] && [ -x "${START_SERVICES_SCRIPT}" ]; then
  "${START_SERVICES_SCRIPT}" start >/dev/null 2>&1 || true
fi

have() {
  command -v "$1" >/dev/null 2>&1
}

notify() {
  local title="$1"
  local body="$2"

  local notifier="${CODEX_NOTIFY_SENDER:-}"
  if [ -z "$notifier" ]; then
    if have wsl-notify-send.exe; then
      notifier="wsl-notify-send.exe"
    elif have wsl-notify-send; then
      notifier="wsl-notify-send"
    fi
  fi

  if [ -n "$notifier" ]; then
    local message="$body"
    if [ -z "$message" ]; then
      message="$title"
    fi
    "$notifier" --category "$title" "$message" &
  fi
}

say_text() {
  local text="$1"
  local speaker="${CODEX_NOTIFY_SPEAKER:-spd-say}"

  if [ -n "$text" ] && have "$speaker"; then
    "$speaker" "$text" &
  fi
}

play_sound() {
  local file="$1"
  local player="${CODEX_NOTIFY_PLAYER:-ffplay}"

  if [ -n "$file" ] && [ -f "$file" ] && have "$player"; then
    "$player" -autoexit -nodisp "$file" >/dev/null 2>&1 &
  fi
}

run_custom() {
  local cmd="$1"
  if [ -n "$cmd" ]; then
    bash -lc "$cmd" &
  fi
}

bell() {
  if [ "${CODEX_NOTIFY_BELL:-1}" != "0" ]; then
    printf '\a'
  fi
}

usage() {
  cat <<EOF
Usage: $(basename "$0") <command> [args...]

Wrap the given command and emit desktop notifications, speech, and sounds
when it exits. Configure behavior with these environment variables:

  CODEX_NOTIFY_SENDER   Override notify executable (default: auto-detected wsl-notify-send)
  CODEX_NOTIFY_SPEAKER  Override speech command (default: spd-say)
  CODEX_NOTIFY_PLAYER   Override sound player (default: ffplay)
  CODEX_NOTIFY_SUCCESS_SOUND  Path to a sound file for successful exit
  CODEX_NOTIFY_FAILURE_SOUND  Path to a sound file for failure exit
  CODEX_NOTIFY_COMMAND_SUCCESS Command to run on success (runs via bash -lc)
  CODEX_NOTIFY_COMMAND_FAILURE Command to run on failure (runs via bash -lc)
  CODEX_NOTIFY_SUCCESS_TEXT   Spoken text for success (default: "Codex finished task")
  CODEX_NOTIFY_FAILURE_TEXT   Spoken text for failure (default: "Codex needs attention")
  CODEX_NOTIFY_TITLE_SUCCESS  Notification title for success (default: "Codex finished")
  CODEX_NOTIFY_TITLE_FAILURE  Notification title for failure (default: "Codex stopped")
  CODEX_NOTIFY_BODY_SUCCESS   Notification body for success (default: elapsed time)
  CODEX_NOTIFY_BODY_FAILURE   Notification body for failure (default: exit code + elapsed time)
  CODEX_NOTIFY_BELL           Set to 0 to disable terminal bell (default: enabled)
EOF
}

if [ "$#" -eq 0 ]; then
  usage
  exit 2
fi

start_ts=$(date +%s)

set +e
"$@"
status=$?
set -e

end_ts=$(date +%s)
elapsed=$((end_ts - start_ts))

format_elapsed() {
  local seconds="$1"
  local mins=$((seconds / 60))
  local secs=$((seconds % 60))
  if [ "$mins" -gt 0 ]; then
    printf "%dm %ds" "$mins" "$secs"
  else
    printf "%ds" "$secs"
  fi
}

elapsed_text=$(format_elapsed "$elapsed")

if [ "$status" -eq 0 ]; then
  bell
  notify "${CODEX_NOTIFY_TITLE_SUCCESS:-Codex finished}" \
         "${CODEX_NOTIFY_BODY_SUCCESS:-Completed in $elapsed_text}"
  say_text "${CODEX_NOTIFY_SUCCESS_TEXT:-Codex finished task.}"
  play_sound "${CODEX_NOTIFY_SUCCESS_SOUND:-}"
  run_custom "${CODEX_NOTIFY_COMMAND_SUCCESS:-}"
else
  bell
  notify "${CODEX_NOTIFY_TITLE_FAILURE:-Codex stopped}" \
         "${CODEX_NOTIFY_BODY_FAILURE:-Exit $status after $elapsed_text}"
  say_text "${CODEX_NOTIFY_FAILURE_TEXT:-Codex needs attention.}"
  play_sound "${CODEX_NOTIFY_FAILURE_SOUND:-}"
  run_custom "${CODEX_NOTIFY_COMMAND_FAILURE:-}"
fi

exit "$status"
