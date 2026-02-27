"""L8 Teams - All team/group routes consolidated into a single blueprint.

Covers:
- Group listing, creation, detail pages (HTML)
- Group invite join flow (HTML)
- API: regenerate invite, create group project
- API: share/unshare projects with groups
- API: Firestore-backed group CRUD, membership, project sharing
"""

from __future__ import annotations

import secrets
import sqlite3
from datetime import datetime
from typing import Any, Dict, List, Optional

from flask import (
    Blueprint,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

import main
from l2_infrastructure.auth import require_auth, require_project_admin
from l3_users.sessions.session import get_user_info
from l2_infrastructure.firebase import clean_firebase_service, firestore_db
from l2_infrastructure.storage import storage_manager, StorageType

l8_bp = Blueprint(
    'l8_teams',
    __name__,
    template_folder='core/templates',
    static_folder='core/static',
    static_url_path='/static/l8_teams',
)


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def _user_is_group_admin(cursor: sqlite3.Cursor, group_id: int, user_id: int) -> bool:
    cursor.execute(
        "SELECT user_id FROM project_groups WHERE id = ?",
        (group_id,),
    )
    group_data = cursor.fetchone()
    return bool(group_data and group_data[0] == user_id)


def _user_is_group_member(cursor: sqlite3.Cursor, group_id: int, user_id: int) -> bool:
    cursor.execute(
        """
        SELECT id FROM group_memberships
        WHERE group_id = ? AND user_id = ?
        """,
        (group_id, user_id),
    )
    return cursor.fetchone() is not None


def _build_group_list(cursor: sqlite3.Cursor, user_id: int) -> List[Dict[str, Any]]:
    """Return metadata for all groups the user belongs to."""
    cursor.execute(
        """
        SELECT g.id, g.name, g.description, g.created_at, g.user_id,
               CASE WHEN g.user_id = ? THEN 1 ELSE 0 END as is_admin
        FROM project_groups g
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE gm.user_id = ?
        ORDER BY g.created_at DESC
        """,
        (user_id, user_id),
    )

    groups: List[Dict[str, Any]] = []
    for group in cursor.fetchall():
        groups.append({
            'id': group[0],
            'name': group[1],
            'description': group[2],
            'created_at': group[3],
            'admin_user_id': group[4],
            'is_admin': bool(group[5]),
        })
    return groups


def _fetch_group_detail(
    cursor: sqlite3.Cursor, group_id: int, user_id: int
) -> Optional[Dict[str, Any]]:
    cursor.execute(
        """
        SELECT g.name, g.description, g.created_at, g.user_id
        FROM project_groups g
        WHERE g.id = ?
        """,
        (group_id,),
    )
    row = cursor.fetchone()
    if not row:
        return None
    return {
        'id': group_id,
        'name': row[0],
        'description': row[1],
        'created_at': row[2],
        'admin_user_id': row[3],
        'is_admin': row[3] == user_id,
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
        members.append({'user_id': member[0], 'joined_at': member[1]})
    return members


def _fetch_group_projects(cursor: sqlite3.Cursor, group_id: int) -> List[Dict[str, Any]]:
    cursor.execute(
        """
        SELECT p.id, p.name, p.created_at, COUNT(w.id) as word_count,
               u.username as creator, ps.shared_at
        FROM projects p
        LEFT JOIN words w ON p.id = w.project_id
        JOIN users u ON p.user_id = u.id
        JOIN project_shares ps ON p.id = ps.project_id
        WHERE ps.group_id = ?
        GROUP BY p.id, p.name, p.created_at, u.username, ps.shared_at
        ORDER BY ps.shared_at DESC
        """,
        (group_id,),
    )
    projects: List[Dict[str, Any]] = []
    for project in cursor.fetchall():
        projects.append({
            'id': project[0],
            'name': project[1],
            'created_at': project[2],
            'word_count': project[3],
            'creator': project[4],
            'shared_at': project[5],
        })
    return projects


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


# ---------------------------------------------------------------------------
# HTML routes — Group listing
# ---------------------------------------------------------------------------

@l8_bp.route('/groups')
@require_auth
def groups_menu():
    """Groups management menu"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        groups = _build_group_list(cursor, user['id'])
    finally:
        conn.close()

    return render_template('groups_menu.html', groups=groups, user=user)


# ---------------------------------------------------------------------------
# HTML routes — Group creation
# ---------------------------------------------------------------------------

@l8_bp.route('/groups/create', methods=['GET', 'POST'])
@require_auth
def create_group():
    """Create a new group"""
    user = get_user_info()

    if request.method == 'POST':
        group_name = request.form.get('name', '').strip()
        group_description = request.form.get('description', '').strip()

        if not group_name:
            flash('Group name is required', 'error')
            return render_template('create_group.html', user=user)

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO groups (name, description, admin_user_id)
                VALUES (?, ?, ?)
            """, (group_name, group_description, user['id']))

            group_id = cursor.lastrowid

            cursor.execute("""
                INSERT INTO group_memberships (group_id, user_id)
                VALUES (?, ?)
            """, (group_id, user['id']))

            _create_initial_invite(cursor, group_id, user['id'])

            conn.commit()
            flash(f'Group "{group_name}" created successfully!', 'success')
            return redirect(url_for('l8_teams.groups_menu'))

        except Exception as e:
            flash(f'Error creating group: {str(e)}', 'error')
        finally:
            conn.close()

    return render_template('create_group.html', user=user)


# ---------------------------------------------------------------------------
# HTML routes — Group detail
# ---------------------------------------------------------------------------

@l8_bp.route('/groups/<int:group_id>')
@require_auth
def group_detail(group_id):
    """Group detail page"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        group = _fetch_group_detail(cursor, group_id, user['id'])
        if not group:
            flash('Group not found or access denied', 'error')
            return redirect(url_for('l8_teams.groups_menu'))

        members = _fetch_group_members(cursor, group_id)
        projects = _fetch_group_projects(cursor, group_id)

        invite_link = None
        if group['is_admin']:
            cursor.execute("SELECT invite_code FROM project_groups WHERE id = ?", (group_id,))
            invite_data = cursor.fetchone()
            if invite_data:
                invite_link = {
                    'token': invite_data[0],
                    'expires_at': invite_data[1] if len(invite_data) > 1 else None,
                    'url': f"{request.host_url}groups/join/{invite_data[0]}"
                }
    finally:
        conn.close()

    return render_template(
        'group_detail.html',
        group=group,
        members=members,
        projects=projects,
        invite_link=invite_link,
        user=user,
    )


# ---------------------------------------------------------------------------
# HTML routes — Join group via invite
# ---------------------------------------------------------------------------

@l8_bp.route('/groups/join/<invite_token>')
def join_group_via_invite(invite_token):
    """Join group via invite link"""
    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, name, invite_code FROM project_groups
            WHERE invite_code = ? AND user_id IS NOT NULL
        """, (invite_token,))

        invite_data = cursor.fetchone()
        if not invite_data:
            flash('Invalid or expired invite link', 'error')
            return redirect(url_for('index'))

        group_id, group_name, invite_code_from_db = invite_data

        user = get_user_info()
        if not user['is_authenticated']:
            session['pending_group_invite'] = invite_token
            flash(f'Please create an account or sign in to join "{group_name}"', 'info')
            return redirect(url_for('login'))

        cursor.execute("""
            SELECT id FROM group_memberships
            WHERE group_id = ? AND user_id = ?
        """, (group_id, user['id']))

        if cursor.fetchone():
            flash(f'You are already a member of "{group_name}"', 'info')
            return redirect(url_for('l8_teams.group_detail', group_id=group_id))

        try:
            cursor.execute("""
                INSERT INTO group_memberships (group_id, user_id)
                VALUES (?, ?)
            """, (group_id, user['id']))
            conn.commit()
            flash(f'Successfully joined "{group_name}"!', 'success')
            return redirect(url_for('l8_teams.group_detail', group_id=group_id))
        except Exception as e:
            flash(f'Error joining group: {str(e)}', 'error')
            return redirect(url_for('l8_teams.groups_menu'))
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# API — Regenerate invite link
# ---------------------------------------------------------------------------

