#!/usr/bin/env python3

"""
test_firebase_config.py

Comprehensive test suite for Firebase Configuration following project testing standards.
Tests Firebase-specific meta-intelligent configuration and recommendations.
"""

import pytest
import json
from unittest.mock import Mock, patch
from datetime import datetime

# Add the project root to the Python path
from pathlib import Path
project_root = Path(__file__).parent.parent.parent.parent.parent
import sys
sys.path.insert(0, str(project_root))

from features.meta_intelligent_orchestration.instances.firebase_config import (
    FirebaseMetaIntelligentConfig, FirebaseProjectProfile, FirebaseProjectType,
    FirebaseService, FirebaseRecommendation
)

class TestFirebaseProjectProfile:
    """Test suite for Firebase Project Profile."""
    
    def test_firebase_project_profile_creation(self):
        """Test Firebase project profile creation."""
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            user_count="medium",
            data_complexity="moderate",
            real_time_requirements=True,
            offline_capability=False,
            security_level="standard",
            budget_range="medium",
            team_size=3,
            development_timeline="standard"
        )
        
        assert profile.project_type == FirebaseProjectType.WEB_APP
        assert profile.user_count == "medium"
        assert profile.data_complexity == "moderate"
        assert profile.real_time_requirements is True
        assert profile.offline_capability is False
        assert profile.security_level == "standard"
        assert profile.budget_range == "medium"
        assert profile.team_size == 3
        assert profile.development_timeline == "standard"
    
    def test_firebase_project_profile_defaults(self):
        """Test Firebase project profile with default values."""
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.MOBILE_APP
        )
        
        assert profile.project_type == FirebaseProjectType.MOBILE_APP
        assert profile.user_count == "small"
        assert profile.data_complexity == "simple"
        assert profile.real_time_requirements is False
        assert profile.offline_capability is False
        assert profile.security_level == "standard"
        assert profile.budget_range == "low"
        assert profile.team_size == 1
        assert profile.development_timeline == "standard"

