# resource_id: "e4e2d1ef-4add-4d41-abef-f8c4c1d0a614"
# resource_type: "document"
# resource_name: "database"
"""Utility helpers for resetting the local SQLite database."""
from __future__ import annotations

import os
import sqlite3
from contextlib import closing
from dataclasses import dataclass
from typing import Callable, Dict, Optional


@dataclass
class ResetResult:
    """Summary information returned after a reset operation."""

    templates_preserved: int
    words_deleted: int
    phonemes_deleted: int

    def to_message(self) -> str:
        template_msg = (
            f" Preserved {self.templates_preserved} phoneme templates."
            if self.templates_preserved
            else ""
        )
        return (
            "Database reset successfully! All words deleted and phonemes reset to default."
            + template_msg
        )


def _ensure_templates_table(cursor: sqlite3.Cursor) -> None:
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


def get_database_snapshot(db_path: str) -> Dict[str, int]:
    """Return basic counts for the SQLite database."""

    if not os.path.exists(db_path):
        return {"phonemes": 0, "words": 0}

    try:
        with closing(sqlite3.connect(db_path)) as conn:
            cursor = conn.cursor()
            counts = {}
            for table in ("phonemes", "words"):
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    counts[table] = cursor.fetchone()[0] or 0
                except sqlite3.Error:
                    counts[table] = 0
            return counts
    except sqlite3.Error:
        return {"phonemes": 0, "words": 0}


def reset_database(
    db_path: str,
    *,
    insert_sample_data: Optional[Callable[[], None]] = None,
) -> ResetResult:
    """Reset phoneme and word data while keeping templates intact."""

    try:
        with closing(sqlite3.connect(db_path)) as conn:
            cursor = conn.cursor()
            _ensure_templates_table(cursor)

            cursor.execute(
                "SELECT name, description, template_data, phoneme_count, created_at FROM phoneme_templates"
            )
            templates_backup = cursor.fetchall()

            cursor.execute("DELETE FROM words")
            words_deleted = max(cursor.rowcount or 0, 0)
            cursor.execute("DELETE FROM phonemes")
            phonemes_deleted = max(cursor.rowcount or 0, 0)

            cursor.execute("DELETE FROM sqlite_sequence WHERE name='words'")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='phonemes'")
            conn.commit()

        if insert_sample_data:
            insert_sample_data()

        return ResetResult(
            templates_preserved=len(templates_backup),
            words_deleted=words_deleted,
            phonemes_deleted=phonemes_deleted,
        )
    except Exception as exc:
        raise RuntimeError(f"Error resetting database: {exc}") from exc