@l8_bp.route('/api/groups/<int:group_id>/regenerate-invite', methods=['POST'])
@require_auth
def api_regenerate_invite_link(group_id):
    """Regenerate invite link for group (admin only)"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id FROM project_groups WHERE id = ?
    """, (group_id,))

    group_data = cursor.fetchone()
    if not group_data or group_data[0] != user['id']:
        conn.close()
        return jsonify({'success': False, 'error': 'Access denied'})

    try:
        invite_code = secrets.token_urlsafe(32)
        cursor.execute("""
            UPDATE project_groups SET invite_code = ?
            WHERE id = ? AND user_id = ?
        """, (invite_code, group_id, user['id']))

        conn.commit()

        invite_url = f"{request.host_url}groups/join/{invite_code}"

        conn.close()
        return jsonify({
            'success': True,
            'invite_link': {
                'token': invite_code,
                'url': invite_url
            },
            'message': 'New invite link generated successfully!'
        })

    except Exception as e:
        conn.close()
        return jsonify({'success': False, 'error': str(e)})


# ---------------------------------------------------------------------------
# API — Create group project
# ---------------------------------------------------------------------------

@l8_bp.route('/api/groups/<int:group_id>/projects', methods=['POST'])
@require_auth
def api_create_group_project(group_id):
    """Create a new project for the group"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT id FROM group_memberships
            WHERE group_id = ? AND user_id = ?
        """, (group_id, user['id']))

        if not cursor.fetchone():
            return jsonify({'success': False, 'error': 'Access denied'})

        data = request.get_json()
        project_name = data.get('name', '').strip()

        if not project_name:
            return jsonify({'success': False, 'error': 'Project name is required'})

        project_id = storage_manager._create_project_sqlite({
            'name': project_name,
            'user_id': user['id'],
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        project_identifier = f"local:{project_id}"

        cursor.execute("""
            INSERT INTO project_shares (project_id, group_id, shared_by, project_identifier, storage_type)
            VALUES (?, ?, ?, ?, ?)
        """, (project_id, group_id, user['id'], project_identifier, 'local'))

        conn.commit()

        return jsonify({
            'success': True,
            'message': f'Project "{project_name}" created and shared with group successfully!',
            'project_id': project_id,
            'project_identifier': project_identifier
        })

    except sqlite3.IntegrityError as e:
        conn.rollback()
        return jsonify({'success': False, 'error': f'Database integrity error: {e}'})
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'error': f'An unexpected error occurred: {e}'})
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# API — Share project with group
# ---------------------------------------------------------------------------

