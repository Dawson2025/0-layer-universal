"""
L4 Phoneme System Routes

Extracted from monolithic app.py — all phoneme-related routes:
- /phonemes (menu)
- /phonemes/nested, /phonemes/full (display)
- /admin, /admin/phonemes (admin landing)
- /api/admin/phonemes*, add-phoneme, update-phoneme-frequency, recalculate, usage, delete, bulk-delete-words, delete-unused
- /api/phonemes/check-single
"""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, session
import sqlite3
import json
import os
from collections import defaultdict

import main
from l2_infrastructure.auth import require_auth, require_project_admin
from l3_users.sessions.session import get_user_info
from l2_infrastructure.firebase import clean_firebase_service, firestore_db
from l2_infrastructure.storage import storage_manager, StorageType
from l2_infrastructure.tts import ipa_tts

l4_bp = Blueprint('l4_phoneme_system', __name__)


# ── Display Routes ──────────────────────────────────────────────────────────

@l4_bp.route('/phonemes')
def phonemes_menu():
    """Phoneme viewing options menu"""
    return render_template('phonemes_menu.html')


@l4_bp.route('/phonemes/nested')
@require_auth
def display_nested():
    """Display phonemes in nested hierarchy (Terminal function: display_nested_phonemes)"""
    try:
        # Check if we're in a project context
        if 'current_project_id' not in session:
            flash('Please enter a project to view phonemes', 'error')
            return redirect(url_for('dashboard'))

        project_id = session['current_project_id']
        phonemes_data = []

        # For Firebase projects, get phonemes from Firestore
        # (Only when the project_id is a non-numeric string identifier.)
        if clean_firebase_service.is_available() and isinstance(project_id, str) and not project_id.isdigit():
            try:
                firebase_project = firestore_db.get_project(project_id)
                if firebase_project:
                    # Get all phonemes for this project
                    firebase_phonemes = firestore_db.get_project_phonemes(project_id)

                    # Convert to tuple format expected by the rest of the function
                    phonemes_data = []
                    for phoneme_doc in firebase_phonemes:
                        phonemes_data.append((
                            phoneme_doc.get('syllable_type', ''),
                            phoneme_doc.get('position', ''),
                            phoneme_doc.get('length_type', ''),
                            phoneme_doc.get('group_type', ''),
                            phoneme_doc.get('subgroup_type', ''),
                            phoneme_doc.get('phoneme', ''),
                            phoneme_doc.get('frequency', 0)
                        ))

                    # Sort phonemes
                    phonemes_data.sort(key=lambda p: (p[0], p[1], p[2], p[3], p[4], p[5]))

                else:
                    # Not a Firebase project, fallback to SQLite
                    conn = sqlite3.connect(main.DB_NAME)
                    cursor = conn.cursor()

                    cursor.execute("""
                        SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                        FROM phonemes
                        ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
                    """)

                    phonemes_data = cursor.fetchall()
                    conn.close()
            except Exception as e:
                print(f"Error getting Firebase phonemes: {e}")
                # Fallback to SQLite
                conn = sqlite3.connect(main.DB_NAME)
                cursor = conn.cursor()

                cursor.execute("""
                    SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                    FROM phonemes
                    ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
                """)

                phonemes_data = cursor.fetchall()
                conn.close()
        else:
            # No Firebase available, use SQLite
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                FROM phonemes
                ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
            """)

            phonemes_data = cursor.fetchall()
            conn.close()

        # Organize data into nested structure
        nested_data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list)))))

        for syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency in phonemes_data:
            nested_data[syllable_type][position][length_type][group_type][subgroup_type].append({
                'phoneme': phoneme,
                'frequency': frequency
            })

        # Convert all nested defaultdicts to regular dicts
        result_data = {}
        for syl_type, syl_data in nested_data.items():
            result_data[syl_type] = {}
            for pos, pos_data in syl_data.items():
                result_data[syl_type][pos] = {}
                for len_type, len_data in pos_data.items():
                    result_data[syl_type][pos][len_type] = {}
                    for grp_type, grp_data in len_data.items():
                        result_data[syl_type][pos][len_type][grp_type] = dict(grp_data)

        return render_template('phonemes_nested.html', nested_data=result_data)
    except Exception as e:
        flash(f'Error displaying nested phonemes: {str(e)}', 'error')
        return redirect(url_for('phonemes_menu'))

@l4_bp.route('/phonemes/full')
@require_auth
def display_full():
    """Display full phoneme hierarchy (Terminal function: display_full)"""
    try:
        # Check if we're in a project context
        if 'current_project_id' not in session:
            flash('Please enter a project to view phonemes', 'error')
            return redirect(url_for('dashboard'))

        project_id = session['current_project_id']
        phonemes_data = []

        # For Firebase projects, get phonemes from Firestore
        # (Only when the project_id is a non-numeric string identifier.)
        if clean_firebase_service.is_available() and isinstance(project_id, str) and not project_id.isdigit():
            try:
                firebase_project = firestore_db.get_project(project_id)
                if firebase_project:
                    # Get all phonemes for this project
                    firebase_phonemes = firestore_db.get_project_phonemes(project_id)

                    # Convert to tuple format expected by the rest of the function
                    phonemes_data = []
                    for phoneme_doc in firebase_phonemes:
                        phonemes_data.append((
                            phoneme_doc.get('syllable_type', ''),
                            phoneme_doc.get('position', ''),
                            phoneme_doc.get('length_type', ''),
                            phoneme_doc.get('group_type', ''),
                            phoneme_doc.get('subgroup_type', ''),
                            phoneme_doc.get('phoneme', ''),
                            phoneme_doc.get('frequency', 0)
                        ))

                    # Sort phonemes (frequency ASC for consistency)
                    phonemes_data.sort(key=lambda p: (p[0], p[1], p[2], p[6], p[3], p[4], p[5]))

                else:
                    # Not a Firebase project, fallback to SQLite
                    conn = sqlite3.connect(main.DB_NAME)
                    cursor = conn.cursor()

                    cursor.execute("""
                        SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                        FROM phonemes
                        ORDER BY syllable_type, position, length_type, frequency ASC, group_type, subgroup_type, phoneme
                    """)

                    phonemes_data = cursor.fetchall()
                    conn.close()
            except Exception as e:
                print(f"Error getting Firebase phonemes: {e}")
                # Fallback to SQLite
                conn = sqlite3.connect(main.DB_NAME)
                cursor = conn.cursor()

                cursor.execute("""
                    SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                    FROM phonemes
                    ORDER BY syllable_type, position, length_type, frequency ASC, group_type, subgroup_type, phoneme
                """)

                phonemes_data = cursor.fetchall()
                conn.close()
        else:
            # No Firebase available, use SQLite
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
                FROM phonemes
                ORDER BY syllable_type, position, length_type, frequency ASC, group_type, subgroup_type, phoneme
            """)

            phonemes_data = cursor.fetchall()
            conn.close()

        # Calculate group frequencies and organize data
        full_data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {'groups': defaultdict(lambda: {'subgroups': defaultdict(list), 'frequency': 0})})))

        for syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency in phonemes_data:
            # Add phoneme to subgroup
            full_data[syllable_type][position][length_type]['groups'][group_type]['subgroups'][subgroup_type].append({
                'phoneme': phoneme,
                'frequency': frequency
            })
            # Update group frequency
            full_data[syllable_type][position][length_type]['groups'][group_type]['frequency'] += frequency

        # Convert all nested defaultdicts to regular dicts
        result_data = {}
        for syl_type, syl_data in full_data.items():
            result_data[syl_type] = {}
            for pos, pos_data in syl_data.items():
                result_data[syl_type][pos] = {}
                for len_type, len_data in pos_data.items():
                    result_data[syl_type][pos][len_type] = {
                        'groups': {}
                    }
                    for grp_type, grp_data in len_data['groups'].items():
                        result_data[syl_type][pos][len_type]['groups'][grp_type] = {
                            'frequency': grp_data['frequency'],
                            'subgroups': dict(grp_data['subgroups'])
                        }

        return render_template('phonemes_full.html', full_data=result_data)
    except Exception as e:
        flash(f'Error displaying full hierarchy: {str(e)}', 'error')
        return redirect(url_for('phonemes_menu'))


