"""
Word Creation Module

Handles word creation workflows and related helper APIs.
Agents can work on creation improvements without affecting search, display, or editing.
"""

from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
import sqlite3
import os
from collections import defaultdict

from core.database import DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
import main
from . import words_bp
from scripts.legacy.flattened_dataset import flattened_dataset


FALLBACK_PHONEMES = defaultdict(list)
for entry in flattened_dataset:
    key = (
        entry.get("syllable_type"),
        entry.get("position"),
        entry.get("length_type"),
    )
    FALLBACK_PHONEMES[key].append(entry)


def allowed_file(filename):
    """Check if file extension is allowed for uploads."""
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@words_bp.route('/words/create')
def create_word_menu():
    """Word creation method selection page."""
    return render_template('words/word_creation_menu.html')


@words_bp.route('/words/create/table-based')
@require_auth
def create_word_table_based():
    """Table-based word creation interface."""
    user = get_user_info()
    return render_template('words/word_creation_table.html', user=user)


# Helper API endpoints for word creation
@words_bp.route('/api/languages')
@require_auth
def get_languages():
    """
    Get list of existing languages for the current user/project.

    Used to populate language dropdown in word creation forms.
    """
    try:
        user = get_user_info()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM phonemes")
        total_phonemes = cursor.fetchone()[0] or 0
        if total_phonemes == 0:
            conn.close()
            main.insert_sample_data()
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

        # Get languages for the current project if one is selected
        current_project = user.get('current_project')
        if current_project:
            # All participants in a shared project can see all languages in that project
            cursor.execute("""
                SELECT DISTINCT language
                FROM words
                WHERE language IS NOT NULL AND language != ''
                AND project_id = ?
                ORDER BY language
            """, (current_project['id'],))
        else:
            # Get all languages for the user, including legacy words
            cursor.execute("""
                SELECT DISTINCT language
                FROM words
                WHERE language IS NOT NULL AND language != ''
                AND (user_id = ? OR (user_id IS NULL AND project_id IS NULL))
                ORDER BY language
            """, (user['id'],))

        languages = [row[0] for row in cursor.fetchall()]
        conn.close()

        return jsonify({
            'success': True,
            'languages': languages
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error loading languages: {str(e)}'
        })


@words_bp.route('/api/last-language')
@require_auth
def get_last_language():
    """
    Get the last used language for the current user/project.

    Used to pre-populate language field in creation forms.
    """
    try:
        user = get_user_info()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get the most recently used language for the current project
        current_project = user.get('current_project')
        if current_project:
            # All participants in a shared project can see the most recent language from all words
            cursor.execute("""
                SELECT language
                FROM words
                WHERE language IS NOT NULL AND language != ''
                AND project_id = ?
                ORDER BY id DESC
                LIMIT 1
            """, (current_project['id'],))
        else:
            # Get the most recently used language for the user, including legacy words
            cursor.execute("""
                SELECT language
                FROM words
                WHERE language IS NOT NULL AND language != ''
                AND (user_id = ? OR (user_id IS NULL AND project_id IS NULL))
                ORDER BY id DESC
                LIMIT 1
            """, (user['id'],))

        result = cursor.fetchone()
        last_language = result[0] if result else 'Constructed Language'
        conn.close()

        return jsonify({
            'success': True,
            'last_language': last_language
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error loading last language: {str(e)}',
            'last_language': 'Constructed Language'
        })


