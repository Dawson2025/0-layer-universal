# resource_id: "35c368ad-df63-41ca-9de9-c5cd663af9b5"
# resource_type: "document"
# resource_name: "__init__"
"""Dashboard feature blueprint and exports."""

from flask import Blueprint


dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/dashboard",
)


# Import sub-modules to register routes
from . import api  # noqa: E402
from . import display  # noqa: E402


__all__ = ["dashboard_bp"]
