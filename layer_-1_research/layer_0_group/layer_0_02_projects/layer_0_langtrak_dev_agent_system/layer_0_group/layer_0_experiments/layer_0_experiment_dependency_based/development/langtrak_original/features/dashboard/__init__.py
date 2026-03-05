# resource_id: "9db717d5-6283-4b4a-9620-2cf772a84e6d"
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
