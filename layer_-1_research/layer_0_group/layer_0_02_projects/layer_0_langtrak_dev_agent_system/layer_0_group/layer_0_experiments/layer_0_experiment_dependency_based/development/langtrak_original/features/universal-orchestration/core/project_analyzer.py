#!/usr/bin/env python3
# resource_id: "1317ba07-869d-4818-980b-194fb909a737"
# resource_type: "document"
# resource_name: "project_analyzer"

"""
project_analyzer.py

Intelligent project analysis engine that determines optimal configurations
based on project characteristics, technology stack, and development stage.
"""

import os
import json
import subprocess
import re
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import yaml

class TechnologyStack(Enum):
    FRONTEND = "frontend"
    BACKEND = "backend"
    DATABASE = "database"
    CACHING = "caching"
    MESSAGING = "messaging"
    MONITORING = "monitoring"
    STORAGE = "storage"
    CDN = "cdn"
    CI_CD = "ci_cd"

class Framework(Enum):
    # Frontend Frameworks
    REACT = "react"
    VUE = "vue"
    ANGULAR = "angular"
    SVELTE = "svelte"
    NEXTJS = "nextjs"
    NUXT = "nuxt"
    
    # Backend Frameworks
    EXPRESS = "express"
    FASTAPI = "fastapi"
    FLASK = "flask"
    DJANGO = "django"
    SPRING = "spring"
    RAILS = "rails"
    LARAVEL = "laravel"
    
    # Mobile Frameworks
    REACT_NATIVE = "react_native"
    FLUTTER = "flutter"
    XAMARIN = "xamarin"
    IONIC = "ionic"
    
    # Database Frameworks
    PRISMA = "prisma"
    SEQUELIZE = "sequelize"
    TYPEORM = "typeorm"
    SQLALCHEMY = "sqlalchemy"

class DatabaseType(Enum):
    RELATIONAL = "relational"
    DOCUMENT = "document"
    KEY_VALUE = "key_value"
    GRAPH = "graph"
    TIME_SERIES = "time_series"
    SEARCH = "search"

@dataclass
class ProjectAnalysis:
    """Comprehensive project analysis results."""
    project_type: str
    development_stage: str
    technology_stack: List[TechnologyStack]
    frameworks: List[Framework]
    database_type: Optional[DatabaseType]
    programming_languages: List[str]
    build_tools: List[str]
    testing_frameworks: List[str]
    deployment_methods: List[str]
    infrastructure_requirements: List[str]
    performance_characteristics: Dict[str, Any]
    security_requirements: List[str]
    scalability_needs: Dict[str, Any]
    compliance_requirements: List[str]
    team_size_estimate: int
    complexity_score: int  # 1-10
    maturity_score: int    # 1-10

