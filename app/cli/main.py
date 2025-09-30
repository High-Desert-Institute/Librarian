#!/usr/bin/env python3
"""
Main CLI entry point for Librarian
"""

import argparse
import sys
from app.common.logging import setup_logging, get_logger

logger = get_logger(__name__)

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Librarian - Meshtastic-focused digital librarian",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m app --help                    # Show this help
  python -m app status                    # Show system status
  python -m app broadcast "Hello world"   # Send urgent broadcast
  python -m app corpus ingest            # Rebuild knowledge base
  python -m app run-core                 # Start core services
        """
    )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version="%(prog)s 0.1.0"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    parser.add_argument(
        "--test", "-t",
        action="store_true",
        help="Run in test mode (no persistent changes)"
    )
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Show system status")
    
    # Broadcast command
    broadcast_parser = subparsers.add_parser("broadcast", help="Send urgent broadcast")
    broadcast_parser.add_argument("message", help="Message to broadcast")
    
    # Schedule commands
    schedule_parser = subparsers.add_parser("schedule", help="Schedule management")
    schedule_subparsers = schedule_parser.add_subparsers(dest="schedule_action")
    schedule_subparsers.add_parser("reload", help="Reload schedule configuration")
    
    # Corpus commands
    corpus_parser = subparsers.add_parser("corpus", help="Knowledge base management")
    corpus_subparsers = corpus_parser.add_subparsers(dest="corpus_action")
    corpus_subparsers.add_parser("ingest", help="Rebuild knowledge base from documents")
    
    # Core service command
    core_parser = subparsers.add_parser("run-core", help="Start core services")
    
    # Log tail command
    tail_parser = subparsers.add_parser("tail", help="Follow logs")
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(verbose=args.verbose, test_mode=args.test)
    
    # Handle commands
    if args.command == "status":
        return handle_status()
    elif args.command == "broadcast":
        return handle_broadcast(args.message)
    elif args.command == "schedule":
        if args.schedule_action == "reload":
            return handle_schedule_reload()
    elif args.command == "corpus":
        if args.corpus_action == "ingest":
            return handle_corpus_ingest()
    elif args.command == "run-core":
        return handle_run_core()
    elif args.command == "tail":
        return handle_tail()
    else:
        parser.print_help()
        return 0

def handle_status():
    """Handle status command"""
    logger.info("Status command requested")
    print("Librarian System Status")
    print("=======================")
    print("Status: Not implemented yet")
    print("Queue depth: 0")
    print("Last announcement: None")
    print("Last error: None")
    return 0

def handle_broadcast(message):
    """Handle broadcast command"""
    logger.info(f"Broadcast command requested: {message}")
    print(f"Broadcasting: {message}")
    print("(Not implemented yet)")
    return 0

def handle_schedule_reload():
    """Handle schedule reload command"""
    logger.info("Schedule reload requested")
    print("Reloading schedule configuration...")
    print("(Not implemented yet)")
    return 0

def handle_corpus_ingest():
    """Handle corpus ingest command"""
    logger.info("Corpus ingest requested")
    print("Rebuilding knowledge base...")
    print("(Not implemented yet)")
    return 0

def handle_run_core():
    """Handle run-core command"""
    logger.info("Starting core services...")
    print("Starting Librarian core services...")
    print("(Not implemented yet)")
    return 0

def handle_tail():
    """Handle tail command"""
    logger.info("Log tail requested")
    print("Following logs...")
    print("(Not implemented yet)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
