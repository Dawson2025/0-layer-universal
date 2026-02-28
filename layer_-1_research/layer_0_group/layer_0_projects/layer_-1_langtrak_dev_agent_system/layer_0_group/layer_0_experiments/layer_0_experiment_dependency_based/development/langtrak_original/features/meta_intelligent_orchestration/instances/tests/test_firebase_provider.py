#!/usr/bin/env python3

"""
test_firebase_provider.py

Comprehensive test suite for Firebase Provider following project testing standards.
Tests Firebase-specific implementation of TechnologyProvider interface.
"""

import pytest
import asyncio
import json
import tempfile
import os
from unittest.mock import Mock, patch, AsyncMock
from datetime import datetime
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
import sys
sys.path.insert(0, str(project_root))

from features.meta_intelligent_orchestration.instances.firebase_provider import FirebaseProvider
from features.meta_intelligent_orchestration.core.orchestration.universal_orchestration_system import Environment, EnvironmentType, Integration

class TestFirebaseProvider:
    """Test suite for Firebase Provider implementation."""
    
    @pytest.fixture
    def firebase_provider(self):
        """Create a Firebase provider instance for testing."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            config = {
                "default_region": "us-central1",
                "firebase_cli_path": "firebase",
                "gcloud_cli_path": "gcloud",
                "project_configs": {}
            }
            json.dump(config, f)
            config_file = f.name
        
        provider = FirebaseProvider(config_file)
        yield provider
        
        # Cleanup
        os.unlink(config_file)
    
    @pytest.fixture
    def sample_environment(self):
        """Create a sample environment for testing."""
        return Environment(
            name="test-env",
            type=EnvironmentType.DEVELOPMENT,
            project_id="test-project",
            region="us-central1",
            status="creating",
            created_at=datetime.now(),
            last_updated=datetime.now(),
            metadata={}
        )
    
    @pytest.fixture
    def sample_integration(self):
        """Create a sample integration for testing."""
        return Integration(
            id="test-integration",
            name="Test Integration",
            type="authentication",
            version="latest",
            status="deploying",
            environment="test-env",
            dependencies=[],
            configuration={},
            health_status="unknown",
            last_checked=datetime.now()
        )
    
    def test_firebase_provider_initialization(self, firebase_provider):
        """Test Firebase provider initialization."""
        assert firebase_provider is not None
        assert firebase_provider.config is not None
        assert firebase_provider.config["default_region"] == "us-central1"
        assert firebase_provider.firebase_projects == {}
    
    def test_load_config(self, firebase_provider):
        """Test configuration loading."""
        config = firebase_provider.config
        assert "default_region" in config
        assert "firebase_cli_path" in config
        assert "gcloud_cli_path" in config
        assert "project_configs" in config
    
    @pytest.mark.asyncio
    async def test_create_environment_success(self, firebase_provider, sample_environment):
        """Test successful environment creation."""
        with patch.object(firebase_provider, '_initialize_firebase_project', return_value=True) as mock_init, \
             patch.object(firebase_provider, '_configure_environment', return_value=True) as mock_config, \
             patch.object(firebase_provider, '_deploy_firebase_services', return_value=True) as mock_deploy:
            
            result = await firebase_provider.create_environment(sample_environment)
            
            assert result is True
            mock_init.assert_called_once_with(sample_environment.project_id)
            mock_config.assert_called_once_with(sample_environment)
            mock_deploy.assert_called_once_with(sample_environment)
    
    @pytest.mark.asyncio
    async def test_create_environment_failure(self, firebase_provider, sample_environment):
        """Test environment creation failure."""
        with patch.object(firebase_provider, '_initialize_firebase_project', return_value=False):
            result = await firebase_provider.create_environment(sample_environment)
            assert result is False
    
    @pytest.mark.asyncio
    async def test_deploy_integration_authentication(self, firebase_provider, sample_integration):
        """Test authentication integration deployment."""
        with patch.object(firebase_provider, '_deploy_firebase_auth', return_value=True) as mock_auth:
            result = await firebase_provider.deploy_integration(sample_integration, "test-env")
            
            assert result is True
            mock_auth.assert_called_once_with(sample_integration, "test-env")
    
    @pytest.mark.asyncio
    async def test_deploy_integration_database(self, firebase_provider):
        """Test database integration deployment."""
        integration = Integration(
            id="test-db",
            name="Test Database",
            type="database",
            version="latest",
            status="deploying",
            environment="test-env",
            dependencies=[],
            configuration={},
            health_status="unknown",
            last_checked=datetime.now()
        )
        
        with patch.object(firebase_provider, '_deploy_firestore', return_value=True) as mock_firestore:
            result = await firebase_provider.deploy_integration(integration, "test-env")
            
            assert result is True
            mock_firestore.assert_called_once_with(integration, "test-env")
    
    @pytest.mark.asyncio
    async def test_deploy_integration_unknown_type(self, firebase_provider):
        """Test deployment of unknown integration type."""
        integration = Integration(
            id="test-unknown",
            name="Test Unknown",
            type="unknown_type",
            version="latest",
            status="deploying",
            environment="test-env",
            dependencies=[],
            configuration={},
            health_status="unknown",
            last_checked=datetime.now()
        )
        
        result = await firebase_provider.deploy_integration(integration, "test-env")
        assert result is False
    
    @pytest.mark.asyncio
    async def test_check_health_authentication(self, firebase_provider, sample_integration):
        """Test authentication health checking."""
        with patch.object(firebase_provider, '_check_auth_health', return_value="healthy") as mock_health:
            result = await firebase_provider.check_health(sample_integration)
            
            assert result == "healthy"
            mock_health.assert_called_once_with(sample_integration)
    
    @pytest.mark.asyncio
    async def test_check_health_exception(self, firebase_provider, sample_integration):
        """Test health checking with exception."""
        with patch.object(firebase_provider, '_check_auth_health', side_effect=Exception("Test error")):
            result = await firebase_provider.check_health(sample_integration)
            assert result == "unhealthy"
    
    @pytest.mark.asyncio
    async def test_get_dependencies(self, firebase_provider):
        """Test dependency retrieval."""
        # Test known integration types
        auth_deps = await firebase_provider.get_dependencies("authentication")
        assert auth_deps == []
        
        db_deps = await firebase_provider.get_dependencies("database")
        assert db_deps == ["authentication"]
        
        func_deps = await firebase_provider.get_dependencies("functions")
        assert func_deps == ["authentication", "database"]
        
        # Test unknown integration type
        unknown_deps = await firebase_provider.get_dependencies("unknown")
        assert unknown_deps == []
    
    @pytest.mark.asyncio
    async def test_initialize_firebase_project_success(self, firebase_provider):
        """Test successful Firebase project initialization."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = "Firebase CLI 12.0.0"
            
            result = await firebase_provider._initialize_firebase_project("test-project")
            
            assert result is True
            assert "test-project" in firebase_provider.firebase_projects
            assert firebase_provider.firebase_projects["test-project"]["initialized"] is True
    
    @pytest.mark.asyncio
    async def test_initialize_firebase_project_cli_not_found(self, firebase_provider):
        """Test Firebase project initialization when CLI is not found."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 1
            mock_run.return_value.stderr = "firebase: command not found"
            
            result = await firebase_provider._initialize_firebase_project("test-project")
            
            assert result is False
    
    @pytest.mark.asyncio
    async def test_configure_environment(self, firebase_provider, sample_environment):
        """Test environment configuration."""
        result = await firebase_provider._configure_environment(sample_environment)
        
        assert result is True
        # Check that config file was created
        config_file = f"firebase-config-{sample_environment.name}.json"
        assert os.path.exists(config_file)
        
        # Cleanup
        os.unlink(config_file)
    
    @pytest.mark.asyncio
    async def test_deploy_firebase_services(self, firebase_provider, sample_environment):
        """Test Firebase services deployment."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            
            result = await firebase_provider._deploy_firebase_services(sample_environment)
            
            assert result is True
            mock_run.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_deploy_firebase_auth(self, firebase_provider, sample_integration):
        """Test Firebase Authentication deployment."""
        result = await firebase_provider._deploy_firebase_auth(sample_integration, "test-env")
        
        assert result is True
        # Check that auth config file was created
        config_file = "auth-config-test-env.json"
        assert os.path.exists(config_file)
        
        # Cleanup
        os.unlink(config_file)
    
    @pytest.mark.asyncio
    async def test_deploy_firestore(self, firebase_provider, sample_integration):
        """Test Firestore deployment."""
        result = await firebase_provider._deploy_firestore(sample_integration, "test-env")
        
        assert result is True
        # Check that firestore config file was created
        config_file = "firestore-config-test-env.json"
        assert os.path.exists(config_file)
        
        # Cleanup
        os.unlink(config_file)
    
    @pytest.mark.asyncio
    async def test_check_auth_health_success(self, firebase_provider, sample_integration):
        """Test successful authentication health check."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            
            result = await firebase_provider._check_auth_health(sample_integration)
            
            assert result == "healthy"
    
    @pytest.mark.asyncio
    async def test_check_auth_health_failure(self, firebase_provider, sample_integration):
        """Test failed authentication health check."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 1
            
            result = await firebase_provider._check_auth_health(sample_integration)
            
            assert result == "unhealthy"
    
    def test_firebase_provider_interface_compliance(self, firebase_provider):
        """Test that Firebase provider implements TechnologyProvider interface."""
        from features.meta_intelligent_orchestration.core.orchestration.universal_orchestration_system import TechnologyProvider
        
        # Check that FirebaseProvider is a subclass of TechnologyProvider
        assert issubclass(FirebaseProvider, TechnologyProvider)
        
        # Check that all required methods exist
        required_methods = [
            'create_environment',
            'deploy_integration', 
            'check_health',
            'get_dependencies'
        ]
        
        for method in required_methods:
            assert hasattr(firebase_provider, method)
            assert callable(getattr(firebase_provider, method))

