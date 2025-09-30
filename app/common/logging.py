#!/usr/bin/env python3
"""
Logging configuration and utilities for Librarian
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

class JSONFormatter(logging.Formatter):
    """Custom JSON formatter for structured logging"""
    
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "message": record.getMessage(),
        }
        
        # Add extra fields if present
        if hasattr(record, 'user_input'):
            log_entry['user_input'] = record.user_input
        if hasattr(record, 'output'):
            log_entry['output'] = record.output
        if hasattr(record, 'component'):
            log_entry['component'] = record.component
        if hasattr(record, 'phase'):
            log_entry['phase'] = record.phase
        
        return json.dumps(log_entry, ensure_ascii=False)

class LibrarianLogger:
    """Custom logger with additional context methods"""
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
    
    def log_user_input(self, input_data: str):
        """Log user input with context"""
        self.logger.info("User input received", extra={
            'user_input': input_data,
            'component': 'cli',
            'phase': 'input'
        })
    
    def log_output(self, output_data: str):
        """Log output with context"""
        self.logger.info("Output generated", extra={
            'output': output_data,
            'component': 'cli',
            'phase': 'output'
        })
    
    def log_operation(self, operation: str, component: str, phase: str, **kwargs):
        """Log operation with structured context"""
        extra = {
            'component': component,
            'phase': phase,
            'operation': operation
        }
        extra.update(kwargs)
        self.logger.info(f"Operation: {operation}", extra=extra)
    
    def __getattr__(self, name):
        """Delegate to underlying logger"""
        return getattr(self.logger, name)

def setup_logging(verbose: bool = False, test_mode: bool = False) -> None:
    """
    Setup logging configuration for Librarian
    
    Args:
        verbose: Enable verbose logging
        test_mode: Run in test mode (different log file)
    """
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Determine log file
    if test_mode:
        log_file = log_dir / "test.log"
    else:
        log_file = log_dir / "librarian.log"
    
    # Set up root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    
    # Clear existing handlers
    root_logger.handlers.clear()
    
    # File handler with JSON formatting
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = JSONFormatter()
    file_handler.setFormatter(file_formatter)
    root_logger.addHandler(file_handler)
    
    # Console handler with simple formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_level = logging.DEBUG if verbose else logging.INFO
    console_handler.setLevel(console_level)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    # Log startup information
    logger = logging.getLogger(__name__)
    logger.info("Logging system initialized", extra={
        'component': 'logging',
        'phase': 'startup',
        'verbose': verbose,
        'test_mode': test_mode,
        'log_file': str(log_file)
    })

def get_logger(name: str) -> LibrarianLogger:
    """
    Get a logger instance with Librarian-specific functionality
    
    Args:
        name: Logger name (usually __name__)
    
    Returns:
        LibrarianLogger instance
    """
    return LibrarianLogger(name)

def log_command_execution(command: str, args: list, output: str, return_code: int):
    """
    Log command execution details
    
    Args:
        command: Command that was executed
        args: Command arguments
        output: Command output
        return_code: Command return code
    """
    logger = get_logger(__name__)
    logger.log_operation(
        operation="command_execution",
        component="cli",
        phase="execution",
        command=command,
        args=args,
        output=output,
        return_code=return_code
    )