class ProjectAnalyzer:
    """Intelligent project analysis engine."""
    
    def __init__(self):
        self.analysis_patterns = self._load_analysis_patterns()
        self.framework_indicators = self._load_framework_indicators()
        self.technology_indicators = self._load_technology_indicators()
    
    def analyze_project(self, project_path: str) -> ProjectAnalysis:
        """Perform comprehensive project analysis."""
        print(f"🔍 Analyzing project at {project_path}...")
        
        # Analyze project structure
        project_type = self._analyze_project_type(project_path)
        development_stage = self._analyze_development_stage(project_path)
        technology_stack = self._analyze_technology_stack(project_path)
        frameworks = self._analyze_frameworks(project_path)
        database_type = self._analyze_database_type(project_path)
        programming_languages = self._analyze_programming_languages(project_path)
        build_tools = self._analyze_build_tools(project_path)
        testing_frameworks = self._analyze_testing_frameworks(project_path)
        deployment_methods = self._analyze_deployment_methods(project_path)
        infrastructure_requirements = self._analyze_infrastructure_requirements(project_path)
        performance_characteristics = self._analyze_performance_characteristics(project_path)
        security_requirements = self._analyze_security_requirements(project_path)
        scalability_needs = self._analyze_scalability_needs(project_path)
        compliance_requirements = self._analyze_compliance_requirements(project_path)
        team_size_estimate = self._estimate_team_size(project_path)
        complexity_score = self._calculate_complexity_score(project_path)
        maturity_score = self._calculate_maturity_score(project_path)
        
        analysis = ProjectAnalysis(
            project_type=project_type,
            development_stage=development_stage,
            technology_stack=technology_stack,
            frameworks=frameworks,
            database_type=database_type,
            programming_languages=programming_languages,
            build_tools=build_tools,
            testing_frameworks=testing_frameworks,
            deployment_methods=deployment_methods,
            infrastructure_requirements=infrastructure_requirements,
            performance_characteristics=performance_characteristics,
            security_requirements=security_requirements,
            scalability_needs=scalability_needs,
            compliance_requirements=compliance_requirements,
            team_size_estimate=team_size_estimate,
            complexity_score=complexity_score,
            maturity_score=maturity_score
        )
        
        print(f"✅ Project analysis complete: {project_type} in {development_stage} stage")
        return analysis
    
    def _analyze_project_type(self, project_path: str) -> str:
        """Analyze project type based on structure and files."""
        # Check for mobile app indicators
        if self._has_file_pattern(project_path, ["android/", "ios/", "*.apk", "*.ipa"]):
            return "mobile_application"
        
        # Check for API service indicators
        if self._has_file_pattern(project_path, ["api/", "routes/", "controllers/", "endpoints/"]):
            return "api_service"
        
        # Check for microservices indicators
        if self._has_file_pattern(project_path, ["services/", "microservices/", "docker-compose.yml"]):
            return "microservices"
        
        # Check for data pipeline indicators
        if self._has_file_pattern(project_path, ["pipeline/", "etl/", "data/", "*.py"]):
            return "data_pipeline"
        
        # Check for ML indicators
        if self._has_file_pattern(project_path, ["models/", "*.pkl", "*.h5", "*.pt", "*.onnx"]):
            return "machine_learning"
        
        # Check for blockchain indicators
        if self._has_file_pattern(project_path, ["contracts/", "*.sol", "*.vy", "truffle/"]):
            return "blockchain_application"
        
        # Check for game indicators
        if self._has_file_pattern(project_path, ["assets/", "sprites/", "*.unity", "*.godot"]):
            return "game_development"
        
        # Check for desktop app indicators
        if self._has_file_pattern(project_path, ["*.exe", "*.app", "*.dmg", "*.deb", "*.rpm"]):
            return "desktop_application"
        
        # Default to web application
        return "web_application"
    
    def _analyze_development_stage(self, project_path: str) -> str:
        """Analyze development stage based on project maturity."""
        # Check for production indicators
        if self._has_file_pattern(project_path, ["docker-compose.prod.yml", "k8s/", "terraform/"]):
            return "production"
        
        # Check for beta indicators
        if self._has_file_pattern(project_path, ["beta/", "preview/", "staging/"]):
            return "beta"
        
        # Check for MVP indicators
        if self._has_file_pattern(project_path, ["README.md", "docs/", "tests/"]):
            with open(os.path.join(project_path, "README.md"), 'r') as f:
                readme_content = f.read().lower()
                if "mvp" in readme_content or "minimum viable" in readme_content:
                    return "mvp"
        
        # Check for prototype indicators
        if self._has_file_pattern(project_path, ["prototype/", "demo/", "example/"]):
            return "prototype"
        
        # Check for concept indicators
        if self._has_file_pattern(project_path, ["concept/", "idea/", "notes/"]):
            return "concept"
        
        # Default to MVP
        return "mvp"
    
    def _analyze_technology_stack(self, project_path: str) -> List[TechnologyStack]:
        """Analyze technology stack components."""
        stack = []
        
        # Frontend analysis
        if self._has_file_pattern(project_path, ["src/", "public/", "static/", "*.html", "*.css", "*.js"]):
            stack.append(TechnologyStack.FRONTEND)
        
        # Backend analysis
        if self._has_file_pattern(project_path, ["server/", "api/", "backend/", "*.py", "*.js", "*.java", "*.go"]):
            stack.append(TechnologyStack.BACKEND)
        
        # Database analysis
        if self._has_file_pattern(project_path, ["*.sql", "migrations/", "schema/", "models/"]):
            stack.append(TechnologyStack.DATABASE)
        
        # Caching analysis
        if self._has_file_pattern(project_path, ["cache/", "redis/", "memcached/"]):
            stack.append(TechnologyStack.CACHING)
        
        # Messaging analysis
        if self._has_file_pattern(project_path, ["queue/", "messaging/", "kafka/", "rabbitmq/"]):
            stack.append(TechnologyStack.MESSAGING)
        
        # Monitoring analysis
        if self._has_file_pattern(project_path, ["monitoring/", "metrics/", "logs/", "prometheus/"]):
            stack.append(TechnologyStack.MONITORING)
        
        # Storage analysis
        if self._has_file_pattern(project_path, ["storage/", "uploads/", "files/", "media/"]):
            stack.append(TechnologyStack.STORAGE)
        
        # CDN analysis
        if self._has_file_pattern(project_path, ["cdn/", "assets/", "static/"]):
            stack.append(TechnologyStack.CDN)
        
        # CI/CD analysis
        if self._has_file_pattern(project_path, [".github/", ".gitlab-ci.yml", "Jenkinsfile", "azure-pipelines.yml"]):
            stack.append(TechnologyStack.CI_CD)
        
        return stack
    
    def _analyze_frameworks(self, project_path: str) -> List[Framework]:
        """Analyze frameworks used in the project."""
        frameworks = []
        
        # Check package.json for frontend frameworks
        if os.path.exists(os.path.join(project_path, "package.json")):
            with open(os.path.join(project_path, "package.json"), 'r') as f:
                package_json = json.load(f)
                dependencies = {**package_json.get("dependencies", {}), **package_json.get("devDependencies", {})}
                
                if "react" in dependencies:
                    frameworks.append(Framework.REACT)
                if "vue" in dependencies:
                    frameworks.append(Framework.VUE)
                if "angular" in dependencies:
                    frameworks.append(Framework.ANGULAR)
                if "svelte" in dependencies:
                    frameworks.append(Framework.SVELTE)
                if "next" in dependencies:
                    frameworks.append(Framework.NEXTJS)
                if "nuxt" in dependencies:
                    frameworks.append(Framework.NUXT)
                if "express" in dependencies:
                    frameworks.append(Framework.EXPRESS)
                if "react-native" in dependencies:
                    frameworks.append(Framework.REACT_NATIVE)
        
        # Check requirements.txt for Python frameworks
        if os.path.exists(os.path.join(project_path, "requirements.txt")):
            with open(os.path.join(project_path, "requirements.txt"), 'r') as f:
                requirements = f.read().lower()
                if "fastapi" in requirements:
                    frameworks.append(Framework.FASTAPI)
                if "flask" in requirements:
                    frameworks.append(Framework.FLASK)
                if "django" in requirements:
                    frameworks.append(Framework.DJANGO)
                if "sqlalchemy" in requirements:
                    frameworks.append(Framework.SQLALCHEMY)
        
        # Check for other framework indicators
        if os.path.exists(os.path.join(project_path, "pom.xml")):
            frameworks.append(Framework.SPRING)
        if os.path.exists(os.path.join(project_path, "Gemfile")):
            frameworks.append(Framework.RAILS)
        if os.path.exists(os.path.join(project_path, "composer.json")):
            frameworks.append(Framework.LARAVEL)
        if os.path.exists(os.path.join(project_path, "pubspec.yaml")):
            frameworks.append(Framework.FLUTTER)
        
        return frameworks
    
    def _analyze_database_type(self, project_path: str) -> Optional[DatabaseType]:
        """Analyze database type used in the project."""
        # Check for SQL files
        if self._has_file_pattern(project_path, ["*.sql", "migrations/", "schema/"]):
            return DatabaseType.RELATIONAL
        
        # Check for NoSQL indicators
        if self._has_file_pattern(project_path, ["*.json", "*.bson", "mongodb/", "mongo/"]):
            return DatabaseType.DOCUMENT
        
        # Check for Redis indicators
        if self._has_file_pattern(project_path, ["redis/", "*.rdb", "*.aof"]):
            return DatabaseType.KEY_VALUE
        
        # Check for graph database indicators
        if self._has_file_pattern(project_path, ["neo4j/", "graph/", "*.cypher"]):
            return DatabaseType.GRAPH
        
        # Check for time series indicators
        if self._has_file_pattern(project_path, ["influxdb/", "timescale/", "*.tsdb"]):
            return DatabaseType.TIME_SERIES
        
        # Check for search engine indicators
        if self._has_file_pattern(project_path, ["elasticsearch/", "solr/", "lucene/"]):
            return DatabaseType.SEARCH
        
        return None
    
    def _analyze_programming_languages(self, project_path: str) -> List[str]:
        """Analyze programming languages used in the project."""
        languages = []
        
        # Count files by extension
        file_counts = {}
        for root, dirs, files in os.walk(project_path):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                file_counts[ext] = file_counts.get(ext, 0) + 1
        
        # Map extensions to languages
        ext_to_lang = {
            '.js': 'javascript',
            '.ts': 'typescript',
            '.py': 'python',
            '.java': 'java',
            '.go': 'go',
            '.rs': 'rust',
            '.cpp': 'cpp',
            '.c': 'c',
            '.cs': 'csharp',
            '.php': 'php',
            '.rb': 'ruby',
            '.swift': 'swift',
            '.kt': 'kotlin',
            '.scala': 'scala',
            '.clj': 'clojure',
            '.hs': 'haskell',
            '.ml': 'ocaml',
            '.fs': 'fsharp',
            '.dart': 'dart',
            '.lua': 'lua',
            '.r': 'r',
            '.m': 'matlab',
            '.sh': 'bash',
            '.ps1': 'powershell',
            '.sql': 'sql',
            '.html': 'html',
            '.css': 'css',
            '.scss': 'scss',
            '.sass': 'sass',
            '.less': 'less',
            '.xml': 'xml',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.json': 'json',
            '.toml': 'toml',
            '.ini': 'ini',
            '.cfg': 'config',
            '.conf': 'config'
        }
        
        # Add languages with significant file counts
        for ext, count in file_counts.items():
            if ext in ext_to_lang and count > 5:  # Threshold for significant usage
                languages.append(ext_to_lang[ext])
        
        return list(set(languages))  # Remove duplicates
    
    def _analyze_build_tools(self, project_path: str) -> List[str]:
        """Analyze build tools used in the project."""
        build_tools = []
        
        # Check for common build tool files
        if os.path.exists(os.path.join(project_path, "webpack.config.js")):
            build_tools.append("webpack")
        if os.path.exists(os.path.join(project_path, "vite.config.js")):
            build_tools.append("vite")
        if os.path.exists(os.path.join(project_path, "rollup.config.js")):
            build_tools.append("rollup")
        if os.path.exists(os.path.join(project_path, "parcel.json")):
            build_tools.append("parcel")
        if os.path.exists(os.path.join(project_path, "gulpfile.js")):
            build_tools.append("gulp")
        if os.path.exists(os.path.join(project_path, "gruntfile.js")):
            build_tools.append("grunt")
        if os.path.exists(os.path.join(project_path, "Makefile")):
            build_tools.append("make")
        if os.path.exists(os.path.join(project_path, "CMakeLists.txt")):
            build_tools.append("cmake")
        if os.path.exists(os.path.join(project_path, "pom.xml")):
            build_tools.append("maven")
        if os.path.exists(os.path.join(project_path, "build.gradle")):
            build_tools.append("gradle")
        if os.path.exists(os.path.join(project_path, "Cargo.toml")):
            build_tools.append("cargo")
        if os.path.exists(os.path.join(project_path, "mix.exs")):
            build_tools.append("mix")
        
        return build_tools
    
    def _analyze_testing_frameworks(self, project_path: str) -> List[str]:
        """Analyze testing frameworks used in the project."""
        testing_frameworks = []
        
        # Check package.json for testing frameworks
        if os.path.exists(os.path.join(project_path, "package.json")):
            with open(os.path.join(project_path, "package.json"), 'r') as f:
                package_json = json.load(f)
                dependencies = {**package_json.get("dependencies", {}), **package_json.get("devDependencies", {})}
                
                if "jest" in dependencies:
                    testing_frameworks.append("jest")
                if "mocha" in dependencies:
                    testing_frameworks.append("mocha")
                if "chai" in dependencies:
                    testing_frameworks.append("chai")
                if "cypress" in dependencies:
                    testing_frameworks.append("cypress")
                if "playwright" in dependencies:
                    testing_frameworks.append("playwright")
                if "puppeteer" in dependencies:
                    testing_frameworks.append("puppeteer")
                if "testing-library" in dependencies:
                    testing_frameworks.append("testing-library")
        
        # Check requirements.txt for Python testing frameworks
        if os.path.exists(os.path.join(project_path, "requirements.txt")):
            with open(os.path.join(project_path, "requirements.txt"), 'r') as f:
                requirements = f.read().lower()
                if "pytest" in requirements:
                    testing_frameworks.append("pytest")
                if "unittest" in requirements:
                    testing_frameworks.append("unittest")
                if "nose" in requirements:
                    testing_frameworks.append("nose")
                if "behave" in requirements:
                    testing_frameworks.append("behave")
        
        # Check for other testing framework indicators
        if self._has_file_pattern(project_path, ["tests/", "test/", "spec/", "specs/"]):
            testing_frameworks.append("custom")
        
        return testing_frameworks
    
    def _analyze_deployment_methods(self, project_path: str) -> List[str]:
        """Analyze deployment methods used in the project."""
        deployment_methods = []
        
        # Check for containerization
        if os.path.exists(os.path.join(project_path, "Dockerfile")):
            deployment_methods.append("docker")
        if os.path.exists(os.path.join(project_path, "docker-compose.yml")):
            deployment_methods.append("docker-compose")
        
        # Check for orchestration
        if self._has_file_pattern(project_path, ["k8s/", "kubernetes/", "*.yaml", "*.yml"]):
            deployment_methods.append("kubernetes")
        
        # Check for cloud deployment
        if self._has_file_pattern(project_path, ["serverless.yml", "template.yaml", "sam.yaml"]):
            deployment_methods.append("serverless")
        if os.path.exists(os.path.join(project_path, "terraform/")):
            deployment_methods.append("terraform")
        if os.path.exists(os.path.join(project_path, "cloudformation/")):
            deployment_methods.append("cloudformation")
        
        # Check for CI/CD
        if self._has_file_pattern(project_path, [".github/workflows/", ".gitlab-ci.yml", "Jenkinsfile"]):
            deployment_methods.append("ci-cd")
        
        return deployment_methods
    
    def _analyze_infrastructure_requirements(self, project_path: str) -> List[str]:
        """Analyze infrastructure requirements."""
        requirements = []
        
        # Check for database requirements
        if self._has_file_pattern(project_path, ["*.sql", "migrations/", "schema/"]):
            requirements.append("database")
        
        # Check for storage requirements
        if self._has_file_pattern(project_path, ["uploads/", "files/", "media/", "static/"]):
            requirements.append("storage")
        
        # Check for caching requirements
        if self._has_file_pattern(project_path, ["cache/", "redis/", "memcached/"]):
            requirements.append("caching")
        
        # Check for messaging requirements
        if self._has_file_pattern(project_path, ["queue/", "messaging/", "kafka/", "rabbitmq/"]):
            requirements.append("messaging")
        
        # Check for monitoring requirements
        if self._has_file_pattern(project_path, ["monitoring/", "metrics/", "logs/"]):
            requirements.append("monitoring")
        
        # Check for CDN requirements
        if self._has_file_pattern(project_path, ["assets/", "static/", "public/"]):
            requirements.append("cdn")
        
        return requirements
    
    def _analyze_performance_characteristics(self, project_path: str) -> Dict[str, Any]:
        """Analyze performance characteristics."""
        characteristics = {
            "cpu_intensive": False,
            "memory_intensive": False,
            "io_intensive": False,
            "network_intensive": False,
            "real_time": False,
            "batch_processing": False
        }
        
        # Check for CPU-intensive indicators
        if self._has_file_pattern(project_path, ["ml/", "ai/", "algorithm/", "compute/"]):
            characteristics["cpu_intensive"] = True
        
        # Check for memory-intensive indicators
        if self._has_file_pattern(project_path, ["cache/", "buffer/", "memory/"]):
            characteristics["memory_intensive"] = True
        
        # Check for IO-intensive indicators
        if self._has_file_pattern(project_path, ["file/", "upload/", "download/", "storage/"]):
            characteristics["io_intensive"] = True
        
        # Check for network-intensive indicators
        if self._has_file_pattern(project_path, ["api/", "http/", "websocket/", "stream/"]):
            characteristics["network_intensive"] = True
        
        # Check for real-time indicators
        if self._has_file_pattern(project_path, ["websocket/", "socket/", "real-time/", "live/"]):
            characteristics["real_time"] = True
        
        # Check for batch processing indicators
        if self._has_file_pattern(project_path, ["batch/", "cron/", "schedule/", "etl/"]):
            characteristics["batch_processing"] = True
        
        return characteristics
    
    def _analyze_security_requirements(self, project_path: str) -> List[str]:
        """Analyze security requirements."""
        requirements = []
        
        # Check for authentication
        if self._has_file_pattern(project_path, ["auth/", "login/", "user/", "session/"]):
            requirements.append("authentication")
        
        # Check for authorization
        if self._has_file_pattern(project_path, ["permission/", "role/", "access/", "authorization/"]):
            requirements.append("authorization")
        
        # Check for encryption
        if self._has_file_pattern(project_path, ["encrypt/", "crypto/", "ssl/", "tls/"]):
            requirements.append("encryption")
        
        # Check for audit logging
        if self._has_file_pattern(project_path, ["audit/", "log/", "track/", "monitor/"]):
            requirements.append("audit_logging")
        
        # Check for compliance
        if self._has_file_pattern(project_path, ["gdpr/", "hipaa/", "pci/", "compliance/"]):
            requirements.append("compliance")
        
        return requirements
    
    def _analyze_scalability_needs(self, project_path: str) -> Dict[str, Any]:
        """Analyze scalability needs."""
        needs = {
            "horizontal_scaling": False,
            "vertical_scaling": False,
            "auto_scaling": False,
            "load_balancing": False,
            "caching": False,
            "database_sharding": False
        }
        
        # Check for horizontal scaling indicators
        if self._has_file_pattern(project_path, ["microservices/", "services/", "api/"]):
            needs["horizontal_scaling"] = True
        
        # Check for vertical scaling indicators
        if self._has_file_pattern(project_path, ["monolith/", "single/", "main/"]):
            needs["vertical_scaling"] = True
        
        # Check for auto-scaling indicators
        if self._has_file_pattern(project_path, ["kubernetes/", "docker/", "container/"]):
            needs["auto_scaling"] = True
        
        # Check for load balancing indicators
        if self._has_file_pattern(project_path, ["proxy/", "gateway/", "router/"]):
            needs["load_balancing"] = True
        
        # Check for caching indicators
        if self._has_file_pattern(project_path, ["cache/", "redis/", "memcached/"]):
            needs["caching"] = True
        
        # Check for database sharding indicators
        if self._has_file_pattern(project_path, ["shard/", "partition/", "distributed/"]):
            needs["database_sharding"] = True
        
        return needs
    
    def _analyze_compliance_requirements(self, project_path: str) -> List[str]:
        """Analyze compliance requirements."""
        requirements = []
        
        # Check for GDPR compliance
        if self._has_file_pattern(project_path, ["gdpr/", "privacy/", "data-protection/"]):
            requirements.append("gdpr")
        
        # Check for HIPAA compliance
        if self._has_file_pattern(project_path, ["hipaa/", "healthcare/", "medical/"]):
            requirements.append("hipaa")
        
        # Check for PCI compliance
        if self._has_file_pattern(project_path, ["pci/", "payment/", "credit-card/"]):
            requirements.append("pci")
        
        # Check for SOC2 compliance
        if self._has_file_pattern(project_path, ["soc2/", "security/", "audit/"]):
            requirements.append("soc2")
        
        return requirements
    
    def _estimate_team_size(self, project_path: str) -> int:
        """Estimate team size based on project complexity."""
        # Count contributors in git history
        try:
            result = subprocess.run(
                ["git", "log", "--pretty=format:%an", "|", "sort", "|", "uniq", "|", "wc", "-l"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return int(result.stdout.strip())
        except:
            pass
        
        # Estimate based on project size and complexity
        file_count = 0
        for root, dirs, files in os.walk(project_path):
            file_count += len(files)
        
        if file_count > 1000:
            return 10
        elif file_count > 500:
            return 5
        elif file_count > 100:
            return 3
        else:
            return 1
    
    def _calculate_complexity_score(self, project_path: str) -> int:
        """Calculate complexity score (1-10)."""
        score = 1
        
        # Add points for different complexity indicators
        if self._has_file_pattern(project_path, ["microservices/", "services/"]):
            score += 2
        if self._has_file_pattern(project_path, ["kubernetes/", "docker/"]):
            score += 2
        if self._has_file_pattern(project_path, ["ml/", "ai/", "algorithm/"]):
            score += 2
        if self._has_file_pattern(project_path, ["real-time/", "websocket/", "stream/"]):
            score += 1
        if self._has_file_pattern(project_path, ["distributed/", "cluster/", "shard/"]):
            score += 2
        
        return min(score, 10)
    
    def _calculate_maturity_score(self, project_path: str) -> int:
        """Calculate maturity score (1-10)."""
        score = 1
        
        # Add points for maturity indicators
        if os.path.exists(os.path.join(project_path, "README.md")):
            score += 1
        if os.path.exists(os.path.join(project_path, "docs/")):
            score += 1
        if os.path.exists(os.path.join(project_path, "tests/")):
            score += 2
        if os.path.exists(os.path.join(project_path, ".github/workflows/")):
            score += 2
        if os.path.exists(os.path.join(project_path, "docker-compose.yml")):
            score += 1
        if os.path.exists(os.path.join(project_path, "k8s/")):
            score += 2
        if os.path.exists(os.path.join(project_path, "monitoring/")):
            score += 1
        
        return min(score, 10)
    
    def _has_file_pattern(self, project_path: str, patterns: List[str]) -> bool:
        """Check if project has files matching any of the patterns."""
        for root, dirs, files in os.walk(project_path):
            for file in files:
                for pattern in patterns:
                    if pattern.endswith('/'):
                        # Directory pattern
                        if pattern.rstrip('/') in root:
                            return True
                    elif pattern.startswith('*'):
                        # File extension pattern
                        if file.endswith(pattern[1:]):
                            return True
                    else:
                        # Exact file pattern
                        if file == pattern:
                            return True
        return False
    
    def _load_analysis_patterns(self) -> Dict[str, Any]:
        """Load analysis patterns for project detection."""
        return {
            "project_types": {
                "web_application": ["src/", "public/", "static/", "*.html"],
                "mobile_application": ["android/", "ios/", "*.apk", "*.ipa"],
                "api_service": ["api/", "routes/", "controllers/", "endpoints/"],
                "microservices": ["services/", "microservices/", "docker-compose.yml"],
                "data_pipeline": ["pipeline/", "etl/", "data/", "*.py"],
                "machine_learning": ["models/", "*.pkl", "*.h5", "*.pt"],
                "blockchain_application": ["contracts/", "*.sol", "*.vy", "truffle/"],
                "game_development": ["assets/", "sprites/", "*.unity", "*.godot"],
                "desktop_application": ["*.exe", "*.app", "*.dmg", "*.deb"]
            }
        }
    
    def _load_framework_indicators(self) -> Dict[str, List[str]]:
        """Load framework indicators for detection."""
        return {
            "react": ["react", "react-dom"],
            "vue": ["vue", "vue-router"],
            "angular": ["@angular/core", "@angular/common"],
            "express": ["express", "express-generator"],
            "fastapi": ["fastapi", "uvicorn"],
            "flask": ["flask", "flask-restful"],
            "django": ["django", "djangorestframework"]
        }
    
    def _load_technology_indicators(self) -> Dict[str, List[str]]:
        """Load technology indicators for detection."""
        return {
            "frontend": ["src/", "public/", "static/", "*.html", "*.css", "*.js"],
            "backend": ["server/", "api/", "backend/", "*.py", "*.js", "*.java"],
            "database": ["*.sql", "migrations/", "schema/", "models/"],
            "caching": ["cache/", "redis/", "memcached/"],
            "monitoring": ["monitoring/", "metrics/", "logs/", "prometheus/"]
        }

def main():
    """Main project analyzer demo."""
    print("🔍 PROJECT ANALYZER DEMO")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = ProjectAnalyzer()
    
    # Analyze current project
    project_path = "/home/dawson/code/lang-trak-in-progress"
    analysis = analyzer.analyze_project(project_path)
    
    # Print analysis results
    print(f"\n📊 Analysis Results:")
    print(f"   Project Type: {analysis.project_type}")
    print(f"   Development Stage: {analysis.development_stage}")
    print(f"   Technology Stack: {[t.value for t in analysis.technology_stack]}")
    print(f"   Frameworks: {[f.value for f in analysis.frameworks]}")
    print(f"   Programming Languages: {analysis.programming_languages}")
    print(f"   Team Size Estimate: {analysis.team_size_estimate}")
    print(f"   Complexity Score: {analysis.complexity_score}/10")
    print(f"   Maturity Score: {analysis.maturity_score}/10")
    
    # Save analysis
    with open("project-analysis.json", "w") as f:
        json.dump(analysis.__dict__, f, indent=2, default=str)
    
    print(f"\n📄 Analysis saved: project-analysis.json")

if __name__ == "__main__":
    main()
