"""
Projects Display Module

Handles viewing and listing projects.
Agents can work on display enhancements without affecting other sub-modules.
"""

from flask import render_template, redirect, url_for, flash
import sqlite3

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from services.firebase import clean_firebase_service
from src.storage_manager import storage_manager
from . import projects_bp


@projects_bp.route('/projects')
@require_auth
def projects_menu():
    """
    Projects management menu - lists all user's projects.

    Returns:
        Rendered template with projects list from both storage types
    """
    print("DEBUG: === PROJECTS ROUTE CALLED ===")
    user = get_user_info()
    print(f"DEBUG: User info: {user}")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Get user's projects from both storage types using storage manager
    print(f"DEBUG: Fetching projects for user {user['id']}")
    projects = storage_manager.get_projects(user['id'])
    print(f"DEBUG: Retrieved {len(projects)} projects: {[p.get('name', 'no name') for p in projects]}")

    firebase_available = clean_firebase_service.is_available()

    # Get user's groups for sharing functionality
    cursor.execute("""
        SELECT g.id, g.name
        FROM groups g
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE gm.user_id = ?
        ORDER BY g.name
    """, (user['id'],))

    user_groups = []
    for group in cursor.fetchall():
        user_groups.append({
            'id': group[0],
            'name': group[1]
        })

    conn.close()

    print(f"DEBUG: About to render template with {len(projects)} projects")
    print(f"DEBUG: First 3 projects: {projects[:3]}")
    print(f"DEBUG: Projects structure check:")
    for i, project in enumerate(projects[:3]):
        print(f"  Project {i}: {project}")

    return render_template('projects_menu.html',
                         projects=projects,
                         user=user,
                         user_groups=user_groups,
                         firebase_available=firebase_available,
                         focused_group=None,
                         parent_group=None)


@projects_bp.route('/projects/group/<group_id>')
@require_auth
def project_group_menu(group_id):
    """
    Focused view of a project group showing its variants and subprojects.

    Args:
        group_id: ID of the project group to display

    Returns:
        Rendered template with focused group view
    """
    user = get_user_info()
    group = storage_manager.get_group_detail(user['id'], group_id)
    if not group:
        flash('Project group not found or access denied', 'error')
        return redirect(url_for('projects.projects_menu'))

    firebase_available = clean_firebase_service.is_available()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT g.id, g.name
        FROM groups g
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE gm.user_id = ?
        ORDER BY g.name
    """, (user['id'],))

    user_groups = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
    conn.close()

    parent_group = None
    parent_id = group.get('parent_group_id')
    if parent_id:
        parent_group = storage_manager.get_group_detail(user['id'], parent_id)

    return render_template(
        'projects_menu.html',
        projects=[group],
        user=user,
        user_groups=user_groups,
        firebase_available=firebase_available,
        focused_group=group,
        parent_group=parent_group
    )


__all__ = ['projects_menu', 'project_group_menu']
