"""
REST-style Blender MCP Server with separate endpoints
This server provides dedicated endpoints for each operation instead of using a single command endpoint
"""
import socket
import json
import logging
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import re
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("RESTBlenderServer")

@dataclass
class BlenderConnection:
    host: str
    port: int
    sock: Optional[socket.socket] = None
    timeout: float = 15.0

    def __post_init__(self):
         if not isinstance(self.host, str):
             raise ValueError("Host must be a string")
         if not isinstance(self.port, int):
             raise ValueError("Port must be an int")

    def connect(self) -> bool:
        if self.sock:
            return True
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            logger.info(f"Connected to Blender at {self.host}:{self.port}")
            self.sock.settimeout(self.timeout)
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Blender: {e!s}")
            self.sock = None
            return False

    def disconnect(self) -> None:
        if self.sock:
            try:
                self.sock.close()
            except Exception as e:
                logger.error(f"Error disconnecting: {e!s}")
            finally:
                self.sock = None

    def _receive_full_response(self, buffer_size: int = 8192) -> bytes:
        """Receive data with timeout using a loop."""
        chunks: List[bytes] = []
        try:
            while True:
                try:
                    chunk = self.sock.recv(buffer_size)
                    if not chunk:
                        if not chunks:
                            raise Exception("Connection closed by Blender before any data was sent")
                        else:
                            raise Exception("Connection closed by Blender mid-stream")
                    chunks.append(chunk)
                    try:
                        data = b''.join(chunks)
                        json.loads(data.decode('utf-8'))
                        logger.debug(f"Received response ({len(data)} bytes)")
                        return data
                    except json.JSONDecodeError:
                        continue
                except socket.timeout:
                    logger.warning("Socket timeout during receive")
                    if chunks:
                        data = b''.join(chunks)
                        try:
                            json.loads(data.decode('utf-8'))
                            return data
                        except json.JSONDecodeError:
                            raise Exception(f"Incomplete JSON data received before timeout. Received: {data[:200]}")
                    else:
                        raise Exception("Timeout waiting for response, no data received.")
        except Exception as e:
            logger.error(f"Error during _receive_full_response: {e!s}")
            raise

    def send_command(self, command_type: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
         if not self.sock and not self.connect():
            raise ConnectionError("Not connected")
         command = {"type": command_type, "params": params or {}}
         try:
              logger.info(f"Sending command: {command_type} with params: {params}")
              self.sock.sendall(json.dumps(command).encode('utf-8'))
              logger.info(f"Command sent, waiting for response...")
              response_data = self._receive_full_response()
              logger.debug(f"Received response ({len(response_data)} bytes)")
              response = json.loads(response_data.decode('utf-8'))
              logger.info(f"Response status: {response.get('status', 'unknown')}")
              if response.get("status") == "error":
                 logger.error(f"Blender error: {response.get('message')}")
                 raise Exception(response.get("message", "Unknown Blender error"))
              return response.get("result", {})
         except Exception as e:
              logger.error(f"Error communicating with Blender: {e!s}")
              self.sock = None
              raise Exception(f"Communication error: {e!s}")

# Global connection
_blender_connection = None

def get_blender_connection() -> BlenderConnection:
    global _blender_connection
    if _blender_connection is None:
        _blender_connection = BlenderConnection("localhost", 9876)
    return _blender_connection

class RESTHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests for health check and scene info"""
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        try:
            if path == "/api/v2/health":
                response = self.handle_health_check()
            elif path == "/api/v2/scene":
                response = self.handle_get_scene_info()
            elif path.startswith("/api/v2/objects/") and not path.endswith("/material"):
                # Extract object name from path: /api/v2/objects/{objectName}
                object_name = path.split("/")[-1]
                response = self.handle_get_object_info(object_name)
            else:
                response = {"status": "error", "message": "Endpoint not found", "error_code": "NOT_FOUND"}
                self.send_json_response(404, response)
                return
                
            self.send_json_response(200, response)
            
        except Exception as e:
            logger.error(f"Error handling GET request: {e}")
            error_response = {"status": "error", "message": str(e), "error_code": "SERVER_ERROR"}
            self.send_json_response(500, error_response)

    def do_POST(self):
        """Handle POST requests for create, execute, and material operations"""
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Read request body
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            post_data = self.rfile.read(content_length)
            try:
                request_data = json.loads(post_data.decode('utf-8'))
            except json.JSONDecodeError:
                error_response = {"status": "error", "message": "Invalid JSON", "error_code": "INVALID_JSON"}
                self.send_json_response(400, error_response)
                return
        else:
            request_data = {}
        
        try:
            if path == "/api/v2/objects":
                response = self.handle_create_object(request_data)
            elif path == "/api/v2/execute":
                response = self.handle_execute_code(request_data)
            elif path == "/api/v2/ai/prompt":
                response = self.handle_ai_prompt(request_data)
            elif "/material" in path and path.startswith("/api/v2/objects/"):
                # Extract object name from path: /api/v2/objects/{objectName}/material
                path_parts = path.split("/")
                if len(path_parts) >= 5:
                    object_name = path_parts[-2]  # Second to last part is object name
                    response = self.handle_apply_material(object_name, request_data)
                else:
                    response = {"status": "error", "message": "Invalid material endpoint", "error_code": "INVALID_ENDPOINT"}
                    self.send_json_response(400, response)
                    return
            else:
                response = {"status": "error", "message": "Endpoint not found", "error_code": "NOT_FOUND"}
                self.send_json_response(404, response)
                return
                
            self.send_json_response(200, response)
            
        except Exception as e:
            logger.error(f"Error handling POST request: {e}")
            error_response = {"status": "error", "message": str(e), "error_code": "SERVER_ERROR"}
            self.send_json_response(500, error_response)

    def do_PUT(self):
        """Handle PUT requests for modifying objects"""
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Read request body
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            post_data = self.rfile.read(content_length)
            try:
                request_data = json.loads(post_data.decode('utf-8'))
            except json.JSONDecodeError:
                error_response = {"status": "error", "message": "Invalid JSON", "error_code": "INVALID_JSON"}
                self.send_json_response(400, error_response)
                return
        else:
            request_data = {}
        
        try:
            if path.startswith("/api/v2/objects/") and not path.endswith("/material"):
                # Extract object name from path: /api/v2/objects/{objectName}
                object_name = path.split("/")[-1]
                response = self.handle_modify_object(object_name, request_data)
            else:
                response = {"status": "error", "message": "Endpoint not found", "error_code": "NOT_FOUND"}
                self.send_json_response(404, response)
                return
                
            self.send_json_response(200, response)
            
        except Exception as e:
            logger.error(f"Error handling PUT request: {e}")
            error_response = {"status": "error", "message": str(e), "error_code": "SERVER_ERROR"}
            self.send_json_response(500, error_response)

    def do_DELETE(self):
        """Handle DELETE requests for removing objects"""
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        try:
            if path.startswith("/api/v2/objects/"):
                # Extract object name from path: /api/v2/objects/{objectName}
                object_name = path.split("/")[-1]
                response = self.handle_remove_object(object_name)
            else:
                response = {"status": "error", "message": "Endpoint not found", "error_code": "NOT_FOUND"}
                self.send_json_response(404, response)
                return
                
            self.send_json_response(200, response)
            
        except Exception as e:
            logger.error(f"Error handling DELETE request: {e}")
            error_response = {"status": "error", "message": str(e), "error_code": "SERVER_ERROR"}
            self.send_json_response(500, error_response)

    def send_json_response(self, status_code: int, data: Dict[str, Any]):
        """Send JSON response with proper headers"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    # Handler methods
    def handle_health_check(self) -> Dict[str, Any]:
        """Handle health check"""
        return {
            "status": "success", 
            "message": "REST Blender server is running!",
            "timestamp": datetime.now().isoformat()
        }
    
    def handle_get_scene_info(self) -> Dict[str, Any]:
        """Handle getting scene information"""
        try:
            blender = get_blender_connection()
            result = blender.send_command("get_scene_info")
            return {"status": "success", "data": result}
        except Exception as e:
            return {"status": "error", "message": str(e), "error_code": "BLENDER_ERROR"}
    
    def handle_get_object_info(self, object_name: str) -> Dict[str, Any]:
        """Handle getting object information"""
        try:
            blender = get_blender_connection()
            result = blender.send_command("get_object_info", {"name": object_name})
            return {"status": "success", "data": result}
        except Exception as e:
            return {"status": "error", "message": str(e), "error_code": "BLENDER_ERROR"}
    
    def handle_create_object(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle creating objects"""
        try:
            # Validate required fields
            if "type" not in params:
                return {"status": "error", "message": "Missing required field: type", "error_code": "MISSING_FIELD"}
            
            # Validate object type
            valid_types = ["CUBE", "SPHERE", "CYLINDER", "PLANE", "CONE", "TORUS", "MONKEY"]
            object_type = params["type"]
            if object_type not in valid_types:
                return {
                    "status": "error", 
                    "message": f"Invalid object type: '{object_type}'. Must be one of: {', '.join(valid_types)}", 
                    "error_code": "INVALID_OBJECT_TYPE"
                }
            
            # Validate location array if provided
            if "location" in params:
                location = params["location"]
                if not isinstance(location, list) or len(location) != 3:
                    return {"status": "error", "message": "Location must be an array of 3 numbers [X, Y, Z]", "error_code": "INVALID_LOCATION"}
                if not all(isinstance(x, (int, float)) for x in location):
                    return {"status": "error", "message": "Location values must be numbers", "error_code": "INVALID_LOCATION"}
            
            # Validate rotation array if provided
            if "rotation" in params:
                rotation = params["rotation"]
                if not isinstance(rotation, list) or len(rotation) != 3:
                    return {"status": "error", "message": "Rotation must be an array of 3 numbers [RX, RY, RZ]", "error_code": "INVALID_ROTATION"}
                if not all(isinstance(x, (int, float)) for x in rotation):
                    return {"status": "error", "message": "Rotation values must be numbers", "error_code": "INVALID_ROTATION"}
            
            # Validate scale array if provided
            if "scale" in params:
                scale = params["scale"]
                if not isinstance(scale, list) or len(scale) != 3:
                    return {"status": "error", "message": "Scale must be an array of 3 numbers [SX, SY, SZ]", "error_code": "INVALID_SCALE"}
                if not all(isinstance(x, (int, float)) for x in scale):
                    return {"status": "error", "message": "Scale values must be numbers", "error_code": "INVALID_SCALE"}
                if any(x <= 0 for x in scale):
                    return {"status": "error", "message": "Scale values must be positive numbers", "error_code": "INVALID_SCALE"}
            
            blender = get_blender_connection()
            result = blender.send_command("create_object", params)
            return {"status": "success", "message": "Object created successfully", "data": result}
        except Exception as e:
            return {"status": "error", "message": str(e), "error_code": "BLENDER_ERROR"}
    
    def handle_modify_object(self, object_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle modifying objects"""
        try:
            # Add object name to params
            params["name"] = object_name
            blender = get_blender_connection()
            result = blender.send_command("modify_object", params)
            return {"status": "success", "message": "Object modified successfully", "data": result}
        except Exception as e:
            return {"status": "error", "message": str(e), "error_code": "BLENDER_ERROR"}
    
    def handle_remove_object(self, object_name: str) -> Dict[str, Any]:
        """Handle removing objects"""
        try:
            blender = get_blender_connection()
            result = blender.send_command("remove_object", {"object_name": object_name})
            return {"status": "success", "message": "Object removed successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e), "error_code": "BLENDER_ERROR"}
    
    def handle_apply_material(self, object_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle applying materials"""
        try:
            # Validate base_color array if provided
            if "base_color" in params:
                base_color = params["base_color"]
                if not isinstance(base_color, list) or len(base_color) != 4:
                    return {"status": "error", "message": "base_color must be an array of 4 numbers [R, G, B, A]", "error_code": "INVALID_COLOR"}
                if not all(isinstance(x, (int, float)) for x in base_color):
                    return {"status": "error", "message": "base_color values must be numbers", "error_code": "INVALID_COLOR"}
                if any(x < 0 or x > 1 for x in base_color):
                    return {"status": "error", "message": "base_color values must be between 0.0 and 1.0", "error_code": "INVALID_COLOR"}
            
            # Set default material name if not provided
            if "material_name" not in params:
                params["material_name"] = f"{object_name}_Material"
            
            # Add object name to params and map base_color to color
            params["object_name"] = object_name
            if "base_color" in params:
                params["color"] = params.pop("base_color")
            
            # Filter out unsupported parameters for set_material
            # The Blender addon only accepts: object_name, material_name, create_if_missing, color
            valid_params = {}
            if "object_name" in params:
                valid_params["object_name"] = params["object_name"] 
            if "material_name" in params:
                valid_params["material_name"] = params["material_name"]
            if "color" in params:
                valid_params["color"] = params["color"]
            if "create_if_missing" in params:
                valid_params["create_if_missing"] = params["create_if_missing"]
            
            blender = get_blender_connection()
            result = blender.send_command("set_material", valid_params)
            return {"status": "success", "message": "Material applied successfully", "data": result}
        except Exception as e:
            return {"status": "error", "message": str(e), "error_code": "BLENDER_ERROR"}
    
    def handle_execute_code(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle executing Python code"""
        try:
            # Validate required fields
            if "code" not in params:
                return {"status": "error", "message": "Missing required field: code", "error_code": "MISSING_FIELD"}
            
            blender = get_blender_connection()
            result = blender.send_command("execute_code", params)
            return {"status": "success", "message": "Code executed successfully", "data": result}
        except Exception as e:
            return {"status": "error", "message": str(e), "error_code": "BLENDER_ERROR"}
    
    def handle_ai_prompt(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle AI prompts"""
        try:
            # Validate required fields
            if "prompt" not in params:
                return {"status": "error", "message": "Missing required field: prompt", "error_code": "MISSING_FIELD"}
            
            blender = get_blender_connection()
            result = blender.send_command("ai_prompt", params)
            return {"status": "success", "message": "AI prompt processed successfully", "data": result}
        except Exception as e:
            return {"status": "error", "message": str(e), "error_code": "BLENDER_ERROR"}

    def log_message(self, format, *args):
        logger.info("%s - %s" % (self.client_address[0], format % args))

def run_rest_server(host: str = "localhost", port: int = 8000):
    """Run the REST HTTP server"""
    server_address = (host, port)
    httpd = HTTPServer(server_address, RESTHTTPHandler)
    logger.info(f"REST Blender MCP Server running on http://{host}:{port}")
    logger.info("Available endpoints:")
    logger.info("  GET  /api/v2/health - Health check")
    logger.info("  GET  /api/v2/scene - Get scene information")
    logger.info("  POST /api/v2/objects - Create new object")
    logger.info("  GET  /api/v2/objects/{name} - Get object info")
    logger.info("  PUT  /api/v2/objects/{name} - Modify object")
    logger.info("  DELETE /api/v2/objects/{name} - Remove object")
    logger.info("  POST /api/v2/objects/{name}/material - Apply material")
    logger.info("  POST /api/v2/execute - Execute Python code")
    logger.info("  POST /api/v2/ai/prompt - AI assistant")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        httpd.shutdown()

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="REST Blender MCP Server")
    parser.add_argument("--host", type=str, default="localhost",
                        help="Host for the server to listen on")
    parser.add_argument("--port", type=int, default=8000,
                        help="Port for the server to listen on")

    args = parser.parse_args()
    run_rest_server(args.host, args.port)

if __name__ == "__main__":
    main()