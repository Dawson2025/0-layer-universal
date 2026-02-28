"""
Universal Environments & Integrations Orchestration System

A comprehensive system for automated environment and integration management
across any combination of services and technologies based on project requirements
and development stages.

This system analyzes and optimizes the ENTIRE development ecosystem including:
- Operating systems and environments (WSL, Docker, native)
- MCP servers and tools (Chrome DevTools, Playwright, Browser Automation)
- AI frameworks (BMAD, GitHub Spec Kit, LangChain, etc.)
- Programming languages and frameworks
- Architecture patterns and design decisions
- Development workflows and processes
- Platform combinations and integrations
- Resource allocation and optimization

Components:
- Universal Master Orchestrator: Main coordination system
- Ecosystem Analyzer: Comprehensive environment analysis
- Workflow Optimizer: Intelligent workflow optimization
- Project Analyzer: Project structure and requirements analysis
- Optimization Engine: AI-powered configuration optimization
- Visual Orchestrator: Planning and management interface
- Browser Automation Strategy: Tool selection and automation strategy
"""

from .core.universal_master_orchestrator import UniversalMasterOrchestrator, ComprehensiveAnalysis
from .core.ecosystem_analyzer import EcosystemAnalyzer
from .core.workflow_optimizer import WorkflowOptimizer
from .core.project_analyzer import ProjectAnalyzer
from .core.optimization_engine import OptimizationEngine
from .core.universal_visual_orchestrator import UniversalVisualOrchestrator
from .core.browser_automation_strategy import BrowserAutomationStrategy

__version__ = "2.0.0"
__author__ = "Universal Orchestration Team"

__all__ = [
    "UniversalMasterOrchestrator",
    "ComprehensiveAnalysis",
    "EcosystemAnalyzer",
    "WorkflowOptimizer", 
    "ProjectAnalyzer",
    "OptimizationEngine",
    "UniversalVisualOrchestrator",
    "BrowserAutomationStrategy"
]
