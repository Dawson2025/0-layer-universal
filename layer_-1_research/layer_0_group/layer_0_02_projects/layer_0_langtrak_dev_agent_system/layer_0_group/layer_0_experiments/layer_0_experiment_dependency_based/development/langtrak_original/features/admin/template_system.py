# resource_id: "98663658-843d-441f-8773-f89893ab4f57"
# resource_type: "document"
# resource_name: "template_system"
"""
Admin Template System Module

Handles phoneme template creation, export, import, and application.
Agents can work on template system without affecting other sub-modules.
"""

from flask import render_template, request, jsonify, make_response
import re
import sqlite3
import json
from datetime import datetime

from core.database import DB_NAME
from core.decorators import require_project_admin
from features.auth import get_user_info
from services.firebase import clean_firebase_service, firestore_db
from src.phoneme_seed import seed_project_phonemes
from . import admin_bp


@admin_bp.route('/admin/templates')
@require_project_admin
def admin_templates():
    """
    Admin templates management page.

    Displays saved templates and current phonemes for template creation.

    Returns:
        Rendered templates management interface
    """
    try:
        conn = sqlite3.connect('data/phonemes.db')
        cursor = conn.cursor()

        # Create templates table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phoneme_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                template_data TEXT NOT NULL,
                phoneme_count INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Get all saved templates
        cursor.execute("""
            SELECT id, name, description, phoneme_count, created_at
            FROM phoneme_templates
            ORDER BY created_at DESC
        """)
        templates = cursor.fetchall()

        # Get current phonemes for template creation
        cursor.execute("SELECT phoneme, frequency FROM phonemes ORDER BY phoneme")
        current_phonemes = cursor.fetchall()

        conn.close()

        return render_template('admin_templates.html',
                             templates=templates,
                             current_phonemes=current_phonemes)
    except Exception as e:
        print(f"Error loading templates: {e}")
        return render_template('admin_templates.html', templates=[], current_phonemes=[])


@admin_bp.route('/api/admin/templates')
@require_project_admin
def api_admin_templates():
    """
    List saved templates as JSON for the admin UI.

    Returns:
        JSON with templates: [{id, name, description, phoneme_count, created_at}]
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, name, description, phoneme_count, created_at
            FROM phoneme_templates
            ORDER BY datetime(created_at) DESC, id DESC
            """
        )
        rows = cursor.fetchall()
        conn.close()
        templates = [
            {
                'id': r[0],
                'name': r[1],
                'description': r[2],
                'phoneme_count': r[3],
                'created_at': r[4],
            }
            for r in rows
        ]
        return jsonify({'success': True, 'templates': templates})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@admin_bp.route('/api/templates', methods=['POST'])
@admin_bp.route('/api/admin/import-template', methods=['POST'])
def api_create_template():
    """
    Create a new phoneme template from current phonemes.

    Request JSON:
        name: Template name (required)
        description: Template description

    Returns:
        JSON response with success status
    """
    try:
        data = request.get_json()
        template_name = data.get('name', '').strip()
        description = data.get('description', '').strip()

        if not template_name:
            return jsonify({'success': False, 'error': 'Template name is required'})

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get current phonemes with full hierarchy
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, subgroup_type,
                   sub_subgroup_type, sub_sub_subgroup_type, phoneme, frequency
            FROM phonemes ORDER BY phoneme
        """)
        phonemes = cursor.fetchall()

        if not phonemes:
            conn.close()
            return jsonify({'success': False, 'error': 'No phonemes available to create template'})

        # Create template data (JSON format) with full hierarchy
        template_data = {
            'phonemes': []
        }

        for phoneme in phonemes:
            template_data['phonemes'].append({
                'syllable_type': phoneme[0],
                'position': phoneme[1],
                'length_type': phoneme[2],
                'group_type': phoneme[3],
                'subgroup_type': phoneme[4],
                'sub_subgroup_type': phoneme[5],
                'sub_sub_subgroup_type': phoneme[6],
                'phoneme': phoneme[7],
                'frequency': 0  # Reset frequencies to 0 for new template
            })

        # Insert template
        cursor.execute("""
            INSERT INTO phoneme_templates (name, description, template_data, phoneme_count)
            VALUES (?, ?, ?, ?)
        """, (template_name, description, json.dumps(template_data), len(phonemes)))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': f'Template "{template_name}" created successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/templates/<int:template_id>', methods=['DELETE'])
@admin_bp.route('/api/admin/delete-template/<int:template_id>', methods=['DELETE'])
def api_delete_template(template_id):
    """
    Delete a phoneme template.

    Args:
        template_id: ID of template to delete

    Returns:
        JSON response with success status
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM phoneme_templates WHERE id = ?", (template_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template deleted successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/templates/<int:template_id>/apply', methods=['POST'])
@admin_bp.route('/api/admin/apply-template/<int:template_id>', methods=['POST'])
def api_apply_template(template_id):
    """
    Apply a template to current phonemes.

    Supports both old format (dict) and new format (list) template data.

    Args:
        template_id: ID of template to apply

    Returns:
        JSON response with success status
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get template data
        cursor.execute("SELECT template_data FROM phoneme_templates WHERE id = ?", (template_id,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            return jsonify({'success': False, 'error': 'Template not found'})

        template_data = json.loads(result[0])
        template_phonemes = template_data.get('phonemes', {})

        # Apply template phonemes to current database
        # Handle both old format (dict with phoneme as key) and new format (list of phoneme objects)
        if isinstance(template_phonemes, dict):
            # Old format - just update frequencies
            for symbol, data in template_phonemes.items():
                frequency = data.get('frequency', 0)
                cursor.execute("""
                    UPDATE phonemes SET frequency = ? WHERE phoneme = ?
                """, (frequency, symbol))
        else:
            # New format - full phoneme data
            for phoneme_data in template_phonemes:
                frequency = phoneme_data.get('frequency', 0)
                cursor.execute("""
                    INSERT OR REPLACE INTO phonemes (syllable_type, position, length_type, group_type,
                                                  subgroup_type, phoneme, frequency, sub_subgroup_type,
                                                  sub_sub_subgroup_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    phoneme_data.get('syllable_type'),
                    phoneme_data.get('position'),
                    phoneme_data.get('length_type'),
                    phoneme_data.get('group_type'),
                    phoneme_data.get('subgroup_type'),
                    phoneme_data.get('phoneme'),
                    frequency,
                    phoneme_data.get('sub_subgroup_type'),
                    phoneme_data.get('sub_sub_subgroup_type')
                ))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template applied successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/admin/download-template/<int:template_id>', methods=['GET'])
