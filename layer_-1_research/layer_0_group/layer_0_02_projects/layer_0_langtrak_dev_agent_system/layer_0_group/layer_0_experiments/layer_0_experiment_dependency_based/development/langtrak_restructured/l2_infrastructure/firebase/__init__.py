# resource_id: "0bfb834a-63e0-495d-ac5f-7a7f14ddcc24"
# resource_type: "document"
# resource_name: "__init__"
"""Firebase service package exports."""

from .config import firebase_config
from .firestore import (
    FirebaseAdminService,
    FirestoreDB,
    clean_firebase_service,
    firebase_admin_service,
    firebase_service,
    firestore_db,
)

__all__ = [
    "firebase_config",
    "FirebaseAdminService",
    "FirestoreDB",
    "firebase_admin_service",
    "clean_firebase_service",
    "firebase_service",
    "firestore_db",
]
