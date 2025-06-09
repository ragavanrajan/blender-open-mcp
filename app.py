"""
Azure Web App Entry Point
Simple entry point for Azure Web App deployment
"""
import sys
import os
from pathlib import Path

# Add src directory to Python path
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

# Import the ASGI application
from blender_open_mcp.server import app

# This is what Azure Web App will use
application = app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 