@l8_bp.route('/api/projects/<project_id>/share', methods=['POST'])
@require_auth
def api_share_project(project_id):
    """Share a project with a group"""
    user = get_user_info()

    try:
        data = request.get_json()
        group_id = data.get('group_id')

        if not group_id:
            return jsonify({'success': False, 'error': 'Group ID is required'})

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Verify project belongs to user
        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (project_id, user['id']))
        project = cursor.fetchone()

        if not project:
            return jsonify({'success': False, 'error': 'Project not found or access denied'})

        # Verify user is member of the group
        cursor.execute("""
            SELECT g.name FROM groups g
            JOIN group_memberships gm ON g.id = gm.group_id
            WHERE g.id = ? AND gm.user_id = ?
        """, (group_id, user['id']))

        group = cursor.fetchone()
        if not group:
            return jsonify({'success': False, 'error': 'Group not found or access denied'})

        # Check if already shared
        cursor.execute("""
            SELECT id FROM project_shares
            WHERE project_id = ? AND group_id = ?
        """, (project_id, group_id))

        if cursor.fetchone():
            return jsonify({'success': False, 'error': 'Project is already shared with this group'})

        # Check if project uses cloud storage before sharing
        project_storage_type = storage_manager.get_project_storage_type(project_id)

        if project_storage_type != 'cloud':
            if not clean_firebase_service.is_available():
                return jsonify({
                    'success': False,
                    'error': 'Group projects require cloud storage, but cloud storage is not available. Please check your connection.'
                })

            success, message = storage_manager.migrate_project_to_cloud(project_id, user['id'])
            if not success:
                return jsonify({
                    'success': False,
                    'error': f'Group projects require cloud storage. Migration failed: {message}'
                })

        # Share the project
        cursor.execute("""
            INSERT INTO project_shares (project_id, group_id, shared_by)
            VALUES (?, ?, ?)
        """, (project_id, group_id, user['id']))

        conn.commit()
        conn.close()

        return jsonify({
            'success': True,
            'message': f'Project "{project[0]}" shared with group "{group[0]}" successfully! (Now using cloud storage for collaboration)'
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


# ---------------------------------------------------------------------------
# API — Get project shares
# ---------------------------------------------------------------------------

@l8_bp.route('/api/projects/<project_id>/shares')
@require_auth
def api_get_project_shares(project_id):
    """Get current sharing information for a project"""
    user = get_user_info()

    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (project_id, user['id']))
        project = cursor.fetchone()

        if not project:
            return jsonify({'success': False, 'error': 'Project not found or access denied'})

        cursor.execute("""
            SELECT ps.group_id, g.name as group_name, ps.shared_at
            FROM project_shares ps
            JOIN project_groups g ON ps.group_id = g.id
            WHERE ps.project_id = ?
            ORDER BY ps.shared_at DESC
        """, (project_id,))

        shares = []
        for share in cursor.fetchall():
            shares.append({
                'group_id': share[0],
                'group_name': share[1],
                'shared_at': share[2]
            })

        conn.close()

        return jsonify({
            'success': True,
            'shares': shares
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


# ---------------------------------------------------------------------------
# API — Unshare project from group
# ---------------------------------------------------------------------------

@l8_bp.route('/api/projects/<project_id>/unshare/<int:group_id>', methods=['DELETE'])
@require_auth
def api_unshare_project(project_id, group_id):
    """Remove project sharing from a group"""
    user = get_user_info()

    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM projects WHERE id = ? AND user_id = ?", (project_id, user['id']))
        project = cursor.fetchone()

        if not project:
            return jsonify({'success': False, 'error': 'Project not found or access denied'})

        cursor.execute("SELECT name FROM groups WHERE id = ?", (group_id,))
        group = cursor.fetchone()

        cursor.execute("""
            DELETE FROM project_shares
            WHERE project_id = ? AND group_id = ?
        """, (project_id, group_id))

        if cursor.rowcount == 0:
            return jsonify({'success': False, 'error': 'Project was not shared with this group'})

        conn.commit()
        conn.close()

        group_name = group[0] if group else 'Unknown Group'

        return jsonify({
            'success': True,
            'message': f'Project "{project[0]}" is no longer shared with "{group_name}"'
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


# ---------------------------------------------------------------------------
# API — Firestore-backed group CRUD
# ---------------------------------------------------------------------------

@l8_bp.route('/api/groups', methods=['GET', 'POST'])
@require_auth
def api_groups():
    """Get user's groups or create a new group"""
    user_id = session.get('user_id')

    if request.method == 'GET':
        try:
            groups = firestore_db.get_user_groups(user_id)
            return jsonify({'success': True, 'groups': groups})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    elif request.method == 'POST':
        try:
            data = request.get_json()
            group_name = data.get('name', '').strip()
            description = data.get('description', '').strip()

            if not group_name:
                return jsonify({'success': False, 'error': 'Group name is required'})

            group_data = {
                'name': group_name,
                'description': description,
                'admin_user_id': user_id
            }

            group_id = firestore_db.create_group(group_data)
            if group_id:
                result = firestore_db.add_group_member(group_id, user_id, 'admin')
                if result['success']:
                    return jsonify({
                        'success': True,
                        'group_id': group_id,
                        'message': f'Group "{group_name}" created successfully!'
                    })
                else:
                    return jsonify({'success': False, 'error': result['error']})
            else:
                return jsonify({'success': False, 'error': 'Failed to create group'})

        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})


@l8_bp.route('/api/groups/<group_id>', methods=['GET', 'PUT', 'DELETE'])
@require_auth
def api_group_detail(group_id):
    """Get, update, or delete a specific group"""
    user_id = session.get('user_id')

    group = firestore_db.get_group(group_id)
    if not group:
        return jsonify({'success': False, 'error': 'Group not found'})

    user_groups = firestore_db.get_user_groups(user_id)
    user_group_ids = [g['id'] for g in user_groups]

    if group_id not in user_group_ids:
        return jsonify({'success': False, 'error': 'Access denied'})

    if request.method == 'GET':
        try:
            members = firestore_db.get_group_members(group_id)
            group['members'] = members
            return jsonify({'success': True, 'group': group})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    elif request.method == 'PUT':
        if group.get('admin_user_id') != user_id:
            return jsonify({'success': False, 'error': 'Only group admin can update group'})

        try:
            data = request.get_json()
            update_data = {}

            if 'name' in data:
                update_data['name'] = data['name'].strip()
            if 'description' in data:
                update_data['description'] = data['description'].strip()

            if not update_data:
                return jsonify({'success': False, 'error': 'No valid fields to update'})

            success = firestore_db.update_group(group_id, update_data)
            if success:
                return jsonify({'success': True, 'message': 'Group updated successfully'})
            else:
                return jsonify({'success': False, 'error': 'Failed to update group'})

        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    elif request.method == 'DELETE':
        if group.get('admin_user_id') != user_id:
            return jsonify({'success': False, 'error': 'Only group admin can delete group'})

        try:
            success = firestore_db.delete_group(group_id)
            if success:
                return jsonify({'success': True, 'message': 'Group deleted successfully'})
            else:
                return jsonify({'success': False, 'error': 'Failed to delete group'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})


# ---------------------------------------------------------------------------
# API — Firestore-backed group membership
# ---------------------------------------------------------------------------

@l8_bp.route('/api/groups/<group_id>/members', methods=['GET', 'POST'])
@require_auth
def api_group_members(group_id):
    """Get group members or add new member"""
    user_id = session.get('user_id')

    user_groups = firestore_db.get_user_groups(user_id)
    user_group_ids = [g['id'] for g in user_groups]

    if group_id not in user_group_ids:
        return jsonify({'success': False, 'error': 'Access denied'})

    if request.method == 'GET':
        try:
            members = firestore_db.get_group_members(group_id)
            return jsonify({'success': True, 'members': members})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    elif request.method == 'POST':
        group = firestore_db.get_group(group_id)
        if group.get('admin_user_id') != user_id:
            return jsonify({'success': False, 'error': 'Only group admin can add members'})

        try:
            data = request.get_json()
            target_user_id = data.get('user_id')
            role = data.get('role', 'member')

            if not target_user_id:
                return jsonify({'success': False, 'error': 'User ID is required'})

            result = firestore_db.add_group_member(group_id, target_user_id, role)
            return jsonify(result)

        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})


@l8_bp.route('/api/groups/<group_id>/members/<member_user_id>', methods=['DELETE', 'PUT'])
@require_auth
def api_group_member_detail(group_id, member_user_id):
    """Remove member from group or update member role"""
    user_id = session.get('user_id')

    group = firestore_db.get_group(group_id)
    if not group or group.get('admin_user_id') != user_id:
        return jsonify({'success': False, 'error': 'Access denied: Only group admin can manage members'})

    if request.method == 'DELETE':
        try:
            success = firestore_db.remove_group_member(group_id, member_user_id)
            if success:
                return jsonify({'success': True, 'message': 'Member removed successfully'})
            else:
                return jsonify({'success': False, 'error': 'Failed to remove member'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            new_role = data.get('role', 'member')

            success = firestore_db.update_member_role(group_id, member_user_id, new_role)
            if success:
                return jsonify({'success': True, 'message': f'Member role updated to {new_role}'})
            else:
                return jsonify({'success': False, 'error': 'Failed to update member role'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})


# ---------------------------------------------------------------------------
# API — Firestore-backed project sharing
# ---------------------------------------------------------------------------

@l8_bp.route('/api/projects/<project_id>/sharing', methods=['GET', 'POST'])
@require_auth
def api_project_sharing(project_id):
    """Get project shares or create new share (Firestore)"""
    user_id = session.get('user_id')

    if not firestore_db.user_has_project_access(user_id, project_id, 'admin'):
        project = firestore_db.get_project(project_id)
        if not project or project.get('user_id') != user_id:
            return jsonify({'success': False, 'error': 'Access denied: You must be the project owner or have admin access'})

    if request.method == 'GET':
        try:
            shares = firestore_db.get_project_shares(project_id)
            return jsonify({'success': True, 'shares': shares})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    elif request.method == 'POST':
        try:
            data = request.get_json()
            share_type = data.get('type', 'user')
            permission_level = data.get('permission_level', 'read')

            if share_type == 'user':
                target_user_id = data.get('user_id')
                if not target_user_id:
                    return jsonify({'success': False, 'error': 'User ID is required'})

                result = firestore_db.share_project_with_user(project_id, target_user_id, user_id, permission_level)

            elif share_type == 'group':
                target_group_id = data.get('group_id')
                if not target_group_id:
                    return jsonify({'success': False, 'error': 'Group ID is required'})

                result = firestore_db.share_project_with_group(project_id, target_group_id, user_id, permission_level)

            else:
                return jsonify({'success': False, 'error': 'Invalid share type'})

            return jsonify(result)

        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})


@l8_bp.route('/api/projects/<project_id>/shares/<share_id>', methods=['DELETE', 'PUT'])
@require_auth
def api_project_share_detail(project_id, share_id):
    """Remove or update a project share"""
    user_id = session.get('user_id')

    project = firestore_db.get_project(project_id)
    if not project or project.get('user_id') != user_id:
        return jsonify({'success': False, 'error': 'Access denied: Only project owner can manage shares'})

    if request.method == 'DELETE':
        try:
            success = firestore_db.remove_project_share(share_id)
            if success:
                return jsonify({'success': True, 'message': 'Share removed successfully'})
            else:
                return jsonify({'success': False, 'error': 'Failed to remove share'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            new_permission = data.get('permission_level', 'read')

            success = firestore_db.update_project_share_permission(share_id, new_permission)
            if success:
                return jsonify({'success': True, 'message': f'Permission updated to {new_permission}'})
            else:
                return jsonify({'success': False, 'error': 'Failed to update permission'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
