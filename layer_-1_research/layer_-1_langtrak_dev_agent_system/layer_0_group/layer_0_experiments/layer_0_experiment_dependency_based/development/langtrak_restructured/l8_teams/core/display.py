"""Display and viewing routes for groups."""

from __future__ import annotations

import sqlite3
from typing import Any, Dict, List, Optional

from flask import flash, redirect, render_template, request, url_for

import main
from features.auth import get_user_info, require_auth
from features.projects import fetch_project_metadata
from services.firebase import clean_firebase_service, firestore_db

from . import groups_bp


def _build_group_list(cursor: sqlite3.Cursor, user_id: int) -> List[Dict[str, Any]]:
    """Return metadata for all groups the user belongs to."""

    cursor.execute(
        """
        SELECT g.id, g.name, g.description, g.created_at, g.admin_user_id,
               CASE WHEN g.admin_user_id = ? THEN 1 ELSE 0 END as is_admin
        FROM groups g
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE gm.user_id = ?
        ORDER BY g.created_at DESC
        """,
        (user_id, user_id),
    )

    groups: List[Dict[str, Any]] = []
    for group in cursor.fetchall():
        groups.append(
            {
                "id": group[0],
                "name": group[1],
                "description": group[2],
                "created_at": group[3],
                "admin_user_id": group[4],
                "is_admin": bool(group[5]),
            }
        )

    return groups


@groups_bp.route("/groups")
@require_auth
def groups_menu():
    """Groups management menu."""

    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        groups = _build_group_list(cursor, user["id"])
    finally:
        conn.close()

    return render_template("groups_menu.html", groups=groups, user=user)


def _fetch_group_detail(
    cursor: sqlite3.Cursor, group_id: int, user_id: int
) -> Optional[Dict[str, Any]]:
    cursor.execute(
        """
        SELECT g.id, g.name, g.description, g.admin_user_id,
               CASE WHEN g.admin_user_id = ? THEN 1 ELSE 0 END as is_admin
        FROM groups g
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE g.id = ? AND gm.user_id = ?
        """,
        (user_id, group_id, user_id),
    )

    row = cursor.fetchone()
    if not row:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "description": row[2],
        "admin_user_id": row[3],
        "is_admin": bool(row[4]),
    }


def _fetch_group_members(cursor: sqlite3.Cursor, group_id: int) -> List[Dict[str, Any]]:
    cursor.execute(
        """
        SELECT u.username, gm.joined_at
        FROM group_memberships gm
        JOIN users u ON gm.user_id = u.id
        WHERE gm.group_id = ?
        ORDER BY gm.joined_at
        """,
        (group_id,),
    )

    members: List[Dict[str, Any]] = []
    for member in cursor.fetchall():
        members.append({"user_id": member[0], "joined_at": member[1]})

    return members


def _fetch_group_projects(
    cursor: sqlite3.Cursor, group_id: int
) -> List[Dict[str, Any]]:
    cursor.execute(
        """
        SELECT
            ps.project_identifier,
            ps.project_id,
            ps.cloud_project_id,
            ps.storage_type,
            ps.shared_by,
            ps.shared_at,
            p.name,
            p.created_at,
            p.updated_at,
            owner.username as owner_name,
            sharer.username as sharer_name
        FROM project_shares ps
        LEFT JOIN projects p ON ps.project_id = p.id
        LEFT JOIN users owner ON p.user_id = owner.id
        LEFT JOIN users sharer ON ps.shared_by = sharer.id
        WHERE ps.group_id = ?
        ORDER BY ps.shared_at DESC
        """,
        (group_id,),
    )

    share_rows = cursor.fetchall()

    local_ids = [row[1] for row in share_rows if row[1] is not None]
    local_word_counts: Dict[int, int] = {}
    if local_ids:
        placeholders = ",".join("?" for _ in local_ids)
        cursor.execute(
            f"SELECT project_id, COUNT(*) FROM words WHERE project_id IN ({placeholders}) GROUP BY project_id",
            tuple(local_ids),
        )
        local_word_counts = {row[0]: row[1] for row in cursor.fetchall()}

    projects: List[Dict[str, Any]] = []
    metadata_cache: Dict[str, Optional[Dict[str, Any]]] = {}

    for row in share_rows:
        (
            project_identifier,
            local_project_id,
            cloud_project_id,
            storage_type,
            _shared_by,
            shared_at,
            local_name,
            local_created_at,
            _local_updated_at,
            owner_name,
            sharer_name,
        ) = row

        display_id = (
            cloud_project_id if storage_type == "cloud" and cloud_project_id else local_project_id
        )
        display_name = local_name or "Shared Project"
        creator_name = owner_name or sharer_name or "Unknown"
        word_count = 0

        if storage_type == "cloud" and cloud_project_id:
            if clean_firebase_service.is_available():
                if cloud_project_id not in metadata_cache:
                    metadata_cache[cloud_project_id] = fetch_project_metadata(
                        "cloud", cloud_project_id
                    )
                metadata = metadata_cache.get(cloud_project_id) or {}
                display_name = metadata.get("name", display_name)
                try:
                    word_count = firestore_db.count_project_words(cloud_project_id)
                except Exception as exc:  # pragma: no cover - diagnostic aid
                    print(
                        f"Error counting words for group shared cloud project {cloud_project_id}: {exc}"
                    )
            else:
                display_name = f"{display_name} (cloud)"
        elif local_project_id is not None:
            word_count = local_word_counts.get(local_project_id, 0)

        projects.append(
            {
                "id": display_id,
                "name": display_name,
                "created_at": local_created_at,
                "word_count": word_count,
                "creator": creator_name,
                "shared_at": shared_at,
                "project_identifier": project_identifier,
            }
        )

    return projects


def _fetch_active_invite(
    cursor: sqlite3.Cursor, group_id: int, host_url: str
) -> Optional[Dict[str, Any]]:
    cursor.execute(
        """
        SELECT invite_token, expires_at
        FROM group_invites
        WHERE group_id = ? AND expires_at > datetime('now')
        ORDER BY created_at DESC
        LIMIT 1
        """,
        (group_id,),
    )
    invite_data = cursor.fetchone()
    if not invite_data:
        return None

    return {
        "token": invite_data[0],
        "expires_at": invite_data[1],
        "url": f"{host_url}groups/join/{invite_data[0]}",
    }


@groups_bp.route("/groups/<int:group_id>")
@require_auth
def group_detail(group_id: int):
    """Group detail page."""

    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        group = _fetch_group_detail(cursor, group_id, user["id"])
        if not group:
            flash("Group not found or access denied", "error")
            return redirect(url_for("groups.groups_menu"))

        members = _fetch_group_members(cursor, group_id)
        projects = _fetch_group_projects(cursor, group_id)
        invite_link = None
        if group["is_admin"]:
            invite_link = _fetch_active_invite(cursor, group_id, request.host_url)

    finally:
        conn.close()

    return render_template(
        "group_detail.html",
        group=group,
        members=members,
        projects=projects,
        invite_link=invite_link,
        user=user,
    )
