"""
Azure Web App Entry Point with proper PORT handling
"""
import os
import sys
from pathlib import Path

# Add src directory to Python path
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

def create_app():
    """Create and return the ASGI application."""
    try:
        from blender_open_mcp.server import app
        print("✅ BlenderMCP application loaded successfully")
        return app
    except Exception as e:
        print(f"❌ Failed to load BlenderMCP: {e}")
        import traceback
        traceback.print_exc()
        
        # Return a simple error app
        async def error_app(scope, receive, send):
            if scope['type'] == 'http':
                await send({
                    'type': 'http.response.start',
                    'status': 500,
                    'headers': [(b'content-type', b'text/html')],
                })
                body = f"""
                <html>
                <body>
                    <h1>Application Error</h1>
                    <p>Failed to start BlenderMCP server:</p>
                    <pre>{str(e)}</pre>
                    <p>Check Azure logs for full traceback.</p>
                </body>
                </html>
                """.encode()
                await send({
                    'type': 'http.response.body',
                    'body': body,
                })
        return error_app

# Create the application
application = create_app()

if __name__ == "__main__":
    import uvicorn
    
    # Azure sets the PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    print(f"🚀 Starting server on {host}:{port}")
    
    uvicorn.run(
        application,
        host=host,
        port=port,
        log_level="info",
        access_log=True
    ) 