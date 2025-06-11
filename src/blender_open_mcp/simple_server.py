"""
Simple Blender MCP Server without external MCP dependencies
This is a basic HTTP server that provides Blender integration functionality
"""
import socket
import json
import logging
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("SimpleBlenderServer")

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
        _blender_connection = BlenderConnection("localhost", 9999)
    return _blender_connection

class SimpleHTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            request_data = json.loads(post_data.decode('utf-8'))
            command = request_data.get('command')
            params = request_data.get('params', {})
            
            response = self.handle_command(command, params)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            logger.error(f"Error handling request: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {"error": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def handle_command(self, command: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle different commands"""
        try:
            if command == "health_check":
                return {"status": "success", "message": "Simple Blender server is running!"}
            
            elif command == "get_scene_info":
                blender = get_blender_connection()
                result = blender.send_command("get_scene_info")
                return {"status": "success", "data": result}
            
            elif command == "create_object":
                blender = get_blender_connection()
                result = blender.send_command("create_object", params)
                return {"status": "success", "data": result}
            
            elif command == "get_object_info":
                blender = get_blender_connection()
                result = blender.send_command("get_object_info", params)
                return {"status": "success", "data": result}
                
            else:
                return {"status": "error", "message": f"Unknown command: {command}"}
                
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def log_message(self, format, *args):
        logger.info("%s - %s" % (self.client_address[0], format % args))

def run_server(host: str = "localhost", port: int = 8000):
    """Run the simple HTTP server"""
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHTTPHandler)
    logger.info(f"Simple Blender MCP Server running on http://{host}:{port}")
    logger.info("Available endpoints:")
    logger.info("  POST / - Send commands as JSON")
    logger.info("Example command: {'command': 'health_check'}")
    logger.info("Example command: {'command': 'get_scene_info'}")
    logger.info("Example command: {'command': 'create_object', 'params': {'type': 'CUBE'}}")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        httpd.shutdown()

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Simple Blender MCP Server")
    parser.add_argument("--host", type=str, default="localhost",
                        help="Host for the server to listen on")
    parser.add_argument("--port", type=int, default=8000,
                        help="Port for the server to listen on")

    args = parser.parse_args()
    run_server(args.host, args.port)

if __name__ == "__main__":
    main() 