@words_bp.route('/api/phoneme-tables')
def get_phoneme_tables():
    """
    Get phoneme tables for word creation interface.

    Returns organized phoneme data based on syllable type and position filters.
    """
    try:
        syllable_type = request.args.get('syllable_type', 'CVC')
        positions = request.args.get('positions', 'onset,nucleus,coda').split(',')

        # Define length types for each position
        length_types = {
            "onset": ["single_consonants", "cluster2", "cluster3"],
            "nucleus": ["monophthongs", "diphthongs"],
            "coda": ["single_consonants", "cluster2", "cluster3"]
        }

        # Get filters from request or use defaults
        filters = {}
        for position in positions:
            filter_key = f"{position}_filter"

            # Set appropriate defaults based on position
            if position == 'nucleus':
                default_filter = 'monophthongs'
            else:  # onset or coda
                default_filter = 'single_consonants'

            filters[position] = request.args.get(filter_key, default_filter)

        # Determine available columns for optional subgroup metadata
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(phonemes)")
        column_names = {row[1] for row in cursor.fetchall()}
        if not column_names:
            cursor.execute("PRAGMA table_info(phonemes)")
            column_names = {row[1] for row in cursor.fetchall()}
        has_sub_subgroup = 'sub_subgroup_type' in column_names
        has_sub_sub_subgroup = 'sub_sub_subgroup_type' in column_names

        tables_data = {}
        available_options = {}

        for position in positions:
            # Initialize position data
            tables_data[position] = []
            available_options[position] = {
                'length_types': length_types.get(position, []),
                'phonemes_by_length': {}
            }

            # Get phonemes for this position and current filter
            select_fields = [
                "id AS number",
                "phoneme",
                "length_type",
                "group_type",
                "subgroup_type",
                "sub_subgroup_type" if has_sub_subgroup else "NULL AS sub_subgroup_type",
                "sub_sub_subgroup_type" if has_sub_sub_subgroup else "NULL AS sub_sub_subgroup_type",
                "frequency",
            ]
            query = f"""
                SELECT {', '.join(select_fields)}
                FROM phonemes
                WHERE syllable_type = ? AND position = ? AND length_type = ?
                ORDER BY frequency ASC, phoneme
            """
            cursor.execute(query, (syllable_type, position, filters[position]))

            current_filter_phonemes = cursor.fetchall()

            # Build table for current filter
            existing_phoneme_codes = set()
            for row in current_filter_phonemes:
                number = row[0]
                phoneme_value = row[1]
                length_type_value = row[2]
                group_type_value = row[3]
                subgroup_type_value = row[4]
                sub_subgroup_value = row[5]
                sub_sub_subgroup_value = row[6]
                frequency_value = row[7] if len(row) > 7 else 0

                tables_data[position].append({
                    'number': number,
                    'phoneme': phoneme_value,
                    'length_type': length_type_value,
                    'group_type': group_type_value,
                    'subgroup_type': subgroup_type_value,
                    'sub_subgroup_type': sub_subgroup_value,
                    'sub_sub_subgroup_type': sub_sub_subgroup_value,
                    'frequency': frequency_value or 0
                })
                existing_phoneme_codes.add(phoneme_value)

            fallback_entries = FALLBACK_PHONEMES.get((syllable_type, position, filters[position]), [])
            next_number = len(tables_data[position]) + 1
            for fallback in fallback_entries:
                fallback_phoneme = fallback.get('phoneme')
                if fallback_phoneme in existing_phoneme_codes:
                    continue
                tables_data[position].append({
                    'number': fallback.get('number') or next_number,
                    'phoneme': fallback_phoneme,
                    'length_type': fallback.get('length_type'),
                    'group_type': fallback.get('group_type'),
                    'subgroup_type': fallback.get('subgroup_type'),
                    'sub_subgroup_type': fallback.get('sub_subgroup_type'),
                    'sub_sub_subgroup_type': fallback.get('sub_sub_subgroup_type'),
                    'frequency': fallback.get('frequency', 0),
                })
                existing_phoneme_codes.add(fallback_phoneme)
                next_number += 1

            # Get all phonemes for this position grouped by length type (for filter dropdown)
            for length_type in length_types.get(position, []):
                cursor.execute("""
                    SELECT phoneme FROM phonemes
                    WHERE syllable_type = ? AND position = ? AND length_type = ?
                    ORDER BY frequency ASC, phoneme
                """, (syllable_type, position, length_type))

                phonemes_for_length = [row[0] for row in cursor.fetchall()]
                fallback_for_length = [
                    entry.get('phoneme')
                    for entry in FALLBACK_PHONEMES.get((syllable_type, position, length_type), [])
                ]
                phoneme_set = set(phonemes_for_length)
                for phoneme in fallback_for_length:
                    if phoneme not in phoneme_set:
                        phonemes_for_length.append(phoneme)
                        phoneme_set.add(phoneme)
                available_options[position]['phonemes_by_length'][length_type] = phonemes_for_length

        conn.close()

        return jsonify({
            'success': True,
            'tables': tables_data,
            'available_options': available_options,
            'current_filters': filters,
            'filters': filters
        })

    except Exception as e:
        print(f"Error in get_phoneme_tables: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


__all__ = ['create_word_menu', 'create_word_table_based', 'get_languages', 'get_last_language', 'get_phoneme_tables']
