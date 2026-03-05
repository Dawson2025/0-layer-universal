# resource_id: "1f3b38a5-5ae4-49ed-b4c5-f629c736b06d"
# resource_type: "document"
# resource_name: "metadata"
"""
Helpers for working with project identifiers and metadata.

This module centralizes logic that was previously embedded inside the main
Flask application so that feature work around projects can evolve in
parallel without touching unrelated application code.
"""

from __future__ import annotations

import sqlite3
from typing import Dict, Optional, Tuple

import main
from services.firebase import clean_firebase_service, firestore_db


def normalize_project_identifier(project_id: Optional[str]) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Convert incoming project identifiers into a canonical tuple of
    (storage_type, identifier, composite).
    """
    if project_id is None:
        return None, None, None

    raw = str(project_id).strip()
    if not raw:
        return None, None, None

    if ":" in raw:
        prefix, ident = raw.split(":", 1)
        prefix = prefix.lower()
        ident = ident.strip()
        if prefix in ("local", "cloud") and ident:
            if prefix == "local" and ident.isdigit():
                ident = str(int(ident))
            return prefix, ident, f"{prefix}:{ident}"

    if raw.isdigit():
        ident = str(int(raw))
        return "local", ident, f"local:{ident}"

    return "cloud", raw, f"cloud:{raw}"


def fetch_project_metadata(
    storage_type: Optional[str],
    identifier: Optional[str],
    owner_id: Optional[str] = None,
) -> Optional[Dict[str, Optional[str]]]:
    """
    Retrieve project metadata for either local or cloud storage.

    Args:
        storage_type: Expected storage type string ("local" or "cloud").
        identifier: Project identifier for the given storage type.
        owner_id: Optional user identifier to enforce ownership.

    Returns:
        A dictionary containing project metadata or None if not found/authorized.
    """
    owner_str = str(owner_id) if owner_id is not None else None

    if storage_type == "local":
        try:
            int_id = int(identifier) if identifier is not None else None
        except (TypeError, ValueError):
            return None

        if int_id is None:
            return None

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, name, user_id, cloud_project_id, updated_at
            FROM projects
            WHERE id = ?
            """,
            (int_id,),
        )
        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        if owner_str is not None and str(row[2]) != owner_str:
            return None

        return {
            "storage_type": "local",
            "project_id": str(row[0]),
            "cloud_project_id": row[3],
            "name": row[1],
            "owner_user_id": row[2],
            "updated_at": row[4],
        }

    if storage_type == "cloud":
        if not clean_firebase_service.is_available():
            return None

        try:
            project_doc = firestore_db.get_project(identifier)
        except Exception as exc:  # pragma: no cover - diagnostics
            print(f"Error fetching cloud project {identifier}: {exc}")
            return None

        if not project_doc:
            return None

        doc_owner = project_doc.get("user_id")
        if doc_owner is None and project_doc.get("user_id_str"):
            doc_owner = project_doc.get("user_id_str")

        if doc_owner is not None and isinstance(doc_owner, (int, float)):
            doc_owner = str(int(doc_owner))
        elif doc_owner is not None:
            doc_owner = str(doc_owner)

        if owner_str is not None and doc_owner is not None and doc_owner != owner_str:
            return None

        return {
            "storage_type": "cloud",
            "project_id": None,
            "cloud_project_id": identifier,
            "name": project_doc.get("name", "Cloud Project"),
            "owner_user_id": doc_owner,
            "updated_at": project_doc.get("updated_at"),
        }

    return None


__all__ = ("normalize_project_identifier", "fetch_project_metadata")
