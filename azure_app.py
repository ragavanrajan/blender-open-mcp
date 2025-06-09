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
    from fastapi import FastAPI, HTTPException
    from fastapi.responses import HTMLResponse, JSONResponse
    from pydantic import BaseModel
    from typing import Optional, List
    import uvicorn
    
    # Try to import MCP components
    try:
        from blender_open_mcp.server import mcp, _ollama_url, _ollama_model, get_blender_connection
        MCP_AVAILABLE = True
    except Exception as e:
        print(f"⚠️ MCP not available: {e}")
        MCP_AVAILABLE = False

    # Create FastAPI app
    app = FastAPI(
        title="BlenderMCP Server",
        description="Blender integration with local AI models via MCP - Copilot Studio Ready",
        version="0.2.0"
    )

    # Pydantic models for Copilot Studio integration
    class BlenderCommand(BaseModel):
        command: str
        description: Optional[str] = None

    class CreateObjectRequest(BaseModel):
        type: str = "CUBE"
        name: Optional[str] = None
        location: Optional[List[float]] = [0, 0, 0]
        rotation: Optional[List[float]] = [0, 0, 0]
        scale: Optional[List[float]] = [1, 1, 1]

    class ModifyObjectRequest(BaseModel):
        name: str
        location: Optional[List[float]] = None
        rotation: Optional[List[float]] = None
        scale: Optional[List[float]] = None
        visible: Optional[bool] = None

    class MaterialRequest(BaseModel):
        object_name: str
        material_name: Optional[str] = None
        color: Optional[List[float]] = None

    class AIPromptRequest(BaseModel):
        prompt: str
        context: Optional[str] = None

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
                <h2>🤖 Copilot Studio Integration Ready!</h2>
                <h3>Available API Endpoints:</h3>
                <ul>
                    <li><strong>GET /health</strong> - Health check</li>
                    <li><strong>GET /api/blender/scene</strong> - Get scene information</li>
                    <li><strong>POST /api/blender/create</strong> - Create objects</li>
                    <li><strong>PUT /api/blender/modify</strong> - Modify objects</li>
                    <li><strong>DELETE /api/blender/delete/{{name}}</strong> - Delete objects</li>
                    <li><strong>POST /api/blender/material</strong> - Apply materials</li>
                    <li><strong>POST /api/blender/code</strong> - Execute Blender code</li>
                    <li><strong>POST /api/ai/prompt</strong> - AI-powered Blender operations</li>
                </ul>
                <p><a href="/docs">📖 View API Documentation</a></p>
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

    # Copilot Studio Integration Endpoints
    @app.get("/api/blender/scene")
    async def get_scene_info():
        """Get current Blender scene information - for Copilot Studio"""
        if not MCP_AVAILABLE:
            raise HTTPException(status_code=503, detail="MCP components not available")
        
        try:
            blender = get_blender_connection()
            result = blender.send_command("get_scene_info")
            return {"success": True, "data": result}
        except Exception as e:
            return {"success": False, "error": str(e), "message": "Failed to get scene info"}

    @app.post("/api/blender/create")
    async def create_object(request: CreateObjectRequest):
        """Create objects in Blender - for Copilot Studio"""
        if not MCP_AVAILABLE:
            raise HTTPException(status_code=503, detail="MCP components not available")
        
        try:
            blender = get_blender_connection()
            params = {
                "type": request.type,
                "location": request.location,
                "rotation": request.rotation,
                "scale": request.scale
            }
            if request.name:
                params["name"] = request.name
                
            result = blender.send_command("create_object", params)
            return {
                "success": True, 
                "message": f"Created {request.type} object: {result.get('name', 'unknown')}",
                "data": result
            }
        except Exception as e:
            return {"success": False, "error": str(e), "message": f"Failed to create {request.type}"}

    @app.put("/api/blender/modify")
    async def modify_object(request: ModifyObjectRequest):
        """Modify objects in Blender - for Copilot Studio"""
        if not MCP_AVAILABLE:
            raise HTTPException(status_code=503, detail="MCP components not available")
        
        try:
            blender = get_blender_connection()
            params = {"name": request.name}
            if request.location is not None:
                params["location"] = request.location
            if request.rotation is not None:
                params["rotation"] = request.rotation
            if request.scale is not None:
                params["scale"] = request.scale
            if request.visible is not None:
                params["visible"] = request.visible
                
            result = blender.send_command("modify_object", params)
            return {
                "success": True,
                "message": f"Modified object: {result.get('name', request.name)}",
                "data": result
            }
        except Exception as e:
            return {"success": False, "error": str(e), "message": f"Failed to modify {request.name}"}

    @app.delete("/api/blender/delete/{object_name}")
    async def delete_object(object_name: str):
        """Delete objects in Blender - for Copilot Studio"""
        if not MCP_AVAILABLE:
            raise HTTPException(status_code=503, detail="MCP components not available")
        
        try:
            blender = get_blender_connection()
            blender.send_command("delete_object", {"name": object_name})
            return {
                "success": True,
                "message": f"Deleted object: {object_name}"
            }
        except Exception as e:
            return {"success": False, "error": str(e), "message": f"Failed to delete {object_name}"}

    @app.post("/api/blender/material")
    async def apply_material(request: MaterialRequest):
        """Apply materials to objects in Blender - for Copilot Studio"""
        if not MCP_AVAILABLE:
            raise HTTPException(status_code=503, detail="MCP components not available")
        
        try:
            blender = get_blender_connection()
            params = {"object_name": request.object_name}
            if request.material_name:
                params["material_name"] = request.material_name
            if request.color:
                params["color"] = request.color
                
            result = blender.send_command("set_material", params)
            return {
                "success": True,
                "message": f"Applied material to {request.object_name}: {result.get('material_name', 'unknown')}",
                "data": result
            }
        except Exception as e:
            return {"success": False, "error": str(e), "message": f"Failed to apply material to {request.object_name}"}

    @app.post("/api/blender/code")
    async def execute_code(request: BlenderCommand):
        """Execute Python code in Blender - for Copilot Studio"""
        if not MCP_AVAILABLE:
            raise HTTPException(status_code=503, detail="MCP components not available")
        
        try:
            blender = get_blender_connection()
            result = blender.send_command("execute_code", {"code": request.command})
            return {
                "success": True,
                "message": f"Code executed successfully",
                "result": result.get('result', ''),
                "data": result
            }
        except Exception as e:
            return {"success": False, "error": str(e), "message": "Failed to execute code"}

    @app.post("/api/ai/prompt")
    async def ai_blender_prompt(request: AIPromptRequest):
        """AI-powered Blender operations using natural language - for Copilot Studio"""
        if not MCP_AVAILABLE:
            raise HTTPException(status_code=503, detail="MCP components not available")
        
        try:
            # This would use the MCP AI integration
            # For now, return a structured response that Copilot Studio can use
            return {
                "success": True,
                "message": "AI prompt received",
                "prompt": request.prompt,
                "suggested_actions": [
                    "This endpoint will process natural language commands",
                    "Integration with Ollama AI for Blender automation",
                    "Convert prompts to Blender operations"
                ],
                "note": "Full AI integration requires Ollama setup"
            }
        except Exception as e:
            return {"success": False, "error": str(e), "message": "Failed to process AI prompt"}

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
    
    print(f"🚀 Starting Azure-compatible server with Copilot Studio integration on {host}:{port}")
    
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