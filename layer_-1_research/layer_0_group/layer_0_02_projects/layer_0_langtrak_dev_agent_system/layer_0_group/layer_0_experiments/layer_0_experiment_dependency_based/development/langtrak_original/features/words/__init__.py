# resource_id: "fb898fed-452b-4b6f-a9b4-d58badad7acc"
# resource_type: "document"
# resource_name: "__init__"
"""
Words Feature

Handles all word-related functionality including creation, display, search, and editing.

Sub-modules organized by concern for parallel development:
- display: View and display words
- creation: Create new words and related helpers
- search: Search and lookup functionality
- editing: Edit existing words
- api_operations: API endpoints for CRUD operations
"""

from flask import Blueprint

words_bp = Blueprint(
    "words",
    __name__,
    url_prefix="",
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/words",
)

# Import all sub-modules to register their routes with the blueprint
# These can be worked on in parallel by different agents!
from . import display          # 🟢 Agent A can work here
from . import creation         # 🟢 Agent B can work here
from . import search           # 🟢 Agent C can work here
from . import editing          # 🟢 Agent D can work here
from . import api_operations   # 🟢 Agent E can work here

__all__ = ("words_bp",)
