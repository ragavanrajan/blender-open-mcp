#!/usr/bin/env python3
"""
Status Checker for Blender MCP Setup
Helps diagnose connection issues
"""
import requests
import socket
import json
import sys

def check_blender_socket():
    """Check if Blender socket is responding"""
    print("🔍 Checking Blender socket connection...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect(("localhost", 9876))
            
            command = {"type": "get_scene_info", "params": {}}
            message = json.dumps(command) + "\n"
            sock.sendall(message.encode())
            
            response = sock.recv(4096).decode()
            result = json.loads(response)
            
            if result.get("status") == "success":
                objects = result.get("result", {}).get("objects", [])
                print(f"   ✅ Blender connected - {len(objects)} objects in scene")
                return True
            else:
                print("   ❌ Blender responded but with error")
                return False
                
    except Exception as e:
        print(f"   ❌ Blender socket error: {e}")
        return False

def check_local_server():
    """Check if local server is responding"""
    print("🔍 Checking local server...")
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Server healthy - Blender connected: {data.get('blender_connected', False)}")
            return True
        else:
            print(f"   ❌ Server returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Local server error: {e}")
        return False

def check_scene_endpoint():
    """Check if scene endpoint works"""
    print("🔍 Checking scene endpoint...")
    try:
        response = requests.get("http://localhost:8000/api/blender/scene", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                objects = data.get("data", {}).get("result", {}).get("objects", [])
                print(f"   ✅ Scene endpoint working - {len(objects)} objects")
                return True
            else:
                print("   ❌ Scene endpoint returned success=false")
                return False
        else:
            print(f"   ❌ Scene endpoint returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Scene endpoint error: {e}")
        return False

def main():
    print("🔧 Blender MCP Status Check")
    print("=" * 30)
    print("")
    
    # Check all components
    blender_ok = check_blender_socket()
    server_ok = check_local_server() 
    scene_ok = check_scene_endpoint()
    
    print("")
    print("📊 Summary:")
    print(f"   Blender Socket (port 9876): {'✅' if blender_ok else '❌'}")
    print(f"   Local Server (port 8000): {'✅' if server_ok else '❌'}")
    print(f"   Scene Endpoint: {'✅' if scene_ok else '❌'}")
    
    if all([blender_ok, server_ok, scene_ok]):
        print("")
        print("🎉 All systems working! Ready for tunnel setup.")
        print("💡 Next step: python cloudflare_tunnel.py")
    else:
        print("")
        print("❌ Issues detected. Fix these first:")
        if not blender_ok:
            print("   • Make sure Blender is running with MCP addon enabled")
        if not server_ok:
            print("   • Start the server: python bypass_server.py")
        if not scene_ok:
            print("   • Check server logs for errors")

if __name__ == "__main__":
    main() 