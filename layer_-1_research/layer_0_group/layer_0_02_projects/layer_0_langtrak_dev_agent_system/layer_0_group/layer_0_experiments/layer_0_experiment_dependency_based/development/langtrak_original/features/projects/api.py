"""
Projects API Module

API endpoints for project management operations.
Agents can work on API improvements without affecting route logic.
"""

from flask import request, jsonify, session

from core.decorators import require_auth
from core.session import get_user_info
from src.storage_manager import storage_manager
from .metadata import normalize_project_identifier
from . import projects_bp


@projects_bp.route('/api/projects/<project_id>/delete', methods=['DELETE'])
@require_auth
def api_delete_project(project_id):
    """
    Delete a project and all its data.

    Handles both local and cloud projects.
    Clears current project from session if deleted.

    Args:
        project_id: ID of project to delete

    Returns:
        JSON response with success status
    """
    user = get_user_info()

    storage_type, identifier, project_identifier = normalize_project_identifier(project_id)
    if not storage_type:
        return jsonify({'success': False, 'error': 'Invalid project identifier'})

    success, message = storage_manager.delete_variant(user['id'], project_identifier)
    if success:
        current = session.get('current_project_id')
        if current in {project_id, identifier, project_identifier}:
            session.pop('current_project_id', None)
        return jsonify({'success': True, 'message': message})
    else:
        return jsonify({'success': False, 'error': message})


@projects_bp.route('/api/projects/<project_id>/cloud-link', methods=['GET'])
@require_auth
def api_get_project_cloud_link(project_id):
    """
    Return the associated cloud project identifier for a given project reference.

    Accepts a local numeric ID, `local:<id>` or `cloud:<id>`.
    """
    user = get_user_info()
    storage_type, identifier, project_identifier = normalize_project_identifier(project_id)
    if not storage_type:
        return jsonify({'success': False, 'error': 'Invalid project identifier'}), 400

    if storage_type == 'cloud':
        return jsonify({'success': True, 'cloudProjectId': identifier})

    try:
        local_id = int(identifier)
    except (TypeError, ValueError):
        return jsonify({'success': False, 'error': 'Invalid local project identifier'}), 400

    cloud_id = storage_manager.get_cloud_project_id(local_id, user['id'])
    if not cloud_id:
        return jsonify({'success': False, 'cloudProjectId': None}), 404

    return jsonify({'success': True, 'cloudProjectId': cloud_id})


@projects_bp.route('/api/project-groups/<group_id>/rename', methods=['POST'])
@require_auth
def api_rename_project_group(group_id):
    """
    Rename a project group.

    Request JSON:
        name: New name for the project group

    Args:
        group_id: ID of project group to rename

    Returns:
        JSON response with success status
    """
    user = get_user_info()
    data = request.get_json(silent=True) or {}
    new_name = (data.get('name') or '').strip()
    success, error = storage_manager.rename_group(user['id'], group_id, new_name)
    if success:
        return jsonify({'success': True, 'message': f'Project renamed to "{new_name}" successfully!'})
    return jsonify({'success': False, 'error': error})


@projects_bp.route('/api/project-groups/<group_id>/delete', methods=['DELETE'])
@require_auth
def api_delete_project_group(group_id):
    """
    Delete a project group and all its variants.

    Clears current project from session if any deleted variant is current.

    Args:
        group_id: ID of project group to delete

    Returns:
        JSON response with success status
    """
    user = get_user_info()
    success, result = storage_manager.delete_group(user['id'], group_id)
    if success:
        deleted_variants = result or []
        current = session.get('current_project_id')
        if current:
            for entry in deleted_variants:
                variant_identifier = entry.get('variant_identifier')
                if not variant_identifier:
                    continue
                prefix, ident = variant_identifier.split(':', 1)
                if current in {variant_identifier, ident}:
                    session.pop('current_project_id', None)
                    break
        return jsonify({'success': True, 'message': 'Project and all variants deleted successfully.'})
    if isinstance(result, dict):
        return jsonify({'success': False, 'error': result.get('error', 'Unable to delete project')})
    return jsonify({'success': False, 'error': result})


@projects_bp.route('/api/projects/<project_id>/merge', methods=['POST'])
@require_auth
def api_merge_project_variant(project_id):
    """
    Merge a source project variant into a target project variant.

    The source project is identified by `project_id` in the URL (e.g. 'local:123').
    The target project is identified by `target_variant` in the JSON payload.
    This operation will overwrite the target's data with the source's data.

    Request JSON:
        target_variant: Target variant identifier (e.g. 'local:456')

    Args:
        project_id: Source variant identifier (from URL)

    Returns:
        JSON response with success status and message
    """
    user = get_user_info()
    payload = request.get_json(silent=True) if request.is_json else request.form.to_dict()
    target_variant_identifier = (payload or {}).get('target_variant', '')

    if not target_variant_identifier:
        return jsonify({'success': False, 'message': 'Target variant is required for merge.'}), 400

    # project_id already contains the local: prefix from the URL
    source_variant_identifier = project_id

    try:
        success, message = storage_manager.merge_variants(user['id'], source_variant_identifier, target_variant_identifier)
        if success:
            return jsonify({'success': True, 'message': message}), 200
        else:
            return jsonify({'success': False, 'message': message}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error merging project variants: {e}'}), 500


__all__ = [
    'api_delete_project',
    'api_get_project_cloud_link',
    'api_rename_project_group',
    'api_delete_project_group',
    'api_merge_project_variant'
]
