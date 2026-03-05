# resource_id: "000f4f22-1b79-496e-8d6a-267319be3327"
# resource_type: "document"
# resource_name: "creation"
"""Group creation functionality."""

from __future__ import annotations

import secrets
import sqlite3

from flask import flash, redirect, render_template, request, url_for

import main
from features.auth import get_user_info, require_auth

from . import groups_bp


def _create_initial_invite(
    cursor: sqlite3.Cursor, group_id: int, created_by: int
) -> None:
    """Create the default invite token for a newly created group."""

    invite_token = secrets.token_urlsafe(32)
    cursor.execute(
        """
        INSERT INTO group_invites (group_id, invite_token, created_by, expires_at)
        VALUES (?, ?, ?, datetime('now', '+30 days'))
        """,
        (group_id, invite_token, created_by),
    )


@groups_bp.route("/groups/create", methods=["GET", "POST"])
@require_auth
def create_group():
    """Create a new group."""

    user = get_user_info()

    if request.method == "POST":
        group_name = request.form.get("name", "").strip()
        group_description = request.form.get("description", "").strip()

        if not group_name:
            flash("Group name is required", "error")
            return render_template("create_group.html", user=user)

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO groups (name, description, admin_user_id)
                VALUES (?, ?, ?)
                """,
                (group_name, group_description, user["id"]),
            )

            group_id = cursor.lastrowid

            cursor.execute(
                """
                INSERT INTO group_memberships (group_id, user_id)
                VALUES (?, ?)
                """,
                (group_id, user["id"]),
            )

            _create_initial_invite(cursor, group_id, user["id"])

            conn.commit()
            flash(f'Group "{group_name}" created successfully!', "success")
            return redirect(url_for("groups.groups_menu"))

        except Exception as exc:  # pragma: no cover - defensive logging aid
            flash(f"Error creating group: {exc}", "error")
        finally:
            conn.close()

    return render_template("create_group.html", user=user)
