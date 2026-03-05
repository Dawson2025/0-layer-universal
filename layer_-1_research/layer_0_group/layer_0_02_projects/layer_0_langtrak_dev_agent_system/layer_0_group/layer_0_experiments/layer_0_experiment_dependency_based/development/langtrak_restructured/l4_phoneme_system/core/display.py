# resource_id: "f4ad06dc-6dbe-4f07-aa71-ed7edd0145c2"
# resource_type: "document"
# resource_name: "display"
"""
Phonemes Display Module

Handles phoneme display modes: flat, nested, and full hierarchy views.
Agents can work on display enhancements without affecting other sub-modules.
"""

from flask import render_template, redirect, url_for, flash
from collections import defaultdict
import sqlite3

from core.database import DB_NAME
import main
from . import phonemes_bp


@phonemes_bp.route('/phonemes/nested')
def display_nested():
    """
    Display phonemes in nested hierarchy.

    Organizes phonemes by:
    - Syllable type (CVC, CV, VC, etc.)
    - Position (onset, nucleus, coda)
    - Length type (short, long, etc.)
    - Group type (plosive, fricative, etc.)
    - Subgroup type (voiced, voiceless, etc.)

    Returns:
        Rendered nested phonemes template
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get nested phoneme data (scoped to current project when available)
        from features.auth import get_user_info
        user = get_user_info()
        current = user.get('current_project') or {}
        project_id = current.get('local_project_id') or current.get('id')
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
            FROM phonemes
            WHERE project_id = ? OR ? IS NULL
            ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
        """, (project_id, project_id))

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
        return redirect(url_for('phonemes.phonemes_menu'))


@phonemes_bp.route('/phonemes/full')
def display_full():
    """
    Display full phoneme hierarchy with frequency calculations.

    Shows complete hierarchical organization with:
    - Group-level frequency totals
    - Subgroup breakdowns
    - Individual phoneme frequencies
    - Sorted by frequency for easy identification of common patterns

    Returns:
        Rendered full hierarchy template
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get full hierarchy data with frequency calculations (scoped to current project when available)
        from features.auth import get_user_info
        user = get_user_info()
        current = user.get('current_project') or {}
        project_id = current.get('local_project_id') or current.get('id')
        cursor.execute("""
            SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
            FROM phonemes
            WHERE project_id = ? OR ? IS NULL
            ORDER BY syllable_type, position, length_type, frequency ASC, group_type, subgroup_type, phoneme
        """, (project_id, project_id))

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
        return redirect(url_for('phonemes.phonemes_menu'))


__all__ = ['display_flat', 'display_nested', 'display_full']
