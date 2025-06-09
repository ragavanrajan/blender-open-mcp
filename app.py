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

try:
    # Import the ASGI application
    from blender_open_mcp.server import app
    
    # This is what Azure Web App will use
    application = app
    print("✅ Successfully imported BlenderMCP application")

except Exception as e:
    print(f"❌ Failed to import BlenderMCP application: {e}")
    # Create a simple fallback ASGI app for debugging
    async def fallback_app(scope, receive, send):
        if scope['type'] == 'http':
            await send({
                'type': 'http.response.start',
                'status': 500,
                'headers': [(b'content-type', b'text/plain')],
            })
            await send({
                'type': 'http.response.body',
                'body': f'Import Error: {str(e)}'.encode(),
            })
    
    application = fallback_app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(application, host="0.0.0.0", port=port) 