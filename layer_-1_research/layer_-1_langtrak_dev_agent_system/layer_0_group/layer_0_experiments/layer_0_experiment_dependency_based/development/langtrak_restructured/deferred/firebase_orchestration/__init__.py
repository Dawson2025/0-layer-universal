"""
Firebase Orchestration System

A comprehensive system for automated Firebase environment and integration management.
Provides goal-oriented planning, visual management, and intelligent orchestration.

Components:
- Core Orchestration System: Environment and integration management
- Visual Orchestrator: Planning and dashboard visualization
- Master Orchestrator: Meta-level coordination and optimization
"""

from .core.orchestration_system import FirebaseOrchestrationSystem
from .core.visual_orchestrator import FirebaseVisualOrchestrator
from .core.master_orchestrator import FirebaseMasterOrchestrator

__version__ = "1.0.0"
__author__ = "Firebase Orchestration Team"

__all__ = [
    "FirebaseOrchestrationSystem",
    "FirebaseVisualOrchestrator", 
    "FirebaseMasterOrchestrator"
]
