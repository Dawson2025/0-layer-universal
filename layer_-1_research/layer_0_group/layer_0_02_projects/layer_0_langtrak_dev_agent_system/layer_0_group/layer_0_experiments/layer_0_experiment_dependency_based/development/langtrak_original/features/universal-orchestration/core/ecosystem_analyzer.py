#!/usr/bin/env python3
# resource_id: "d9fcf2f8-e85c-420c-9f8d-13ca4c996eaf"
# resource_type: "document"
# resource_name: "ecosystem_analyzer"

"""
ecosystem_analyzer.py

Comprehensive ecosystem analyzer that considers the entire development environment:
- Operating systems and environments (WSL, Docker, native)
- MCP servers and tools
- AI frameworks and systems
- Programming languages and frameworks
- Architecture patterns
- Development workflows
- Platform combinations
"""

import os
import platform
import subprocess
import json
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import psutil

class OperatingSystem(Enum):
    WINDOWS = "windows"
    WINDOWS_WSL = "windows_wsl"
    LINUX = "linux"
    MACOS = "macos"
    DOCKER = "docker"
    CONTAINER = "container"

class DevelopmentEnvironment(Enum):
    LOCAL = "local"
    WSL = "wsl"
    DOCKER = "docker"
    VM = "vm"
    CLOUD = "cloud"
    HYBRID = "hybrid"

class AIFramework(Enum):
    # Agentic AI Frameworks
    BMAD = "bmad"
    GITHUB_SPEC_KIT = "github_spec_kit"
    LANGCHAIN = "langchain"
    LANGGRAPH = "langgraph"
    AUTOGEN = "autogen"
    CREWAI = "crewai"
    SEMANTIC_KERNEL = "semantic_kernel"
    HAYSTACK = "haystack"
    
    # LLM Frameworks
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    COHERE = "cohere"
    HUGGINGFACE = "huggingface"
    OLLAMA = "ollama"
    LITELLM = "litellm"

class MCPCategory(Enum):
    BROWSER_AUTOMATION = "browser_automation"
    DEVELOPMENT = "development"
    CLOUD_SERVICES = "cloud_services"
    DATABASE = "database"
    MONITORING = "monitoring"
    COMMUNICATION = "communication"
    FILE_SYSTEM = "file_system"
    VERSION_CONTROL = "version_control"

class ArchitecturePattern(Enum):
    MONOLITH = "monolith"
    MICROSERVICES = "microservices"
    SERVERLESS = "serverless"
    EVENT_DRIVEN = "event_driven"
    LAYERED = "layered"
    HEXAGONAL = "hexagonal"
    CLEAN_ARCHITECTURE = "clean_architecture"
    DOMAIN_DRIVEN = "domain_driven"

class DevelopmentStage(Enum):
    CONCEPT = "concept"
    PROTOTYPE = "prototype"
    MVP = "mvp"
    BETA = "beta"
    PRODUCTION = "production"
    SCALE = "scale"
    MAINTENANCE = "maintenance"

@dataclass
class SystemEnvironment:
    """Represents the system environment configuration."""
    os_type: OperatingSystem
    development_env: DevelopmentEnvironment
    wsl_distro: Optional[str]
    docker_available: bool
    container_runtime: Optional[str]
    shell: str
    package_manager: str
    python_version: str
    node_version: Optional[str]
    available_tools: List[str]
    system_resources: Dict[str, Any]

@dataclass
class MCPConfiguration:
    """Represents MCP server configuration."""
    server_name: str
    category: MCPCategory
    tools_count: int
    enabled: bool
    priority: int
    use_cases: List[str]
    dependencies: List[str]
    resource_usage: Dict[str, Any]

@dataclass
class AIFrameworkConfig:
    """Represents AI framework configuration."""
    framework: AIFramework
    version: str
    capabilities: List[str]
    best_for: List[str]
    resource_requirements: Dict[str, Any]
    integration_complexity: str
    community_support: str

@dataclass
class TechnologyStack:
    """Represents the complete technology stack."""
    programming_languages: List[str]
    frameworks: List[str]
    databases: List[str]
    caching: List[str]
    messaging: List[str]
    monitoring: List[str]
    testing: List[str]
    deployment: List[str]
    ai_frameworks: List[AIFramework]
    mcp_servers: List[MCPConfiguration]

@dataclass
class ArchitectureRecommendation:
    """Represents architecture recommendations."""
    pattern: ArchitecturePattern
    reasoning: str
    components: List[str]
    data_flow: str
    scalability_approach: str
    security_considerations: List[str]
    deployment_strategy: str

@dataclass
class WorkflowRecommendation:
    """Represents workflow recommendations."""
    stage: DevelopmentStage
    tools: List[str]
    processes: List[str]
    automation_level: str
    collaboration_tools: List[str]
    quality_gates: List[str]
    deployment_pipeline: List[str]

