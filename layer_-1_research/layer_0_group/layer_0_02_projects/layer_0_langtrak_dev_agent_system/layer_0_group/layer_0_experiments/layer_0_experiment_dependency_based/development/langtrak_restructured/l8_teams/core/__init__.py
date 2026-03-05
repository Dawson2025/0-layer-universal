# resource_id: "1e12aae9-494c-4001-ab46-a8d70a7099af"
# resource_type: "document"
# resource_name: "__init__"
"""Groups feature blueprint and exports."""

from flask import Blueprint


groups_bp = Blueprint(
    "groups",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/groups",
)


# Import sub-modules to register routes
from . import api  # noqa: E402
from . import creation  # noqa: E402
from . import display  # noqa: E402
from . import membership  # noqa: E402


__all__ = ["groups_bp"]
