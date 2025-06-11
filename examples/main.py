import sys
import os
from pathlib import Path

# Add src directory to Python path
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

def main():
    """Auto-detect and use the best available server."""
    # Check Python version and MCP availability
    python_version = sys.version_info
    
    if python_version >= (3, 10):
        try:
            # Try to import and use the full MCP server
            from blender_open_mcp.server import main as mcp_main
            print(f"🚀 Starting Full MCP Server (Python {python_version.major}.{python_version.minor})...")
            print("✅ Full Model Context Protocol features available!")
            mcp_main()
            return
        except ImportError as e:
            print(f"⚠️  FastMCP not available: {e}")
            print("💡 Install with: pip install fastmcp")
    
    # Fallback to simple server
    from blender_open_mcp.simple_server import main as simple_main
    print(f"📡 Starting Simple Server (Python {python_version.major}.{python_version.minor} compatible)...")
    if python_version >= (3, 10):
        print("💡 For full MCP features, install: pip install fastmcp")
    simple_main()

if __name__ == "__main__":
    main()