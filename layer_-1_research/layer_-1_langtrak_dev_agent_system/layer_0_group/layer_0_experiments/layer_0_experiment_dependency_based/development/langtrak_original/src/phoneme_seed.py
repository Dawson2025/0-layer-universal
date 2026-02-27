"""
Project phoneme seeding utilities.

Seeds a new project with a fixed, code-defined default phoneme template
(English baseline). Edits in any project do NOT affect this default;
we always copy-from-default on project creation.
"""
from __future__ import annotations

from datetime import datetime
from typing import Iterable, Dict, Any
import sqlite3

from scripts.legacy.flattened_dataset import flattened_dataset
from services.firebase import clean_firebase_service, firestore_db
import main

# Fallback immutable in-code default; only used if no saved template is found
DEFAULT_FALLBACK: Iterable[Dict[str, Any]] = flattened_dataset


def _load_default_template_phonemes() -> Iterable[Dict[str, Any]]:
    """Load the canonical default template, preferring cloud first.

    Preference order:
    1) Firestore: newest template whose name is 'audit' (case-insensitive)
    2) Firestore: newest template overall
    3) SQLite: same order as above
    4) Fallback to DEFAULT_FALLBACK
    """
    import sqlite3
    import json

    # --- Try Firestore first ---
    if clean_firebase_service.is_available():
        try:
            docs = firestore_db._service.get_documents(  # type: ignore[attr-defined]
                firestore_db.PHONEME_TEMPLATES_COLLECTION
            ) or []
            if docs:
                # Prefer name == 'audit' (case-insensitive)
                def _key(doc):
                    ts = doc.get('created_at')
                    return ts.timestamp() if hasattr(ts, 'timestamp') else 0
                audit_docs = [d for d in docs if str(d.get('name','')).lower() == 'audit']
                chosen = None
                if audit_docs:
                    chosen = max(audit_docs, key=_key)
                else:
                    chosen = max(docs, key=_key)
                tdata = chosen.get('template_data')
                if isinstance(tdata, str) and tdata.strip():
                    data = json.loads(tdata)
                    ph = data.get('phonemes')
                    if isinstance(ph, dict):
                        out = []
                        for symbol, meta in ph.items():
                            m = dict(meta or {})
                            m['phoneme'] = symbol
                            out.append(m)
                        return out
                    if isinstance(ph, list):
                        return ph
        except Exception:
            pass

    # --- Fallback to SQLite ---
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        # Ensure table exists
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS phoneme_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                template_data TEXT NOT NULL,
                phoneme_count INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        # Try to find preferred template by name
        cursor.execute(
            """
            SELECT template_data FROM phoneme_templates
            WHERE LOWER(name) IN ('audit','default','english default')
            ORDER BY datetime(created_at) DESC, id DESC
            LIMIT 1
            """
        )
        row = cursor.fetchone()
        if not row:
            cursor.execute(
                """
                SELECT template_data FROM phoneme_templates
                ORDER BY datetime(created_at) DESC, id DESC
                LIMIT 1
                """
            )
            row = cursor.fetchone()
        conn.close()
        if row and row[0]:
            data = json.loads(row[0])
            ph = data.get('phonemes')
            if isinstance(ph, dict):
                # Old format mapping: {symbol: {fields...}}
                out = []
                for symbol, meta in ph.items():
                    m = dict(meta or {})
                    m['phoneme'] = symbol
                    out.append(m)
                return out
            if isinstance(ph, list):
                return ph
    except Exception:
        pass
    return DEFAULT_FALLBACK


def seed_project_phonemes(project_id: str, user_id: int | None, storage_type: str) -> None:
    """
    Seed the given project with the default phoneme template.

    Args:
        project_id: String identifier. For local, pass the integer id as str.
        user_id: Optional owner user id for attribution.
        storage_type: 'local' or 'cloud'
    """
    created_at = datetime.utcnow()

    # Resolve the canonical template once
    template_rows = list(_load_default_template_phonemes())

    if storage_type == "cloud" and clean_firebase_service.is_available():
        for p in template_rows:
            firestore_db.create_phoneme({
                "phoneme": p.get("phoneme"),
                "language": "en",
                "frequency": int(p.get("frequency", 0) or 0),
                "syllable_type": p.get("syllable_type"),
                "position": p.get("position"),
                "length_type": p.get("length_type"),
                "group_type": p.get("group_type"),
                "subgroup_type": p.get("subgroup_type"),
                "sub_subgroup_type": p.get("sub_subgroup_type"),
                "sub_sub_subgroup_type": p.get("sub_sub_subgroup_type"),
                "user_id": user_id,
                "project_id": project_id,
                "created_at": created_at,
                "updated_at": created_at,
            })
        return

    # Local SQLite
    conn = sqlite3.connect(main.DB_NAME)
    try:
        cursor = conn.cursor()
        for p in template_rows:
            cursor.execute(
                """
                INSERT OR IGNORE INTO phonemes (
                    project_id, user_id,
                    syllable_type, position, length_type,
                    group_type, subgroup_type, sub_subgroup_type, sub_sub_subgroup_type,
                    phoneme, frequency
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    int(project_id) if project_id is not None and project_id.isdigit() else project_id,
                    user_id,
                    p.get("syllable_type"),
                    p.get("position"),
                    p.get("length_type"),
                    p.get("group_type"),
                    p.get("subgroup_type"),
                    p.get("sub_subgroup_type"),
                    p.get("sub_sub_subgroup_type"),
                    p.get("phoneme"),
                    int(p.get("frequency", 0) or 0),
                ),
            )
        conn.commit()
    finally:
        conn.close()