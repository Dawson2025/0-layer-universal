# resource_id: "424af4e3-cb66-4b7f-95c2-be104859a1b9"
# resource_type: "document"
# resource_name: "menu"
"""
Phonemes Menu Module

Handles phoneme viewing options menu.
Agents can work on menu improvements without affecting display logic.
"""

from flask import render_template

from . import phonemes_bp


@phonemes_bp.route('/phonemes')
def phonemes_menu():
    """
    Phoneme viewing options menu.

    Provides navigation to different phoneme display modes:
    - Flat view: Simple list of all phonemes
    - Nested view: Hierarchical organization
    - Full view: Complete hierarchy with frequency calculations

    Returns:
        Rendered phoneme menu template
    """
    return render_template('phonemes_menu.html')


__all__ = ['phonemes_menu']