# ── Admin Landing Routes ────────────────────────────────────────────────────

@l4_bp.route('/admin')
@require_project_admin
def admin_menu():
    """Admin panel menu (Terminal function: admin_menu)"""
    user = get_user_info()
    return render_template('admin_menu.html', user=user)

@l4_bp.route('/admin/phonemes')
@require_project_admin
def admin_phonemes():
    """Admin phoneme management"""
    return render_template('admin_phonemes.html')


# ── Admin API Routes ────────────────────────────────────────────────────────

@l4_bp.route('/api/admin/phonemes')
@require_project_admin
def api_admin_phonemes():
    """API endpoint to get all phonemes for admin management"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, syllable_type, position, length_type, group_type,
                   subgroup_type, phoneme, frequency
            FROM phonemes
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
        """)

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

@l4_bp.route('/api/admin/add-phoneme', methods=['POST'])
@require_project_admin
def api_admin_add_phoneme():
    """API endpoint to add a new phoneme (Terminal function: add_new_phoneme)"""
    try:
        data = request.get_json()

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO phonemes (syllable_type, position, length_type, group_type,
                                subgroup_type, phoneme, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get('syllable_type'),
            data.get('position'),
            data.get('length_type'),
            data.get('group_type'),
            data.get('subgroup_type'),
            data.get('phoneme'),
            data.get('frequency', 0)
        ))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Phoneme added successfully!'})

    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'error': 'Phoneme already exists'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@l4_bp.route('/api/admin/update-phoneme-frequency', methods=['POST'])
