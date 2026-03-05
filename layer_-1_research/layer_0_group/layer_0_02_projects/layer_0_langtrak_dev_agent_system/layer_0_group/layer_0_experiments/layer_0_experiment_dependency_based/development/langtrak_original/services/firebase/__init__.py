# resource_id: "246debb5-158c-4777-8427-002f20da1e5e"
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