class EcosystemAnalyzer:
    """Comprehensive ecosystem analyzer for development environments."""
    
    def __init__(self):
        self.system_info = self._analyze_system_environment()
        self.mcp_servers = self._analyze_mcp_servers()
        self.ai_frameworks = self._load_ai_framework_database()
        self.architecture_patterns = self._load_architecture_patterns()
        self.workflow_templates = self._load_workflow_templates()
    
    def analyze_complete_ecosystem(self, project_requirements: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze the complete development ecosystem."""
        print("🔍 Analyzing complete development ecosystem...")
        
        # Analyze system environment
        system_env = self._analyze_system_environment()
        
        # Analyze project requirements
        project_analysis = self._analyze_project_requirements(project_requirements)
        
        # Recommend MCP servers
        mcp_recommendations = self._recommend_mcp_servers(project_analysis, system_env)
        
        # Recommend AI frameworks
        ai_recommendations = self._recommend_ai_frameworks(project_analysis, system_env)
        
        # Recommend technology stack
        tech_stack = self._recommend_technology_stack(project_analysis, system_env)
        
        # Recommend architecture
        architecture = self._recommend_architecture(project_analysis, system_env)
        
        # Recommend workflow
        workflow = self._recommend_workflow(project_analysis, system_env)
        
        # Generate optimal configuration
        optimal_config = self._generate_optimal_configuration(
            system_env, mcp_recommendations, ai_recommendations, 
            tech_stack, architecture, workflow, project_analysis
        )
        
        return optimal_config
    
    def _analyze_system_environment(self) -> SystemEnvironment:
        """Analyze the current system environment."""
        print("🖥️ Analyzing system environment...")
        
        # Detect operating system
        os_type = self._detect_operating_system()
        
        # Detect development environment
        dev_env = self._detect_development_environment()
        
        # Check WSL
        wsl_distro = self._detect_wsl_distro()
        
        # Check Docker
        docker_available = self._check_docker_availability()
        container_runtime = self._detect_container_runtime()
        
        # Get shell and package manager
        shell = os.environ.get('SHELL', '/bin/bash').split('/')[-1]
        package_manager = self._detect_package_manager()
        
        # Get language versions
        python_version = self._get_python_version()
        node_version = self._get_node_version()
        
        # Get available tools
        available_tools = self._detect_available_tools()
        
        # Get system resources
        system_resources = self._analyze_system_resources()
        
        return SystemEnvironment(
            os_type=os_type,
            development_env=dev_env,
            wsl_distro=wsl_distro,
            docker_available=docker_available,
            container_runtime=container_runtime,
            shell=shell,
            package_manager=package_manager,
            python_version=python_version,
            node_version=node_version,
            available_tools=available_tools,
            system_resources=system_resources
        )
    
    def _detect_operating_system(self) -> OperatingSystem:
        """Detect the operating system type."""
        system = platform.system().lower()
        
        if system == "windows":
            # Check if running in WSL
            if "microsoft" in platform.release().lower():
                return OperatingSystem.WINDOWS_WSL
            return OperatingSystem.WINDOWS
        elif system == "linux":
            # Check if running in Docker
            if os.path.exists("/.dockerenv"):
                return OperatingSystem.DOCKER
            return OperatingSystem.LINUX
        elif system == "darwin":
            return OperatingSystem.MACOS
        
        return OperatingSystem.LINUX
    
    def _detect_development_environment(self) -> DevelopmentEnvironment:
        """Detect the development environment."""
        if os.path.exists("/.dockerenv"):
            return DevelopmentEnvironment.DOCKER
        elif "microsoft" in platform.release().lower():
            return DevelopmentEnvironment.WSL
        elif os.environ.get('VIRTUAL_ENV') or os.environ.get('CONDA_DEFAULT_ENV'):
            return DevelopmentEnvironment.LOCAL
        else:
            return DevelopmentEnvironment.LOCAL
    
    def _detect_wsl_distro(self) -> Optional[str]:
        """Detect WSL distribution."""
        if "microsoft" in platform.release().lower():
            try:
                with open("/etc/os-release", "r") as f:
                    content = f.read()
                    if "ubuntu" in content.lower():
                        return "ubuntu"
                    elif "debian" in content.lower():
                        return "debian"
                    elif "fedora" in content.lower():
                        return "fedora"
            except:
                pass
        return None
    
    def _check_docker_availability(self) -> bool:
        """Check if Docker is available."""
        try:
            result = subprocess.run(["docker", "--version"], 
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except:
            return False
    
    def _detect_container_runtime(self) -> Optional[str]:
        """Detect container runtime."""
        if self._check_docker_availability():
            return "docker"
        elif subprocess.run(["podman", "--version"], capture_output=True).returncode == 0:
            return "podman"
        elif subprocess.run(["containerd", "--version"], capture_output=True).returncode == 0:
            return "containerd"
        return None
    
    def _detect_package_manager(self) -> str:
        """Detect package manager."""
        if subprocess.run(["apt", "--version"], capture_output=True).returncode == 0:
            return "apt"
        elif subprocess.run(["yum", "--version"], capture_output=True).returncode == 0:
            return "yum"
        elif subprocess.run(["dnf", "--version"], capture_output=True).returncode == 0:
            return "dnf"
        elif subprocess.run(["pacman", "--version"], capture_output=True).returncode == 0:
            return "pacman"
        elif subprocess.run(["brew", "--version"], capture_output=True).returncode == 0:
            return "brew"
        elif subprocess.run(["choco", "--version"], capture_output=True).returncode == 0:
            return "chocolatey"
        else:
            return "unknown"
    
    def _get_python_version(self) -> str:
        """Get Python version."""
        try:
            result = subprocess.run(["python3", "--version"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return result.stdout.strip()
        except:
            pass
        
        try:
            result = subprocess.run(["python", "--version"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return result.stdout.strip()
        except:
            pass
        
        return "unknown"
    
    def _get_node_version(self) -> Optional[str]:
        """Get Node.js version."""
        try:
            result = subprocess.run(["node", "--version"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return result.stdout.strip()
        except:
            pass
        return None
    
    def _detect_available_tools(self) -> List[str]:
        """Detect available development tools."""
        tools = []
        
        # Check for common development tools
        tool_commands = {
            "git": "git --version",
            "docker": "docker --version",
            "kubectl": "kubectl version --client",
            "terraform": "terraform --version",
            "ansible": "ansible --version",
            "vagrant": "vagrant --version",
            "vscode": "code --version",
            "vim": "vim --version",
            "emacs": "emacs --version",
            "curl": "curl --version",
            "wget": "wget --version",
            "jq": "jq --version",
            "yq": "yq --version",
            "helm": "helm version",
            "kustomize": "kustomize version",
            "skaffold": "skaffold version",
            "minikube": "minikube version",
            "kind": "kind version",
            "k3s": "k3s --version",
            "podman": "podman --version",
            "buildah": "buildah --version",
            "skopeo": "skopeo --version"
        }
        
        for tool, command in tool_commands.items():
            try:
                result = subprocess.run(command.split(), 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    tools.append(tool)
            except:
                pass
        
        return tools
    
    def _analyze_system_resources(self) -> Dict[str, Any]:
        """Analyze system resources."""
        try:
            return {
                "cpu_count": psutil.cpu_count(),
                "memory_total_gb": round(psutil.virtual_memory().total / (1024**3), 2),
                "memory_available_gb": round(psutil.virtual_memory().available / (1024**3), 2),
                "disk_total_gb": round(psutil.disk_usage('/').total / (1024**3), 2),
                "disk_free_gb": round(psutil.disk_usage('/').free / (1024**3), 2),
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent
            }
        except:
            return {
                "cpu_count": 1,
                "memory_total_gb": 4.0,
                "memory_available_gb": 2.0,
                "disk_total_gb": 100.0,
                "disk_free_gb": 50.0,
                "cpu_percent": 0.0,
                "memory_percent": 0.0
            }
    
    def _analyze_mcp_servers(self) -> List[MCPConfiguration]:
        """Analyze available MCP servers."""
        print("🔌 Analyzing MCP servers...")
        
        # This would typically read from MCP configuration files
        # For now, return a comprehensive list of available MCP servers
        mcp_servers = [
            MCPConfiguration(
                server_name="chrome-devtools",
                category=MCPCategory.BROWSER_AUTOMATION,
                tools_count=27,
                enabled=True,
                priority=1,
                use_cases=["debugging", "performance_analysis", "network_inspection"],
                dependencies=["chrome"],
                resource_usage={"memory_mb": 200, "cpu_percent": 5}
            ),
            MCPConfiguration(
                server_name="playwright",
                category=MCPCategory.BROWSER_AUTOMATION,
                tools_count=21,
                enabled=True,
                priority=2,
                use_cases=["cross_browser_testing", "mobile_testing", "screenshot_analysis"],
                dependencies=["node", "browsers"],
                resource_usage={"memory_mb": 150, "cpu_percent": 3}
            ),
            MCPConfiguration(
                server_name="browser",
                category=MCPCategory.BROWSER_AUTOMATION,
                tools_count=21,
                enabled=True,
                priority=3,
                use_cases=["simple_automation", "form_filling", "data_extraction"],
                dependencies=["browser"],
                resource_usage={"memory_mb": 100, "cpu_percent": 2}
            ),
            MCPConfiguration(
                server_name="web-search",
                category=MCPCategory.DEVELOPMENT,
                tools_count=4,
                enabled=True,
                priority=4,
                use_cases=["research", "information_gathering", "market_analysis"],
                dependencies=["internet"],
                resource_usage={"memory_mb": 50, "cpu_percent": 1}
            ),
            MCPConfiguration(
                server_name="github-search",
                category=MCPCategory.VERSION_CONTROL,
                tools_count=8,
                enabled=False,
                priority=5,
                use_cases=["code_search", "repository_analysis", "issue_tracking"],
                dependencies=["github_api"],
                resource_usage={"memory_mb": 30, "cpu_percent": 1}
            ),
            MCPConfiguration(
                server_name="filesystem",
                category=MCPCategory.FILE_SYSTEM,
                tools_count=12,
                enabled=True,
                priority=6,
                use_cases=["file_management", "project_structure", "backup"],
                dependencies=["filesystem"],
                resource_usage={"memory_mb": 20, "cpu_percent": 0.5}
            ),
            MCPConfiguration(
                server_name="slack",
                category=MCPCategory.COMMUNICATION,
                tools_count=6,
                enabled=False,
                priority=7,
                use_cases=["team_communication", "notifications", "collaboration"],
                dependencies=["slack_api"],
                resource_usage={"memory_mb": 40, "cpu_percent": 1}
            ),
            MCPConfiguration(
                server_name="postgres",
                category=MCPCategory.DATABASE,
                tools_count=15,
                enabled=False,
                priority=8,
                use_cases=["database_management", "query_execution", "schema_analysis"],
                dependencies=["postgresql"],
                resource_usage={"memory_mb": 300, "cpu_percent": 10}
            )
        ]
        
        return mcp_servers
    
    def _load_ai_framework_database(self) -> Dict[AIFramework, AIFrameworkConfig]:
        """Load AI framework database."""
        return {
            AIFramework.BMAD: AIFrameworkConfig(
                framework=AIFramework.BMAD,
                version="latest",
                capabilities=["agent_orchestration", "task_planning", "multi_agent_coordination"],
                best_for=["complex_workflows", "enterprise_automation", "multi_step_tasks"],
                resource_requirements={"memory_gb": 4, "cpu_cores": 2},
                integration_complexity="high",
                community_support="growing"
            ),
            AIFramework.GITHUB_SPEC_KIT: AIFrameworkConfig(
                framework=AIFramework.GITHUB_SPEC_KIT,
                version="latest",
                capabilities=["code_generation", "repository_management", "ci_cd_integration"],
                best_for=["github_workflows", "code_automation", "repository_management"],
                resource_requirements={"memory_gb": 2, "cpu_cores": 1},
                integration_complexity="medium",
                community_support="strong"
            ),
            AIFramework.LANGCHAIN: AIFrameworkConfig(
                framework=AIFramework.LANGCHAIN,
                version="0.1.0",
                capabilities=["llm_integration", "chain_construction", "memory_management"],
                best_for=["llm_applications", "conversational_ai", "document_processing"],
                resource_requirements={"memory_gb": 1, "cpu_cores": 1},
                integration_complexity="low",
                community_support="very_strong"
            ),
            AIFramework.LANGGRAPH: AIFrameworkConfig(
                framework=AIFramework.LANGGRAPH,
                version="latest",
                capabilities=["graph_based_workflows", "state_management", "conditional_logic"],
                best_for=["complex_workflows", "stateful_applications", "decision_trees"],
                resource_requirements={"memory_gb": 2, "cpu_cores": 1},
                integration_complexity="medium",
                community_support="strong"
            ),
            AIFramework.AUTOGEN: AIFrameworkConfig(
                framework=AIFramework.AUTOGEN,
                version="latest",
                capabilities=["multi_agent_conversation", "agent_negotiation", "collaborative_problem_solving"],
                best_for=["multi_agent_systems", "collaborative_ai", "conversational_workflows"],
                resource_requirements={"memory_gb": 3, "cpu_cores": 2},
                integration_complexity="high",
                community_support="moderate"
            ),
            AIFramework.CREWAI: AIFrameworkConfig(
                framework=AIFramework.CREWAI,
                version="latest",
                capabilities=["crew_management", "task_delegation", "agent_specialization"],
                best_for=["specialized_agents", "task_orchestration", "role_based_automation"],
                resource_requirements={"memory_gb": 2, "cpu_cores": 1},
                integration_complexity="medium",
                community_support="growing"
            )
        }
    
    def _load_architecture_patterns(self) -> Dict[ArchitecturePattern, Dict[str, Any]]:
        """Load architecture pattern database."""
        return {
            ArchitecturePattern.MONOLITH: {
                "description": "Single deployable unit with all functionality",
                "best_for": ["small_teams", "simple_applications", "rapid_prototyping"],
                "scalability": "vertical",
                "complexity": "low",
                "deployment": "simple",
                "technologies": ["express", "django", "rails", "spring_boot"]
            },
            ArchitecturePattern.MICROSERVICES: {
                "description": "Multiple independent services communicating over network",
                "best_for": ["large_teams", "complex_applications", "independent_scaling"],
                "scalability": "horizontal",
                "complexity": "high",
                "deployment": "complex",
                "technologies": ["docker", "kubernetes", "service_mesh", "api_gateway"]
            },
            ArchitecturePattern.SERVERLESS: {
                "description": "Event-driven functions without server management",
                "best_for": ["event_processing", "sporadic_workloads", "cost_optimization"],
                "scalability": "automatic",
                "complexity": "medium",
                "deployment": "simple",
                "technologies": ["aws_lambda", "azure_functions", "google_cloud_functions"]
            },
            ArchitecturePattern.EVENT_DRIVEN: {
                "description": "Asynchronous communication through events",
                "best_for": ["real_time_applications", "loose_coupling", "scalable_systems"],
                "scalability": "horizontal",
                "complexity": "high",
                "deployment": "complex",
                "technologies": ["kafka", "rabbitmq", "event_sourcing", "cqrs"]
            },
            ArchitecturePattern.CLEAN_ARCHITECTURE: {
                "description": "Dependency inversion with clear separation of concerns",
                "best_for": ["maintainable_code", "testable_systems", "long_term_projects"],
                "scalability": "moderate",
                "complexity": "medium",
                "deployment": "moderate",
                "technologies": ["dependency_injection", "interfaces", "layers"]
            }
        }
    
    def _load_workflow_templates(self) -> Dict[DevelopmentStage, Dict[str, Any]]:
        """Load workflow templates for different development stages."""
        return {
            DevelopmentStage.CONCEPT: {
                "tools": ["browser_automation", "web_search", "filesystem"],
                "processes": ["research", "prototyping", "validation"],
                "automation_level": "low",
                "collaboration_tools": ["slack", "github"],
                "quality_gates": ["concept_validation"],
                "deployment_pipeline": ["local_testing"]
            },
            DevelopmentStage.PROTOTYPE: {
                "tools": ["browser_automation", "playwright", "filesystem", "github_search"],
                "processes": ["rapid_development", "user_feedback", "iteration"],
                "automation_level": "medium",
                "collaboration_tools": ["slack", "github", "figma"],
                "quality_gates": ["prototype_review", "user_validation"],
                "deployment_pipeline": ["local_testing", "staging_deployment"]
            },
            DevelopmentStage.MVP: {
                "tools": ["chrome_devtools", "playwright", "filesystem", "github_search", "postgres"],
                "processes": ["agile_development", "continuous_integration", "user_testing"],
                "automation_level": "high",
                "collaboration_tools": ["slack", "github", "jira", "confluence"],
                "quality_gates": ["code_review", "automated_testing", "user_acceptance"],
                "deployment_pipeline": ["ci_cd", "staging", "production"]
            },
            DevelopmentStage.BETA: {
                "tools": ["chrome_devtools", "playwright", "filesystem", "github_search", "postgres", "monitoring"],
                "processes": ["beta_testing", "performance_optimization", "security_auditing"],
                "automation_level": "very_high",
                "collaboration_tools": ["slack", "github", "jira", "confluence", "datadog"],
                "quality_gates": ["performance_testing", "security_scanning", "beta_feedback"],
                "deployment_pipeline": ["ci_cd", "staging", "beta_production", "rollback"]
            },
            DevelopmentStage.PRODUCTION: {
                "tools": ["chrome_devtools", "playwright", "filesystem", "github_search", "postgres", "monitoring", "alerting"],
                "processes": ["production_support", "monitoring", "optimization", "maintenance"],
                "automation_level": "maximum",
                "collaboration_tools": ["slack", "github", "jira", "confluence", "datadog", "pagerduty"],
                "quality_gates": ["production_readiness", "security_compliance", "performance_sla"],
                "deployment_pipeline": ["ci_cd", "blue_green", "canary", "rollback", "monitoring"]
            }
        }
    
    def _analyze_project_requirements(self, requirements: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze project requirements to determine optimal configurations."""
        analysis = {
            "complexity": requirements.get("complexity", "medium"),
            "team_size": requirements.get("team_size", 3),
            "timeline": requirements.get("timeline", "flexible"),
            "budget": requirements.get("budget", "medium"),
            "scalability_needs": requirements.get("scalability_needs", "moderate"),
            "security_requirements": requirements.get("security_requirements", "standard"),
            "compliance_needs": requirements.get("compliance_needs", []),
            "integration_complexity": requirements.get("integration_complexity", "medium"),
            "ai_requirements": requirements.get("ai_requirements", "basic"),
            "automation_level": requirements.get("automation_level", "medium")
        }
        return analysis
    
    def _recommend_mcp_servers(self, project_analysis: Dict[str, Any], 
                             system_env: SystemEnvironment) -> List[MCPConfiguration]:
        """Recommend optimal MCP servers based on project and system analysis."""
        recommendations = []
        
        # Always include core servers
        core_servers = ["filesystem", "web_search"]
        for server in self.mcp_servers:
            if server.server_name in core_servers:
                recommendations.append(server)
        
        # Add browser automation based on project needs
        if project_analysis.get("automation_level") in ["high", "very_high", "maximum"]:
            if project_analysis.get("complexity") == "high":
                # Use Playwright for complex automation
                playwright_server = next(s for s in self.mcp_servers if s.server_name == "playwright")
                recommendations.append(playwright_server)
            else:
                # Use simple browser automation
                browser_server = next(s for s in self.mcp_servers if s.server_name == "browser")
                recommendations.append(browser_server)
        
        # Add Chrome DevTools for debugging and analysis
        if project_analysis.get("complexity") in ["high", "very_high"]:
            chrome_server = next(s for s in self.mcp_servers if s.server_name == "chrome-devtools")
            recommendations.append(chrome_server)
        
        # Add database server if needed
        if project_analysis.get("integration_complexity") in ["high", "very_high"]:
            postgres_server = next(s for s in self.mcp_servers if s.server_name == "postgres")
            recommendations.append(postgres_server)
        
        # Add communication tools for team collaboration
        if project_analysis.get("team_size", 1) > 3:
            slack_server = next(s for s in self.mcp_servers if s.server_name == "slack")
            recommendations.append(slack_server)
        
        # Add GitHub search for code management
        if project_analysis.get("automation_level") in ["high", "very_high", "maximum"]:
            github_server = next(s for s in self.mcp_servers if s.server_name == "github-search")
            recommendations.append(github_server)
        
        return recommendations
    
    def _recommend_ai_frameworks(self, project_analysis: Dict[str, Any], 
                               system_env: SystemEnvironment) -> List[AIFrameworkConfig]:
        """Recommend optimal AI frameworks based on project requirements."""
        recommendations = []
        
        ai_requirements = project_analysis.get("ai_requirements", "basic")
        complexity = project_analysis.get("complexity", "medium")
        team_size = project_analysis.get("team_size", 3)
        
        # Basic AI requirements
        if ai_requirements == "basic":
            langchain = self.ai_frameworks[AIFramework.LANGCHAIN]
            recommendations.append(langchain)
        
        # Advanced AI requirements
        elif ai_requirements in ["advanced", "enterprise"]:
            if complexity == "high" and team_size > 5:
                # Use BMAD for complex enterprise workflows
                bmad = self.ai_frameworks[AIFramework.BMAD]
                recommendations.append(bmad)
            else:
                # Use LangGraph for complex workflows
                langgraph = self.ai_frameworks[AIFramework.LANGGRAPH]
                recommendations.append(langgraph)
            
            # Add specialized frameworks
            if project_analysis.get("integration_complexity") == "high":
                autogen = self.ai_frameworks[AIFramework.AUTOGEN]
                recommendations.append(autogen)
        
        # GitHub-specific requirements
        if project_analysis.get("platform_preference") == "github":
            spec_kit = self.ai_frameworks[AIFramework.GITHUB_SPEC_KIT]
            recommendations.append(spec_kit)
        
        return recommendations
    
    def _recommend_technology_stack(self, project_analysis: Dict[str, Any], 
                                  system_env: SystemEnvironment) -> TechnologyStack:
        """Recommend optimal technology stack."""
        
        # Base recommendations
        programming_languages = ["python", "javascript"]
        frameworks = []
        databases = ["postgresql"]
        caching = ["redis"]
        messaging = []
        monitoring = ["prometheus", "grafana"]
        testing = ["pytest", "jest"]
        deployment = ["docker"]
        ai_frameworks = []
        mcp_servers = []
        
        # Adjust based on system environment
        if system_env.os_type == OperatingSystem.WINDOWS_WSL:
            programming_languages.append("bash")
            frameworks.extend(["node", "npm"])
        elif system_env.os_type == OperatingSystem.LINUX:
            programming_languages.extend(["bash", "shell"])
        
        # Adjust based on project complexity
        if project_analysis.get("complexity") == "high":
            frameworks.extend(["fastapi", "react", "typescript"])
            databases.extend(["mongodb", "elasticsearch"])
            messaging.extend(["kafka", "rabbitmq"])
            deployment.extend(["kubernetes", "terraform"])
        else:
            frameworks.extend(["flask", "express"])
        
        # Adjust based on scalability needs
        if project_analysis.get("scalability_needs") == "high":
            deployment.extend(["kubernetes", "helm", "istio"])
            monitoring.extend(["datadog", "new_relic"])
        
        # Adjust based on security requirements
        if project_analysis.get("security_requirements") == "high":
            frameworks.extend(["oauth2", "jwt"])
            monitoring.extend(["security_scanner", "vault"])
        
        return TechnologyStack(
            programming_languages=programming_languages,
            frameworks=frameworks,
            databases=databases,
            caching=caching,
            messaging=messaging,
            monitoring=monitoring,
            testing=testing,
            deployment=deployment,
            ai_frameworks=ai_frameworks,
            mcp_servers=mcp_servers
        )
    
    def _recommend_architecture(self, project_analysis: Dict[str, Any], 
                              system_env: SystemEnvironment) -> ArchitectureRecommendation:
        """Recommend optimal architecture pattern."""
        
        complexity = project_analysis.get("complexity", "medium")
        team_size = project_analysis.get("team_size", 3)
        scalability_needs = project_analysis.get("scalability_needs", "moderate")
        
        if complexity == "low" and team_size <= 3:
            pattern = ArchitecturePattern.MONOLITH
            reasoning = "Simple project with small team - monolith provides simplicity and speed"
        elif complexity == "high" and team_size > 5:
            pattern = ArchitecturePattern.MICROSERVICES
            reasoning = "Complex project with large team - microservices enable independent development"
        elif scalability_needs == "high":
            pattern = ArchitecturePattern.EVENT_DRIVEN
            reasoning = "High scalability needs - event-driven architecture provides better scaling"
        else:
            pattern = ArchitecturePattern.CLEAN_ARCHITECTURE
            reasoning = "Balanced approach - clean architecture provides maintainability and flexibility"
        
        return ArchitectureRecommendation(
            pattern=pattern,
            reasoning=reasoning,
            components=self.architecture_patterns[pattern]["technologies"],
            data_flow="request-response" if pattern == ArchitecturePattern.MONOLITH else "event-driven",
            scalability_approach=self.architecture_patterns[pattern]["scalability"],
            security_considerations=["authentication", "authorization", "encryption"],
            deployment_strategy=self.architecture_patterns[pattern]["deployment"]
        )
    
    def _recommend_workflow(self, project_analysis: Dict[str, Any], 
                          system_env: SystemEnvironment) -> WorkflowRecommendation:
        """Recommend optimal development workflow."""
        
        # Determine development stage
        if project_analysis.get("timeline") == "aggressive":
            stage = DevelopmentStage.MVP
        elif project_analysis.get("complexity") == "high":
            stage = DevelopmentStage.BETA
        else:
            stage = DevelopmentStage.PROTOTYPE
        
        # Get workflow template
        workflow_template = self.workflow_templates[stage]
        
        return WorkflowRecommendation(
            stage=stage,
            tools=workflow_template["tools"],
            processes=workflow_template["processes"],
            automation_level=workflow_template["automation_level"],
            collaboration_tools=workflow_template["collaboration_tools"],
            quality_gates=workflow_template["quality_gates"],
            deployment_pipeline=workflow_template["deployment_pipeline"]
        )
    
    def _generate_optimal_configuration(self, system_env: SystemEnvironment,
                                      mcp_recommendations: List[MCPConfiguration],
                                      ai_recommendations: List[AIFrameworkConfig],
                                      tech_stack: TechnologyStack,
                                      architecture: ArchitectureRecommendation,
                                      workflow: WorkflowRecommendation,
                                      project_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate the complete optimal configuration."""
        
        return {
            "system_environment": asdict(system_env),
            "mcp_servers": [asdict(server) for server in mcp_recommendations],
            "ai_frameworks": [asdict(framework) for framework in ai_recommendations],
            "technology_stack": asdict(tech_stack),
            "architecture": asdict(architecture),
            "workflow": asdict(workflow),
            "project_analysis": project_analysis,
            "recommendations": {
                "os_optimization": self._get_os_optimization_recommendations(system_env),
                "mcp_optimization": self._get_mcp_optimization_recommendations(mcp_recommendations),
                "ai_optimization": self._get_ai_optimization_recommendations(ai_recommendations),
                "workflow_optimization": self._get_workflow_optimization_recommendations(workflow)
            },
            "setup_instructions": self._generate_setup_instructions(system_env, mcp_recommendations, ai_recommendations),
            "estimated_resources": self._calculate_resource_requirements(mcp_recommendations, ai_recommendations),
            "compatibility_matrix": self._generate_compatibility_matrix(system_env, mcp_recommendations, ai_recommendations)
        }
    
    def _get_os_optimization_recommendations(self, system_env: SystemEnvironment) -> List[str]:
        """Get OS-specific optimization recommendations."""
        recommendations = []
        
        if system_env.os_type == OperatingSystem.WINDOWS_WSL:
            recommendations.extend([
                "Use WSL2 for better performance",
                "Enable Docker Desktop with WSL2 backend",
                "Configure VS Code with WSL extension",
                "Set up proper file permissions for cross-platform compatibility"
            ])
        elif system_env.os_type == OperatingSystem.LINUX:
            recommendations.extend([
                "Use systemd for service management",
                "Configure proper user permissions",
                "Set up firewall rules for development ports",
                "Enable swap if memory is limited"
            ])
        elif system_env.os_type == OperatingSystem.MACOS:
            recommendations.extend([
                "Use Homebrew for package management",
                "Configure proper security settings",
                "Set up Xcode command line tools",
                "Enable developer mode for advanced features"
            ])
        
        return recommendations
    
    def _get_mcp_optimization_recommendations(self, mcp_servers: List[MCPConfiguration]) -> List[str]:
        """Get MCP optimization recommendations."""
        recommendations = []
        
        total_memory = sum(server.resource_usage.get("memory_mb", 0) for server in mcp_servers)
        total_cpu = sum(server.resource_usage.get("cpu_percent", 0) for server in mcp_servers)
        
        if total_memory > 1000:
            recommendations.append("Consider disabling non-essential MCP servers to reduce memory usage")
        
        if total_cpu > 20:
            recommendations.append("Monitor CPU usage and consider load balancing for MCP servers")
        
        # Specific recommendations
        browser_servers = [s for s in mcp_servers if s.category == MCPCategory.BROWSER_AUTOMATION]
        if len(browser_servers) > 1:
            recommendations.append("Use only one browser automation server to avoid conflicts")
        
        return recommendations
    
    def _get_ai_optimization_recommendations(self, ai_frameworks: List[AIFrameworkConfig]) -> List[str]:
        """Get AI framework optimization recommendations."""
        recommendations = []
        
        total_memory = sum(framework.resource_requirements.get("memory_gb", 0) for framework in ai_frameworks)
        total_cpu = sum(framework.resource_requirements.get("cpu_cores", 0) for framework in ai_frameworks)
        
        if total_memory > 8:
            recommendations.append("Consider using cloud-based AI services for memory-intensive frameworks")
        
        if total_cpu > 4:
            recommendations.append("Monitor CPU usage and consider distributed processing")
        
        # Framework-specific recommendations
        for framework in ai_frameworks:
            if framework.integration_complexity == "high":
                recommendations.append(f"Plan extra time for {framework.framework.value} integration")
        
        return recommendations
    
    def _get_workflow_optimization_recommendations(self, workflow: WorkflowRecommendation) -> List[str]:
        """Get workflow optimization recommendations."""
        recommendations = []
        
        if workflow.automation_level == "low":
            recommendations.append("Consider increasing automation level for better efficiency")
        
        if len(workflow.tools) > 10:
            recommendations.append("Consider consolidating tools to reduce complexity")
        
        if workflow.stage in [DevelopmentStage.PRODUCTION, DevelopmentStage.SCALE]:
            recommendations.append("Implement comprehensive monitoring and alerting")
            recommendations.append("Set up automated backup and disaster recovery")
        
        return recommendations
    
    def _generate_setup_instructions(self, system_env: SystemEnvironment,
                                   mcp_servers: List[MCPConfiguration],
                                   ai_frameworks: List[AIFrameworkConfig]) -> Dict[str, List[str]]:
        """Generate setup instructions for the recommended configuration."""
        
        instructions = {
            "system_setup": [],
            "mcp_setup": [],
            "ai_framework_setup": [],
            "development_environment": []
        }
        
        # System setup
        if system_env.os_type == OperatingSystem.WINDOWS_WSL:
            instructions["system_setup"].extend([
                "Install WSL2 with Ubuntu distribution",
                "Install Docker Desktop with WSL2 backend",
                "Install VS Code with WSL extension",
                "Configure Windows Terminal for better development experience"
            ])
        
        # MCP setup
        for server in mcp_servers:
            if server.server_name == "chrome-devtools":
                instructions["mcp_setup"].extend([
                    "Install Google Chrome browser",
                    "Enable Chrome DevTools Protocol",
                    "Configure MCP server with Chrome instance"
                ])
            elif server.server_name == "playwright":
                instructions["mcp_setup"].extend([
                    "Install Playwright: npm install playwright",
                    "Install browser dependencies: npx playwright install",
                    "Configure MCP server with Playwright"
                ])
        
        # AI framework setup
        for framework in ai_frameworks:
            if framework.framework == AIFramework.LANGCHAIN:
                instructions["ai_framework_setup"].extend([
                    "Install LangChain: pip install langchain",
                    "Install required dependencies: pip install langchain-community",
                    "Set up environment variables for API keys"
                ])
            elif framework.framework == AIFramework.BMAD:
                instructions["ai_framework_setup"].extend([
                    "Install BMAD framework",
                    "Configure agent definitions",
                    "Set up orchestration environment"
                ])
        
        return instructions
    
    def _calculate_resource_requirements(self, mcp_servers: List[MCPConfiguration],
                                       ai_frameworks: List[AIFrameworkConfig]) -> Dict[str, Any]:
        """Calculate total resource requirements."""
        
        total_memory_mb = sum(server.resource_usage.get("memory_mb", 0) for server in mcp_servers)
        total_cpu_percent = sum(server.resource_usage.get("cpu_percent", 0) for server in mcp_servers)
        
        total_ai_memory_gb = sum(framework.resource_requirements.get("memory_gb", 0) for framework in ai_frameworks)
        total_ai_cpu_cores = sum(framework.resource_requirements.get("cpu_cores", 0) for framework in ai_frameworks)
        
        return {
            "mcp_servers": {
                "memory_mb": total_memory_mb,
                "cpu_percent": total_cpu_percent
            },
            "ai_frameworks": {
                "memory_gb": total_ai_memory_gb,
                "cpu_cores": total_ai_cpu_cores
            },
            "total_estimated": {
                "memory_gb": round((total_memory_mb / 1024) + total_ai_memory_gb, 2),
                "cpu_cores": max(total_ai_cpu_cores, round(total_cpu_percent / 25))  # Rough estimate
            }
        }
    
    def _generate_compatibility_matrix(self, system_env: SystemEnvironment,
                                     mcp_servers: List[MCPConfiguration],
                                     ai_frameworks: List[AIFrameworkConfig]) -> Dict[str, Any]:
        """Generate compatibility matrix for the recommended configuration."""
        
        compatibility = {
            "os_compatibility": {
                "windows_wsl": system_env.os_type == OperatingSystem.WINDOWS_WSL,
                "linux": system_env.os_type == OperatingSystem.LINUX,
                "macos": system_env.os_type == OperatingSystem.MACOS
            },
            "mcp_compatibility": {
                server.server_name: {
                    "os_support": ["linux", "macos", "windows"],
                    "python_version": "3.8+",
                    "node_version": "16+" if server.server_name in ["playwright", "browser"] else None
                }
                for server in mcp_servers
            },
            "ai_framework_compatibility": {
                framework.framework.value: {
                    "os_support": ["linux", "macos", "windows"],
                    "python_version": "3.8+",
                    "memory_requirement_gb": framework.resource_requirements.get("memory_gb", 1)
                }
                for framework in ai_frameworks
            }
        }
        
        return compatibility

def main():
    """Main ecosystem analyzer demo."""
    print("🌍 ECOSYSTEM ANALYZER DEMO")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = EcosystemAnalyzer()
    
    # Sample project requirements
    project_requirements = {
        "complexity": "high",
        "team_size": 5,
        "timeline": "flexible",
        "budget": "medium",
        "scalability_needs": "high",
        "security_requirements": "high",
        "compliance_needs": ["gdpr"],
        "integration_complexity": "high",
        "ai_requirements": "advanced",
        "automation_level": "very_high",
        "platform_preference": "github"
    }
    
    # Analyze complete ecosystem
    ecosystem_config = analyzer.analyze_complete_ecosystem(project_requirements)
    
    # Print results
    print(f"\n🖥️ System Environment:")
    print(f"   OS: {ecosystem_config['system_environment']['os_type']}")
    print(f"   Development Environment: {ecosystem_config['system_environment']['development_env']}")
    print(f"   WSL Distro: {ecosystem_config['system_environment']['wsl_distro']}")
    print(f"   Docker Available: {ecosystem_config['system_environment']['docker_available']}")
    
    print(f"\n🔌 Recommended MCP Servers:")
    for server in ecosystem_config['mcp_servers']:
        print(f"   {server['server_name']}: {server['tools_count']} tools, {server['category']}")
    
    print(f"\n🤖 Recommended AI Frameworks:")
    for framework in ecosystem_config['ai_frameworks']:
        print(f"   {framework['framework']}: {framework['integration_complexity']} complexity")
    
    print(f"\n🏗️ Recommended Architecture:")
    print(f"   Pattern: {ecosystem_config['architecture']['pattern']}")
    print(f"   Reasoning: {ecosystem_config['architecture']['reasoning']}")
    
    print(f"\n⚡ Resource Requirements:")
    resources = ecosystem_config['estimated_resources']
    print(f"   Total Memory: {resources['total_estimated']['memory_gb']} GB")
    print(f"   Total CPU Cores: {resources['total_estimated']['cpu_cores']}")
    
    # Save configuration
    with open("ecosystem_configuration.json", "w") as f:
        json.dump(ecosystem_config, f, indent=2, default=str)
    
    print(f"\n📄 Complete ecosystem configuration saved: ecosystem_configuration.json")
    print("✅ Ecosystem Analyzer Demo Complete!")

if __name__ == "__main__":
    main()
