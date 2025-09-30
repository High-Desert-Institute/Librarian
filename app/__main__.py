#!/usr/bin/env python3
"""
Librarian - Meshtastic-focused digital librarian
Main entry point for the application
"""

import sys
import argparse
from app.cli.main import main

if __name__ == "__main__":
    sys.exit(main())