@require_project_admin
def api_admin_update_phoneme_frequency():
    """API endpoint to update phoneme frequency (Terminal functions: increase/decrease_frequency)"""
    try:
        data = request.get_json()
        phoneme_id = data.get('id')
        increment = data.get('increment', 1)

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE phonemes SET frequency = frequency + ?
            WHERE id = ? AND (frequency + ?) >= 0
        """, (increment, phoneme_id, increment))

        if cursor.rowcount == 0:
            return jsonify({'success': False, 'error': 'Cannot reduce frequency below 0 or phoneme not found'})

        conn.commit()
        conn.close()

        action = "increased" if increment > 0 else "decreased"
        return jsonify({'success': True, 'message': f'Phoneme frequency {action} successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@l4_bp.route('/api/admin/recalculate-phoneme-frequencies', methods=['POST'])
@require_project_admin
def api_admin_recalculate_phoneme_frequencies():
    """API endpoint to recalculate all phoneme frequencies based on actual word usage"""
    try:
        project_id = session.get('current_project_id')

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # First, reset all phoneme frequencies to 0
        cursor.execute("UPDATE phonemes SET frequency = 0")

        # Get all words (filtered by project if applicable)
        if project_id:
            cursor.execute("""
                SELECT onset_phoneme, onset_length_type, nucleus_phoneme, nucleus_length_type,
                       coda_phoneme, coda_length_type, syllable_type, syllables_data
                FROM words
                WHERE project_id = ?
            """, (project_id,))
        else:
            cursor.execute("""
                SELECT onset_phoneme, onset_length_type, nucleus_phoneme, nucleus_length_type,
                       coda_phoneme, coda_length_type, syllable_type, syllables_data
                FROM words
            """)

        words = cursor.fetchall()
        total_updates = 0

        # Count phoneme usage from words
        for word_data in words:
            # Safely unpack word data
            if len(word_data) >= 8:
                onset, onset_len, nucleus, nucleus_len, coda, coda_len, syl_type, syllables_data = word_data
            else:
                onset, onset_len, nucleus, nucleus_len, coda, coda_len, syl_type = word_data
                syllables_data = None

            # Handle multi-syllable words
            if syllables_data:
                try:
                    syllables_data = json.loads(syllables_data)
                    for syllable in syllables_data:
                        syl_type_current = syllable.get('syllableType', 'CVC')
                        phonemes = syllable.get('phonemes', {})

                        for position in ['onset', 'nucleus', 'coda']:
                            if position in phonemes:
                                phoneme_info = phonemes[position]
                                phoneme = phoneme_info.get('phoneme')
                                length_type = phoneme_info.get('length_type', '')

                                if phoneme:
                                    cursor.execute("""
                                        UPDATE phonemes
                                        SET frequency = frequency + 1
                                        WHERE syllable_type = ? AND position = ? AND length_type = ? AND phoneme = ?
                                    """, (syl_type_current, position, length_type, phoneme))
                                    total_updates += cursor.rowcount
                except:
                    pass  # If syllables_data parsing fails, fall back to single syllable

            # Handle single-syllable words (backward compatibility)
            if not syllables_data:
                if onset:
                    cursor.execute("""
                        UPDATE phonemes
                        SET frequency = frequency + 1
                        WHERE syllable_type = ? AND position = 'onset' AND length_type = ? AND phoneme = ?
                    """, (syl_type, onset_len, onset))
                    total_updates += cursor.rowcount

                if nucleus:
                    cursor.execute("""
                        UPDATE phonemes
                        SET frequency = frequency + 1
                        WHERE syllable_type = ? AND position = 'nucleus' AND length_type = ? AND phoneme = ?
                    """, (syl_type, nucleus_len, nucleus))
                    total_updates += cursor.rowcount

                if coda:
                    cursor.execute("""
                        UPDATE phonemes
                        SET frequency = frequency + 1
                        WHERE syllable_type = ? AND position = 'coda' AND length_type = ? AND phoneme = ?
                    """, (syl_type, coda_len, coda))
                    total_updates += cursor.rowcount

        conn.commit()
        conn.close()

        message = f'Phoneme frequencies recalculated successfully. Processed {len(words)} words with {total_updates} frequency updates.'
        return jsonify({'success': True, 'message': message, 'words_processed': len(words), 'updates': total_updates})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@l4_bp.route('/api/admin/phoneme-usage/<int:phoneme_id>')
@require_project_admin
def api_admin_phoneme_usage(phoneme_id):
    """API endpoint to get words that use a specific phoneme"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # First, get phoneme details
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

        # Convert to list of dictionaries with position information
        words_list = []
        for word in words_data:
            # Determine which position(s) use this phoneme
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

