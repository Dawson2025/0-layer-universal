#!/usr/bin/env python3

"""
optimization_engine.py

Intelligent optimization engine that analyzes project requirements and
generates optimal configurations for any combination of services and technologies.
"""

import json
import os
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import math

class OptimizationGoal(Enum):
    COST = "cost"
    PERFORMANCE = "performance"
    SECURITY = "security"
    SCALABILITY = "scalability"
    RELIABILITY = "reliability"
    MAINTAINABILITY = "maintainability"

class OptimizationStrategy(Enum):
    COST_FIRST = "cost_first"
    PERFORMANCE_FIRST = "performance_first"
    BALANCED = "balanced"
    ENTERPRISE = "enterprise"
    STARTUP = "startup"

@dataclass
class OptimizationResult:
    """Result of optimization analysis."""
    strategy: OptimizationStrategy
    recommended_providers: List[str]
    service_configurations: List[Dict[str, Any]]
    estimated_costs: Dict[str, float]
    performance_estimates: Dict[str, Any]
    security_score: int
    scalability_score: int
    reliability_score: int
    maintainability_score: int
    optimization_recommendations: List[str]
    trade_offs: List[Dict[str, Any]]

@dataclass
class ServiceRecommendation:
    """Recommendation for a specific service."""
    service_type: str
    recommended_providers: List[str]
    configuration: Dict[str, Any]
    reasoning: str
    cost_estimate: float
    performance_impact: str
    security_impact: str

