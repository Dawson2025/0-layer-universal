#!/usr/bin/env bash
#
# Reset the working SQLite database to a known-good snapshot.
# Copy data/phonemes.template.db -> data/phonemes.db
# (Create phonemes.template.db once from a clean state.)

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TEMPLATE_DB="${ROOT_DIR}/data/phonemes.template.db"
TARGET_DB="${ROOT_DIR}/data/phonemes.db"

if [[ ! -f "${TEMPLATE_DB}" ]]; then
  echo "reset_db.sh: missing template database ${TEMPLATE_DB}" >&2
  echo "Create it by copying a clean data/phonemes.db snapshot:" >&2
  echo "  cp data/phonemes.db data/phonemes.template.db" >&2
  exit 1
fi

cp "${TEMPLATE_DB}" "${TARGET_DB}"
echo "reset_db.sh: restored ${TARGET_DB} from ${TEMPLATE_DB}"
