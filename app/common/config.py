#!/usr/bin/env python3
"""
Configuration management for Librarian
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import toml
from app.common.logging import get_logger

logger = get_logger(__name__)

class Config:
    """Configuration manager for Librarian"""
    
    def __init__(self, config_path: str = "configs/config.toml"):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.load_config()
    
    def load_config(self) -> None:
        """Load configuration from TOML file"""
        if not self.config_path.exists():
            logger.info(f"Config file {self.config_path} not found, creating default")
            self.create_default_config()
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = toml.load(f)
            logger.info(f"Loaded configuration from {self.config_path}")
        except toml.TomlDecodeError as e:
            logger.error(f"Invalid TOML syntax in {self.config_path}: {e}")
            raise RuntimeError(f"Invalid TOML syntax in config file: {e}")
        except FileNotFoundError:
            logger.error(f"Config file not found: {self.config_path}")
            raise RuntimeError(f"Config file not found: {self.config_path}")
        except Exception as e:
            logger.error(f"Failed to load config from {self.config_path}: {e}")
            raise RuntimeError(f"Failed to load config: {e}")
    
    def create_default_config(self) -> None:
        """Create default configuration file"""
        default_config = {
            "node": {
                "name": "hdl-librarian-01",
                "serial_device": "/dev/ttyACM0",
                "time_zone": "America/Los_Angeles"
            },
            "meshtastic": {
                "group_channel": "decomp25",
                "dm_ack_enabled": True,
                "dm_ack_text": "📚 Noted. Consulting the archives…",
                "backlog_notice_threshold": 8,
                "backlog_notice_text": "⏳ Many queries in queue; replies may take a bit."
            },
            "ollama": {
                "host": "127.0.0.1",
                "port": 11434,
                "model": "qwen3:4b-instruct-q4",
                "max_tokens": 256,
                "temperature": 0.3
            },
            "rag": {
                "db_path": "./corpus/index",
                "top_k": 6,
                "max_chunk_tokens": 350,
                "fallback_lexical": True
            },
            "announce": {
                "schedule_file": "./configs/schedule.yml",
                "pre_start_offsets": [30, 10],
                "post_start_repeat_minutes": 0
            },
            "logging": {
                "level": "INFO",
                "dir": "./logs"
            }
        }
        
        # Ensure configs directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.config_path, 'w', encoding='utf-8') as f:
            toml.dump(default_config, f)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key (supports dot notation)"""
        keys = key.split('.')
        value = self.config
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value by key (supports dot notation)"""
        keys = key.split('.')
        config = self.config
        
        # Navigate to the parent of the target key
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        # Set the value
        config[keys[-1]] = value
    
    def save(self) -> None:
        """Save configuration to file"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            toml.dump(self.config, f)
    
    def reload(self) -> None:
        """Reload configuration from file"""
        self.load_config()
    
    def validate(self) -> bool:
        """Validate configuration with detailed error reporting"""
        errors = []
        warnings = []
        
        # Check required sections
        required_sections = ['node', 'meshtastic', 'ollama', 'rag', 'announce', 'logging']
        for section in required_sections:
            if section not in self.config:
                errors.append(f"Missing required section: {section}")
        
        if errors:
            for error in errors:
                logger.error(error)
            return False
        
        # Validate node section
        node_config = self.config.get('node', {})
        if not node_config.get('name'):
            errors.append("Node name is required")
        if not node_config.get('serial_device'):
            errors.append("Serial device is required")
        
        # Validate meshtastic section
        meshtastic_config = self.config.get('meshtastic', {})
        if not meshtastic_config.get('group_channel'):
            errors.append("Group channel is required")
        
        # Validate ollama section
        ollama_config = self.config.get('ollama', {})
        if not ollama_config.get('host'):
            errors.append("Ollama host is required")
        if not ollama_config.get('model'):
            errors.append("Ollama model is required")
        
        # Validate rag section
        rag_config = self.config.get('rag', {})
        if not rag_config.get('db_path'):
            errors.append("RAG database path is required")
        
        # Check for reasonable values
        if ollama_config.get('max_tokens', 0) <= 0:
            warnings.append("Ollama max_tokens should be positive")
        
        if rag_config.get('top_k', 0) <= 0:
            warnings.append("RAG top_k should be positive")
        
        # Log warnings
        for warning in warnings:
            logger.warning(warning)
        
        # Log errors and return
        if errors:
            for error in errors:
                logger.error(error)
            return False
        
        logger.info("Configuration validation passed")
        return True
    
    def get_validation_errors(self) -> List[str]:
        """Get list of validation errors without logging"""
        errors = []
        
        # Check required sections
        required_sections = ['node', 'meshtastic', 'ollama', 'rag', 'announce', 'logging']
        for section in required_sections:
            if section not in self.config:
                errors.append(f"Missing required section: {section}")
        
        if errors:
            return errors
        
        # Validate specific values
        if not self.config['node'].get('name'):
            errors.append("Node name is required")
        if not self.config['meshtastic'].get('group_channel'):
            errors.append("Group channel is required")
        if not self.config['ollama'].get('host'):
            errors.append("Ollama host is required")
        if not self.config['rag'].get('db_path'):
            errors.append("RAG database path is required")
        
        return errors

# Global config instance
_config: Optional[Config] = None

def get_config() -> Config:
    """Get global configuration instance"""
    global _config
    if _config is None:
        _config = Config()
    return _config

def reload_config() -> None:
    """Reload global configuration"""
    global _config
    if _config is not None:
        _config.reload()