class TestFirebaseProviderIntegration:
    """Integration tests for Firebase Provider."""
    
    @pytest.fixture
    def firebase_provider(self):
        """Create a Firebase provider for integration testing."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            config = {
                "default_region": "us-central1",
                "firebase_cli_path": "firebase",
                "gcloud_cli_path": "gcloud",
                "project_configs": {}
            }
            json.dump(config, f)
            config_file = f.name
        
        provider = FirebaseProvider(config_file)
        yield provider
        
        # Cleanup
        os.unlink(config_file)
    
    @pytest.mark.asyncio
    async def test_full_environment_creation_workflow(self, firebase_provider):
        """Test complete environment creation workflow."""
        environment = Environment(
            name="integration-test-env",
            type=EnvironmentType.DEVELOPMENT,
            project_id="integration-test-project",
            region="us-central1",
            status="creating",
            created_at=datetime.now(),
            last_updated=datetime.now(),
            metadata={}
        )
        
        with patch.object(firebase_provider, '_initialize_firebase_project', return_value=True), \
             patch.object(firebase_provider, '_configure_environment', return_value=True), \
             patch.object(firebase_provider, '_deploy_firebase_services', return_value=True):
            
            result = await firebase_provider.create_environment(environment)
            assert result is True
    
    @pytest.mark.asyncio
    async def test_full_integration_deployment_workflow(self, firebase_provider):
        """Test complete integration deployment workflow."""
        integration = Integration(
            id="integration-test-auth",
            name="Integration Test Auth",
            type="authentication",
            version="latest",
            status="deploying",
            environment="integration-test-env",
            dependencies=[],
            configuration={"providers": ["google", "email"]},
            health_status="unknown",
            last_checked=datetime.now()
        )
        
        with patch.object(firebase_provider, '_deploy_firebase_auth', return_value=True):
            result = await firebase_provider.deploy_integration(integration, "integration-test-env")
            assert result is True
    
    @pytest.mark.asyncio
    async def test_health_monitoring_workflow(self, firebase_provider):
        """Test health monitoring workflow."""
        integration = Integration(
            id="health-test-auth",
            name="Health Test Auth",
            type="authentication",
            version="latest",
            status="active",
            environment="health-test-env",
            dependencies=[],
            configuration={},
            health_status="unknown",
            last_checked=datetime.now()
        )
        
        with patch.object(firebase_provider, '_check_auth_health', return_value="healthy"):
            result = await firebase_provider.check_health(integration)
            assert result == "healthy"

if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
