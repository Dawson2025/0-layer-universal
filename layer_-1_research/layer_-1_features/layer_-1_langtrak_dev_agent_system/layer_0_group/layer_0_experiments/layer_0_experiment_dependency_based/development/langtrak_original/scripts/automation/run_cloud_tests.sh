#!/usr/bin/env bash
#
# Run Firebase cloud integration tests in offline and optional online modes.
# Usage:
#   bash scripts/automation/run_cloud_tests.sh [--online]
#     --online  Run a second pass with RUN_FIREBASE_INTEGRATION_TESTS=1

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ARTIFACT_ROOT="${ROOT_DIR}/artifacts/cloud_tests"
TIMESTAMP="$(date -u +"%Y%m%dT%H%M%SZ")"
RUN_DIR="${ARTIFACT_ROOT}/${TIMESTAMP}"
mkdir -p "${RUN_DIR}"

RUN_ONLINE=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --online)
      RUN_ONLINE=true
      shift
      ;;
    --help|-h)
      echo "Usage: bash $(basename "$0") [--online]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

PYTHON_BIN="python3"
if [[ -x "${ROOT_DIR}/.venv/bin/python" ]]; then
  PYTHON_BIN="${ROOT_DIR}/.venv/bin/python"
fi

TEST_MODULE="tests.integration.test_cloud_integration"

declare -a RUN_RESULTS=()

run_case() {
  local mode="$1"
  local online_flag="$2"
  local logfile="${RUN_DIR}/${mode}.log"
  local started_at ended_at exit_code outcome

  started_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

  if [[ "${online_flag}" == "online" ]]; then
    echo "[cloud-tests] Running online mode (${mode})..."
    if RUN_FIREBASE_INTEGRATION_TESTS=1 "${PYTHON_BIN}" -m unittest "${TEST_MODULE}" >"${logfile}" 2>&1; then
      exit_code=0
    else
      exit_code=$?
    fi
  else
    echo "[cloud-tests] Running offline mode (${mode})..."
    if RUN_FIREBASE_INTEGRATION_TESTS=0 "${PYTHON_BIN}" -m unittest "${TEST_MODULE}" >"${logfile}" 2>&1; then
      exit_code=0
    else
      exit_code=$?
    fi
  fi

  ended_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

  if grep -qi "skipped" "${logfile}"; then
    outcome="skipped"
  elif [[ "${exit_code}" -eq 0 ]]; then
    outcome="passed"
  else
    outcome="failed"
  fi

  local rel_log="${logfile#${ROOT_DIR}/}"
  RUN_RESULTS+=("${mode}|${online_flag}|${exit_code}|${outcome}|${rel_log}|${started_at}|${ended_at}")

  echo "[cloud-tests] ${mode} completed with status '${outcome}' (exit ${exit_code}). Log: ${rel_log}"
}

run_case "offline" "offline"

if "${RUN_ONLINE}"; then
  run_case "online" "online"
fi

SUMMARY_FILE="${RUN_DIR}/summary.json"
RUN_DATA_FILE="${RUN_DIR}/runs.txt"
printf '%s\n' "${RUN_RESULTS[@]}" > "${RUN_DATA_FILE}"

"${PYTHON_BIN}" - "$SUMMARY_FILE" "$RUN_DATA_FILE" <<'PY'
import json
import os
import sys

runs_file = sys.argv[2]
with open(runs_file, "r", encoding="utf-8") as handle:
    lines = [line.strip() for line in handle if line.strip()]
entries = []
for line in lines:
    mode, flag, exit_code, outcome, log_file, started_at, ended_at = line.split("|", 6)
    entries.append(
        {
            "mode": mode,
            "run_type": flag,
            "exit_code": int(exit_code),
            "outcome": outcome,
            "log_file": log_file,
            "started_at": started_at,
            "ended_at": ended_at,
        }
    )

summary = {
    "timestamp": os.path.basename(os.path.dirname(sys.argv[1])),
    "artifacts": os.path.dirname(sys.argv[1]),
    "runs": entries,
}

with open(sys.argv[1], "w", encoding="utf-8") as fp:
    json.dump(summary, fp, indent=2)
PY

echo "[cloud-tests] Summary written to ${SUMMARY_FILE#${ROOT_DIR}/}"
