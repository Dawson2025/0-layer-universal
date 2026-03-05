# resource_id: "a80277a8-4012-49bc-94f5-7acfa0a095a6"
# resource_type: "document"
# resource_name: "storage_ops"
"""
Projects Storage Operations Module

Handles cloud/local storage operations: migration, sync, fork.
Agents can work on storage operations without affecting other sub-modules.
"""

from flask import render_template, request, redirect, url_for, flash, jsonify
import sqlite3

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from services.firebase import clean_firebase_service
from src.storage_manager import storage_manager
from . import projects_bp


@projects_bp.route('/projects/<project_id>/migrate-to-cloud', methods=['POST'])
@require_auth
def migrate_project_to_cloud(project_id):
    """
    Migrate a local project to cloud storage.

    Args:
        project_id: ID of local project to migrate

    Returns:
        Redirect to projects menu with flash message
    """
    user = get_user_info()
    if not user:
        return redirect(url_for('auth.login'))

    if not clean_firebase_service.is_available():
        flash('Cloud storage is not available', 'error')
        return redirect(url_for('projects.projects_menu'))

    success, message = storage_manager.migrate_project_to_cloud(project_id, user['id'])

    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')

    return redirect(url_for('projects.projects_menu'))


@projects_bp.route('/projects/<project_id>/fork-to-local', methods=['POST'])
@require_auth
def fork_project_to_local(project_id):
    """
    Create a local copy of a cloud project.

    Args:
        project_id: ID of cloud project to fork

    Request JSON:
        name: Optional new name for local copy

    Returns:
        JSON response with success status and new project ID
    """
    user = get_user_info()
    if not clean_firebase_service.is_available():
        return jsonify({'success': False, 'error': 'Cloud storage is not available'}), 400

    data = request.get_json(silent=True) or {}
    new_name = data.get('name')

    success, result = storage_manager.fork_cloud_project_to_local(project_id, user['id'], new_name)
    if success:
        flash('Local copy created successfully!', 'success')
        return jsonify({'success': True, 'project_id': result})
    else:
        return jsonify({'success': False, 'error': result}), 400


@projects_bp.route('/projects/<int:project_id>/sync-to-cloud', methods=['POST'])
@require_auth
def sync_project_to_cloud(project_id):
    """
    Push local project changes to cloud.

    Args:
        project_id: ID of local project to sync

    Returns:
        JSON response with success status
    """
    user = get_user_info()
    success, message = storage_manager.sync_local_to_cloud(project_id, user['id'])
    status_code = 200 if success else 400
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return jsonify({'success': success, 'message': message}), status_code


@projects_bp.route('/projects/<int:project_id>/sync-from-cloud', methods=['POST'])
@require_auth
def sync_project_from_cloud(project_id):
    """
    Pull latest cloud changes into local project.

    Args:
        project_id: ID of local project to update

    Returns:
        JSON response with success status
    """
    user = get_user_info()
    success, message = storage_manager.sync_cloud_to_local(project_id, user['id'])
    status_code = 200 if success else 400
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return jsonify({'success': success, 'message': message}), status_code


@projects_bp.route('/admin/storage')
@require_auth
def admin_storage():
    """
    Dedicated panel for managing cloud/local project storage.

    Only available to project owners.

    Returns:
        Rendered storage management panel
    """
    if not clean_firebase_service.is_available():
        flash('Cloud storage features are currently unavailable.', 'error')
        return redirect(url_for('main_menu'))

    user = get_user_info()
    current_project = user.get('current_project')
    if not current_project or not current_project.get('is_owner'):
        flash('Only project owners can manage cloud/local storage.', 'error')
        return redirect(url_for('main_menu'))

    project_summary = storage_manager.get_project_detail(user['id'], current_project['id'])
    if not project_summary:
        flash('Project details not found.', 'error')
        return redirect(url_for('main_menu'))

    project_summary['local_variants'] = [v for v in project_summary.get('variants', []) if v['type'] == 'local']
    project_summary['cloud_variants'] = [v for v in project_summary.get('variants', []) if v['type'] == 'cloud']
    project_summary['display_name'] = project_summary.get('name')

    return render_template(
        'admin_storage.html',
        user=user,
        project=project_summary,
        firebase_available=clean_firebase_service.is_available()
    )


__all__ = [
    'migrate_project_to_cloud',
    'fork_project_to_local',
    'sync_project_to_cloud',
    'sync_project_from_cloud',
    'admin_storage'
]
