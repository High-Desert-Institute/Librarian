#!/usr/bin/env python3
"""
Unit tests for secrets management
"""

import pytest
import tempfile
import os
import stat
from pathlib import Path
from app.common.secrets import SecretsManager

class TestSecrets:
    """Test secrets management"""
    
    def test_secrets_creation(self):
        """Test creating secrets manager"""
        with tempfile.TemporaryDirectory() as temp_dir:
            secrets_path = Path(temp_dir) / "test_secrets"
            secrets_manager = SecretsManager(str(secrets_path))
            
            # Should create example secrets
            assert secrets_path.exists()
    
    def test_secrets_loading(self):
        """Test loading secrets from file"""
        with tempfile.TemporaryDirectory() as temp_dir:
            secrets_path = Path(temp_dir) / "test_secrets"
            
            # Create test secrets file
            with open(secrets_path, 'w') as f:
                f.write("test_channel:test_psk\n")
                f.write("another_channel:another_psk\n")
            
            # Set proper permissions
            os.chmod(secrets_path, 0o600)
            
            secrets_manager = SecretsManager(str(secrets_path))
            
            assert secrets_manager.get_psk("test_channel") == "test_psk"
            assert secrets_manager.get_psk("another_channel") == "another_psk"
    
    def test_secrets_set_get(self):
        """Test setting and getting PSKs"""
        with tempfile.TemporaryDirectory() as temp_dir:
            secrets_path = Path(temp_dir) / "test_secrets"
            secrets_manager = SecretsManager(str(secrets_path))
            
            # Set PSK
            secrets_manager.set_psk("test_channel", "test_psk")
            
            # Get PSK
            assert secrets_manager.get_psk("test_channel") == "test_psk"
    
    def test_secrets_validation(self):
        """Test secrets validation"""
        with tempfile.TemporaryDirectory() as temp_dir:
            secrets_path = Path(temp_dir) / "test_secrets"
            secrets_manager = SecretsManager(str(secrets_path))
            
            # Should be invalid (no required channels)
            assert not secrets_manager.validate_secrets()
            
            # Add required channel
            secrets_manager.set_psk("decomp25", "real_psk")
            assert secrets_manager.validate_secrets()
    
    def test_secrets_file_permissions(self):
        """Test that secrets file has correct permissions"""
        with tempfile.TemporaryDirectory() as temp_dir:
            secrets_path = Path(temp_dir) / "test_secrets"
            secrets_manager = SecretsManager(str(secrets_path))
            
            # Create example secrets
            secrets_manager.create_example_secrets()
            
            # Check permissions
            file_stat = secrets_path.stat()
            file_mode = stat.filemode(file_stat.st_mode)
            assert file_mode == '-rw-------'
    
    def test_secrets_list_channels(self):
        """Test listing configured channels"""
        with tempfile.TemporaryDirectory() as temp_dir:
            secrets_path = Path(temp_dir) / "test_secrets"
            secrets_manager = SecretsManager(str(secrets_path))
            
            # Add some channels
            secrets_manager.set_psk("channel1", "psk1")
            secrets_manager.set_psk("channel2", "psk2")
            
            channels = secrets_manager.list_channels()
            assert "channel1" in channels
            assert "channel2" in channels

if __name__ == "__main__":
    pytest.main([__file__])
