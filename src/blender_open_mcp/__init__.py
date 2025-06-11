"""Blender integration through the Model Context Protocol."""

__version__ = "0.2.0"  # Updated version

# For Python 3.8 compatibility, expose classes from simple_server instead
try:
    # Try to import from the full MCP server (requires Python 3.10+)
    from .server import BlenderConnection, get_blender_connection
except ImportError:
    # Fall back to simple server for Python 3.8 compatibility
    from .simple_server import BlenderConnection, get_blender_connection