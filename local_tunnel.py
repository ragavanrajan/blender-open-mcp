#!/usr/bin/env python3
"""
Local Tunnel Setup for Blender MCP Server
Run this to make your local Blender MCP server accessible to Copilot Studio
"""
import os
import sys
import time
import threading
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from pyngrok import ngrok
    import uvicorn
    from azure_app import app
    print("✅ All required modules imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install required packages:")
    print("pip install pyngrok uvicorn fastapi")
    sys.exit(1)

def run_server():
    """Run the FastAPI server"""
    print("🚀 Starting FastAPI server...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )

def setup_tunnel():
    """Setup ngrok tunnel"""
    print("🔗 Setting up ngrok tunnel...")
    
    # Set your ngrok auth token if you have one
    # ngrok.set_auth_token("your_auth_token_here")
    
    # Create tunnel
    tunnel = ngrok.connect(8000)
    public_url = tunnel.public_url
    
    print(f"✅ Tunnel created!")
    print(f"🌐 Public URL: {public_url}")
    print(f"📝 Use this URL in your Copilot Studio custom connector")
    print("")
    print("📋 Update your connector with:")
    print(f"   Base URL: {public_url}")
    print("   OpenAPI/Swagger: {public_url}/docs")
    print("")
    print("⚠️  Keep this script running while testing!")
    print("   Press Ctrl+C to stop")
    
    return tunnel

def main():
    """Main function"""
    print("🔧 Blender MCP Local Tunnel Setup")
    print("=" * 40)
    
    # Check if Blender is running (you should start Blender with the addon first)
    print("📍 Make sure:")
    print("   1. Blender is running")
    print("   2. Blender MCP addon is enabled and active")
    print("   3. Socket server is listening on port 8275")
    print("")
    
    try:
        # Setup tunnel first
        tunnel = setup_tunnel()
        
        # Start server in a separate thread
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        
        # Keep the main thread running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Shutting down...")
            ngrok.disconnect(tunnel.public_url)
            ngrok.kill()
            print("✅ Cleanup complete!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure ngrok is installed and configured properly")

if __name__ == "__main__":
    main() 