class TestFirebaseMetaIntelligentConfig:
    """Test suite for Firebase Meta-Intelligent Configuration."""
    
    @pytest.fixture
    def firebase_config(self):
        """Create a Firebase configuration instance for testing."""
        return FirebaseMetaIntelligentConfig()
    
    def test_firebase_config_initialization(self, firebase_config):
        """Test Firebase configuration initialization."""
        assert firebase_config is not None
        assert firebase_config.firebase_services is not None
        assert firebase_config.project_profiles is not None
        assert firebase_config.recommendation_rules is not None
    
    def test_firebase_services_loaded(self, firebase_config):
        """Test that Firebase services are properly loaded."""
        services = firebase_config.firebase_services
        
        # Check that all expected services are present
        expected_services = [
            FirebaseService.AUTHENTICATION,
            FirebaseService.FIRESTORE,
            FirebaseService.REALTIME_DATABASE,
            FirebaseService.STORAGE,
            FirebaseService.FUNCTIONS,
            FirebaseService.HOSTING,
            FirebaseService.ANALYTICS,
            FirebaseService.CRASHLYTICS,
            FirebaseService.PERFORMANCE,
            FirebaseService.REMOTE_CONFIG,
            FirebaseService.MESSAGING,
            FirebaseService.DYNAMIC_LINKS,
            FirebaseService.TEST_LAB,
            FirebaseService.APPMESSAGING,
            FirebaseService.PREDICTIONS,
            FirebaseService.ML
        ]
        
        for service in expected_services:
            assert service in services
            service_config = services[service]
            assert "name" in service_config
            assert "adoption_rate" in service_config
            assert "community_activity" in service_config
            assert "learning_curve" in service_config
            assert "cost_tier" in service_config
            assert "scalability" in service_config
            assert "security_features" in service_config
            assert "best_for" in service_config
    
    def test_project_profiles_loaded(self, firebase_config):
        """Test that project profiles are properly loaded."""
        profiles = firebase_config.project_profiles
        
        # Check that all expected project types are present
        expected_types = [
            FirebaseProjectType.WEB_APP,
            FirebaseProjectType.MOBILE_APP,
            FirebaseProjectType.BACKEND_SERVICE,
            FirebaseProjectType.MICROSERVICE,
            FirebaseProjectType.FULL_STACK
        ]
        
        for project_type in expected_types:
            assert project_type in profiles
            profile_config = profiles[project_type]
            assert "description" in profile_config
            assert "complexity" in profile_config
            assert "cost_estimate" in profile_config
            assert "development_time" in profile_config
            assert "recommended_services" in profile_config
    
    def test_recommendation_rules_loaded(self, firebase_config):
        """Test that recommendation rules are properly loaded."""
        rules = firebase_config.recommendation_rules
        
        assert "base_recommendations" in rules
        assert "user_count_rules" in rules
        assert "security_level_rules" in rules
        assert "budget_range_rules" in rules
        assert "integration_rules" in rules
        assert "performance_rules" in rules
    
    def test_get_firebase_recommendations_web_app(self, firebase_config):
        """Test Firebase recommendations for web app."""
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            user_count="medium",
            security_level="standard",
            budget_range="medium"
        )
        
        recommendations = firebase_config.get_firebase_recommendations(profile)
        
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0
        
        # Check that recommendations have required fields
        for rec in recommendations:
            assert isinstance(rec, FirebaseRecommendation)
            assert rec.service is not None
            assert rec.recommendation is not None
            assert rec.confidence >= 0.0
            assert rec.confidence <= 1.0
            assert rec.cost_impact is not None
            assert rec.implementation_effort is not None
            assert rec.security_notes is not None
            assert rec.performance_notes is not None
    
    def test_get_firebase_recommendations_mobile_app(self, firebase_config):
        """Test Firebase recommendations for mobile app."""
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.MOBILE_APP,
            user_count="large",
            security_level="high",
            budget_range="high"
        )
        
        recommendations = firebase_config.get_firebase_recommendations(profile)
        
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0
        
        # Check for mobile-specific services
        service_names = [rec.service for rec in recommendations]
        assert FirebaseService.CRASHLYTICS in service_names
        assert FirebaseService.PERFORMANCE in service_names
        assert FirebaseService.MESSAGING in service_names
    
    def test_get_firebase_recommendations_high_security(self, firebase_config):
        """Test Firebase recommendations for high security requirements."""
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            user_count="enterprise",
            security_level="critical",
            budget_range="high"
        )
        
        recommendations = firebase_config.get_firebase_recommendations(profile)
        
        # Check for security-focused recommendations
        for rec in recommendations:
            if rec.service == FirebaseService.AUTHENTICATION:
                assert "MFA" in rec.security_notes or "multi-factor" in rec.security_notes.lower()
    
    def test_get_firebase_recommendations_low_budget(self, firebase_config):
        """Test Firebase recommendations for low budget."""
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            user_count="small",
            security_level="standard",
            budget_range="low"
        )
        
        recommendations = firebase_config.get_firebase_recommendations(profile)
        
        # Check that recommendations consider budget constraints
        for rec in recommendations:
            if "usage-based" in rec.cost_impact.lower():
                assert rec.confidence < 0.9  # Lower confidence for potentially expensive services
    
    def test_get_optimal_firebase_setup(self, firebase_config):
        """Test optimal Firebase setup generation."""
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.FULL_STACK,
            user_count="medium",
            security_level="standard",
            budget_range="medium"
        )
        
        setup = firebase_config.get_optimal_firebase_setup(profile)
        
        assert isinstance(setup, dict)
        assert "project_profile" in setup
        assert "recommended_services" in setup
        assert "detailed_recommendations" in setup
        assert "overall_cost_estimate" in setup
        assert "overall_security_posture" in setup
        assert "setup_script_template" in setup
        
        assert setup["project_profile"] == profile
        assert isinstance(setup["recommended_services"], list)
        assert isinstance(setup["detailed_recommendations"], list)
    
    def test_firebase_service_scoring(self, firebase_config):
        """Test Firebase service scoring algorithm."""
        # Test a high-adoption service
        auth_service = firebase_config.firebase_services[FirebaseService.AUTHENTICATION]
        auth_score = firebase_config._calculate_service_score(auth_service)
        
        # Authentication should have a high score due to high adoption
        assert auth_score > 0.7
        
        # Test a specialized service
        ml_service = firebase_config.firebase_services[FirebaseService.ML]
        ml_score = firebase_config._calculate_service_score(ml_service)
        
        # ML should have a lower score due to specialized use case
        assert ml_score < auth_score
    
    def test_project_complexity_scoring(self, firebase_config):
        """Test project complexity scoring."""
        # Simple project
        simple_profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            user_count="small",
            data_complexity="simple"
        )
        simple_score = firebase_config._calculate_project_complexity(simple_profile)
        
        # Complex project
        complex_profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.FULL_STACK,
            user_count="enterprise",
            data_complexity="complex"
        )
        complex_score = firebase_config._calculate_project_complexity(complex_profile)
        
        assert complex_score > simple_score
    
    def test_recommendation_confidence_calculation(self, firebase_config):
        """Test recommendation confidence calculation."""
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            user_count="medium",
            security_level="standard",
            budget_range="medium"
        )
        
        recommendations = firebase_config.get_firebase_recommendations(profile)
        
        # All recommendations should have valid confidence scores
        for rec in recommendations:
            assert 0.0 <= rec.confidence <= 1.0
            assert isinstance(rec.confidence, float)
    
    def test_firebase_service_dependencies(self, firebase_config):
        """Test Firebase service dependency management."""
        # Test that services with dependencies are handled correctly
        functions_service = firebase_config.firebase_services[FirebaseService.FUNCTIONS]
        assert "dependencies" in functions_service
        
        # Test dependency resolution
        dependencies = firebase_config._get_service_dependencies(FirebaseService.FUNCTIONS)
        assert isinstance(dependencies, list)
    
    def test_firebase_cost_optimization(self, firebase_config):
        """Test Firebase cost optimization recommendations."""
        # Low budget profile
        low_budget_profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            budget_range="low"
        )
        
        low_budget_recs = firebase_config.get_firebase_recommendations(low_budget_profile)
        
        # High budget profile
        high_budget_profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            budget_range="high"
        )
        
        high_budget_recs = firebase_config.get_firebase_recommendations(high_budget_profile)
        
        # High budget should have more services recommended
        assert len(high_budget_recs) >= len(low_budget_recs)
    
    def test_firebase_security_recommendations(self, firebase_config):
        """Test Firebase security-focused recommendations."""
        # High security profile
        high_security_profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            security_level="critical"
        )
        
        high_security_recs = firebase_config.get_firebase_recommendations(high_security_profile)
        
        # Standard security profile
        standard_security_profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.WEB_APP,
            security_level="standard"
        )
        
        standard_security_recs = firebase_config.get_firebase_recommendations(standard_security_profile)
        
        # High security should have more security-focused recommendations
        high_security_count = sum(1 for rec in high_security_recs if "security" in rec.security_notes.lower())
        standard_security_count = sum(1 for rec in standard_security_recs if "security" in rec.security_notes.lower())
        
        assert high_security_count >= standard_security_count

