# resource_id: "e1e81730-f87d-422e-9b75-de47538b72e5"
# resource_type: "document"
# resource_name: "phoneme_management"
"""
Admin Phoneme Management Module

Handles phoneme CRUD operations, frequency management, and usage tracking.
Agents can work on phoneme management without affecting other sub-modules.
"""

from flask import render_template, request, jsonify
import sqlite3
import json
import os

from core.database import get_db_connection, DB_NAME
from core.decorators import require_project_admin
from features.auth import get_user_info
from services.firebase import clean_firebase_service, firestore_db
import main
from . import admin_bp


@admin_bp.route('/admin/phonemes')
@require_project_admin
def admin_phonemes():
    """
    Admin phoneme management interface.

    Returns:
        Rendered phoneme management template
    """
    return render_template('admin_phonemes.html')


@admin_bp.route('/api/admin/phonemes')
@require_project_admin
def api_admin_phonemes():
    """
    API endpoint to get all phonemes for admin management.

    Returns:
        JSON response with all phonemes
    """
    try:
        user = get_user_info()
        current = user.get('current_project') or {}
        storage_type = (current.get('storage_type') or 'local').lower()

        if storage_type == 'cloud' and clean_firebase_service.is_available():
            project_id = current.get('cloud_project_id') or current.get('id')
            items = firestore_db.get_project_phonemes(str(project_id))
            phonemes_list = []
            for it in items:
                phonemes_list.append({
                    'id': it.get('id'),
                    'syllable_type': it.get('syllable_type'),
                    'position': it.get('position'),
                    'length_type': it.get('length_type'),
                    'group_type': it.get('group_type'),
                    'subgroup_type': it.get('subgroup_type'),
                    'phoneme': it.get('phoneme'),
                    'frequency': it.get('frequency', 0),
                })
            return jsonify({'success': True, 'phonemes': phonemes_list})

        # Local SQLite fallback
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        project_id = current.get('local_project_id') or current.get('id')
        cursor.execute("""
            SELECT id, syllable_type, position, length_type, group_type,
                   subgroup_type, phoneme, frequency
            FROM phonemes
            WHERE project_id = ?
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
        """, (project_id,))

        phonemes = cursor.fetchall()
        conn.close()

        phonemes_list = []
        for phoneme in phonemes:
            phonemes_list.append({
                'id': phoneme[0],
                'syllable_type': phoneme[1],
                'position': phoneme[2],
                'length_type': phoneme[3],
                'group_type': phoneme[4],
                'subgroup_type': phoneme[5],
                'phoneme': phoneme[6],
                'frequency': phoneme[7]
            })

        return jsonify({'success': True, 'phonemes': phonemes_list})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/admin/add-phoneme', methods=['POST'])
