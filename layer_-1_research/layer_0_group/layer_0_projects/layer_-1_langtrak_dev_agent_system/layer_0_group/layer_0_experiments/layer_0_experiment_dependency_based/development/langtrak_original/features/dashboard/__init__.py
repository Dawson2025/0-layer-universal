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
