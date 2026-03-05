# resource_id: "22d5bb6f-753a-46f9-9a65-8fda7e989e94"
# resource_type: "document"
# resource_name: "firestore"
"""Unified Firebase Admin and Firestore services."""
from __future__ import annotations

import importlib
import importlib.util
import json
import os
from datetime import datetime
from types import ModuleType
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from .config import firebase_config

_DISABLE_FIREBASE = os.getenv("DISABLE_FIREBASE", "").lower() in {"1", "true", "yes", "on"}

firebase_admin_spec = importlib.util.find_spec("firebase_admin")
if firebase_admin_spec is None:  # pragma: no cover - depends on optional dependency
    FIREBASE_AVAILABLE = False
    firebase_admin: Optional[ModuleType] = None
    auth: Optional[ModuleType] = None
    credentials: Optional[ModuleType] = None
    firestore: Optional[ModuleType] = None
else:
    firebase_admin = importlib.import_module("firebase_admin")
    auth = importlib.import_module("firebase_admin.auth")
    credentials = importlib.import_module("firebase_admin.credentials")
    firestore = importlib.import_module("firebase_admin.firestore")
    FIREBASE_AVAILABLE = True


class FirebaseAdminService:
    """High-level wrapper around the Firebase Admin SDK."""

    def __init__(self) -> None:
        self.app: Optional[Any] = None
        self.db: Optional[Any] = None
        self.initialize()

    # ------------------------------------------------------------------
    # Initialization helpers
    # ------------------------------------------------------------------
    def initialize(self, force: bool = False) -> None:
        """Initialise the Firebase Admin SDK if available."""

        if _DISABLE_FIREBASE:
            print("Firebase disabled via DISABLE_FIREBASE environment variable - using local storage only")
            self.app = None
            self.db = None
            return

        if not FIREBASE_AVAILABLE:
            print("Firebase packages not available - using local storage only")
            self.app = None
            self.db = None
            return

        if self.app and self.db and not force:
            # Already initialised
            return

        try:
            self._clear_existing_apps()

            firebase_config.refresh()
            project_id = firebase_config.project_id
            credentials_path = firebase_config.credentials_path

            print(f"Initializing Firebase for {firebase_config.environment} environment")
            print(f"Project ID: {project_id}")

            if not os.path.exists(credentials_path):
                print(f"Credentials file not found: {credentials_path}")
                print("Please download the service account key and place it in the project directory")
                self.app = None
                self.db = None
                return

            cred = credentials.Certificate(credentials_path)  # type: ignore[arg-type]
            self.app = firebase_admin.initialize_app(cred, {  # type: ignore[arg-type]
                "projectId": project_id,
            })

            self.db = firestore.client()  # type: ignore[call-arg]

            if self._test_connection():
                print(f"✅ Firebase {firebase_config.environment} environment ready!")
            else:
                print("⚠️  Firebase connected but write test failed")

        except Exception as exc:  # pragma: no cover - defensive fallback
            print(f"Error initializing Firebase: {exc}")
            self.app = None
            self.db = None

    def _clear_existing_apps(self) -> None:
        if not FIREBASE_AVAILABLE or not firebase_admin:  # pragma: no cover - safe guard
            return

        for app_name in list(firebase_admin._apps.keys()):  # type: ignore[attr-defined]
            firebase_admin.delete_app(firebase_admin._apps[app_name])  # type: ignore[index]

    def _test_connection(self) -> bool:
        if _DISABLE_FIREBASE or not self.db or not FIREBASE_AVAILABLE:
            return False

        try:
            test_ref = self.db.collection("_connection_test").document("test")
            test_ref.set({
                "environment": firebase_config.environment,
                "test": True,
                "timestamp": firestore.SERVER_TIMESTAMP,  # type: ignore[operator]
            })

            doc = test_ref.get()
            success = bool(doc.exists and doc.to_dict().get("test"))
            test_ref.delete()
            return success
        except Exception as exc:  # pragma: no cover - fallback path when emulator unavailable
            print(f"Connection test failed: {exc}")
            return False

    # ------------------------------------------------------------------
    # Public helpers
    # ------------------------------------------------------------------
    def is_available(self) -> bool:
        return bool(self.db and FIREBASE_AVAILABLE and not _DISABLE_FIREBASE)

    # Authentication helpers -------------------------------------------------
    def verify_token(self, id_token: str) -> Optional[Dict[str, Any]]:
        if not FIREBASE_AVAILABLE or not auth:
            return None
        try:
            return auth.verify_id_token(id_token)
        except Exception as exc:  # pragma: no cover - network specific failures
            print(f"Error verifying token: {exc}")
            return None

    def get_user_by_uid(self, uid: str) -> Optional[Dict[str, Any]]:
        if not FIREBASE_AVAILABLE or not auth:
            return None
        try:
            user = auth.get_user(uid)
            return {
                "uid": user.uid,
                "email": user.email,
                "display_name": user.display_name,
                "photo_url": user.photo_url,
                "email_verified": user.email_verified,
            }
        except Exception as exc:  # pragma: no cover - network specific failures
            print(f"Error getting user: {exc}")
            return None

    def create_custom_token(self, uid: str) -> Optional[Any]:
        if not FIREBASE_AVAILABLE or not auth:
            return None
        try:
            return auth.create_custom_token(uid)
        except Exception as exc:  # pragma: no cover - network specific failures
            print(f"Error creating custom token: {exc}")
            return None

    # Firestore helpers ------------------------------------------------------
    def get_collection(self, collection_name: str):
        if not self.db:
            return None
        return self.db.collection(collection_name)

    def add_document(self, collection_name: str, document_data: Dict[str, Any], document_id: Optional[str] = None) -> Optional[str]:
        if not self.db:
            return None
        try:
            collection = self.db.collection(collection_name)
            if document_id:
                doc_ref = collection.document(document_id)
                doc_ref.set(document_data)
                return document_id
            doc_ref = collection.add(document_data)
            return doc_ref[1].id
        except Exception as exc:
            print(f"Error adding document: {exc}")
            return None

    def get_document(self, collection_name: str, document_id: str) -> Optional[Dict[str, Any]]:
        if not self.db:
            return None
        try:
            doc_ref = self.db.collection(collection_name).document(document_id)
            doc = doc_ref.get()
            if doc.exists:
                data = doc.to_dict() or {}
                data["id"] = doc.id
                return data
            return None
        except Exception as exc:
            print(f"Error getting document: {exc}")
            return None

    def get_documents(
        self,
        collection_name: str,
        where_conditions: Optional[Sequence[Sequence[Any]]] = None,
        order_by: Optional[Sequence[Any]] = None,
        limit: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        if not self.db:
            return []
        try:
            query = self.db.collection(collection_name)

            if where_conditions:
                for condition in where_conditions:
                    if len(condition) == 3:
                        field, operator, value = condition
                        query = query.where(field, operator, value)

            if order_by:
                for order in order_by:
                    if isinstance(order, tuple):
                        field, direction = order
                        query = query.order_by(field, direction=direction)
                    else:
                        query = query.order_by(order)

            if limit:
                query = query.limit(limit)

            docs = query.get()
            results: List[Dict[str, Any]] = []
            for doc in docs:
                data = doc.to_dict() or {}
                data["id"] = doc.id
                results.append(data)
            return results
        except Exception as exc:
            print(f"Error getting documents: {exc}")
            return []

    def update_document(self, collection_name: str, document_id: str, update_data: Dict[str, Any]) -> bool:
        if not self.db:
            return False
        try:
            doc_ref = self.db.collection(collection_name).document(document_id)
            doc_ref.update(update_data)
            return True
        except Exception as exc:
            print(f"Error updating document: {exc}")
            return False

    def delete_document(self, collection_name: str, document_id: str) -> bool:
        if not self.db:
            return False
        try:
            self.db.collection(collection_name).document(document_id).delete()
            return True
        except Exception as exc:
            print(f"Error deleting document: {exc}")
            return False


class FirestoreDB:
    """Higher-level Firestore helpers used across the project."""

    USERS_COLLECTION = "users"
    PROJECTS_COLLECTION = "projects"
    GROUPS_COLLECTION = "groups"
    GROUP_MEMBERSHIPS_COLLECTION = "group_memberships"
    GROUP_INVITES_COLLECTION = "group_invites"
    PROJECT_SHARES_COLLECTION = "project_shares"
    PHONEMES_COLLECTION = "phonemes"
    WORDS_COLLECTION = "words"
    PHONEME_TEMPLATES_COLLECTION = "phoneme_templates"

    def __init__(self, service: FirebaseAdminService):
        self._service = service

    # ------------------------------------------------------------------
    # User operations
    # ------------------------------------------------------------------
    def create_user(self, user_data: Dict[str, Any]) -> Optional[str]:
        try:
            user_doc = {
                "username": user_data.get("username"),
                "email": user_data.get("email"),
                "firebase_uid": user_data.get("firebase_uid"),
                "password_hash": user_data.get("password_hash", ""),
                "created_at": datetime.utcnow(),
                "is_active": True,
            }
            return self._service.add_document(self.USERS_COLLECTION, user_doc)
        except Exception as exc:
            print(f"Error creating user: {exc}")
            return None

    def get_user_by_firebase_uid(self, firebase_uid: str) -> Optional[Dict[str, Any]]:
        try:
            users = self._service.get_documents(
                self.USERS_COLLECTION,
                where_conditions=[("firebase_uid", "==", firebase_uid)],
            )
            return users[0] if users else None
        except Exception as exc:
            print(f"Error getting user by Firebase UID: {exc}")
            return None

    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        try:
            users = self._service.get_documents(
                self.USERS_COLLECTION,
                where_conditions=[("email", "==", email)],
            )
            return users[0] if users else None
        except Exception as exc:
            print(f"Error getting user by email: {exc}")
            return None

    def update_user(self, user_id: str, update_data: Dict[str, Any]) -> bool:
        try:
            return self._service.update_document(self.USERS_COLLECTION, user_id, update_data)
        except Exception as exc:
            print(f"Error updating user: {exc}")
            return False

    # ------------------------------------------------------------------
    # Project operations
    # ------------------------------------------------------------------
    def create_project(self, project_data: Dict[str, Any]) -> Optional[str]:
        try:
            user_id = project_data.get("user_id")
            created_at = self._ensure_datetime(project_data.get("created_at"))
            updated_at = self._ensure_datetime(project_data.get("updated_at"))

            print(
                f"DEBUG: Creating Firebase project '{project_data.get('name')}' for user {user_id} (type: {type(user_id)})"
            )

            project_doc = {
                "name": project_data.get("name"),
                "user_id": user_id,
                "user_id_str": str(user_id) if user_id is not None else None,
                "firebase_uid": project_data.get("firebase_uid"),
                "created_at": created_at,
                "updated_at": updated_at,
                "original_sqlite_id": project_data.get("original_sqlite_id"),
            }

            doc_ref = self._service.add_document(self.PROJECTS_COLLECTION, project_doc)
            print(f"DEBUG: Firebase project created with ID: {doc_ref}")
            return doc_ref
        except Exception as exc:
            print(f"Error creating project: {exc}")
            return None

    def get_user_projects(self, user_id: Any) -> List[Dict[str, Any]]:
        try:
            print(f"DEBUG: Getting Firebase projects for user {user_id} (type: {type(user_id)})")
            projects = self._service.get_documents(
                self.PROJECTS_COLLECTION,
                where_conditions=[("user_id", "==", user_id)],
            )

            if not projects:
                projects = self._service.get_documents(
                    self.PROJECTS_COLLECTION,
                    where_conditions=[("user_id", "==", str(user_id))],
                )

            if not projects:
                projects = self._service.get_documents(
                    self.PROJECTS_COLLECTION,
                    where_conditions=[("user_id_str", "==", str(user_id))],
                )
            print(
                f"DEBUG: Retrieved {len(projects)} Firebase projects: {[p.get('name', 'no name') for p in projects]}"
            )
            return projects
        except Exception as exc:
            print(f"Error getting user projects: {exc}")
            return []

    def get_project(self, project_id: str) -> Optional[Dict[str, Any]]:
        try:
            return self._service.get_document(self.PROJECTS_COLLECTION, project_id)
        except Exception as exc:
            print(f"Error getting project: {exc}")
            return None

    def update_project(self, project_id: str, update_data: Dict[str, Any]) -> bool:
        try:
            update_data = dict(update_data)
            update_data["updated_at"] = datetime.utcnow()
            return self._service.update_document(self.PROJECTS_COLLECTION, project_id, update_data)
        except Exception as exc:
            print(f"Error updating project: {exc}")
            return False

    # ------------------------------------------------------------------
    # Word operations
    # ------------------------------------------------------------------
    def create_word(self, word_data: Dict[str, Any]) -> Optional[str]:
        try:
            english_words = self._normalise_words(word_data.get("english_words"))
            created_at = self._ensure_datetime(word_data.get("created_at"))
            updated_raw = word_data.get("updated_at") or created_at
            updated_at = self._ensure_datetime(updated_raw)

            word_doc = {
                "language": word_data.get("language"),
                "english_words": english_words,
                "new_language_word": word_data.get("new_language_word"),
                "ipa_phonetics": word_data.get("ipa_phonetics"),
                "dictionary_phonetics": word_data.get("dictionary_phonetics"),
                "video_path": word_data.get("video_path"),
                "syllable_type": word_data.get("syllable_type"),
                "onset_phoneme": word_data.get("onset_phoneme"),
                "onset_length_type": word_data.get("onset_length_type"),
                "nucleus_phoneme": word_data.get("nucleus_phoneme"),
                "nucleus_length_type": word_data.get("nucleus_length_type"),
                "coda_phoneme": word_data.get("coda_phoneme"),
                "coda_length_type": word_data.get("coda_length_type"),
                "user_id": word_data.get("user_id"),
                "project_id": word_data.get("project_id"),
                "created_at": created_at,
                "updated_at": updated_at,
            }
            if "syllables_data" in word_data:
                word_doc["syllables_data"] = word_data.get("syllables_data")
            if "source" in word_data:
                word_doc["source"] = word_data.get("source")

            return self._service.add_document(self.WORDS_COLLECTION, word_doc)
        except Exception as exc:
            print(f"Error creating word: {exc}")
            return None

    def get_project_words(self, project_id: str) -> List[Dict[str, Any]]:
        try:
            return self._service.get_documents(
                self.WORDS_COLLECTION,
                where_conditions=[("project_id", "==", project_id)],
            )
        except Exception as exc:
            print(f"Error getting project words: {exc}")
            return []

    def get_word(self, word_id: str) -> Optional[Dict[str, Any]]:
        try:
            return self._service.get_document(self.WORDS_COLLECTION, word_id)
        except Exception as exc:
            print(f"Error getting word: {exc}")
            return None

    def update_word(self, word_id: str, update_data: Dict[str, Any]) -> bool:
        try:
            return self._service.update_document(self.WORDS_COLLECTION, word_id, update_data)
        except Exception as exc:
            print(f"Error updating word: {exc}")
            return False

    def delete_word(self, word_id: str) -> bool:
        try:
            return self._service.delete_document(self.WORDS_COLLECTION, word_id)
        except Exception as exc:
            print(f"Error deleting word: {exc}")
            return False

    def count_project_words(self, project_id: str) -> int:
        words = self.get_project_words(project_id)
        return len(words)

    # ------------------------------------------------------------------
    # Phoneme operations
    # ------------------------------------------------------------------
    def create_phoneme(self, phoneme_data: Dict[str, Any]) -> Optional[str]:
        try:
            phoneme_doc = {
                "phoneme": phoneme_data.get("phoneme"),
                "language": phoneme_data.get("language"),
                "frequency": phoneme_data.get("frequency", 0),
                "syllable_type": phoneme_data.get("syllable_type"),
                "position": phoneme_data.get("position"),
                "length_type": phoneme_data.get("length_type"),
                "group_type": phoneme_data.get("group_type"),
                "subgroup_type": phoneme_data.get("subgroup_type"),
                "sub_subgroup_type": phoneme_data.get("sub_subgroup_type"),
                "sub_sub_subgroup_type": phoneme_data.get("sub_sub_subgroup_type"),
                "user_id": phoneme_data.get("user_id"),
                "project_id": phoneme_data.get("project_id"),
                "created_at": self._ensure_datetime(phoneme_data.get("created_at")),
                "updated_at": self._ensure_datetime(phoneme_data.get("updated_at") or phoneme_data.get("created_at")),
            }
            return self._service.add_document(self.PHONEMES_COLLECTION, phoneme_doc)
        except Exception as exc:
            print(f"Error creating phoneme: {exc}")
            return None

    def get_project_phonemes(self, project_id: str) -> List[Dict[str, Any]]:
        try:
            return self._service.get_documents(
                self.PHONEMES_COLLECTION,
                where_conditions=[("project_id", "==", project_id)],
            )
        except Exception as exc:
            print(f"Error getting project phonemes: {exc}")
            return []

    def update_phoneme(self, phoneme_id: str, update_data: Dict[str, Any]) -> bool:
        try:
            return self._service.update_document(self.PHONEMES_COLLECTION, phoneme_id, update_data)
        except Exception as exc:
            print(f"Error updating phoneme: {exc}")
            return False

    def delete_phoneme(self, phoneme_id: str) -> bool:
        try:
            return self._service.delete_document(self.PHONEMES_COLLECTION, phoneme_id)
        except Exception as exc:
            print(f"Error deleting phoneme: {exc}")
            return False

    def delete_project_phonemes(self, project_id: str) -> None:
        try:
            phonemes = self.get_project_phonemes(project_id)
            for phoneme in phonemes:
                if "id" in phoneme:
                    self.delete_phoneme(phoneme["id"])
        except Exception as exc:
            print(f"Error deleting project phonemes: {exc}")

    # ------------------------------------------------------------------
    # Project clean up helpers
    # ------------------------------------------------------------------
    def delete_project(self, project_id: str) -> bool:
        return self._service.delete_document(self.PROJECTS_COLLECTION, project_id)

    def delete_project_words(self, project_id: str) -> None:
        words = self.get_project_words(project_id)
        for word in words:
            if "id" in word:
                self.delete_word(word["id"])

    # ------------------------------------------------------------------
    # Group operations
    # ------------------------------------------------------------------
    def create_group(self, group_data: Dict[str, Any]) -> Optional[str]:
        try:
            group_doc = {
                "name": group_data.get("name"),
                "description": group_data.get("description"),
                "owner_id": group_data.get("owner_id"),
                "project_id": group_data.get("project_id"),
                "created_at": self._ensure_datetime(group_data.get("created_at")),
            }
            return self._service.add_document(self.GROUPS_COLLECTION, group_doc)
        except Exception as exc:
            print(f"Error creating group: {exc}")
            return None

    def add_group_membership(self, membership_data: Dict[str, Any]) -> Optional[str]:
        try:
            membership_doc = {
                "group_id": membership_data.get("group_id"),
                "user_id": membership_data.get("user_id"),
                "role": membership_data.get("role", "member"),
                "joined_at": self._ensure_datetime(membership_data.get("joined_at")),
            }
            return self._service.add_document(self.GROUP_MEMBERSHIPS_COLLECTION, membership_doc)
        except Exception as exc:
            print(f"Error creating group membership: {exc}")
            return None

    def get_group_memberships(self, group_id: str) -> List[Dict[str, Any]]:
        try:
            return self._service.get_documents(
                self.GROUP_MEMBERSHIPS_COLLECTION,
                where_conditions=[("group_id", "==", group_id)],
            )
        except Exception as exc:
            print(f"Error getting group memberships: {exc}")
            return []

    def delete_group(self, group_id: str) -> bool:
        return self._service.delete_document(self.GROUPS_COLLECTION, group_id)

    # ------------------------------------------------------------------
    # Utility helpers
    # ------------------------------------------------------------------
    def _ensure_datetime(self, value: Any) -> datetime:
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                return datetime.utcnow()
        if value:
            return datetime.fromtimestamp(value)
        return datetime.utcnow()

    def _normalise_words(self, english_words: Any) -> List[str]:
        if isinstance(english_words, str):
            try:
                loaded = json.loads(english_words)
                if isinstance(loaded, list):
                    return [str(word) for word in loaded]
                return [str(loaded)]
            except json.JSONDecodeError:
                return [english_words]
        if isinstance(english_words, Iterable):
            return [str(word) for word in english_words]
        return []


firebase_admin_service = FirebaseAdminService()
clean_firebase_service = firebase_admin_service  # Backwards compatibility alias
firebase_service = firebase_admin_service  # Legacy alias used by migration scripts
firestore_db = FirestoreDB(firebase_admin_service)

__all__ = [
    "firebase_admin_service",
    "clean_firebase_service",
    "firebase_service",
    "firestore_db",
    "FirebaseAdminService",
    "FirestoreDB",
]
