"""
Azure-compatible FastAPI wrapper for BlenderMCP
This creates a simple HTTP API that Azure can handle properly
"""
import sys
import os
from pathlib import Path

# Add src directory to Python path
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

try:
    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse, JSONResponse
    import uvicorn
    
    # Try to import MCP components
    try:
        from blender_open_mcp.server import mcp, _ollama_url, _ollama_model
        MCP_AVAILABLE = True
    except Exception as e:
        print(f"⚠️ MCP not available: {e}")
        MCP_AVAILABLE = False

    # Create FastAPI app
    app = FastAPI(
        title="BlenderMCP Server",
        description="Blender integration with local AI models via MCP",
        version="0.2.0"
    )

    @app.get("/", response_class=HTMLResponse)
    async def root():
        if MCP_AVAILABLE:
            status = "✅ BlenderMCP Server is running"
            mcp_status = "Available"
        else:
            status = "⚠️ BlenderMCP Server started but MCP components not available"
            mcp_status = "Not Available"
            
        return f"""
        <html>
            <head><title>BlenderMCP Server</title></head>
            <body>
                <h1>{status}</h1>
                <p><strong>Status:</strong> Server is running</p>
                <p><strong>MCP Components:</strong> {mcp_status}</p>
                <p><strong>Python Version:</strong> {sys.version}</p>
                <p><strong>Platform:</strong> {sys.platform}</p>
                {f'<p><strong>Ollama URL:</strong> {_ollama_url}</p>' if MCP_AVAILABLE else ''}
                {f'<p><strong>Ollama Model:</strong> {_ollama_model}</p>' if MCP_AVAILABLE else ''}
                <hr>
                <p>This server provides MCP (Model Context Protocol) integration for Blender.</p>
                <p>Access the MCP interface through appropriate MCP clients.</p>
            </body>
        </html>
        """

    @app.get("/health")
    async def health_check():
        return {
            "status": "healthy",
            "mcp_available": MCP_AVAILABLE,
            "python_version": sys.version,
            "platform": sys.platform
        }

    @app.get("/info")
    async def server_info():
        info = {
            "status": "running",
            "mcp_available": MCP_AVAILABLE,
            "python_version": sys.version,
            "platform": sys.platform,
        }
        
        if MCP_AVAILABLE:
            info.update({
                "ollama_url": _ollama_url,
                "ollama_model": _ollama_model,
            })
        
        return info

    # If MCP is available, mount it as a sub-app
    if MCP_AVAILABLE:
        try:
            # Mount the MCP app at /mcp path
            app.mount("/mcp", mcp.app)
            print("✅ MCP app mounted at /mcp")
        except Exception as e:
            print(f"⚠️ Failed to mount MCP app: {e}")

    # This is what Azure will use
    application = app

except ImportError as e:
    print(f"❌ Failed to import FastAPI: {e}")
    
    # Create a minimal ASGI app as fallback
    async def fallback_app(scope, receive, send):
        if scope['type'] == 'http':
            await send({
                'type': 'http.response.start',
                'status': 200,
                'headers': [(b'content-type', b'text/html')],
            })
            body = f"""
            <html>
                <body>
                    <h1>Server Started (Minimal Mode)</h1>
                    <p>FastAPI not available, but server is running.</p>
                    <p>Error: {str(e)}</p>
                    <p>Python: {sys.version}</p>
                </body>
            </html>
            """.encode()
            await send({
                'type': 'http.response.body',
                'body': body,
            })
    
    application = fallback_app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    print(f"🚀 Starting Azure-compatible server on {host}:{port}")
    
    try:
        uvicorn.run(
            application,
            host=host,
            port=port,
            log_level="info",
            access_log=True
        )
    except Exception as e:
        print(f"❌ Failed to start uvicorn: {e}")
        print("Server startup failed") 