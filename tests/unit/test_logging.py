#!/usr/bin/env python3
"""
Unit tests for logging system
"""

import pytest
import tempfile
import json
from pathlib import Path
from app.common.logging import setup_logging, get_logger, LibrarianLogger

class TestLogging:
    """Test logging functionality"""
    
    def test_logger_creation(self):
        """Test logger creation"""
        logger = get_logger("test")
        assert isinstance(logger, LibrarianLogger)
        assert logger.logger.name == "test"
    
    def test_logger_methods(self):
        """Test custom logger methods"""
        logger = get_logger("test")
        
        # Test log_user_input
        logger.log_user_input("test input")
        
        # Test log_output
        logger.log_output("test output")
        
        # Test log_operation
        logger.log_operation("test_op", "test_component", "test_phase", key="value")
    
    def test_setup_logging(self):
        """Test logging setup"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Change to temp directory
            original_cwd = Path.cwd()
            try:
                os.chdir(temp_dir)
                setup_logging(verbose=True, test_mode=True)
                
                # Check that log file was created
                log_file = Path("logs/test.log")
                assert log_file.exists()
                
            finally:
                os.chdir(original_cwd)
    
    def test_json_logging(self):
        """Test JSON log format"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            try:
                os.chdir(temp_dir)
                setup_logging(verbose=True, test_mode=True)
                
                logger = get_logger("test")
                logger.info("Test message")
                
                # Check log file content
                log_file = Path("logs/test.log")
                assert log_file.exists()
                
                with open(log_file, 'r') as f:
                    log_line = f.readline().strip()
                    log_data = json.loads(log_line)
                    
                    assert 'timestamp' in log_data
                    assert 'level' in log_data
                    assert 'message' in log_data
                    assert log_data['message'] == "Test message"
                    
            finally:
                os.chdir(original_cwd)

if __name__ == "__main__":
    pytest.main([__file__])