class TestFirebaseConfigurationIntegration:
    """Integration tests for Firebase Configuration."""
    
    @pytest.fixture
    def firebase_config(self):
        """Create a Firebase configuration for integration testing."""
        return FirebaseMetaIntelligentConfig()
    
    def test_end_to_end_recommendation_workflow(self, firebase_config):
        """Test complete recommendation workflow."""
        # Create a complex project profile
        profile = FirebaseProjectProfile(
            project_type=FirebaseProjectType.FULL_STACK,
            user_count="large",
            data_complexity="complex",
            real_time_requirements=True,
            offline_capability=True,
            security_level="high",
            budget_range="high",
            team_size=5,
            development_timeline="extended"
        )
        
        # Get recommendations
        recommendations = firebase_config.get_firebase_recommendations(profile)
        
        # Get optimal setup
        setup = firebase_config.get_optimal_firebase_setup(profile)
        
        # Validate results
        assert len(recommendations) > 0
        assert setup is not None
        assert setup["project_profile"] == profile
        
        # Check that recommendations align with setup
        recommended_services = [rec.service for rec in recommendations]
        setup_services = setup["recommended_services"]
        
        # All recommended services should be in the setup
        for service in recommended_services:
            assert service.value in setup_services
    
    def test_multiple_project_types_comparison(self, firebase_config):
        """Test recommendations across different project types."""
        project_types = [
            FirebaseProjectType.WEB_APP,
            FirebaseProjectType.MOBILE_APP,
            FirebaseProjectType.BACKEND_SERVICE,
            FirebaseProjectType.MICROSERVICE,
            FirebaseProjectType.FULL_STACK
        ]
        
        recommendations_by_type = {}
        
        for project_type in project_types:
            profile = FirebaseProjectProfile(project_type=project_type)
            recommendations = firebase_config.get_firebase_recommendations(profile)
            recommendations_by_type[project_type] = recommendations
        
        # Each project type should have different recommendations
        for i, type1 in enumerate(project_types):
            for type2 in project_types[i+1:]:
                recs1 = recommendations_by_type[type1]
                recs2 = recommendations_by_type[type2]
                
                # Different project types should have different service recommendations
                services1 = {rec.service for rec in recs1}
                services2 = {rec.service for rec in recs2}
                
                # They shouldn't be identical (though some overlap is expected)
                assert services1 != services2 or len(services1) == 0

if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
