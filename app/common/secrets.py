#!/usr/bin/env python3
"""
Secrets management for Librarian
Handles secure storage and loading of sensitive configuration data
"""

import os
import stat
from pathlib import Path
from typing import Dict, Optional, Any
from app.common.logging import get_logger

logger = get_logger(__name__)

class SecretsManager:
    """Manages secure storage and loading of secrets"""
    
    def __init__(self, secrets_file: str = "configs/channels.secrets"):
        self.secrets_file = Path(secrets_file)
        self.secrets: Dict[str, str] = {}
        self.load_secrets()
    
    def load_secrets(self) -> None:
        """Load secrets from file with proper security checks"""
        if not self.secrets_file.exists():
            logger.warning(f"Secrets file {self.secrets_file} does not exist")
            return
        
        # Check file permissions (should be 0600)
        file_stat = self.secrets_file.stat()
        file_mode = stat.filemode(file_stat.st_mode)
        
        if file_mode != '-rw-------':
            logger.warning(f"Secrets file {self.secrets_file} has incorrect permissions: {file_mode}")
            logger.warning("Expected: -rw------- (0600)")
        
        try:
            with open(self.secrets_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    
                    # Parse channel:psk format
                    if ':' not in line:
                        logger.warning(f"Invalid secrets format at line {line_num}: {line}")
                        continue
                    
                    channel, psk = line.split(':', 1)
                    self.secrets[channel.strip()] = psk.strip()
                    
            logger.info(f"Loaded {len(self.secrets)} secrets from {self.secrets_file}")
            
        except Exception as e:
            logger.error(f"Failed to load secrets from {self.secrets_file}: {e}")
            raise RuntimeError(f"Failed to load secrets: {e}")
    
    def get_psk(self, channel: str) -> Optional[str]:
        """Get PSK for a specific channel"""
        return self.secrets.get(channel)
    
    def set_psk(self, channel: str, psk: str) -> None:
        """Set PSK for a specific channel"""
        self.secrets[channel] = psk
        self.save_secrets()
    
    def save_secrets(self) -> None:
        """Save secrets to file with proper permissions"""
        # Ensure configs directory exists
        self.secrets_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(self.secrets_file, 'w', encoding='utf-8') as f:
                f.write("# Channel PSKs for Librarian\n")
                f.write("# Format: channel_name:psk_value\n")
                f.write("# This file should have permissions 0600 (readable only by owner)\n\n")
                
                for channel, psk in self.secrets.items():
                    f.write(f"{channel}:{psk}\n")
            
            # Set proper permissions (0600)
            os.chmod(self.secrets_file, 0o600)
            logger.info(f"Saved {len(self.secrets)} secrets to {self.secrets_file}")
            
        except Exception as e:
            logger.error(f"Failed to save secrets to {self.secrets_file}: {e}")
            raise RuntimeError(f"Failed to save secrets: {e}")
    
    def create_example_secrets(self) -> None:
        """Create example secrets file with placeholder values"""
        example_secrets = {
            "decomp25": "EXAMPLE_PSK_VALUE_REPLACE_WITH_REAL_PSK",
            "test_channel": "TEST_PSK_VALUE"
        }
        
        # Ensure configs directory exists
        self.secrets_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.secrets_file, 'w', encoding='utf-8') as f:
            f.write("# Channel PSKs for Librarian\n")
            f.write("# Format: channel_name:psk_value\n")
            f.write("# This file should have permissions 0600 (readable only by owner)\n")
            f.write("# Replace EXAMPLE_PSK_VALUE with actual PSK values\n\n")
            
            for channel, psk in example_secrets.items():
                f.write(f"{channel}:{psk}\n")
        
        # Set proper permissions (0600)
        os.chmod(self.secrets_file, 0o600)
        logger.info(f"Created example secrets file at {self.secrets_file}")
    
    def validate_secrets(self) -> bool:
        """Validate that required secrets are present"""
        required_channels = ["decomp25"]  # Add more as needed
        
        missing_channels = []
        for channel in required_channels:
            if channel not in self.secrets:
                missing_channels.append(channel)
        
        if missing_channels:
            logger.error(f"Missing secrets for channels: {missing_channels}")
            return False
        
        # Check for placeholder values
        placeholder_values = ["EXAMPLE_PSK_VALUE", "TEST_PSK_VALUE"]
        for channel, psk in self.secrets.items():
            if psk in placeholder_values:
                logger.warning(f"Channel {channel} has placeholder PSK value: {psk}")
        
        return True
    
    def list_channels(self) -> list:
        """Get list of configured channels"""
        return list(self.secrets.keys())

# Global secrets manager instance
_secrets_manager: Optional[SecretsManager] = None

def get_secrets_manager() -> SecretsManager:
    """Get global secrets manager instance"""
    global _secrets_manager
    if _secrets_manager is None:
        _secrets_manager = SecretsManager()
    return _secrets_manager

def reload_secrets() -> None:
    """Reload global secrets manager"""
    global _secrets_manager
    if _secrets_manager is not None:
        _secrets_manager.load_secrets()
