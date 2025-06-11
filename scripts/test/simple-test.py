#!/usr/bin/env python3
"""Simple test server to verify basic functionality"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

def main():
    """Start the simple server directly."""
    
    print("🧪 Starting Simple Test Server...")
    print("📡 This will use the basic FastAPI server")
    
    # Import the simple server directly
    from blender_open_mcp.simple_server import main as simple_main
    
    print("✅ Simple server imported successfully!")
    print("🚀 Starting server on localhost:8000...")
    
    # Start the simple server
    simple_main()

if __name__ == "__main__":
    main() 