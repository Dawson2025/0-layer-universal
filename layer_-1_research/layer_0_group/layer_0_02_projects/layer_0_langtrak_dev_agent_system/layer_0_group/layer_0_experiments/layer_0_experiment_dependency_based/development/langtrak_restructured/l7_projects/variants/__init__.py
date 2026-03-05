# resource_id: "dc4822f9-fb8b-4758-b0ef-e1b142bac3f7"
# resource_type: "document"
# resource_name: "__init__"
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
