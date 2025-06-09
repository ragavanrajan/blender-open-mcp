"""
WSGI/ASGI configuration for Azure Web App deployment
"""
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from blender_open_mcp.server import app

# This is what Azure Web App will use
application = app 