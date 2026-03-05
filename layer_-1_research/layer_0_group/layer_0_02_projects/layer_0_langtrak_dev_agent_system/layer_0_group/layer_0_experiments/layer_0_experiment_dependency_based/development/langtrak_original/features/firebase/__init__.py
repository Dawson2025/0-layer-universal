# resource_id: "97031f67-56c3-4e35-b39a-a4962a8cb3b6"
# resource_type: "document"
# resource_name: "__init__"
"""
Helpers for Firebase-related configuration and utilities.
"""

from .config import get_firebase_client_config, parse_firebase_config_js

__all__ = ("get_firebase_client_config", "parse_firebase_config_js")
