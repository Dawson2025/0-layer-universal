#!/usr/bin/env bash
# resource_id: "b213e73d-ab93-4296-833c-75327f30ad11"
# resource_type: "script"
# resource_name: "start_production"
#
# Start Language Tracker production server with Gunicorn
#
# Usage:
#   bash scripts/prod/start_production.sh            # start production server
#   bash scripts/prod/start_production.sh --stop     # stop production server
#   bash scripts/prod/start_production.sh --status   # show production server status
#   bash scripts/prod/start_production.sh --restart  # restart production server

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PID_DIR="${ROOT_DIR}/tmp"
GUNICORN_PID_FILE="${PID_DIR}/gunicorn.pid"
PORT="${PORT:-5000}"
WORKERS="${WORKERS:-$(nproc)}"

mkdir -p "${PID_DIR}"

have() {
  command -v "$1" >/dev/null 2>&1
}

start_gunicorn() {
  if [[ -f "${GUNICORN_PID_FILE}" ]] && ps -p "$(cat "${GUNICORN_PID_FILE}")" >/dev/null 2>&1; then
    echo "[production] Gunicorn already running (PID $(cat "${GUNICORN_PID_FILE}"))."
    return
  fi

  if ! have gunicorn; then
    echo "[production] gunicorn not found. Installing..." >&2
    if [[ -d ".venv" ]]; then
      source ".venv/bin/activate"
      pip install gunicorn
    else
      echo "[production] No virtual environment found. Please install gunicorn manually." >&2
      exit 1
    fi
  fi

  echo "[production] Starting Language Tracker production server..."
  echo "[production] Port: ${PORT}"
  echo "[production] Workers: ${WORKERS}"
  echo "[production] Config: gunicorn.conf.py"
  
  # Ensure logs directory exists
  mkdir -p "${ROOT_DIR}/logs"
  
  (
    cd "${ROOT_DIR}"
    if [[ -d ".venv" ]]; then
      source ".venv/bin/activate"
    fi
    
    # Start Gunicorn with configuration file
    gunicorn --config gunicorn.conf.py app:app &
    echo $! > "${GUNICORN_PID_FILE}"
  )
  
  # Wait a moment for startup
  sleep 2
  
  if ps -p "$(cat "${GUNICORN_PID_FILE}")" >/dev/null 2>&1; then
    echo "[production] ✅ Gunicorn started successfully (PID $(cat "${GUNICORN_PID_FILE}"))."
    echo "[production] 🌐 Server available at: http://localhost:${PORT}"
    echo "[production] 📊 Logs: logs/gunicorn-access.log, logs/gunicorn-error.log"
  else
    echo "[production] ❌ Failed to start Gunicorn. Check logs/gunicorn-error.log"
    exit 1
  fi
}

stop_gunicorn() {
  if [[ -f "${GUNICORN_PID_FILE}" ]]; then
    local pid
    pid="$(cat "${GUNICORN_PID_FILE}")"
    if ps -p "${pid}" >/dev/null 2>&1; then
      echo "[production] Stopping Gunicorn (PID ${pid})..."
      kill -TERM "${pid}" >/dev/null 2>&1 || true
      
      # Wait for graceful shutdown
      local count=0
      while ps -p "${pid}" >/dev/null 2>&1 && [ $count -lt 30 ]; do
        sleep 1
        count=$((count + 1))
      done
      
      # Force kill if still running
      if ps -p "${pid}" >/dev/null 2>&1; then
        echo "[production] Force killing Gunicorn..."
        kill -KILL "${pid}" >/dev/null 2>&1 || true
      fi
      
      echo "[production] ✅ Gunicorn stopped."
    else
      echo "[production] Gunicorn not running."
    fi
    rm -f "${GUNICORN_PID_FILE}"
  else
    echo "[production] No PID file found. Gunicorn may not be running."
  fi
}

status_gunicorn() {
  if [[ -f "${GUNICORN_PID_FILE}" ]]; then
    local pid
    pid="$(cat "${GUNICORN_PID_FILE}")"
    if ps -p "${pid}" >/dev/null 2>&1; then
      echo "[production] ✅ Gunicorn running (PID ${pid})."
      echo "[production] 🌐 Server: http://localhost:${PORT}"
      
      # Check if port is listening
      if ss -tlnp | grep -q ":${PORT}"; then
        echo "[production] ✅ Port ${PORT} is listening."
      else
        echo "[production] ⚠️  Port ${PORT} not listening (may be starting up)."
      fi
      
      # Show worker count
      local workers
      workers=$(ps --no-headers -o pid --ppid "${pid}" | wc -l)
      echo "[production] 👷 Workers: ${workers}"
      
      return
    fi
  fi
  echo "[production] ❌ Gunicorn not running."
}

restart_gunicorn() {
  echo "[production] Restarting Gunicorn..."
  stop_gunicorn
  sleep 2
  start_gunicorn
}

ensure_logs_dir() {
  mkdir -p "${ROOT_DIR}/logs"
}

case "${1:-start}" in
  start)
    ensure_logs_dir
    start_gunicorn
    ;;
  stop)
    stop_gunicorn
    ;;
  restart)
    restart_gunicorn
    ;;
  status)
    status_gunicorn
    ;;
  *)
    echo "Usage: $(basename "$0") [start|stop|restart|status]" >&2
    echo ""
    echo "Environment variables:"
    echo "  PORT=${PORT}     - Server port (default: 5000)"
    echo "  WORKERS=${WORKERS} - Number of workers (default: $(nproc))"
    exit 2
    ;;
esac
