#!/usr/bin/env bash
#
# Bring up local services (Flask app + Playwright MCP server) in the background.
#
# Usage:
#   bash scripts/dev/start_services.sh            # start Flask + MCP
#   bash scripts/dev/start_services.sh --stop     # stop background services
#   bash scripts/dev/start_services.sh --status   # show running status

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PID_DIR="${ROOT_DIR}/tmp"
FLASK_PID_FILE="${PID_DIR}/flask.pid"
MCP_PID_FILE="${PID_DIR}/mcp.pid"
PORT="${PORT:-5000}"
MCP_PORT="${MCP_PORT:-3334}"

mkdir -p "${PID_DIR}"

have() {
  command -v "$1" >/dev/null 2>&1
}

start_flask() {
  if [[ -f "${FLASK_PID_FILE}" ]] && ps -p "$(cat "${FLASK_PID_FILE}")" >/dev/null 2>&1; then
    echo "[start-services] Flask already running (PID $(cat "${FLASK_PID_FILE}"))."
    return
  fi

  if ! have python3; then
    echo "[start-services] python3 not found in PATH." >&2
    exit 1
  fi

  echo "[start-services] Launching Flask on port ${PORT}..."
  (
    cd "${ROOT_DIR}"
    if [[ -d ".venv" ]]; then
      # shellcheck disable=SC1091
      source ".venv/bin/activate"
    fi
    PORT="${PORT}" python3 app.py >"${ROOT_DIR}/logs/flask.log" 2>&1 &
    echo $! > "${FLASK_PID_FILE}"
  )
  echo "[start-services] Flask PID $(cat "${FLASK_PID_FILE}"). Logs: logs/flask.log"
}

start_mcp() {
  if [[ -f "${MCP_PID_FILE}" ]] && ps -p "$(cat "${MCP_PID_FILE}")" >/dev/null 2>&1; then
    echo "[start-services] Playwright MCP already running (PID $(cat "${MCP_PID_FILE}"))."
    return
  fi

  if ! have npx; then
    echo "[start-services] npx not found. Install Node.js or npm." >&2
    exit 1
  fi

  echo "[start-services] Launching Playwright MCP on port ${MCP_PORT}..."
  (
    cd "${ROOT_DIR}"
    npx -y @playwright/mcp@latest --browser chromium --port "${MCP_PORT}" --isolated >"${ROOT_DIR}/logs/mcp.log" 2>&1 &
    echo $! > "${MCP_PID_FILE}"
  )
  echo "[start-services] MCP PID $(cat "${MCP_PID_FILE}"). Logs: logs/mcp.log"
}

stop_process() {
  local file="$1"
  local name="$2"
  if [[ -f "${file}" ]]; then
    local pid
    pid="$(cat "${file}")"
    if ps -p "${pid}" >/dev/null 2>&1; then
      echo "[start-services] Stopping ${name} (PID ${pid})..."
      kill "${pid}" >/dev/null 2>&1 || true
    fi
    rm -f "${file}"
  fi
}

status_process() {
  local file="$1"
  local name="$2"
  if [[ -f "${file}" ]]; then
    local pid
    pid="$(cat "${file}")"
    if ps -p "${pid}" >/dev/null 2>&1; then
      echo "[start-services] ${name} running (PID ${pid})."
      return
    fi
  fi
  echo "[start-services] ${name} not running."
}

ensure_logs_dir() {
  mkdir -p "${ROOT_DIR}/logs"
}

case "${1:-start}" in
  start)
    ensure_logs_dir
    start_flask
    start_mcp
    ;;
  stop)
    stop_process "${FLASK_PID_FILE}" "Flask"
    stop_process "${MCP_PID_FILE}" "Playwright MCP"
    ;;
  status)
    status_process "${FLASK_PID_FILE}" "Flask"
    status_process "${MCP_PID_FILE}" "Playwright MCP"
    ;;
  *)
    echo "Usage: $(basename "$0") [start|stop|status]" >&2
    exit 2
    ;;
esac
