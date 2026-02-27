"""
Admin Feature

Handles admin panel functionality including phoneme management, templates, and database tools.

Sub-modules organized by concern for parallel development:
- dashboard: Admin landing page and overview
- phoneme_management: Phoneme CRUD operations and frequency management
- template_system: Template creation, export, import, and application
- database_tools: Database maintenance utilities (reset, bulk operations)
"""

from flask import Blueprint

admin_bp = Blueprint(
    "admin",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/admin",
)

# Import all sub-modules to register their routes
from . import dashboard           # 🟢 Agent A
from . import phoneme_management  # 🟢 Agent B
from . import template_system     # 🟢 Agent C
from . import database_tools      # 🟢 Agent D

__all__ = ["admin_bp"]
