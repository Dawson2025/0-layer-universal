"""
L2 Infrastructure Layer

The foundation layer. Everything the system needs to run.
Sub-layers: App Factory, Database, Firebase, Storage, Auth, DB Admin, Firebase Sync, TTS

Provides: IStorageProvider, IAuthProvider
Depends On: (nothing — foundation layer)
"""

from flask import Blueprint

l2_bp = Blueprint('l2_infrastructure', __name__)

# Import sub-module routes to register them on the blueprint
from . import routes