class OptimizationEngine:
    """Intelligent optimization engine for service selection and configuration."""
    
    def __init__(self):
        self.provider_database = self._load_provider_database()
        self.optimization_rules = self._load_optimization_rules()
        self.cost_models = self._load_cost_models()
        self.performance_models = self._load_performance_models()
    
    def optimize_configuration(self, project_analysis: Any, goals: List[OptimizationGoal], 
                             strategy: OptimizationStrategy = OptimizationStrategy.BALANCED) -> OptimizationResult:
        """Optimize configuration based on project analysis and goals."""
        print(f"🎯 Optimizing configuration for {strategy.value} strategy...")
        
        # Analyze project requirements
        requirements = self._analyze_requirements(project_analysis)
        
        # Select optimal providers
        recommended_providers = self._select_optimal_providers(requirements, goals, strategy)
        
        # Generate service configurations
        service_configurations = self._generate_service_configurations(requirements, recommended_providers, strategy)
        
        # Calculate estimates
        estimated_costs = self._calculate_estimated_costs(service_configurations)
        performance_estimates = self._calculate_performance_estimates(service_configurations)
        
        # Calculate scores
        security_score = self._calculate_security_score(service_configurations)
        scalability_score = self._calculate_scalability_score(service_configurations)
        reliability_score = self._calculate_reliability_score(service_configurations)
        maintainability_score = self._calculate_maintainability_score(service_configurations)
        
        # Generate recommendations
        optimization_recommendations = self._generate_optimization_recommendations(
            service_configurations, goals, strategy
        )
        
        # Identify trade-offs
        trade_offs = self._identify_trade_offs(service_configurations, goals)
        
        result = OptimizationResult(
            strategy=strategy,
            recommended_providers=recommended_providers,
            service_configurations=service_configurations,
            estimated_costs=estimated_costs,
            performance_estimates=performance_estimates,
            security_score=security_score,
            scalability_score=scalability_score,
            reliability_score=reliability_score,
            maintainability_score=maintainability_score,
            optimization_recommendations=optimization_recommendations,
            trade_offs=trade_offs
        )
        
        print("✅ Optimization complete")
        return result
    
    def _analyze_requirements(self, project_analysis: Any) -> Dict[str, Any]:
        """Analyze project requirements from analysis."""
        requirements = {
            "project_type": project_analysis.project_type,
            "development_stage": project_analysis.development_stage,
            "technology_stack": [t.value for t in project_analysis.technology_stack],
            "frameworks": [f.value for f in project_analysis.frameworks],
            "programming_languages": project_analysis.programming_languages,
            "team_size": project_analysis.team_size_estimate,
            "complexity": project_analysis.complexity_score,
            "maturity": project_analysis.maturity_score,
            "performance_characteristics": project_analysis.performance_characteristics,
            "security_requirements": project_analysis.security_requirements,
            "scalability_needs": project_analysis.scalability_needs,
            "compliance_requirements": project_analysis.compliance_requirements
        }
        return requirements
    
    def _select_optimal_providers(self, requirements: Dict[str, Any], 
                                goals: List[OptimizationGoal], 
                                strategy: OptimizationStrategy) -> List[str]:
        """Select optimal service providers based on requirements and goals."""
        providers = []
        
        # Get base providers for project type
        project_type = requirements["project_type"]
        base_providers = self._get_base_providers_for_project_type(project_type)
        
        # Filter by strategy
        if strategy == OptimizationStrategy.COST_FIRST:
            providers = self._filter_by_cost_optimization(base_providers, requirements)
        elif strategy == OptimizationStrategy.PERFORMANCE_FIRST:
            providers = self._filter_by_performance_optimization(base_providers, requirements)
        elif strategy == OptimizationStrategy.ENTERPRISE:
            providers = self._filter_by_enterprise_requirements(base_providers, requirements)
        elif strategy == OptimizationStrategy.STARTUP:
            providers = self._filter_by_startup_requirements(base_providers, requirements)
        else:  # BALANCED
            providers = self._filter_by_balanced_requirements(base_providers, requirements)
        
        # Add specialized providers based on requirements
        if "authentication" in requirements["security_requirements"]:
            providers.extend(self._get_auth_providers(requirements))
        
        if "database" in requirements["technology_stack"]:
            providers.extend(self._get_database_providers(requirements))
        
        if "monitoring" in requirements["technology_stack"]:
            providers.extend(self._get_monitoring_providers(requirements))
        
        return list(set(providers))  # Remove duplicates
    
    def _get_base_providers_for_project_type(self, project_type: str) -> List[str]:
        """Get base providers for project type."""
        provider_mapping = {
            "web_application": ["aws", "google_cloud", "azure", "digital_ocean"],
            "mobile_application": ["firebase", "aws", "google_cloud"],
            "api_service": ["aws", "google_cloud", "azure", "heroku"],
            "microservices": ["aws", "google_cloud", "azure", "kubernetes"],
            "data_pipeline": ["aws", "google_cloud", "azure"],
            "machine_learning": ["aws", "google_cloud", "azure"],
            "iot_application": ["aws", "google_cloud", "azure"],
            "blockchain_application": ["aws", "google_cloud", "azure"],
            "game_development": ["aws", "google_cloud", "azure"],
            "desktop_application": ["aws", "google_cloud", "azure"]
        }
        return provider_mapping.get(project_type, ["aws", "google_cloud", "azure"])
    
    def _filter_by_cost_optimization(self, providers: List[str], requirements: Dict[str, Any]) -> List[str]:
        """Filter providers for cost optimization."""
        cost_effective_providers = ["digital_ocean", "linode", "vultr", "heroku"]
        enterprise_providers = ["aws", "google_cloud", "azure"]
        
        if requirements["development_stage"] in ["concept", "prototype"]:
            return [p for p in providers if p in cost_effective_providers]
        else:
            return [p for p in providers if p in cost_effective_providers or p in enterprise_providers]
    
    def _filter_by_performance_optimization(self, providers: List[str], requirements: Dict[str, Any]) -> List[str]:
        """Filter providers for performance optimization."""
        high_performance_providers = ["aws", "google_cloud", "azure"]
        return [p for p in providers if p in high_performance_providers]
    
    def _filter_by_enterprise_requirements(self, providers: List[str], requirements: Dict[str, Any]) -> List[str]:
        """Filter providers for enterprise requirements."""
        enterprise_providers = ["aws", "google_cloud", "azure", "oracle_cloud"]
        return [p for p in providers if p in enterprise_providers]
    
    def _filter_by_startup_requirements(self, providers: List[str], requirements: Dict[str, Any]) -> List[str]:
        """Filter providers for startup requirements."""
        startup_friendly_providers = ["heroku", "vercel", "netlify", "firebase", "digital_ocean"]
        return [p for p in providers if p in startup_friendly_providers]
    
    def _filter_by_balanced_requirements(self, providers: List[str], requirements: Dict[str, Any]) -> List[str]:
        """Filter providers for balanced requirements."""
        balanced_providers = ["aws", "google_cloud", "azure", "digital_ocean"]
        return [p for p in providers if p in balanced_providers]
    
    def _get_auth_providers(self, requirements: Dict[str, Any]) -> List[str]:
        """Get authentication providers based on requirements."""
        auth_providers = []
        
        if "firebase" in requirements["frameworks"]:
            auth_providers.append("firebase_auth")
        else:
            auth_providers.append("auth0")
        
        if requirements["compliance_requirements"]:
            auth_providers.append("okta")
        
        return auth_providers
    
    def _get_database_providers(self, requirements: Dict[str, Any]) -> List[str]:
        """Get database providers based on requirements."""
        db_providers = []
        
        if "mongodb" in requirements["frameworks"]:
            db_providers.append("mongodb_atlas")
        else:
            db_providers.append("postgresql")
        
        if requirements["scalability_needs"].get("database_sharding", False):
            db_providers.append("cockroachdb")
        
        return db_providers
    
    def _get_monitoring_providers(self, requirements: Dict[str, Any]) -> List[str]:
        """Get monitoring providers based on requirements."""
        monitoring_providers = []
        
        if requirements["team_size"] > 10:
            monitoring_providers.append("datadog")
        else:
            monitoring_providers.append("new_relic")
        
        monitoring_providers.append("sentry")
        
        return monitoring_providers
    
    def _generate_service_configurations(self, requirements: Dict[str, Any], 
                                       providers: List[str], 
                                       strategy: OptimizationStrategy) -> List[Dict[str, Any]]:
        """Generate service configurations for selected providers."""
        configurations = []
        
        for provider in providers:
            provider_config = self.provider_database.get(provider, {})
            
            for service in provider_config.get("services", []):
                config = {
                    "provider": provider,
                    "service": service,
                    "configuration": self._get_service_configuration(provider, service, requirements, strategy),
                    "cost_estimate": self._estimate_service_cost(provider, service, requirements),
                    "performance_metrics": self._get_service_performance_metrics(provider, service),
                    "security_features": self._get_service_security_features(provider, service),
                    "scalability_options": self._get_service_scalability_options(provider, service)
                }
                configurations.append(config)
        
        return configurations
    
    def _get_service_configuration(self, provider: str, service: str, 
                                 requirements: Dict[str, Any], 
                                 strategy: OptimizationStrategy) -> Dict[str, Any]:
        """Get service configuration based on provider, service, and requirements."""
        base_config = {
            "region": "us-east-1",
            "environment": requirements["development_stage"],
            "scaling": requirements["scalability_needs"].get("auto_scaling", False)
        }
        
        # Adjust configuration based on strategy
        if strategy == OptimizationStrategy.COST_FIRST:
            base_config["instance_type"] = "t3.micro"
            base_config["storage_type"] = "standard"
        elif strategy == OptimizationStrategy.PERFORMANCE_FIRST:
            base_config["instance_type"] = "c5.large"
            base_config["storage_type"] = "ssd"
        elif strategy == OptimizationStrategy.ENTERPRISE:
            base_config["instance_type"] = "m5.large"
            base_config["storage_type"] = "premium"
            base_config["high_availability"] = True
        else:  # BALANCED or STARTUP
            base_config["instance_type"] = "t3.small"
            base_config["storage_type"] = "gp2"
        
        return base_config
    
    def _estimate_service_cost(self, provider: str, service: str, requirements: Dict[str, Any]) -> float:
        """Estimate service cost based on provider, service, and requirements."""
        base_costs = self.cost_models.get(provider, {}).get(service, 10)
        
        # Adjust based on development stage
        stage_multipliers = {
            "concept": 0.1,
            "prototype": 0.3,
            "mvp": 0.7,
            "beta": 1.0,
            "production": 1.5,
            "scale": 2.0
        }
        
        multiplier = stage_multipliers.get(requirements["development_stage"], 1.0)
        return base_costs * multiplier
    
    def _get_service_performance_metrics(self, provider: str, service: str) -> Dict[str, Any]:
        """Get performance metrics for a service."""
        return self.performance_models.get(provider, {}).get(service, {
            "latency_ms": 100,
            "throughput_rps": 1000,
            "availability_percentage": 99.9
        })
    
    def _get_service_security_features(self, provider: str, service: str) -> List[str]:
        """Get security features for a service."""
        security_features = {
            "aws": ["encryption_at_rest", "encryption_in_transit", "iam", "vpc", "waf"],
            "google_cloud": ["encryption_at_rest", "encryption_in_transit", "iam", "vpc", "cloud_armor"],
            "azure": ["encryption_at_rest", "encryption_in_transit", "rbac", "vnet", "ddos_protection"],
            "firebase": ["authentication", "security_rules", "ssl", "audit_logs"],
            "auth0": ["mfa", "sso", "audit_logs", "compliance", "breach_detection"]
        }
        return security_features.get(provider, ["basic_security"])
    
    def _get_service_scalability_options(self, provider: str, service: str) -> List[str]:
        """Get scalability options for a service."""
        scalability_options = {
            "aws": ["auto_scaling", "load_balancing", "multi_az", "spot_instances"],
            "google_cloud": ["auto_scaling", "load_balancing", "multi_region", "preemptible"],
            "azure": ["auto_scaling", "load_balancing", "availability_zones", "spot_vms"],
            "firebase": ["auto_scaling", "global_cdn", "offline_support"],
            "heroku": ["auto_scaling", "add_ons", "dyno_scaling"]
        }
        return scalability_options.get(provider, ["manual_scaling"])
    
    def _calculate_estimated_costs(self, configurations: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calculate estimated costs for all configurations."""
        total_cost = sum(config["cost_estimate"] for config in configurations)
        
        costs_by_provider = {}
        for config in configurations:
            provider = config["provider"]
            costs_by_provider[provider] = costs_by_provider.get(provider, 0) + config["cost_estimate"]
        
        return {
            "total_monthly": total_cost,
            "by_provider": costs_by_provider,
            "breakdown": {config["service"]: config["cost_estimate"] for config in configurations}
        }
    
    def _calculate_performance_estimates(self, configurations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate performance estimates for all configurations."""
        if not configurations:
            return {"overall_latency_ms": 0, "overall_throughput_rps": 0, "overall_availability_percentage": 0}
        
        # Calculate weighted averages
        total_latency = sum(config["performance_metrics"]["latency_ms"] for config in configurations)
        total_throughput = sum(config["performance_metrics"]["throughput_rps"] for config in configurations)
        total_availability = sum(config["performance_metrics"]["availability_percentage"] for config in configurations)
        
        count = len(configurations)
        
        return {
            "overall_latency_ms": total_latency / count,
            "overall_throughput_rps": total_throughput / count,
            "overall_availability_percentage": total_availability / count,
            "bottlenecks": self._identify_performance_bottlenecks(configurations)
        }
    
    def _identify_performance_bottlenecks(self, configurations: List[Dict[str, Any]]) -> List[str]:
        """Identify potential performance bottlenecks."""
        bottlenecks = []
        
        for config in configurations:
            if config["performance_metrics"]["latency_ms"] > 500:
                bottlenecks.append(f"High latency in {config['service']} ({config['provider']})")
            if config["performance_metrics"]["throughput_rps"] < 100:
                bottlenecks.append(f"Low throughput in {config['service']} ({config['provider']})")
            if config["performance_metrics"]["availability_percentage"] < 99.5:
                bottlenecks.append(f"Low availability in {config['service']} ({config['provider']})")
        
        return bottlenecks
    
    def _calculate_security_score(self, configurations: List[Dict[str, Any]]) -> int:
        """Calculate overall security score (0-100)."""
        if not configurations:
            return 0
        
        total_security_features = sum(len(config["security_features"]) for config in configurations)
        max_possible_features = len(configurations) * 5  # Assuming max 5 security features per service
        
        score = int((total_security_features / max_possible_features) * 100) if max_possible_features > 0 else 0
        return min(score, 100)
    
    def _calculate_scalability_score(self, configurations: List[Dict[str, Any]]) -> int:
        """Calculate overall scalability score (0-100)."""
        if not configurations:
            return 0
        
        total_scalability_options = sum(len(config["scalability_options"]) for config in configurations)
        max_possible_options = len(configurations) * 4  # Assuming max 4 scalability options per service
        
        score = int((total_scalability_options / max_possible_options) * 100) if max_possible_options > 0 else 0
        return min(score, 100)
    
    def _calculate_reliability_score(self, configurations: List[Dict[str, Any]]) -> int:
        """Calculate overall reliability score (0-100)."""
        if not configurations:
            return 0
        
        avg_availability = sum(config["performance_metrics"]["availability_percentage"] for config in configurations) / len(configurations)
        return int(avg_availability)
    
    def _calculate_maintainability_score(self, configurations: List[Dict[str, Any]]) -> int:
        """Calculate overall maintainability score (0-100)."""
        if not configurations:
            return 0
        
        # Factors: number of providers (fewer is better), documentation quality, tooling support
        unique_providers = len(set(config["provider"] for config in configurations))
        provider_diversity_penalty = max(0, (unique_providers - 3) * 10)  # Penalty for too many providers
        
        base_score = 80
        maintainability_score = max(0, base_score - provider_diversity_penalty)
        
        return min(maintainability_score, 100)
    
    def _generate_optimization_recommendations(self, configurations: List[Dict[str, Any]], 
                                             goals: List[OptimizationGoal], 
                                             strategy: OptimizationStrategy) -> List[str]:
        """Generate optimization recommendations."""
        recommendations = []
        
        # Cost optimization recommendations
        if OptimizationGoal.COST in goals:
            total_cost = sum(config["cost_estimate"] for config in configurations)
            if total_cost > 1000:
                recommendations.append("Consider using spot instances or reserved instances to reduce costs")
            if len(set(config["provider"] for config in configurations)) > 3:
                recommendations.append("Consolidate providers to reduce management overhead and costs")
        
        # Performance optimization recommendations
        if OptimizationGoal.PERFORMANCE in goals:
            bottlenecks = self._identify_performance_bottlenecks(configurations)
            if bottlenecks:
                recommendations.append(f"Address performance bottlenecks: {', '.join(bottlenecks)}")
            recommendations.append("Implement caching strategies to improve performance")
            recommendations.append("Use CDN for static content delivery")
        
        # Security optimization recommendations
        if OptimizationGoal.SECURITY in goals:
            recommendations.append("Enable multi-factor authentication for all services")
            recommendations.append("Implement regular security audits and vulnerability scanning")
            recommendations.append("Use encryption for all data at rest and in transit")
        
        # Scalability optimization recommendations
        if OptimizationGoal.SCALABILITY in goals:
            recommendations.append("Implement auto-scaling for all services")
            recommendations.append("Use load balancing for high-traffic services")
            recommendations.append("Consider microservices architecture for better scalability")
        
        # Reliability optimization recommendations
        if OptimizationGoal.RELIABILITY in goals:
            recommendations.append("Implement redundancy and failover mechanisms")
            recommendations.append("Set up monitoring and alerting for all services")
            recommendations.append("Regular backup and disaster recovery testing")
        
        return recommendations
    
    def _identify_trade_offs(self, configurations: List[Dict[str, Any]], goals: List[OptimizationGoal]) -> List[Dict[str, Any]]:
        """Identify trade-offs in the configuration."""
        trade_offs = []
        
        # Cost vs Performance trade-off
        if OptimizationGoal.COST in goals and OptimizationGoal.PERFORMANCE in goals:
            trade_offs.append({
                "type": "cost_vs_performance",
                "description": "Lower cost configurations may have reduced performance",
                "impact": "medium"
            })
        
        # Security vs Usability trade-off
        if OptimizationGoal.SECURITY in goals:
            trade_offs.append({
                "type": "security_vs_usability",
                "description": "Enhanced security measures may impact user experience",
                "impact": "low"
            })
        
        # Scalability vs Complexity trade-off
        if OptimizationGoal.SCALABILITY in goals:
            trade_offs.append({
                "type": "scalability_vs_complexity",
                "description": "Higher scalability may increase system complexity",
                "impact": "high"
            })
        
        return trade_offs
    
    def _load_provider_database(self) -> Dict[str, Any]:
        """Load provider database with service information."""
        return {
            "aws": {
                "services": ["ec2", "rds", "s3", "lambda", "cloudfront", "cognito", "cloudwatch"],
                "regions": ["us-east-1", "us-west-2", "eu-west-1"],
                "cost_tier": "enterprise"
            },
            "google_cloud": {
                "services": ["compute", "cloud-sql", "storage", "functions", "firebase", "monitoring"],
                "regions": ["us-central1", "us-east1", "europe-west1"],
                "cost_tier": "enterprise"
            },
            "azure": {
                "services": ["vm", "sql-database", "blob-storage", "functions", "active-directory", "monitor"],
                "regions": ["eastus", "westus2", "westeurope"],
                "cost_tier": "enterprise"
            },
            "digital_ocean": {
                "services": ["droplets", "managed-databases", "spaces", "functions"],
                "regions": ["nyc1", "sfo2", "lon1"],
                "cost_tier": "budget"
            },
            "firebase": {
                "services": ["auth", "firestore", "storage", "functions", "hosting", "analytics"],
                "regions": ["us-central1", "europe-west1"],
                "cost_tier": "startup"
            },
            "heroku": {
                "services": ["dynos", "postgres", "redis", "add-ons"],
                "regions": ["us", "eu"],
                "cost_tier": "startup"
            }
        }
    
    def _load_optimization_rules(self) -> Dict[str, Any]:
        """Load optimization rules and heuristics."""
        return {
            "cost_optimization": {
                "prefer_spot_instances": True,
                "consolidate_providers": True,
                "use_managed_services": True
            },
            "performance_optimization": {
                "prefer_ssd_storage": True,
                "use_cdn": True,
                "implement_caching": True
            },
            "security_optimization": {
                "enable_encryption": True,
                "use_iam": True,
                "enable_monitoring": True
            }
        }
    
    def _load_cost_models(self) -> Dict[str, Dict[str, float]]:
        """Load cost models for different providers and services."""
        return {
            "aws": {
                "ec2": 20,
                "rds": 50,
                "s3": 5,
                "lambda": 1,
                "cloudfront": 10,
                "cognito": 5,
                "cloudwatch": 3
            },
            "google_cloud": {
                "compute": 15,
                "cloud-sql": 40,
                "storage": 4,
                "functions": 0.5,
                "firebase": 8,
                "monitoring": 2
            },
            "azure": {
                "vm": 18,
                "sql-database": 45,
                "blob-storage": 4.5,
                "functions": 0.8,
                "active-directory": 6,
                "monitor": 2.5
            },
            "digital_ocean": {
                "droplets": 5,
                "managed-databases": 15,
                "spaces": 2,
                "functions": 0.2
            },
            "firebase": {
                "auth": 0,
                "firestore": 0,
                "storage": 0,
                "functions": 0,
                "hosting": 0,
                "analytics": 0
            },
            "heroku": {
                "dynos": 7,
                "postgres": 9,
                "redis": 3,
                "add-ons": 5
            }
        }
    
    def _load_performance_models(self) -> Dict[str, Dict[str, Dict[str, Any]]]:
        """Load performance models for different providers and services."""
        return {
            "aws": {
                "ec2": {"latency_ms": 50, "throughput_rps": 10000, "availability_percentage": 99.95},
                "rds": {"latency_ms": 10, "throughput_rps": 5000, "availability_percentage": 99.99},
                "s3": {"latency_ms": 100, "throughput_rps": 1000, "availability_percentage": 99.999999999}
            },
            "google_cloud": {
                "compute": {"latency_ms": 45, "throughput_rps": 12000, "availability_percentage": 99.95},
                "cloud-sql": {"latency_ms": 8, "throughput_rps": 6000, "availability_percentage": 99.99},
                "storage": {"latency_ms": 80, "throughput_rps": 1200, "availability_percentage": 99.999999999}
            },
            "firebase": {
                "auth": {"latency_ms": 200, "throughput_rps": 1000, "availability_percentage": 99.9},
                "firestore": {"latency_ms": 100, "throughput_rps": 10000, "availability_percentage": 99.95},
                "hosting": {"latency_ms": 50, "throughput_rps": 50000, "availability_percentage": 99.9}
            }
        }

def main():
    """Main optimization engine demo."""
    print("🎯 OPTIMIZATION ENGINE DEMO")
    print("=" * 50)
    
    # Initialize optimization engine
    engine = OptimizationEngine()
    
    # Create sample project analysis
    from project_analyzer import ProjectAnalysis, ProjectType, DevelopmentStage, TechnologyStack, Framework
    
    sample_analysis = ProjectAnalysis(
        project_type="web_application",
        development_stage="mvp",
        technology_stack=[TechnologyStack.FRONTEND, TechnologyStack.BACKEND, TechnologyStack.DATABASE],
        frameworks=[Framework.REACT, Framework.EXPRESS],
        database_type=None,
        programming_languages=["javascript", "python"],
        build_tools=["webpack"],
        testing_frameworks=["jest"],
        deployment_methods=["docker"],
        infrastructure_requirements=["database", "storage", "monitoring"],
        performance_characteristics={"cpu_intensive": False, "memory_intensive": False, "io_intensive": True},
        security_requirements=["authentication", "encryption"],
        scalability_needs={"horizontal_scaling": True, "auto_scaling": True},
        compliance_requirements=[],
        team_size_estimate=3,
        complexity_score=6,
        maturity_score=7
    )
    
    # Optimize configuration
    goals = [OptimizationGoal.COST, OptimizationGoal.PERFORMANCE, OptimizationGoal.SECURITY]
    result = engine.optimize_configuration(sample_analysis, goals, OptimizationStrategy.BALANCED)
    
    # Print results
    print(f"\n📊 Optimization Results:")
    print(f"   Strategy: {result.strategy.value}")
    print(f"   Recommended Providers: {result.recommended_providers}")
    print(f"   Estimated Monthly Cost: ${result.estimated_costs['total_monthly']:.2f}")
    print(f"   Security Score: {result.security_score}/100")
    print(f"   Scalability Score: {result.scalability_score}/100")
    print(f"   Reliability Score: {result.reliability_score}/100")
    print(f"   Maintainability Score: {result.maintainability_score}/100")
    
    print(f"\n💡 Recommendations:")
    for rec in result.optimization_recommendations:
        print(f"   • {rec}")
    
    # Save results
    with open("optimization-results.json", "w") as f:
        json.dump(asdict(result), f, indent=2, default=str)
    
    print(f"\n📄 Results saved: optimization-results.json")

if __name__ == "__main__":
    main()
