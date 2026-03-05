# resource_id: "253d494e-7332-4587-8951-04a91f8fd606"
# resource_type: "document"
# resource_name: "__init__"
"""
Phonemes Feature

Handles phoneme viewing and display in multiple formats.

Sub-modules organized by concern for parallel development:
- menu: Phoneme viewing options menu
- display: All display modes (flat, nested, full hierarchy)
"""

from flask import Blueprint

phonemes_bp = Blueprint(
    "phonemes",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/phonemes",
)

# Import all sub-modules to register their routes
from . import menu       # 🟢 Agent A
from . import display    # 🟢 Agent B

__all__ = ["phonemes_bp"]
