#!/usr/bin/env python3
"""
Startup script for Azure Web App deployment
"""
import os
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Set environment variables for production
os.environ.setdefault("PYTHONPATH", str(src_path))

# Import and run the application
if __name__ == "__main__":
    import uvicorn
    from blender_open_mcp.server import app
    
    # Get port from environment variable (Azure sets this)
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    # Set default Ollama URL if not set
    if not os.environ.get("OLLAMA_URL"):
        os.environ["OLLAMA_URL"] = "http://localhost:11434"
    
    uvicorn.run(
        app,
        host=host,
        port=port,
        workers=1,
        timeout_keep_alive=600,
        access_log=True
    ) 