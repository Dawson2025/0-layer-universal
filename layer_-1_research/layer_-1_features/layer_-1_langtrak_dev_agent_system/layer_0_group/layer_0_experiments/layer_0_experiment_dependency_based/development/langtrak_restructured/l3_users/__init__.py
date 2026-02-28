"""L3 Users Layer - User model, profiles, sessions"""
from flask import Blueprint

l3_bp = Blueprint('l3_users', __name__)

from . import routes  # noqa: E402
