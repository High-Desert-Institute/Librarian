#!/usr/bin/env python3
"""
Secrets management CLI commands
"""

import argparse
from app.common.secrets import get_secrets_manager
from app.common.logging import get_logger

logger = get_logger(__name__)

def handle_secrets_command(args):
    """Handle secrets management commands"""
    secrets_manager = get_secrets_manager()
    
    if args.secrets_action == "list":
        return handle_secrets_list(secrets_manager)
    elif args.secrets_action == "set":
        return handle_secrets_set(secrets_manager, args.channel, args.psk)
    elif args.secrets_action == "get":
        return handle_secrets_get(secrets_manager, args.channel)
    elif args.secrets_action == "validate":
        return handle_secrets_validate(secrets_manager)
    elif args.secrets_action == "create-example":
        return handle_secrets_create_example(secrets_manager)

def handle_secrets_list(secrets_manager):
    """List all configured channels"""
    channels = secrets_manager.list_channels()
    
    if not channels:
        print("No channels configured")
        return 0
    
    print("Configured channels:")
    for channel in channels:
        psk = secrets_manager.get_psk(channel)
        # Mask PSK for security
        masked_psk = psk[:8] + "..." if len(psk) > 8 else "***"
        print(f"  {channel}: {masked_psk}")
    
    return 0

def handle_secrets_set(secrets_manager, channel, psk):
    """Set PSK for a channel"""
    if not channel or not psk:
        print("Error: Channel and PSK are required")
        return 1
    
    secrets_manager.set_psk(channel, psk)
    print(f"Set PSK for channel '{channel}'")
    return 0

def handle_secrets_get(secrets_manager, channel):
    """Get PSK for a channel"""
    if not channel:
        print("Error: Channel is required")
        return 1
    
    psk = secrets_manager.get_psk(channel)
    if psk is None:
        print(f"No PSK found for channel '{channel}'")
        return 1
    
    # Mask PSK for security
    masked_psk = psk[:8] + "..." if len(psk) > 8 else "***"
    print(f"Channel '{channel}': {masked_psk}")
    return 0

def handle_secrets_validate(secrets_manager):
    """Validate secrets configuration"""
    is_valid = secrets_manager.validate_secrets()
    
    if is_valid:
        print("Secrets configuration is valid")
        return 0
    else:
        print("Secrets configuration has issues")
        return 1

def handle_secrets_create_example(secrets_manager):
    """Create example secrets file"""
    secrets_manager.create_example_secrets()
    print("Created example secrets file")
    return 0

def add_secrets_parser(subparsers):
    """Add secrets management subparser"""
    secrets_parser = subparsers.add_parser("secrets", help="Secrets management")
    secrets_subparsers = secrets_parser.add_subparsers(dest="secrets_action")
    
    # List secrets
    secrets_subparsers.add_parser("list", help="List configured channels")
    
    # Set secret
    set_parser = secrets_subparsers.add_parser("set", help="Set PSK for a channel")
    set_parser.add_argument("channel", help="Channel name")
    set_parser.add_argument("psk", help="PSK value")
    
    # Get secret
    get_parser = secrets_subparsers.add_parser("get", help="Get PSK for a channel")
    get_parser.add_argument("channel", help="Channel name")
    
    # Validate secrets
    secrets_subparsers.add_parser("validate", help="Validate secrets configuration")
    
    # Create example
    secrets_subparsers.add_parser("create-example", help="Create example secrets file")
    
    return secrets_parser
