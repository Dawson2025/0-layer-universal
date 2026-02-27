"""
Admin Dashboard Module

Handles admin panel landing page and overview.
Agents can work on dashboard improvements without affecting other sub-modules.
"""

from flask import render_template

from core.decorators import require_project_admin
from core.session import get_user_info
from . import admin_bp


@admin_bp.route('/admin')
@require_project_admin
def admin_menu():
    """
    Admin panel menu - main landing page.

    Provides navigation to all admin features:
    - Phoneme management
    - Template system
    - Storage management
    - Database tools

    Returns:
        Rendered admin menu template
    """
    user = get_user_info()
    return render_template('admin_menu.html', user=user)


__all__ = ['admin_menu']