@require_project_admin
def api_admin_add_phoneme():
    """
    API endpoint to add a new phoneme.

    Request JSON:
        syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency

    Returns:
        JSON response with success status
    """
    try:
        data = request.get_json()
        user = get_user_info()
        current = user.get('current_project') or {}
        storage_type = (current.get('storage_type') or 'local').lower()
        owner_id = user.get('id')

        if storage_type == 'cloud' and clean_firebase_service.is_available():
            project_id = current.get('cloud_project_id') or current.get('id')
            created = firestore_db.create_phoneme({
                'phoneme': data.get('phoneme'),
                'language': 'en',
                'frequency': int(data.get('frequency', 0) or 0),
                'syllable_type': data.get('syllable_type'),
                'position': data.get('position'),
                'length_type': data.get('length_type'),
                'group_type': data.get('group_type'),
                'subgroup_type': data.get('subgroup_type'),
                'user_id': owner_id,
                'project_id': str(project_id),
            })
            if created:
                return jsonify({'success': True, 'message': 'Phoneme added successfully!'})
            return jsonify({'success': False, 'error': 'Failed to add phoneme to cloud project'})

        # Local SQLite fallback
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        project_id = current.get('local_project_id') or current.get('id')

        cursor.execute("""
            INSERT INTO phonemes (project_id, user_id, syllable_type, position, length_type, group_type,
                                subgroup_type, phoneme, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            project_id,
            owner_id,
            data.get('syllable_type'),
            data.get('position'),
            data.get('length_type'),
            data.get('group_type'),
            data.get('subgroup_type'),
            data.get('phoneme'),
            int(data.get('frequency', 0) or 0)
        ))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Phoneme added successfully!'})

    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'error': 'Phoneme already exists'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/admin/update-phoneme-frequency', methods=['POST'])
@require_project_admin
def api_admin_update_phoneme_frequency():
    """
    API endpoint to update phoneme frequency.

    Request JSON:
        id: Phoneme ID
        increment: Amount to change (positive or negative)

    Returns:
        JSON response with success status
    """
    try:
        data = request.get_json()
        phoneme_id = data.get('id')
        increment = int(data.get('increment', 1) or 1)

        user = get_user_info()
        current = user.get('current_project') or {}
        storage_type = (current.get('storage_type') or 'local').lower()

        if storage_type == 'cloud' and clean_firebase_service.is_available():
            # Fetch current value then update
            doc = firestore_db._service.get_document(firestore_db.PHONEMES_COLLECTION, phoneme_id)  # type: ignore[attr-defined]
            if not doc:
                return jsonify({'success': False, 'error': 'Phoneme not found'})
            new_freq = max(0, int(doc.get('frequency', 0) or 0) + increment)
            ok = firestore_db.update_phoneme(phoneme_id, {'frequency': new_freq})
            if not ok:
                return jsonify({'success': False, 'error': 'Failed to update frequency'})
            action = "increased" if increment > 0 else "decreased"
            return jsonify({'success': True, 'message': f'Phoneme frequency {action} successfully!'})

        # Local SQLite fallback
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE phonemes SET frequency = MAX(0, frequency + ?)
            WHERE id = ?
        """, (increment, phoneme_id))

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'success': False, 'error': 'Cannot reduce frequency below 0 or phoneme not found'})

        conn.commit()
        conn.close()

        action = "increased" if increment > 0 else "decreased"
        return jsonify({'success': True, 'message': f'Phoneme frequency {action} successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/admin/phoneme-usage/<int:phoneme_id>')
@require_project_admin
def api_admin_phoneme_usage(phoneme_id):
    """
    API endpoint to get words that use a specific phoneme.

    Args:
        phoneme_id: ID of phoneme to check

    Returns:
        JSON response with phoneme details, words using it, and replacement options
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get phoneme details
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type,
                   subgroup_type, phoneme, frequency
            FROM phonemes WHERE id = ?
        """, (phoneme_id,))

        phoneme_data = cursor.fetchone()
        if not phoneme_data:
            conn.close()
            return jsonify({'success': False, 'error': 'Phoneme not found'})

        syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency = phoneme_data

        # Find words using this phoneme
        cursor.execute("""
            SELECT id, language, english_words, new_language_word, ipa_phonetics,
                   dictionary_phonetics, syllable_type, onset_phoneme, onset_length_type,
                   nucleus_phoneme, nucleus_length_type, coda_phoneme, coda_length_type,
                   video_path, project_id
            FROM words
            WHERE (onset_phoneme = ? AND onset_length_type = ?)
               OR (nucleus_phoneme = ? AND nucleus_length_type = ?)
               OR (coda_phoneme = ? AND coda_length_type = ?)
            ORDER BY id DESC
        """, (phoneme, length_type, phoneme, length_type, phoneme, length_type))

        words_data = cursor.fetchall()

        # Get available replacement phonemes for this position
        cursor.execute("""
            SELECT phoneme, group_type, subgroup_type, length_type
            FROM phonemes
            WHERE syllable_type = ? AND position = ? AND id != ?
            ORDER BY length_type, group_type, subgroup_type, phoneme
        """, (syllable_type, position, phoneme_id))

        replacement_options = []
        for replacement_data in cursor.fetchall():
            replacement_options.append({
                'phoneme': replacement_data[0],
                'group_type': replacement_data[1],
                'subgroup_type': replacement_data[2],
                'length_type': replacement_data[3]
            })

        conn.close()

        # Convert words to list of dictionaries
        words_list = []
        for word in words_data:
            positions_used = []
            if word[7] == phoneme and word[8] == length_type:  # onset
                positions_used.append('onset')
            if word[9] == phoneme and word[10] == length_type:  # nucleus
                positions_used.append('nucleus')
            if word[11] == phoneme and word[12] == length_type:  # coda
                positions_used.append('coda')

            # Parse english_words JSON safely
            try:
                english_words_data = json.loads(word[2]) if word[2] else []
                if isinstance(english_words_data, list):
                    english_display = ', '.join(english_words_data)
                else:
                    english_display = str(word[2])
            except (json.JSONDecodeError, TypeError):
                english_display = word[2] or 'No translation'

            words_list.append({
                'id': word[0],
                'language': word[1] or 'Constructed Language',
                'english_words': english_display,
                'new_language_word': word[3] or 'Unnamed',
                'ipa_phonetics': word[4] or '',
                'dictionary_phonetics': word[5] or '',
                'syllable_type': word[6] or '',
                'video_path': word[13],
                'project_id': word[14],
                'positions_used': positions_used
            })

        return jsonify({
            'success': True,
            'phoneme': {
                'id': phoneme_id,
                'syllable_type': syllable_type,
                'position': position,
                'length_type': length_type,
                'group_type': group_type,
                'subgroup_type': subgroup_type,
                'phoneme': phoneme,
                'frequency': frequency
            },
            'words': words_list,
            'replacement_options': replacement_options,
            'count': len(words_list)
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/admin/delete-phoneme/<int:phoneme_id>', methods=['DELETE'])
@require_project_admin
def api_admin_delete_phoneme(phoneme_id):
    """
    API endpoint to delete a phoneme with conflict resolution.

    Request JSON:
        force_delete: Boolean to skip conflict check
        phoneme_handling: Dict of handling strategies for conflicts

    Args:
        phoneme_id: ID of phoneme to delete

    Returns:
        JSON response with success status or conflict details
    """
    try:
        data = request.get_json() or {}
        force_delete = data.get('force_delete', False)
        phoneme_handling = data.get('phoneme_handling', {})

        user = get_user_info()
        current = user.get('current_project') or {}
        storage_type = (current.get('storage_type') or 'local').lower()

        if storage_type == 'cloud' and clean_firebase_service.is_available():
            # For cloud, compute usage to warn, but allow force delete
            # Build minimal usage report
            proj_id = current.get('cloud_project_id') or current.get('id')
            ph_doc = firestore_db._service.get_document(firestore_db.PHONEMES_COLLECTION, phoneme_id)  # type: ignore[attr-defined]
            if not ph_doc:
                return jsonify({'success': False, 'error': 'Phoneme not found'})

            words = firestore_db.get_project_words(str(proj_id))
            position = ph_doc.get('position')
            length_type = ph_doc.get('length_type')
            symbol = ph_doc.get('phoneme')
            words_using = []
            for w in words:
                if (position == 'onset' and w.get('onset_phoneme') == symbol and w.get('onset_length_type') == length_type) or \
                   (position == 'nucleus' and w.get('nucleus_phoneme') == symbol and w.get('nucleus_length_type') == length_type) or \
                   (position == 'coda' and w.get('coda_phoneme') == symbol and w.get('coda_length_type') == length_type):
                    words_using.append({'id': w.get('id'), 'new_language_word': w.get('new_language_word', ''), 'ipa_phonetics': w.get('ipa_phonetics', '')})

            if words_using and not force_delete:
                return jsonify({
                    'success': False,
                    'error': 'phoneme_in_use',
                    'phoneme_info': {
                        'id': phoneme_id,
                        'phoneme': symbol,
                        'syllable_type': ph_doc.get('syllable_type'),
                        'position': position,
                        'length_type': length_type,
                        'group_type': ph_doc.get('group_type'),
                        'subgroup_type': ph_doc.get('subgroup_type'),
                        'frequency': ph_doc.get('frequency', 0)
                    },
                    'words_using_phoneme': words_using,
                    'replacement_options': [],
                    'words_count': len(words_using),
                })

            ok = firestore_db.delete_phoneme(phoneme_id)
            if not ok:
                return jsonify({'success': False, 'error': 'Failed to delete phoneme'})
            return jsonify({'success': True, 'message': f'Phoneme "{symbol}" deleted successfully!'})

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get phoneme details before deletion
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type,
                   subgroup_type, phoneme, frequency
            FROM phonemes WHERE id = ?
        """, (phoneme_id,))

        phoneme_data = cursor.fetchone()
        if not phoneme_data:
            conn.close()
            return jsonify({'success': False, 'error': 'Phoneme not found'})

        syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency = phoneme_data

        # Check if phoneme is used in any words
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

        # If phoneme is in use and not forced, return conflict info
        if words_using_phoneme and not force_delete:
            # Get available replacement phonemes
            cursor.execute("""
                SELECT phoneme, group_type, subgroup_type, length_type
                FROM phonemes
                WHERE syllable_type = ? AND position = ? AND id != ?
                ORDER BY length_type, group_type, subgroup_type, phoneme
            """, (syllable_type, position, phoneme_id))

            replacement_options = []
            for replacement_data in cursor.fetchall():
                replacement_options.append({
                    'phoneme': replacement_data[0] or '',
                    'group_type': replacement_data[1] or 'Other',
                    'subgroup_type': replacement_data[2] or 'none',
                    'length_type': replacement_data[3] or 'unknown'
                })

            # Format word details
            phoneme_word_details = []
            for word_data in words_using_phoneme:
                try:
                    english_words_data = json.loads(word_data[1]) if word_data[1] else []
                    if isinstance(english_words_data, list):
                        english_display = ', '.join(english_words_data)
                    else:
                        english_display = str(word_data[1])
                except (json.JSONDecodeError, TypeError):
                    english_display = word_data[1] or 'No translation'

                phoneme_word_details.append({
                    'id': word_data[0],
                    'english_words': english_display,
                    'new_language_word': word_data[2] or 'Unnamed',
                    'ipa_phonetics': word_data[3] or ''
                })

            conn.close()
            return jsonify({
                'success': False,
                'error': 'phoneme_in_use',
                'phoneme_info': {
                    'id': phoneme_id,
                    'phoneme': phoneme,
                    'syllable_type': syllable_type,
                    'position': position,
                    'length_type': length_type,
                    'group_type': group_type,
                    'subgroup_type': subgroup_type,
                    'frequency': frequency
                },
                'words_using_phoneme': phoneme_word_details,
                'replacement_options': replacement_options,
                'words_count': len(words_using_phoneme),
                'message': f'Phoneme "{phoneme}" is used in {len(words_using_phoneme)} word(s). Choose how to handle the conflicts.'
            })

        # Delete the phoneme
        cursor.execute("DELETE FROM phonemes WHERE id = ?", (phoneme_id,))

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'success': False, 'error': 'Phoneme not found'})

        conn.commit()
        conn.close()

        return jsonify({
            'success': True,
            'message': f'Phoneme "{phoneme}" deleted successfully!'
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@admin_bp.route('/api/admin/delete-unused-phonemes', methods=['POST'])
@require_project_admin
def api_admin_delete_unused_phonemes():
    """
    API endpoint to delete all phonemes with frequency 0.

    Returns:
        JSON response with count of deleted phonemes
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        user = get_user_info()
        current = user.get('current_project') or {}
        storage_type = (current.get('storage_type') or 'local').lower()

        if storage_type == 'cloud' and clean_firebase_service.is_available():
            proj_id = current.get('cloud_project_id') or current.get('id')
            items = firestore_db.get_project_phonemes(str(proj_id))
            to_delete = [it for it in items if int(it.get('frequency', 0) or 0) == 0]
            deleted = 0
            for it in to_delete:
                if it.get('id') and firestore_db.delete_phoneme(it['id']):
                    deleted += 1
            return jsonify({'success': True, 'message': f'Successfully deleted {deleted} unused phonemes!', 'deleted_count': deleted})

        # Local SQLite
        project_id = current.get('local_project_id') or current.get('id')
        # Count how many will be deleted
        cursor.execute("SELECT COUNT(*) FROM phonemes WHERE project_id = ? AND frequency = 0", (project_id,))
        count_to_delete = cursor.fetchone()[0]

        # Delete unused phonemes
        cursor.execute("DELETE FROM phonemes WHERE project_id = ? AND frequency = 0", (project_id,))

        conn.commit()
        conn.close()

        return jsonify({
            'success': True,
            'message': f'Successfully deleted {count_to_delete} unused phonemes!',
            'deleted_count': count_to_delete
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


__all__ = [
    'admin_phonemes',
    'api_admin_phonemes',
    'api_admin_add_phoneme',
    'api_admin_update_phoneme_frequency',
    'api_admin_phoneme_usage',
    'api_admin_delete_phoneme',
    'api_admin_delete_unused_phonemes'
]
