# resource_id: "9e7eabbd-07ce-49af-a2a3-ba293df143a4"
# resource_type: "document"
# resource_name: "database_tools"
"""
Admin Database Tools Module

Handles database maintenance operations: reset, bulk operations, cleanup.
Agents can work on database tools without affecting other sub-modules.
"""

from flask import request, jsonify
import sqlite3
import os

from core.database import DB_NAME
from core.decorators import require_project_admin
from services.reset import reset_database as reset_database_service
import main
from . import admin_bp


@admin_bp.route('/api/admin/bulk-delete-words', methods=['POST'])
@require_project_admin
def api_admin_bulk_delete_words():
    """
    API endpoint to delete multiple words at once.

    Request JSON:
        word_ids: List of word IDs to delete

    Returns:
        JSON response with deleted count
    """
    try:
        data = request.get_json()
        word_ids = data.get('word_ids', [])

        if not word_ids:
            return jsonify({'success': False, 'error': 'No word IDs provided'})

        conn = sqlite3.connect(DB_NAME)
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


@admin_bp.route('/api/admin/reset-database', methods=['POST'])
@require_project_admin
def api_admin_reset_database():
    """
    API endpoint to reset database.

    WARNING: This will delete all data and recreate tables.

    Returns:
        JSON response with success status
    """
    try:
        result = reset_database_service(DB_NAME, insert_sample_data=main.insert_sample_data)
    except RuntimeError as exc:
        return jsonify({'success': False, 'error': str(exc)}), 500

    return jsonify({'success': True, 'message': result.to_message()})


@admin_bp.route('/api/admin/fix-video-paths', methods=['POST'])
@require_project_admin
def api_admin_fix_video_paths():
    """
    Normalize stored video paths in the words table (basic cleanup).
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, video_path FROM words WHERE video_path IS NOT NULL AND video_path != ''")
        rows = cursor.fetchall()
        updated = 0
        for row in rows:
            word_id, vp = row[0], row[1]
            if vp is None:
                continue
            new_vp = str(vp).strip().strip('"').strip("'").replace('\\\\', '/').replace('\\', '/')
            if new_vp != vp:
                cursor.execute("UPDATE words SET video_path = ? WHERE id = ?", (new_vp, word_id))
                updated += 1
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': f'Normalized {updated} video paths', 'updated_count': updated})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


__all__ = [
    'api_admin_bulk_delete_words',
    'api_admin_reset_database',
    'api_admin_fix_video_paths'
]
