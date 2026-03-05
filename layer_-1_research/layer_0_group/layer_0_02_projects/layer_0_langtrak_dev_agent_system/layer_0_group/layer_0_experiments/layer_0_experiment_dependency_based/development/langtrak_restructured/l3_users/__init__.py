# resource_id: "d233005f-a882-45cd-814a-7d0bb5c71d2b"
# resource_type: "document"
# resource_name: "__init__"
"""L3 Users Layer - User model, profiles, sessions"""
from flask import Blueprint

l3_bp = Blueprint('l3_users', __name__)

from . import routes  # noqa: E402