def api_download_template(template_id):
    """
    Download a phoneme template as a JSON file.

    Args:
        template_id: ID of the template to download

    Returns:
        JSON file response or error JSON payload
    """
    try:
        conn = sqlite3.connect('data/phonemes.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name, template_data
            FROM phoneme_templates
            WHERE id = ?
        """, (template_id,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            return jsonify({'success': False, 'error': 'Template not found'}), 404

        template_name, template_data = result
        if not template_data:
            return jsonify({'success': False, 'error': 'Template data is empty'}), 404

        # template_data is stored as JSON string
        filename_safe = re.sub(r'[^A-Za-z0-9_-]+', '_', template_name or 'template')
        response = make_response(template_data)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Content-Disposition'] = f'attachment; filename={filename_safe}.json'
        return response

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@admin_bp.route('/api/admin/export-template', methods=['POST'])
@require_project_admin
def api_admin_export_template():
    """
    API endpoint to export current phonemes as a template.

    Request JSON:
        name: Template name (default: 'Phoneme Template')
        description: Template description

    Returns:
        JSON response with success status
    """
    try:
        data = request.get_json()
        template_name = data.get('name', 'Phoneme Template')
        template_description = data.get('description', '')

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create templates table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phoneme_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                template_data TEXT NOT NULL,
                phoneme_count INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Get all current phonemes with full 4-level hierarchy
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type,
                   subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, phoneme
        """)

        phonemes = cursor.fetchall()

        # Convert to template format
        template_data = {
            'name': template_name,
            'description': template_description,
            'export_date': datetime.now().isoformat(),
            'phonemes': []
        }

        for phoneme in phonemes:
            template_data['phonemes'].append({
                'syllable_type': phoneme[0],
                'position': phoneme[1],
                'length_type': phoneme[2],
                'group_type': phoneme[3],
                'subgroup_type': phoneme[4],
                'sub_subgroup_type': phoneme[5],
                'sub_sub_subgroup_type': phoneme[6],
                'phoneme': phoneme[7],
                'frequency': phoneme[8]
            })

        # Save template to database
        cursor.execute("""
            INSERT INTO phoneme_templates (name, description, template_data, phoneme_count)
            VALUES (?, ?, ?, ?)
        """, (template_name, template_description, json.dumps(template_data), len(phonemes)))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template exported successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/admin/reset-to-default', methods=['POST'])
@require_project_admin
def api_admin_reset_to_default():
    """
    Reset the current project's phonemes to the default template.
    """
    try:
        user = get_user_info()
        current = user.get('current_project') or {}
        storage_type = (current.get('storage_type') or 'local').lower()

        if storage_type == 'cloud' and clean_firebase_service.is_available():
            proj_id = current.get('cloud_project_id') or current.get('id')
            # Delete existing phonemes in this project
            items = firestore_db.get_project_phonemes(str(proj_id)) or []
            for it in items:
                if it.get('id'):
                    try:
                        firestore_db.delete_phoneme(it['id'])
                    except Exception:
                        pass
            # Seed defaults
            seed_project_phonemes(str(proj_id), user.get('id'), 'cloud')
        else:
            proj_id = current.get('local_project_id') or current.get('id')
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM phonemes WHERE project_id = ?", (proj_id,))
            conn.commit()
            conn.close()
            # Seed defaults
            seed_project_phonemes(str(proj_id), user.get('id'), 'local')

        return jsonify({'success': True, 'message': 'Phonemes reset to default template.'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


__all__ = [
    'admin_templates',
    'api_create_template',
    'api_delete_template',
    'api_apply_template',
    'api_download_template',
    'api_admin_export_template'
]
