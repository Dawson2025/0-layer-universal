"""Variant menu feature blueprint and exports.

Note: Variant menu functionality is integrated into the projects feature.
This blueprint is kept as a placeholder for potential future use.
"""

from flask import Blueprint


variant_menu_bp = Blueprint(
    "variant_menu",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/variant_menu",
)


from . import api  # noqa: E402


__all__ = ["variant_menu_bp"]
