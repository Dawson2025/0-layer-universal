"""Dashboard display - user's main view of projects and groups."""

from datetime import datetime
import sqlite3

from flask import render_template

from core.decorators import require_auth
from core.session import get_user_info
from features.projects import fetch_project_metadata
from services.firebase import clean_firebase_service, firestore_db
from src.storage_manager import storage_manager
import main

from . import dashboard_bp


@dashboard_bp.route('/dashboard')
@require_auth
def dashboard():
    """User dashboard showing projects and groups"""
    user = get_user_info()

    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Gather projects from both local and cloud storage
    raw_projects = storage_manager.get_projects(user['id'])
    projects = []

    for project in raw_projects:
        storage_type = project.get('storage_type', 'local')
        project_id = project.get('id')
        project_name = project.get('name', 'Untitled')

        created_at = project.get('created_at')
        updated_at = project.get('updated_at')

        # Normalize timestamps to ISO strings for template slicing
        if hasattr(created_at, 'isoformat'):
            created_at = created_at.isoformat()
        if hasattr(updated_at, 'isoformat'):
            updated_at = updated_at.isoformat()
        created_at = created_at or datetime.utcnow().isoformat()
        updated_at = updated_at or datetime.utcnow().isoformat()

        # Word counts: local projects from SQLite, cloud projects fallback to zero for now
        if storage_type == 'local':
            try:
                cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (int(project_id),))
                word_count = cursor.fetchone()[0]
            except Exception:
                word_count = 0
        else:
            # TODO: add Firestore word counting
            word_count = project.get('word_count', 0)

        projects.append({
            'id': project_id,
            'name': project_name,
            'created_at': created_at,
            'updated_at': updated_at,
            'word_count': word_count,
            'storage_type': storage_type,
            'cloud_project_id': project.get('cloud_project_id'),
            'cloud_last_sync': project.get('cloud_last_sync')
        })

    # Sort projects by updated_at descending for consistency
    projects.sort(key=lambda p: p['updated_at'], reverse=True)

    cursor.execute("""
        SELECT
            ps.project_identifier,
            ps.project_id,
            ps.cloud_project_id,
            ps.storage_type,
            ps.group_id,
            ps.shared_by,
            ps.shared_at,
            g.name as group_name,
            p.name as local_name,
            p.created_at,
            p.updated_at,
            p.user_id as local_owner_id,
            owner.username as local_owner_name,
            sharer.username as sharer_name
        FROM project_shares ps
        JOIN groups g ON ps.group_id = g.id
        JOIN group_memberships gm ON g.id = gm.group_id
        LEFT JOIN projects p ON ps.project_id = p.id
        LEFT JOIN users owner ON p.user_id = owner.id
        LEFT JOIN users sharer ON ps.shared_by = sharer.id
        WHERE gm.user_id = ?
    """, (user['id'],))

    share_rows = cursor.fetchall()
    local_project_ids = [row[1] for row in share_rows if row[1] is not None]
    local_word_counts = {}
    if local_project_ids:
        placeholders = ",".join("?" for _ in local_project_ids)
        cursor.execute(
            f"SELECT project_id, COUNT(*) FROM words WHERE project_id IN ({placeholders}) GROUP BY project_id",
            tuple(local_project_ids)
        )
        local_word_counts = {row[0]: row[1] for row in cursor.fetchall()}

    shared_projects_map = {}
    user_id_str = str(user['id'])

    for row in share_rows:
        project_identifier, local_project_id, cloud_project_id, storage_type, group_id, shared_by, shared_at, group_name, local_name, local_created_at, local_updated_at, local_owner_id, local_owner_name, sharer_name = row
        if str(shared_by) == user_id_str:
            continue  # Skip projects we shared ourselves

        entry = shared_projects_map.get(project_identifier)
        if not entry:
            entry = {
                'id': cloud_project_id if storage_type == 'cloud' and cloud_project_id else local_project_id,
                'name': local_name or 'Shared Project',
                'word_count': 0,
                'owner_name': sharer_name or local_owner_name or 'Unknown',
                'group_names': set(),
                'updated_at': local_updated_at or shared_at,
                'storage_type': storage_type,
                'cloud_project_id': cloud_project_id
            }

            if storage_type == 'cloud' and cloud_project_id and clean_firebase_service.is_available():
                metadata = fetch_project_metadata('cloud', cloud_project_id)
                if metadata:
                    entry['name'] = metadata.get('name') or entry['name']
                    updated_val = metadata.get('updated_at')
                    if hasattr(updated_val, 'isoformat'):
                        updated_val = updated_val.isoformat()
                    entry['updated_at'] = updated_val or entry['updated_at']
                try:
                    entry['word_count'] = firestore_db.count_project_words(cloud_project_id)
                except Exception as exc:
                    print(f"Error counting words for shared cloud project {cloud_project_id}: {exc}")
            elif local_project_id is not None:
                entry['word_count'] = local_word_counts.get(local_project_id, 0)

            shared_projects_map[project_identifier] = entry

        entry['group_names'].add(group_name)

    shared_projects = []
    for entry in shared_projects_map.values():
        updated_str = entry['updated_at']
        if hasattr(updated_str, 'isoformat'):
            updated_str = updated_str.isoformat()
        elif updated_str is None:
            updated_str = ''

        group_display = ', '.join(sorted(entry['group_names'])) if entry['group_names'] else ''

        shared_projects.append({
            'id': entry['id'],
            'name': entry['name'],
            'word_count': entry['word_count'],
            'owner_name': entry['owner_name'],
            'group_name': group_display,
            'updated_at': updated_str
        })

    # Get user's groups
    cursor.execute("""
        SELECT g.id, g.name, g.description, g.created_at, g.admin_user_id,
               CASE WHEN g.admin_user_id = ? THEN 1 ELSE 0 END as is_admin
        FROM groups g
        JOIN group_memberships gm ON g.id = gm.group_id
        WHERE gm.user_id = ?
        ORDER BY g.created_at DESC
    """, (user['id'], user['id']))

    groups = []
    for group in cursor.fetchall():
        groups.append({
            'id': group[0],
            'name': group[1],
            'description': group[2],
            'created_at': group[3],
            'admin_user_id': group[4],
            'is_admin': bool(group[5])
        })

    conn.close()

    return render_template('dashboard.html', projects=projects, shared_projects=shared_projects, groups=groups, user=user)
