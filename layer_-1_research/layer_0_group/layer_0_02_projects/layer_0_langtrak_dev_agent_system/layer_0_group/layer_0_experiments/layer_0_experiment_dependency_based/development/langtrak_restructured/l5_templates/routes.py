# resource_id: "cc1a555e-191f-4e36-86ce-d02faa58b9e9"
# resource_type: "document"
# resource_name: "routes"
"""L5 Templates - All template routes (local, cloud, admin, phoneme templates)"""

from flask import Blueprint, render_template, request, jsonify, session, Response
import sqlite3
import json
from datetime import datetime

import main
from l2_infrastructure.auth import require_auth, require_project_admin
from l3_users.sessions.session import get_user_info
from l2_infrastructure.firebase import clean_firebase_service, firestore_db
from l2_infrastructure.storage import storage_manager, StorageType

l5_bp = Blueprint('l5_templates', __name__)


# =============================================================================
# Local Template Routes
# =============================================================================

@l5_bp.route('/admin/templates')
@require_project_admin
def admin_templates():
    """Admin templates management page"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
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

        # Get all saved templates (if any exist)
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

        return render_template('admin_templates.html', templates=templates, current_phonemes=current_phonemes)
    except Exception as e:
        print(f"Error loading templates: {e}")
        return render_template('admin_templates.html', templates=[], current_phonemes=[])


@l5_bp.route('/api/templates', methods=['POST'])
def api_create_template():
    """Create a new phoneme template"""
    try:
        data = request.get_json()
        template_name = data.get('name', '').strip()
        description = data.get('description', '').strip()

        if not template_name:
            return jsonify({'success': False, 'error': 'Template name is required'})

        conn = sqlite3.connect(main.DB_NAME)
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

        template_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': f'Template "{template_name}" created successfully', 'template_id': template_id})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/templates/<int:template_id>', methods=['DELETE'])
def api_delete_template(template_id):
    """Delete a phoneme template"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM phoneme_templates WHERE id = ?", (template_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template deleted successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/templates/<int:template_id>/apply', methods=['POST'])
def api_apply_template(template_id):
    """Apply a template to current phonemes"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
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


# =============================================================================
# Admin Template Routes
# =============================================================================

@l5_bp.route('/api/admin/export-template', methods=['POST'])
@require_project_admin
def api_admin_export_template():
    """API endpoint to export current phonemes as a template"""
    try:
        data = request.get_json()
        template_name = data.get('name', 'Phoneme Template')
        template_description = data.get('description', '')

        conn = sqlite3.connect(main.DB_NAME)
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

        template_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template exported successfully!', 'template_id': template_id})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/admin/templates')
@require_project_admin
def api_admin_get_templates():
    """API endpoint to get all saved templates"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

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

        cursor.execute("SELECT id, name, description, phoneme_count, created_at FROM phoneme_templates ORDER BY created_at DESC")
        templates = cursor.fetchall()
        conn.close()

        templates_list = []
        for template in templates:
            templates_list.append({
                'id': template[0],
                'name': template[1],
                'description': template[2],
                'phoneme_count': template[3],
                'created_at': template[4]
            })
        return jsonify({'success': True, 'templates': templates_list})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/admin/apply-template/<int:template_id>', methods=['POST'])
@require_project_admin
def api_admin_apply_template(template_id):
    """API endpoint to apply a phoneme template with enhanced validation and options"""
    try:
        data = request.get_json() or {}
        preserve_frequencies = data.get('preserve_frequencies', False)
        force_apply = data.get('force_apply', False)
        phoneme_handling = data.get('phoneme_handling', {})

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Get template data
        cursor.execute("""
            SELECT name, template_data FROM phoneme_templates WHERE id = ?
        """, (template_id,))

        result = cursor.fetchone()
        if not result:
            conn.close()
            return jsonify({'success': False, 'error': 'Template not found'})

        template_name, template_data_json = result
        template_data = json.loads(template_data_json)

        # Get current phonemes with their usage details
        cursor.execute("""
            SELECT id, syllable_type, position, length_type, group_type,
                   subgroup_type, phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
        """)
        current_phonemes = cursor.fetchall()

        # Create sets and dictionaries for comparison
        template_phonemes_set = set()
        template_phonemes_dict = {}

        for phoneme_data in template_data['phonemes']:
            key = (
                phoneme_data.get('syllable_type'),
                phoneme_data.get('position'),
                phoneme_data.get('length_type'),
                phoneme_data.get('group_type'),
                phoneme_data.get('subgroup_type'),
                phoneme_data.get('phoneme')
            )
            template_phonemes_set.add(key)
            template_phonemes_dict[key] = phoneme_data

        current_phonemes_set = set()
        current_phonemes_dict = {}

        for phoneme in current_phonemes:
            key = (
                phoneme[1], phoneme[2], phoneme[3], phoneme[4], phoneme[5], phoneme[6]
            )
            current_phonemes_set.add(key)
            current_phonemes_dict[key] = {
                'id': phoneme[0],
                'syllable_type': phoneme[1],
                'position': phoneme[2],
                'length_type': phoneme[3],
                'group_type': phoneme[4],
                'subgroup_type': phoneme[5],
                'phoneme': phoneme[6],
                'frequency': phoneme[7]
            }

        # Find phonemes that will be removed
        phonemes_to_remove = current_phonemes_set - template_phonemes_set
        phonemes_in_common = current_phonemes_set & template_phonemes_set
        phonemes_to_add = template_phonemes_set - current_phonemes_set

        # Check if any phonemes to be removed are used in words
        phonemes_in_use = []
        phoneme_word_details = {}

        if phonemes_to_remove and not force_apply:
            for phoneme_key in phonemes_to_remove:
                syllable_type, position, length_type, group_type, subgroup_type, phoneme = phoneme_key

                # Get detailed word information for this phoneme
                if position == 'onset':
                    cursor.execute("""
                        SELECT id, english_words, new_language_word, ipa_phonetics
                        FROM words WHERE onset_phoneme = ? AND onset_length_type = ?
                    """, (phoneme, length_type))
                elif position == 'nucleus':
                    cursor.execute("""
                        SELECT id, english_words, new_language_word, ipa_phonetics
                        FROM words WHERE nucleus_phoneme = ? AND nucleus_length_type = ?
                    """, (phoneme, length_type))
                elif position == 'coda':
                    cursor.execute("""
                        SELECT id, english_words, new_language_word, ipa_phonetics
                        FROM words WHERE coda_phoneme = ? AND coda_length_type = ?
                    """, (phoneme, length_type))

                words_using_phoneme = cursor.fetchall()
                if words_using_phoneme:
                    phoneme_key_str = f"{phoneme}_{position}_{length_type}"
                    phoneme_word_details[phoneme_key_str] = []

                    for word_data in words_using_phoneme:
                        try:
                            english_words_data = json.loads(word_data[1]) if word_data[1] else []
                            if isinstance(english_words_data, list):
                                english_display = ', '.join(english_words_data)
                            else:
                                english_display = str(word_data[1])
                        except (json.JSONDecodeError, TypeError):
                            english_display = word_data[1] or 'No translation'

                        phoneme_word_details[phoneme_key_str].append({
                            'id': word_data[0],
                            'english_words': english_display,
                            'new_language_word': word_data[2] or 'Unnamed',
                            'ipa_phonetics': word_data[3] or ''
                        })

                    phonemes_in_use.append({
                        'phoneme': phoneme,
                        'position': position,
                        'length_type': length_type,
                        'group_type': group_type,
                        'subgroup_type': subgroup_type,
                        'usage_count': len(words_using_phoneme),
                        'phoneme_key': phoneme_key_str
                    })

        # If phonemes are in use and not forced, return conflict info with word details
        if phonemes_in_use and not force_apply:
            replacement_options = {}

            # Get all available phonemes from the template for each position
            template_phonemes_by_position = {}
            for template_phoneme_key, template_p_data in template_phonemes_dict.items():
                position = template_p_data.get('position')
                if position not in template_phonemes_by_position:
                    template_phonemes_by_position[position] = []

            # Fetch replacement options for each phoneme in use
            for item_in_use in phonemes_in_use:
                position = item_in_use['position']

                # Get all phonemes from the template that match this position
                available_replacements = []
                for template_p_key, template_p_data in template_phonemes_dict.items():
                    if template_p_data.get('position') == position:
                        available_replacements.append({
                            'phoneme': template_p_data.get('phoneme'),
                            'group_type': template_p_data.get('group_type'),
                            'subgroup_type': template_p_data.get('subgroup_type'),
                            'length_type': template_p_data.get('length_type')
                        })
                replacement_options[item_in_use['phoneme_key']] = available_replacements


            conn.close()
            return jsonify({
                'success': False,
                'error': 'phonemes_in_use',
                'phonemes_in_use': phonemes_in_use,
                'phoneme_word_details': phoneme_word_details,
                'replacement_options': replacement_options,
                'phonemes_to_remove_count': len(phonemes_to_remove),
                'phonemes_to_add_count': len(phonemes_to_add),
                'phonemes_in_common_count': len(phonemes_in_common),
                'template_name': template_name,
                'message': f'{len(phonemes_in_use)} phonemes from the current set are used in words and would be removed by this template.'
            })

        # Apply the template with phoneme handling
        words_updated = 0
        words_with_orphaned_phonemes = 0

        if phoneme_handling and force_apply:
            # Handle phoneme conflicts based on user choices
            pass

        # Clear existing phonemes and insert template phonemes
        cursor.execute("DELETE FROM phonemes")

        preserved_count = 0
        new_count = 0

        for template_p_data in template_data['phonemes']:
            frequency = template_p_data.get('frequency', 0)
            new_count += 1

            cursor.execute("""
                INSERT INTO phonemes (syllable_type, position, length_type, group_type, subgroup_type,
                                    phoneme, frequency, sub_subgroup_type, sub_sub_subgroup_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                template_p_data.get('syllable_type'),
                template_p_data.get('position'),
                template_p_data.get('length_type'),
                template_p_data.get('group_type'),
                template_p_data.get('subgroup_type'),
                template_p_data.get('phoneme'),
                frequency,
                template_p_data.get('sub_subgroup_type'),
                template_p_data.get('sub_sub_subgroup_type')
            ))

        conn.commit()
        conn.close()

        applied_msg = f'Template "{template_name}" applied successfully!'
        if new_count > 0:
            applied_msg += f' Added {new_count} phonemes.'

        return jsonify({
            'success': True,
            'message': applied_msg,
            'statistics': {
                'phonemes_added': new_count,
                'phonemes_removed': len(phonemes_to_remove),
                'phonemes_preserved': preserved_count
            }
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/admin/download-template/<int:template_id>')
@require_project_admin
def api_admin_download_template(template_id):
    """API endpoint to download a phoneme template as JSON file"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT name, template_data FROM phoneme_templates WHERE id = ?", (template_id,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            return jsonify({'success': False, 'error': 'Template not found'}), 404

        template_name, template_data = result

        response = Response(
            template_data,
            mimetype='application/json',
            headers={'Content-Disposition': f'attachment; filename="{template_name.replace(" ", "_")}.json"'}
        )
        return response

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@l5_bp.route('/api/admin/import-template', methods=['POST'])
@require_project_admin
def api_admin_import_template():
    """API endpoint to import a phoneme template from JSON file or by template_id"""
    try:
        request_data = request.get_json()
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # Check if importing by template_id
        if 'template_id' in request_data:
            template_id = request_data['template_id']

            # Get template data from database
            cursor.execute("""
                SELECT name, description, template_data FROM phoneme_templates
                WHERE id = ?
            """, (template_id,))

            result = cursor.fetchone()
            if not result:
                return jsonify({'success': False, 'error': 'Template not found'})

            template_name, template_description, template_data_json = result
            template_data = json.loads(template_data_json)
        else:
            # Import full template data
            template_data = request_data
            required_keys = ['name', 'phonemes']
            for key in required_keys:
                if key not in template_data:
                    return jsonify({'success': False, 'error': f'Missing required field: {key}'})

            template_name = template_data['name'] + ' (Imported)'
            template_description = template_data.get('description', 'Imported template')

        # Clear existing phonemes
        cursor.execute("DELETE FROM phonemes")

        # Import phonemes from template
        phoneme_count = 0
        for phoneme_data in template_data['phonemes']:
            cursor.execute("""
                INSERT INTO phonemes (syllable_type, position, length_type, group_type,
                                    subgroup_type, sub_subgroup_type, sub_sub_subgroup_type,
                                    phoneme, frequency)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                phoneme_data['syllable_type'],
                phoneme_data['position'],
                phoneme_data['length_type'],
                phoneme_data['group_type'],
                phoneme_data['subgroup_type'],
                phoneme_data['sub_subgroup_type'],
                phoneme_data['sub_sub_subgroup_type'],
                phoneme_data['phoneme'],
                phoneme_data['frequency']
            ))
            phoneme_count += 1

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': f'Template imported successfully! {phoneme_count} phonemes restored.'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/admin/delete-template/<int:template_id>', methods=['DELETE'])
@require_project_admin
def api_admin_delete_template(template_id):
    """API endpoint to delete a phoneme template"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM phoneme_templates WHERE id = ?", (template_id,))
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'success': False, 'error': 'Template not found'})

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Template deleted successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


# =============================================================================
# Cloud Template Routes
# =============================================================================

@l5_bp.route('/api/cloud-templates', methods=['GET'])
def api_get_cloud_templates():
    """Get available cloud phoneme templates"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'})

        # Get templates from Firebase
        templates = firestore_db.get_phoneme_templates(user_id=user_id, include_public=True)

        # Format templates for frontend
        template_list = []
        for template in templates:
            template_list.append({
                'id': template['id'],
                'name': template.get('name', ''),
                'description': template.get('description', ''),
                'language_family': template.get('language_family', ''),
                'phoneme_count': len(template.get('phonemes', [])),
                'created_by': template.get('created_by'),
                'is_public': template.get('is_public', False),
                'is_system_default': template.get('is_system_default', False),
                'created_at': template.get('created_at'),
                'is_mine': template.get('created_by') == user_id
            })

        return jsonify({'success': True, 'templates': template_list})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/cloud-templates', methods=['POST'])
def api_upload_template_to_cloud():
    """Upload current project phonemes as a cloud template"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'})

        data = request.get_json()
        template_name = data.get('name', '').strip()
        description = data.get('description', '').strip()
        language_family = data.get('language_family', '').strip()
        is_public = data.get('is_public', False)

        if not template_name:
            return jsonify({'success': False, 'error': 'Template name is required'})

        # Get current project info
        user_info = get_user_info()
        current_project = user_info.get('current_project')
        if not current_project:
            return jsonify({'success': False, 'error': 'No active project'})

        project_id = current_project['id']

        # Get phonemes from current project
        if clean_firebase_service.is_available() and len(str(project_id)) > 10:  # Firebase project
            phonemes = firestore_db.get_project_phonemes(project_id)

            # Convert Firebase phonemes to template format
            template_phonemes = []
            for phoneme in phonemes:
                template_phonemes.append({
                    'syllable_type': phoneme.get('syllable_type'),
                    'position': phoneme.get('position'),
                    'length_type': phoneme.get('length_type'),
                    'group_type': phoneme.get('group_type'),
                    'subgroup_type': phoneme.get('subgroup_type'),
                    'sub_subgroup_type': phoneme.get('sub_subgroup_type', ''),
                    'sub_sub_subgroup_type': phoneme.get('sub_sub_subgroup_type', ''),
                    'phoneme': phoneme.get('phoneme'),
                    'frequency': 0  # Reset frequencies for template
                })
        else:
            # Local project - get from SQLite
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT syllable_type, position, length_type, group_type,
                       subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, phoneme
                FROM phonemes
                ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
            """)

            phonemes = cursor.fetchall()
            conn.close()

            template_phonemes = []
            for phoneme in phonemes:
                template_phonemes.append({
                    'syllable_type': phoneme[0],
                    'position': phoneme[1],
                    'length_type': phoneme[2],
                    'group_type': phoneme[3],
                    'subgroup_type': phoneme[4],
                    'sub_subgroup_type': phoneme[5] or '',
                    'sub_sub_subgroup_type': phoneme[6] or '',
                    'phoneme': phoneme[7],
                    'frequency': 0  # Reset frequencies for template
                })

        if not template_phonemes:
            return jsonify({'success': False, 'error': 'No phonemes found in current project'})

        # Create template data
        template_data = {
            'name': template_name,
            'description': description,
            'language_family': language_family,
            'phonemes': template_phonemes,
            'created_by': user_id,
            'is_public': is_public,
            'is_system_default': False
        }

        # Upload to Firebase
        template_id = firestore_db.create_phoneme_template(template_data)

        if template_id:
            return jsonify({
                'success': True,
                'message': f'Template "{template_name}" uploaded to cloud successfully!',
                'template_id': template_id
            })
        else:
            return jsonify({'success': False, 'error': 'Failed to upload template to cloud'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/cloud-templates/<template_id>/download', methods=['POST'])
def api_download_cloud_template(template_id):
    """Download and apply a cloud template to current project"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'})

        data = request.get_json() or {}
        target_storage = data.get('target_storage', 'current')  # 'current', 'local', or 'firebase'

        # Get current project info
        user_info = get_user_info()
        current_project = user_info.get('current_project')
        if not current_project:
            return jsonify({'success': False, 'error': 'No active project'})

        project_id = current_project['id']

        # Get template from Firebase
        template = firestore_db.get_phoneme_template(template_id)
        if not template:
            return jsonify({'success': False, 'error': 'Template not found'})

        template_phonemes = template.get('phonemes', [])
        if not template_phonemes:
            return jsonify({'success': False, 'error': 'Template has no phonemes'})

        # Apply to current project based on storage type
        if target_storage == 'current' or target_storage == 'firebase':
            if firestore_db.is_available() and len(str(project_id)) > 10:  # Firebase project
                # Clear existing phonemes for this project
                existing_phonemes = firestore_db.get_project_phonemes(project_id)
                for phoneme in existing_phonemes:
                    firestore_db.delete_phoneme(phoneme['id'])

                # Apply template to Firebase project
                success = firestore_db.initialize_project_phonemes_from_template(project_id, template_id, user_id)

                if success:
                    return jsonify({
                        'success': True,
                        'message': f'Template "{template["name"]}" applied to Firebase project successfully!'
                    })
                else:
                    return jsonify({'success': False, 'error': 'Failed to apply template to Firebase project'})

            elif target_storage == 'current':  # Local project
                # Apply to local SQLite database
                conn = sqlite3.connect(main.DB_NAME)
                cursor = conn.cursor()

                # Clear existing phonemes
                cursor.execute("DELETE FROM phonemes")

                # Apply template phonemes
                for phoneme_data in template_phonemes:
                    cursor.execute("""
                        INSERT INTO phonemes (syllable_type, position, length_type, group_type,
                                              subgroup_type, sub_subgroup_type, sub_sub_subgroup_type, phoneme, frequency)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        phoneme_data.get('syllable_type'),
                        phoneme_data.get('position'),
                        phoneme_data.get('length_type'),
                        phoneme_data.get('group_type'),
                        phoneme_data.get('subgroup_type'),
                        phoneme_data.get('sub_subgroup_type', ''),
                        phoneme_data.get('sub_sub_subgroup_type', ''),
                        phoneme_data.get('phoneme'),
                        phoneme_data.get('frequency', 0)
                    ))

                conn.commit()
                conn.close()

                return jsonify({
                    'success': True,
                    'message': f'Template "{template["name"]}" applied to local project successfully!'
                })

        elif target_storage == 'local':
            # Force apply to local SQLite regardless of current project type
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()

            # Create local template
            template_data = {
                'name': template['name'],
                'description': template.get('description', ''),
                'export_date': datetime.now().isoformat(),
                'phonemes': template_phonemes
            }

            cursor.execute("""
                INSERT INTO phoneme_templates (name, description, template_data, phoneme_count)
                VALUES (?, ?, ?, ?)
            """, (
                template['name'] + ' (Downloaded)',
                template.get('description', '') + ' (Downloaded from cloud)',
                json.dumps(template_data),
                len(template_phonemes)
            ))

            conn.commit()
            conn.close()

            return jsonify({
                'success': True,
                'message': f'Template "{template["name"]}" downloaded and saved locally!'
            })

        return jsonify({'success': False, 'error': 'Invalid target storage type'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@l5_bp.route('/api/cloud-templates/<template_id>', methods=['DELETE'])
def api_delete_cloud_template(template_id):
    """Delete a cloud template (only if owned by user)"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'})

        # Get template to check ownership
        template = firestore_db.get_phoneme_template(template_id)
        if not template:
            return jsonify({'success': False, 'error': 'Template not found'})

        if template.get('created_by') != user_id:
            return jsonify({'success': False, 'error': 'You can only delete templates you created'})

        # Delete template
        success = firestore_db.delete_phoneme_template(template_id)

        if success:
            return jsonify({
                'success': True,
                'message': f'Template "{template["name"]}" deleted successfully!'
            })
        else:
            return jsonify({'success': False, 'error': 'Failed to delete template'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


# =============================================================================
# Phoneme Templates (Firebase-backed)
# =============================================================================

@l5_bp.route('/api/phoneme-templates')
@require_auth
def api_get_phoneme_templates():
    """Get available phoneme templates"""
    try:
        if not clean_firebase_service.is_available():
            return jsonify({
                'success': False,
                'error': 'Firebase service not available',
                'templates': []
            })

        user = get_user_info()
        templates = firestore_db.get_phoneme_templates(user['id'], include_public=True)

        return jsonify({
            'success': True,
            'templates': templates
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'templates': []
        })


@l5_bp.route('/api/phoneme-templates', methods=['POST'])
@require_auth
def api_create_phoneme_template():
    """Create a new phoneme template from current SQLite phonemes"""
    try:
        if not clean_firebase_service.is_available():
            return jsonify({
                'success': False,
                'error': 'Firebase service not available'
            })

        user = get_user_info()
        data = request.get_json()

        # Get current SQLite phonemes
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type,
                   subgroup_type, sub_subgroup_type, sub_sub_subgroup_type,
                   phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, phoneme
        """)
        phonemes_data = cursor.fetchall()
        conn.close()

        # Convert to template format
        phonemes_list = []
        for phoneme_row in phonemes_data:
            phonemes_list.append({
                'syllable_type': phoneme_row[0],
                'position': phoneme_row[1],
                'length_type': phoneme_row[2],
                'group_type': phoneme_row[3],
                'subgroup_type': phoneme_row[4],
                'sub_subgroup_type': phoneme_row[5],
                'sub_sub_subgroup_type': phoneme_row[6],
                'phoneme': phoneme_row[7],
                'frequency': phoneme_row[8]
            })

        template_data = {
            'name': data.get('name', 'Unnamed Template'),
            'description': data.get('description', ''),
            'language_family': data.get('language_family', ''),
            'phonemes': phonemes_list,
            'created_by': user['id'],
            'is_public': data.get('is_public', False)
        }

        template_id = firestore_db.create_phoneme_template(template_data)
        if template_id:
            return jsonify({
                'success': True,
                'template_id': template_id,
                'message': f'Template "{template_data["name"]}" created successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to create template'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })


@l5_bp.route('/api/phoneme-templates/<template_id>', methods=['DELETE'])
@require_auth
def api_delete_phoneme_template(template_id):
    """Delete a phoneme template"""
    try:
        if not clean_firebase_service.is_available():
            return jsonify({
                'success': False,
                'error': 'Firebase service not available'
            })

        user = get_user_info()

        # Check if user owns the template
        template = firestore_db.get_phoneme_template(template_id)
        if not template:
            return jsonify({
                'success': False,
                'error': 'Template not found'
            })

        if template.get('created_by') != user['id']:
            return jsonify({
                'success': False,
                'error': 'Access denied. You can only delete your own templates.'
            })

        success = firestore_db.delete_phoneme_template(template_id)
        if success:
            return jsonify({
                'success': True,
                'message': 'Template deleted successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to delete template'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })
