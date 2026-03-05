# resource_id: "651fdea3-a870-497c-a099-d106fd796c61"
# resource_type: "document"
# resource_name: "__init__"
"""
Meta-Intelligent Universal Orchestration System

A meta-intelligent system that actively recommends optimal choices for future projects
and continuously adapts to evolving best practices and tools.

This system provides:
- Active recommendation engine for technology choices
- Real-time learning from multiple data sources
- Future-proofing analysis and trend prediction
- Meta-analysis across multiple decision dimensions
- Scenario-specific recommendations and optimization

Core Components:
- Meta Decision Engine: Intelligent decision-making for technology choices
- Adaptive Learning System: Continuous learning from trends and best practices
- Meta Recommendation Engine: Comprehensive recommendation orchestration
- Real-Time Data Integration: Multiple data source monitoring and analysis
- Trend Analysis: Technology trend prediction and forecasting
"""

from .core.meta_decision_engine import MetaDecisionEngine, MetaRecommendation, DecisionContext
from .core.adaptive_learning_system import AdaptiveLearningSystem, LearningInsight, TrendAnalysis
from .core.meta_recommendation_engine import MetaRecommendationEngine, MetaRecommendationSet, ProjectScenario
from .core.orchestration.universal_orchestration_system import UniversalOrchestrationSystem, TechnologyProvider
from .core.orchestration.universal_visual_orchestrator import UniversalVisualOrchestrator
from .core.orchestration.universal_master_orchestrator import UniversalMasterOrchestrator, ComprehensiveAnalysis
from .instances.firebase_provider import FirebaseProvider
from .instances.firebase_config import FirebaseMetaIntelligentConfig, FirebaseProjectProfile, FirebaseProjectType

__version__ = "1.0.0"
__author__ = "Meta-Intelligent Orchestration Team"

__all__ = [
    "MetaDecisionEngine",
    "MetaRecommendation", 
    "DecisionContext",
    "AdaptiveLearningSystem",
    "LearningInsight",
    "TrendAnalysis",
    "MetaRecommendationEngine",
    "MetaRecommendationSet",
    "ProjectScenario",
    "UniversalOrchestrationSystem",
    "TechnologyProvider",
    "UniversalVisualOrchestrator",
    "UniversalMasterOrchestrator",
    "ComprehensiveAnalysis",
    "FirebaseProvider",
    "FirebaseMetaIntelligentConfig",
    "FirebaseProjectProfile",
    "FirebaseProjectType"
]