@l4_bp.route('/api/admin/delete-phoneme/<int:phoneme_id>', methods=['DELETE'])
@require_project_admin
def api_admin_delete_phoneme(phoneme_id):
    """API endpoint to delete a phoneme with conflict resolution similar to template application"""
    try:
        data = request.get_json() or {}
        force_delete = data.get('force_delete', False)
        phoneme_handling = data.get('phoneme_handling', {}) # Stores handling strategy for each conflicting phoneme

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # First, get phoneme details before deletion
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

        # Check if phoneme is used in any words and get detailed information
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
            # Get available replacement phonemes for the same position (any length type) from other phonemes
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
                'replacement_options': replacement_options, # Pass replacement options
                'words_count': len(words_using_phoneme),
                'message': f'Phoneme "{phoneme}" is used in {len(words_using_phoneme)} word(s). Choose how to handle the conflicts.'
            })

        # Handle phoneme conflicts if force_delete is True or no words use it
        words_updated = 0
        words_with_orphaned_phonemes = 0

        if phoneme_handling and force_delete:
            # Handle phoneme conflicts based on user choices
            pass

        # Delete the phoneme from the phonemes table
        cursor.execute("DELETE FROM phonemes WHERE id = ?", (phoneme_id,))

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'success': False, 'error': 'Phoneme not found'})

        conn.commit()
        conn.close()

        # Prepare success message
        success_msg = f'Phoneme "{phoneme}" deleted successfully!'
        if words_updated:
            success_msg += f' Updated {words_updated} words.'
        if words_with_orphaned_phonemes:
            success_msg += f' {words_with_orphaned_phonemes} words kept their original phoneme (orphaned).'

        return jsonify({
            'success': True,
            'message': success_msg,
            'statistics': {
                'words_updated': words_updated,
                'words_with_orphaned_phonemes': words_with_orphaned_phonemes
            }
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@l4_bp.route('/api/admin/bulk-delete-words', methods=['POST'])
@require_project_admin
def api_admin_bulk_delete_words():
    """API endpoint to delete multiple words at once"""
    try:
        data = request.get_json()
        word_ids = data.get('word_ids', [])

        if not word_ids:
            return jsonify({'success': False, 'error': 'No word IDs provided'})

        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        deleted_count = 0
        video_files_to_delete = []

        for word_id in word_ids:
            # Get word data before deletion for frequency updates and video cleanup
            cursor.execute("""
                SELECT syllable_type, onset_phoneme, onset_length_type,
                       nucleus_phoneme, nucleus_length_type,
                       coda_phoneme, coda_length_type, video_path
                FROM words WHERE id = ?
            """, (word_id,))

            word_data = cursor.fetchone()
            if word_data:
                # Delete the word
                cursor.execute("DELETE FROM words WHERE id = ?", (word_id,))
                if cursor.rowcount > 0:
                    deleted_count += 1

                    # Update phoneme frequencies (decrease)
                    syllable_type = word_data[0]
                    positions = [
                        ('onset', word_data[1], word_data[2]),
                        ('nucleus', word_data[3], word_data[4]),
                        ('coda', word_data[5], word_data[6])
                    ]

                    for position, phoneme, length_type in positions:
                        if phoneme:
                            cursor.execute("""
                                UPDATE phonemes SET frequency = frequency - 1
                                WHERE syllable_type = ? AND position = ? AND length_type = ? AND phoneme = ?
                                AND frequency > 0
                            """, (syllable_type, position, length_type, phoneme))

                    # Track video file for deletion
                    if word_data[7]:
                        video_files_to_delete.append(word_data[7])

        # Delete video files
        for video_path in video_files_to_delete:
            if os.path.exists(video_path):
                try:
                    os.remove(video_path)
                except OSError as e:
                    print(f"Error removing video file {video_path} during bulk deletion: {e}")

        conn.commit()
        conn.close()

        return jsonify({
            'success': True,
            'message': f'Successfully deleted {deleted_count} words!',
            'deleted_count': deleted_count
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@l4_bp.route('/api/admin/delete-unused-phonemes', methods=['POST'])
@require_project_admin
def api_admin_delete_unused_phonemes():
    """API endpoint to delete all phonemes with frequency 0"""
    try:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        # First count how many will be deleted
        cursor.execute("SELECT COUNT(*) FROM phonemes WHERE frequency = 0")
        count_to_delete = cursor.fetchone()[0]

        # Delete unused phonemes
        cursor.execute("DELETE FROM phonemes WHERE frequency = 0")

        conn.commit()
        conn.close()

        return jsonify({
            'success': True,
            'message': f'Successfully deleted {count_to_delete} unused phonemes!',
            'deleted_count': count_to_delete
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


# ── Public API Routes ───────────────────────────────────────────────────────

@l4_bp.route('/api/phonemes/check-single', methods=['POST'])
def api_check_single_phoneme():
    """Check if a string represents a single phoneme block in the database"""
    try:
        data = request.get_json()
        phoneme = data.get('phoneme', '').strip()

        if not phoneme:
            return jsonify({'success': False, 'error': 'Phoneme is required'}), 400

        # Check if the phoneme exists in the database as a single phoneme
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) FROM phonemes
            WHERE phoneme = ?
        """, (phoneme,))

        count = cursor.fetchone()[0]
        conn.close()

        is_single_phoneme = count > 0

        return jsonify({
            'success': True,
            'phoneme': phoneme,
            'is_single_phoneme': is_single_phoneme
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
