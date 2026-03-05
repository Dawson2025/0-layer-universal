# resource_id: "fa3e43e0-396b-41f1-b210-39797e6f944a"
# resource_type: "document"
# resource_name: "config"
"""Firebase configuration helpers."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class FirebaseConfig:
    """Configuration wrapper for Firebase environments."""

    environment: str = ""

    def __post_init__(self) -> None:
        self.refresh()

    def refresh(self) -> None:
        """Reload environment information from OS variables."""
        self.environment = os.getenv("FIREBASE_ENV", "development")

    def get_config(self) -> dict[str, str]:
        """Return configuration payload for the active environment."""
        if self.environment == "production":
            return {
                "project_id": "lang-trak-prod",
                "credentials_file": "config/firebase/firebase-service-account-prod.json",
                "database_id": "(default)",
            }

        return {
            "project_id": os.getenv("FIREBASE_DEV_PROJECT_ID", "lang-trak-dev"),
            "credentials_file": "config/firebase/firebase-service-account-dev.json",
            "database_id": "(default)",
        }

    @property
    def project_id(self) -> str:
        return self.get_config()["project_id"]

    @property
    def credentials_path(self) -> str:
        # Resolve from project root (two levels up from services/firebase)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        return os.path.join(project_root, self.get_config()["credentials_file"])

    @property
    def database_id(self) -> str:
        return self.get_config()["database_id"]

    # Backwards-compatible helpers -------------------------------------------------
    def get_project_id(self) -> str:
        return self.project_id

    def get_credentials_path(self) -> str:
        return self.credentials_path

    def get_database_id(self) -> str:
        return self.database_id

    def is_development(self) -> bool:
        return self.environment == "development"

    def is_production(self) -> bool:
        return self.environment == "production"


firebase_config = FirebaseConfig()
