#!/usr/bin/env python3
"""
Unit tests for configuration management
"""

import pytest
import tempfile
import os
from pathlib import Path
from app.common.config import Config

class TestConfig:
    """Test configuration management"""
    
    def test_default_config_creation(self):
        """Test that default config is created when file doesn't exist"""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.toml"
            config = Config(str(config_path))
            
            assert config_path.exists()
            assert config.get('node.name') == "hdl-librarian-01"
            assert config.get('meshtastic.group_channel') == "decomp25"
    
    def test_config_loading(self):
        """Test loading existing configuration"""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.toml"
            
            # Create config file
            config = Config(str(config_path))
            
            # Test loading
            config2 = Config(str(config_path))
            assert config2.get('node.name') == "hdl-librarian-01"
    
    def test_config_get_set(self):
        """Test getting and setting configuration values"""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.toml"
            config = Config(str(config_path))
            
            # Test getting values
            assert config.get('node.name') == "hdl-librarian-01"
            assert config.get('nonexistent.key', 'default') == 'default'
            
            # Test setting values
            config.set('node.name', 'test-node')
            assert config.get('node.name') == 'test-node'
    
    def test_config_validation(self):
        """Test configuration validation"""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.toml"
            config = Config(str(config_path))
            
            # Default config should be valid
            assert config.validate() == True
    
    def test_config_save_reload(self):
        """Test saving and reloading configuration"""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.toml"
            config = Config(str(config_path))
            
            # Modify config
            config.set('node.name', 'modified-node')
            config.save()
            
            # Reload and verify
            config.reload()
            assert config.get('node.name') == 'modified-node'

if __name__ == "__main__":
    pytest.main([__file__])
