#!/usr/bin/env python3
"""Quick start script for BlenderMCP server - bypasses auto-detection issues"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

def main():
    """Start the server directly with uvicorn for FastAPI compatibility"""
    import uvicorn
    
    # Import the FastMCP app
    from blender_open_mcp.server import app
    
    print("🚀 Starting BlenderMCP Server with uvicorn...")
    print("📡 Server will be available at: http://localhost:8000")
    print("📖 API docs will be at: http://localhost:8000/docs")
    print("✅ Blender connection: localhost:9876 (ensure Blender addon is running)")
    
    # Start the server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )

if __name__ == "__main__":
    main() 