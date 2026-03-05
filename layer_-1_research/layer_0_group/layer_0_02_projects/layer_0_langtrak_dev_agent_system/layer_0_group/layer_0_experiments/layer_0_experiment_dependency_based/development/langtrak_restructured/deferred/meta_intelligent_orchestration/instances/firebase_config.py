#!/usr/bin/env python3
# resource_id: "0cd3489f-a337-4c63-9ddf-d6ab2ff1b94d"
# resource_type: "document"
# resource_name: "firebase_config"

"""
firebase_config.py

Firebase-specific configuration for the Meta-Intelligent Orchestration System.
This defines Firebase and Google Cloud as a specific instance of the meta-intelligent system.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

class FirebaseService(Enum):
    AUTHENTICATION = "authentication"
    FIRESTORE = "firestore"
    REALTIME_DATABASE = "realtime_database"
    STORAGE = "storage"
    HOSTING = "hosting"
    FUNCTIONS = "functions"
    ANALYTICS = "analytics"
    CRASHLYTICS = "crashlytics"
    PERFORMANCE = "performance"
    REMOTE_CONFIG = "remote_config"
    DYNAMIC_LINKS = "dynamic_links"
    MESSAGING = "cloud_messaging"
    TEST_LAB = "test_lab"
    APPMESSAGING = "in_app_messaging"
    PREDICTIONS = "predictions"
    ML = "machine_learning"

class FirebaseProjectType(Enum):
    WEB_APP = "web_app"
    MOBILE_APP = "mobile_app"
    BACKEND_SERVICE = "backend_service"
    MICROSERVICE = "microservice"
    FULL_STACK = "full_stack"

@dataclass
class FirebaseRecommendation:
    """Firebase-specific recommendation configuration."""
    service: FirebaseService
    recommendation: str
    confidence: float
    reasoning: str
    alternatives: List[str]
    implementation_effort: str
    cost_impact: str
    security_considerations: Optional[List[str]] = None
    security_notes: str = ""  # Added for test compatibility
    performance_notes: str = "" # Added for test compatibility
    performance_impact: str = "medium"
    scalability_impact: str = "medium"

    def __post_init__(self):
        if self.security_considerations and not self.security_notes:
            self.security_notes = "; ".join(self.security_considerations)
        if not self.performance_notes:
            self.performance_notes = f"Scalability: {self.scalability_impact}"

@dataclass
class FirebaseProjectProfile:
    """Profile for Firebase project configuration."""
    project_type: FirebaseProjectType
    user_count: str = "small"  # small, medium, large, enterprise
    data_complexity: str = "simple"  # simple, moderate, complex
    real_time_requirements: bool = False
    offline_capability: bool = False
    security_level: str = "standard"  # basic, standard, high, enterprise
    budget_range: str = "low"  # low, medium, high, enterprise
    team_size: int = 1
    development_timeline: str = "standard"  # rapid, standard, extended

class FirebaseMetaIntelligentConfig:
    """Firebase-specific configuration for meta-intelligent orchestration."""
    
    def __init__(self):
        self.firebase_services = self._initialize_firebase_services()
        self.project_profiles = self._initialize_project_profiles()
        self.recommendation_rules = self._initialize_recommendation_rules()
        self.cost_optimization_rules = self._initialize_cost_optimization_rules()
        self.security_rules = self._initialize_security_rules()
    
    def _initialize_firebase_services(self) -> Dict[FirebaseService, Dict[str, Any]]:
        """Initialize Firebase services with their characteristics."""
        return {
            FirebaseService.AUTHENTICATION: {
                "name": "Firebase Authentication",
                "category": "identity",
                "complexity": "medium",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "high",
                "learning_curve": "medium",
                "integration_effort": "low",
                "use_cases": ["user_management", "social_login", "multi_factor_auth"],
                "alternatives": ["Auth0", "AWS Cognito", "Supabase Auth"],
                "trending_score": 0.85,
                "adoption_rate": 0.78,
                "community_activity": 0.82,
                "best_for": ["apps_needing_auth"],
                "security_features": ["mfa", "id_token"]
            },
            FirebaseService.FIRESTORE: {
                "name": "Cloud Firestore",
                "category": "database",
                "complexity": "medium",
                "cost_tier": "pay_per_use",
                "scalability": "very_high",
                "security_level": "high",
                "learning_curve": "medium",
                "integration_effort": "medium",
                "use_cases": ["real_time_data", "offline_sync", "scalable_database"],
                "alternatives": ["MongoDB Atlas", "AWS DynamoDB", "Supabase"],
                "trending_score": 0.88,
                "adoption_rate": 0.65,
                "community_activity": 0.85,
                "best_for": ["flexible_data"],
                "security_features": ["security_rules"]
            },
            FirebaseService.REALTIME_DATABASE: {
                "name": "Realtime Database",
                "category": "database",
                "complexity": "low",
                "cost_tier": "pay_per_use",
                "scalability": "high",
                "security_level": "medium",
                "learning_curve": "low",
                "integration_effort": "low",
                "use_cases": ["simple_sync", "presence"],
                "alternatives": ["Firestore", "Pusher"],
                "trending_score": 0.60,
                "adoption_rate": 0.50,
                "community_activity": 0.60,
                "best_for": ["low_latency_sync"],
                "security_features": ["security_rules"]
            },
            FirebaseService.STORAGE: {
                "name": "Cloud Storage",
                "category": "storage",
                "complexity": "low",
                "cost_tier": "pay_per_use",
                "scalability": "very_high",
                "security_level": "high",
                "learning_curve": "low",
                "integration_effort": "low",
                "use_cases": ["file_upload", "media_storage", "backup"],
                "alternatives": ["AWS S3", "Google Cloud Storage", "Azure Blob"],
                "trending_score": 0.75,
                "adoption_rate": 0.70,
                "community_activity": 0.78,
                "best_for": ["file_storage"],
                "security_features": ["security_rules"]
            },
            FirebaseService.HOSTING: {
                "name": "Firebase Hosting",
                "category": "hosting",
                "complexity": "low",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "medium",
                "learning_curve": "low",
                "integration_effort": "low",
                "use_cases": ["static_sites", "spa_hosting", "cdn"],
                "alternatives": ["Vercel", "Netlify", "AWS S3 + CloudFront"],
                "trending_score": 0.80,
                "adoption_rate": 0.72,
                "community_activity": 0.80,
                "best_for": ["web_apps"],
                "security_features": ["ssl"]
            },
            FirebaseService.FUNCTIONS: {
                "name": "Cloud Functions",
                "category": "serverless",
                "complexity": "high",
                "cost_tier": "pay_per_use",
                "scalability": "very_high",
                "security_level": "high",
                "learning_curve": "high",
                "integration_effort": "high",
                "use_cases": ["api_endpoints", "background_tasks", "webhooks"],
                "alternatives": ["AWS Lambda", "Vercel Functions", "Google Cloud Functions"],
                "trending_score": 0.82,
                "adoption_rate": 0.58,
                "community_activity": 0.83,
                "dependencies": ["firestore", "authentication"],
                "best_for": ["backend_logic"],
                "security_features": ["iam"]
            },
            FirebaseService.ANALYTICS: {
                "name": "Firebase Analytics",
                "category": "analytics",
                "complexity": "low",
                "cost_tier": "free_tier_available",
                "scalability": "very_high",
                "security_level": "medium",
                "learning_curve": "low",
                "integration_effort": "low",
                "use_cases": ["user_behavior", "app_performance", "conversion_tracking"],
                "alternatives": ["Google Analytics", "Mixpanel", "Amplitude"],
                "trending_score": 0.78,
                "adoption_rate": 0.85,
                "community_activity": 0.75,
                "best_for": ["insights"],
                "security_features": ["privacy_controls"]
            },
            FirebaseService.CRASHLYTICS: {
                "name": "Firebase Crashlytics",
                "category": "monitoring",
                "complexity": "low",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "high",
                "learning_curve": "low",
                "integration_effort": "low",
                "use_cases": ["crash_reporting", "error_tracking", "stability_monitoring"],
                "alternatives": ["Sentry", "Bugsnag", "Rollbar"],
                "trending_score": 0.85,
                "adoption_rate": 0.68,
                "community_activity": 0.80,
                "best_for": ["crash_reporting"],
                "security_features": ["data_privacy"]
            },
            FirebaseService.PERFORMANCE: {
                "name": "Firebase Performance",
                "category": "monitoring",
                "complexity": "medium",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "medium",
                "learning_curve": "medium",
                "integration_effort": "medium",
                "use_cases": ["performance_monitoring", "bottleneck_identification", "optimization"],
                "alternatives": ["New Relic", "DataDog", "Google PageSpeed"],
                "trending_score": 0.72,
                "adoption_rate": 0.45,
                "community_activity": 0.70,
                "best_for": ["perf_monitoring"],
                "security_features": ["data_privacy"]
            },
            FirebaseService.REMOTE_CONFIG: {
                "name": "Firebase Remote Config",
                "category": "configuration",
                "complexity": "medium",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "high",
                "learning_curve": "medium",
                "integration_effort": "medium",
                "use_cases": ["feature_flags", "a_b_testing", "dynamic_configuration"],
                "alternatives": ["LaunchDarkly", "Split.io", "ConfigCat"],
                "trending_score": 0.75,
                "adoption_rate": 0.52,
                "community_activity": 0.72,
                "best_for": ["feature_flags"],
                "security_features": ["access_controls"]
            },
            FirebaseService.DYNAMIC_LINKS: {
                "name": "Firebase Dynamic Links",
                "category": "marketing",
                "complexity": "low",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "medium",
                "learning_curve": "low",
                "integration_effort": "low",
                "use_cases": ["deep_linking", "marketing_campaigns", "user_acquisition"],
                "alternatives": ["Branch.io", "Adjust", "AppsFlyer"],
                "trending_score": 0.68,
                "adoption_rate": 0.38,
                "community_activity": 0.65,
                "best_for": ["deep_linking"],
                "security_features": ["url_allowlist"]
            },
            FirebaseService.MESSAGING: {
                "name": "Cloud Messaging",
                "category": "messaging",
                "complexity": "medium",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "medium",
                "learning_curve": "medium",
                "integration_effort": "medium",
                "use_cases": ["push_notifications"],
                "alternatives": ["OneSignal"],
                "trending_score": 0.80,
                "adoption_rate": 0.80,
                "community_activity": 0.80,
                "best_for": ["notifications"],
                "security_features": ["auth_tokens"]
            },
            FirebaseService.TEST_LAB: {
                "name": "Test Lab",
                "category": "testing",
                "complexity": "medium",
                "cost_tier": "pay_per_use",
                "scalability": "high",
                "security_level": "high",
                "learning_curve": "medium",
                "integration_effort": "medium",
                "use_cases": ["automated_testing"],
                "alternatives": ["BrowserStack"],
                "trending_score": 0.60,
                "adoption_rate": 0.40,
                "community_activity": 0.50,
                "best_for": ["device_testing"],
                "security_features": ["secure_devices"]
            },
            FirebaseService.APPMESSAGING: {
                "name": "In-App Messaging",
                "category": "marketing",
                "complexity": "low",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "medium",
                "learning_curve": "low",
                "integration_effort": "low",
                "use_cases": ["user_engagement"],
                "alternatives": ["Braze"],
                "trending_score": 0.50,
                "adoption_rate": 0.30,
                "community_activity": 0.40,
                "best_for": ["engagement"],
                "security_features": ["data_privacy"]
            },
            FirebaseService.PREDICTIONS: {
                "name": "Predictions",
                "category": "ml",
                "complexity": "high",
                "cost_tier": "free_tier_available",
                "scalability": "high",
                "security_level": "high",
                "learning_curve": "high",
                "integration_effort": "medium",
                "use_cases": ["user_churn"],
                "alternatives": ["Custom ML"],
                "trending_score": 0.40,
                "adoption_rate": 0.20,
                "community_activity": 0.30,
                "best_for": ["user_predictions"],
                "security_features": ["data_privacy"]
            },
            FirebaseService.ML: {
                "name": "ML Kit",
                "category": "ml",
                "complexity": "high",
                "cost_tier": "pay_per_use",
                "scalability": "high",
                "security_level": "high",
                "learning_curve": "high",
                "integration_effort": "medium",
                "use_cases": ["vision", "text"],
                "alternatives": ["Google Cloud Vision"],
                "trending_score": 0.55,
                "adoption_rate": 0.35,
                "community_activity": 0.45,
                "best_for": ["on_device_ml"],
                "security_features": ["data_privacy"]
            }
        }
    
    def _initialize_project_profiles(self) -> Dict[FirebaseProjectType, Dict[str, Any]]:
        """Initialize Firebase project type profiles."""
        return {
            FirebaseProjectType.WEB_APP: {
                "description": "Web application with Firebase backend",
                "recommended_services": [
                    FirebaseService.AUTHENTICATION,
                    FirebaseService.FIRESTORE,
                    FirebaseService.STORAGE,
                    FirebaseService.HOSTING,
                    FirebaseService.ANALYTICS
                ],
                "optional_services": [
                    FirebaseService.FUNCTIONS,
                    FirebaseService.CRASHLYTICS,
                    FirebaseService.PERFORMANCE
                ],
                "complexity": "medium",
                "cost_estimate": "low_to_medium",
                "development_time": "2_4_weeks"
            },
            FirebaseProjectType.MOBILE_APP: {
                "description": "Mobile application with Firebase backend",
                "recommended_services": [
                    FirebaseService.AUTHENTICATION,
                    FirebaseService.FIRESTORE,
                    FirebaseService.STORAGE,
                    FirebaseService.ANALYTICS,
                    FirebaseService.CRASHLYTICS,
                    FirebaseService.MESSAGING,
                    FirebaseService.PERFORMANCE
                ],
                "optional_services": [
                    FirebaseService.FUNCTIONS,
                    FirebaseService.REMOTE_CONFIG,
                    FirebaseService.DYNAMIC_LINKS
                ],
                "complexity": "high",
                "cost_estimate": "medium_to_high",
                "development_time": "4_8_weeks"
            },
            FirebaseProjectType.BACKEND_SERVICE: {
                "description": "Backend service using Firebase",
                "recommended_services": [
                    FirebaseService.AUTHENTICATION,
                    FirebaseService.FIRESTORE,
                    FirebaseService.FUNCTIONS,
                    FirebaseService.STORAGE
                ],
                "optional_services": [
                    FirebaseService.ANALYTICS,
                    FirebaseService.PERFORMANCE
                ],
                "complexity": "high",
                "cost_estimate": "medium_to_high",
                "development_time": "3_6_weeks"
            },
            FirebaseProjectType.MICROSERVICE: {
                "description": "Microservice architecture with Firebase",
                "recommended_services": [
                    FirebaseService.FUNCTIONS,
                    FirebaseService.FIRESTORE,
                    FirebaseService.STORAGE
                ],
                "optional_services": [
                    FirebaseService.AUTHENTICATION,
                    FirebaseService.ANALYTICS,
                    FirebaseService.PERFORMANCE
                ],
                "complexity": "very_high",
                "cost_estimate": "high",
                "development_time": "6_12_weeks"
            },
            FirebaseProjectType.FULL_STACK: {
                "description": "Full-stack application with Firebase",
                "recommended_services": [
                    FirebaseService.AUTHENTICATION,
                    FirebaseService.FIRESTORE,
                    FirebaseService.STORAGE,
                    FirebaseService.HOSTING,
                    FirebaseService.FUNCTIONS,
                    FirebaseService.ANALYTICS
                ],
                "optional_services": [
                    FirebaseService.CRASHLYTICS,
                    FirebaseService.PERFORMANCE,
                    FirebaseService.REMOTE_CONFIG
                ],
                "complexity": "very_high",
                "cost_estimate": "high",
                "development_time": "8_16_weeks"
            }
        }
    
    def _initialize_recommendation_rules(self) -> Dict[str, Any]:
        """Initialize Firebase-specific recommendation rules."""
        return {
            "base_recommendations": {
                "authentication_rules": {
                    "always_recommend": ["Firebase Authentication"],
                    "when_to_consider": ["user_management_required", "social_login_needed"],
                    "alternatives": ["Auth0", "AWS Cognito", "Supabase Auth"],
                    "confidence_factors": ["security_requirements", "user_count", "integration_complexity"]
                },
                "database_rules": {
                    "always_recommend": ["Cloud Firestore"],
                    "when_to_consider": ["real_time_data", "offline_sync", "scalable_database"],
                    "alternatives": ["MongoDB Atlas", "AWS DynamoDB", "Supabase"],
                    "confidence_factors": ["data_complexity", "scalability_needs", "real_time_requirements"]
                },
                "hosting_rules": {
                    "always_recommend": ["Firebase Hosting"],
                    "when_to_consider": ["static_sites", "spa_hosting", "cdn_requirements"],
                    "alternatives": ["Vercel", "Netlify", "AWS S3 + CloudFront"],
                    "confidence_factors": ["site_type", "performance_requirements", "cost_constraints"]
                },
                "functions_rules": {
                    "conditional_recommend": ["Cloud Functions"],
                    "when_to_consider": ["api_endpoints", "background_tasks", "webhooks"],
                    "alternatives": ["AWS Lambda", "Vercel Functions", "Google Cloud Functions"],
                    "confidence_factors": ["complexity_requirements", "team_expertise", "cost_constraints"]
                }
            },
            "user_count_rules": {},
            "security_level_rules": {},
            "budget_range_rules": {},
            "integration_rules": {},
            "performance_rules": {}
        }
    
    def _initialize_cost_optimization_rules(self) -> Dict[str, Any]:
        """Initialize Firebase cost optimization rules."""
        return {
            "free_tier_services": [
                "Firebase Authentication",
                "Firebase Hosting",
                "Firebase Analytics",
                "Firebase Crashlytics",
                "Firebase Performance",
                "Firebase Remote Config",
                "Firebase Dynamic Links"
            ],
            "pay_per_use_services": [
                "Cloud Firestore",
                "Cloud Storage",
                "Cloud Functions"
            ],
            "cost_optimization_strategies": {
                "firestore": [
                    "Use offline persistence to reduce reads",
                    "Implement proper indexing",
                    "Use batch operations",
                    "Monitor query patterns"
                ],
                "storage": [
                    "Use appropriate storage classes",
                    "Implement lifecycle policies",
                    "Compress files before upload",
                    "Use CDN for frequently accessed files"
                ],
                "functions": [
                    "Optimize cold start times",
                    "Use appropriate memory allocation",
                    "Implement proper error handling",
                    "Monitor execution times"
                ]
            }
        }
    
    def _initialize_security_rules(self) -> Dict[str, Any]:
        """Initialize Firebase security rules."""
        return {
            "authentication_security": [
                "Enable multi-factor authentication",
                "Implement proper user validation",
                "Use secure password policies",
                "Monitor authentication events"
            ],
            "firestore_security": [
                "Write comprehensive security rules",
                "Implement proper data validation",
                "Use least privilege access",
                "Monitor data access patterns"
            ],
            "storage_security": [
                "Implement proper access controls",
                "Use signed URLs for sensitive files",
                "Encrypt sensitive data",
                "Monitor file access patterns"
            ],
            "functions_security": [
                "Implement proper authentication",
                "Validate input parameters",
                "Use secure environment variables",
                "Monitor function execution"
            ]
        }
    
    def get_firebase_recommendations(self, project_profile: FirebaseProjectProfile) -> List[FirebaseRecommendation]:
        """Get Firebase-specific recommendations based on project profile."""
        recommendations = []
        
        # Get recommended services for project type
        project_type_config = self.project_profiles.get(project_profile.project_type, {})
        recommended_services = project_type_config.get("recommended_services", [])
        optional_services = project_type_config.get("optional_services", [])
        
        # Generate recommendations for each service
        for service in recommended_services:
            service_config = self.firebase_services.get(service, {})
            recommendation = FirebaseRecommendation(
                service=service,
                recommendation=f"Implement {service_config.get('name', service.value)}",
                confidence=self._calculate_confidence(service, project_profile),
                reasoning=self._generate_reasoning(service, project_profile),
                alternatives=service_config.get("alternatives", []),
                implementation_effort=service_config.get("integration_effort", "medium"),
                cost_impact=self._calculate_cost_impact(service, project_profile),
                security_considerations=self._get_security_considerations(service),
                performance_impact=service_config.get("scalability", "medium"),
                scalability_impact=service_config.get("scalability", "medium")
            )
            recommendations.append(recommendation)
        
        return recommendations
    
    def _calculate_confidence(self, service: FirebaseService, profile: FirebaseProjectProfile) -> float:
        """Calculate confidence score for a Firebase service recommendation."""
        service_config = self.firebase_services.get(service, {})
        
        # Base confidence from service characteristics
        base_confidence = service_config.get("trending_score", 0.5)
        
        # Adjust based on project profile
        if profile.user_count == "enterprise" and service_config.get("scalability") == "very_high":
            base_confidence += 0.1
        elif profile.user_count == "small" and service_config.get("cost_tier") == "free_tier_available":
            base_confidence += 0.1
        
        if profile.security_level == "high" and service_config.get("security_level") == "high":
            base_confidence += 0.1
        elif profile.security_level == "basic" and service_config.get("complexity") == "low":
            base_confidence += 0.1
        
        return min(base_confidence, 1.0)
    
    def _generate_reasoning(self, service: FirebaseService, profile: FirebaseProjectProfile) -> str:
        """Generate reasoning for a Firebase service recommendation."""
        service_config = self.firebase_services.get(service, {})
        service_name = service_config.get("name", service.value)
        
        reasoning_parts = [f"Recommended {service_name} because:"]
        
        # Add reasoning based on project profile
        if profile.user_count in ["large", "enterprise"] and service_config.get("scalability") == "very_high":
            reasoning_parts.append("- Excellent scalability for large user bases")
        
        if profile.security_level == "high" and service_config.get("security_level") == "high":
            reasoning_parts.append("- High security level matches requirements")
        
        if profile.budget_range == "low" and service_config.get("cost_tier") == "free_tier_available":
            reasoning_parts.append("- Free tier available for cost optimization")
        
        if profile.team_size < 5 and service_config.get("learning_curve") == "low":
            reasoning_parts.append("- Low learning curve suitable for small teams")
        
        # Add general service benefits
        if service_config.get("adoption_rate", 0) > 0.7:
            reasoning_parts.append("- High adoption rate in the community")
        
        if service_config.get("community_activity", 0) > 0.8:
            reasoning_parts.append("- Active community support available")
        
        return " ".join(reasoning_parts)
    
    def _calculate_cost_impact(self, service: FirebaseService, profile: FirebaseProjectProfile) -> str:
        """Calculate cost impact for a Firebase service."""
        service_config = self.firebase_services.get(service, {})
        
        if service_config.get("cost_tier") == "free_tier_available":
            return "Low (Free tier available)"
        elif service_config.get("cost_tier") == "pay_per_use":
            if profile.user_count in ["small", "medium"]:
                return "Medium (Pay per use, scales with usage)"
            else:
                return "High (Pay per use, high usage expected)"
        else:
            return "Unknown"
    
    def _get_security_considerations(self, service: FirebaseService) -> List[str]:
        """Get security considerations for a Firebase service."""
        security_rules = self.security_rules
        
        if service == FirebaseService.AUTHENTICATION:
            return security_rules["authentication_security"]
        elif service == FirebaseService.FIRESTORE:
            return security_rules["firestore_security"]
        elif service == FirebaseService.STORAGE:
            return security_rules["storage_security"]
        elif service == FirebaseService.FUNCTIONS:
            return security_rules["functions_security"]
        else:
            return ["Follow Firebase security best practices"]

    def _calculate_service_score(self, service_config: Dict[str, Any]) -> float:
        """Calculate scoring for a service based on its characteristics."""
        score = 0.0
        if service_config.get("adoption_rate", 0) > 0.7:
            score += 0.4
        elif service_config.get("adoption_rate", 0) > 0.4:
            score += 0.2
            
        if service_config.get("community_activity", 0) > 0.7:
            score += 0.3
        elif service_config.get("community_activity", 0) > 0.4:
            score += 0.15
            
        if service_config.get("complexity") == "low":
            score += 0.3
        elif service_config.get("complexity") == "medium":
            score += 0.1
            
        return min(score, 1.0)

    def _calculate_project_complexity(self, profile: FirebaseProjectProfile) -> int:
        """Calculate numeric complexity score for a project profile."""
        score = 0
        
        complexity_scores = {
            "simple": 1,
            "moderate": 2,
            "complex": 3
        }
        score += complexity_scores.get(profile.data_complexity, 1)
        
        user_scores = {
            "small": 1,
            "medium": 2,
            "large": 3,
            "enterprise": 4
        }
        score += user_scores.get(profile.user_count, 1)
        
        if profile.real_time_requirements:
            score += 1
        if profile.offline_capability:
            score += 1
            
        return score

    def _get_service_dependencies(self, service: FirebaseService) -> List[str]:
        """Get dependencies for a specific service."""
        service_config = self.firebase_services.get(service, {})
        return service_config.get("dependencies", [])

    def get_optimal_firebase_setup(self, profile: FirebaseProjectProfile) -> Dict[str, Any]:
        """Generate optimal Firebase setup based on project profile."""
        recommendations = self.get_firebase_recommendations(profile)
        recommended_services = [rec.service.value for rec in recommendations]
        
        cost_estimate = "Low"
        if profile.user_count in ["large", "enterprise"] or profile.data_complexity == "complex":
            cost_estimate = "High"
        elif profile.user_count == "medium":
            cost_estimate = "Medium"
            
        security_posture = "Standard"
        if profile.security_level in ["high", "critical", "enterprise"]:
            security_posture = "Advanced"
            
        return {
            "project_profile": profile,
            "recommended_services": recommended_services,
            "detailed_recommendations": recommendations,
            "overall_cost_estimate": cost_estimate,
            "overall_security_posture": security_posture,
            "setup_script_template": "# Firebase setup script placeholder"
        }

def main():
    """Demo Firebase meta-intelligent configuration."""
    print("🔥 FIREBASE META-INTELLIGENT CONFIGURATION DEMO")
    print("=" * 60)
    
    # Initialize Firebase configuration
    config = FirebaseMetaIntelligentConfig()
    
    # Demo different project profiles
    profiles = [
        FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            user_count="medium",
            data_complexity="moderate",
            real_time_requirements=True,
            offline_capability=False,
            security_level="standard",
            budget_range="medium",
            team_size=3,
            development_timeline="standard"
        ),
        FirebaseProjectProfile(
            project_type=FirebaseProjectType.MOBILE_APP,
            user_count="large",
            data_complexity="complex",
            real_time_requirements=True,
            offline_capability=True,
            security_level="high",
            budget_range="high",
            team_size=5,
            development_timeline="extended"
        )
    ]
    
    for profile in profiles:
        print(f"\n🎯 {profile.project_type.value.replace('_', ' ').title()} Profile:")
        print(f"   User Count: {profile.user_count}")
        print(f"   Security Level: {profile.security_level}")
        print(f"   Budget Range: {profile.budget_range}")
        print(f"   Team Size: {profile.team_size}")
        
        # Get recommendations
        recommendations = config.get_firebase_recommendations(profile)
        
        print(f"\n   📋 Firebase Recommendations:")
        for rec in recommendations[:3]:  # Show first 3 recommendations
            print(f"     • {rec.service.value}: {rec.recommendation}")
            print(f"       Confidence: {rec.confidence:.2f}")
            print(f"       Cost Impact: {rec.cost_impact}")
            print(f"       Implementation: {rec.implementation_effort}")
    
    print("\n✅ Firebase Meta-Intelligent Configuration Demo Complete!")

if __name__ == "__main__":
    main()