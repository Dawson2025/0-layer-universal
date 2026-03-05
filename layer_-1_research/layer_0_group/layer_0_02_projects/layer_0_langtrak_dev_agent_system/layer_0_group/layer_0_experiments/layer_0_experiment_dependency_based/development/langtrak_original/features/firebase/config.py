# resource_id: "8807177e-8a34-471d-9188-73e041c8ff63"
# resource_type: "document"
# resource_name: "config"
"""
Firebase client configuration helpers.

Centralizes the logic for loading Firebase credentials so that multiple
features can share the same behavior without duplicating code in the
main application module.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Dict, Mapping, Optional

_FIREBASE_WEB_CONFIG_KEYS = (
    "apiKey",
    "authDomain",
    "projectId",
    "storageBucket",
    "messagingSenderId",
    "appId",
)

_FIREBASE_ENV_KEY_MAP = {
    "apiKey": "VITE_FIREBASE_API_KEY",
    "appId": "VITE_FIREBASE_APP_ID",
    "authDomain": "VITE_FIREBASE_AUTH_DOMAIN",
    "projectId": "VITE_FIREBASE_PROJECT_ID",
    "storageBucket": "VITE_FIREBASE_STORAGE_BUCKET",
    "messagingSenderId": "VITE_FIREBASE_MESSAGING_SENDER_ID",
}


def _default_config_path() -> Path:
    """Return the repository-level firebase-config.js path."""
    return Path(__file__).resolve().parents[2] / "config/firebase/firebase-config.js"


def parse_firebase_config_js(config_path: Optional[Path] = None) -> Dict[str, str]:
    """
    Parse firebase-config.js for fallback web credentials.

    Args:
        config_path: Optional explicit path to the configuration file.

    Returns:
        A dictionary containing any credentials discovered in the file.
    """
    path = Path(config_path) if config_path else _default_config_path()
    fallback: Dict[str, str] = {}

    if not path.exists():
        return fallback

    try:
        contents = path.read_text(encoding="utf-8")
        match = re.search(r"const\s+firebaseConfig\s*=\s*\{(.*?)\};", contents, re.DOTALL)
        if not match:
            return fallback

        block = match.group(1)
        for raw_line in block.splitlines():
            line = raw_line.strip().rstrip(",")
            if not line or line.startswith("//") or ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            fallback[key] = value
    except Exception as exc:  # pragma: no cover - defensive logging
        print(f"Warning: Unable to parse firebase-config.js for fallback config: {exc}")

    return fallback


def get_firebase_client_config(
    *,
    config_path: Optional[Path] = None,
    environ: Optional[Mapping[str, str]] = None,
) -> Dict[str, str]:
    """
    Build Firebase client configuration for templates with sensible fallbacks.

    Args:
        config_path: Optional explicit path to firebase-config.js.
        environ: Optional environment mapping (defaults to os.environ).

    Returns:
        A dict containing all required Firebase config keys with string values.
    """
    env = environ or os.environ
    config = parse_firebase_config_js(config_path=config_path)

    for key, env_var in _FIREBASE_ENV_KEY_MAP.items():
        value = env.get(env_var)
        if value:
            config[key] = value.strip()

    project_id = config.get("projectId", "").strip()
    if project_id:
        config.setdefault("authDomain", f"{project_id}.firebaseapp.com")
        config.setdefault("storageBucket", f"{project_id}.firebasestorage.app")

    return {key: (config.get(key) or "") for key in _FIREBASE_WEB_CONFIG_KEYS}


__all__ = ("get_firebase_client_config", "parse_firebase_config_js")
