#!/usr/bin/env python3
"""
Comprehensive test script for the Full MCP Server
Tests both simple and full MCP modes
"""
import sys
import time
import json
import requests
import subprocess
from pathlib import Path

def check_python_compatibility():
    """Check Python version and MCP capabilities"""
    version = sys.version_info
    print(f"🐍 Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version >= (3, 10):
        try:
            import fastmcp
            print("✅ FastMCP available - Full MCP mode supported")
            return "full_mcp"
        except ImportError:
            print("⚠️  FastMCP not installed - Using simple mode")
            return "simple"
    else:
        print("📱 Python 3.8-3.9 - Simple mode only")
        return "simple"

def test_server_detection():
    """Test automatic server detection"""
    print("\n🔍 Testing Server Auto-Detection...")
    
    try:
        # Run python main.py --help to see which server is detected
        result = subprocess.run([sys.executable, "main.py", "--help"], 
                               capture_output=True, text=True, timeout=10)
        
        if "Full MCP Server" in result.stdout:
            print("✅ Auto-detected: Full MCP Server")
            return "full_mcp"
        elif "Simple" in result.stdout:
            print("✅ Auto-detected: Simple Server")
            return "simple"
        else:
            print(f"⚠️  Unknown server type detected")
            return "unknown"
            
    except Exception as e:
        print(f"❌ Error testing server detection: {e}")
        return "error"

def test_health_check(server_type, port=8000):
    """Test basic health check functionality"""
    print(f"\n💓 Testing Health Check ({server_type} mode)...")
    
    try:
        if server_type == "simple":
            # Simple mode uses JSON API
            response = requests.post(f'http://localhost:{port}/', 
                                   json={'command': 'health_check'},
                                   timeout=5)
        else:
            # For full MCP, we might need different endpoint testing
            # For now, test the simple endpoint which should work
            response = requests.post(f'http://localhost:{port}/', 
                                   json={'command': 'health_check'},
                                   timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot connect to server on port {port}")
        print("   Make sure server is running with: python main.py")
        return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_blender_commands(server_type, port=8000):
    """Test Blender-specific commands"""
    print(f"\n🎨 Testing Blender Commands ({server_type} mode)...")
    
    commands = [
        {"command": "get_scene_info", "description": "Get scene information"},
        {"command": "create_object", "params": {"type": "CUBE", "name": "TestCube"}, 
         "description": "Create a test cube"},
    ]
    
    for cmd in commands:
        try:
            print(f"  Testing: {cmd['description']}")
            response = requests.post(f'http://localhost:{port}/', 
                                   json=cmd,
                                   timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    print(f"    ✅ Success: {cmd['command']}")
                else:
                    print(f"    ⚠️  {cmd['command']}: {data.get('message', 'Unknown error')}")
            else:
                print(f"    ❌ HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"    ❌ Error testing {cmd['command']}: {e}")

def test_server_modes():
    """Test both server modes"""
    print("\n🔄 Testing Both Server Modes...")
    
    # Test simple server explicitly
    print("\n--- Testing Simple Server ---")
    try:
        simple_result = subprocess.run([sys.executable, "src/blender_open_mcp/simple_server.py", "--help"], 
                                     capture_output=True, text=True, timeout=5)
        if simple_result.returncode == 0:
            print("✅ Simple server available")
        else:
            print("❌ Simple server has issues")
    except Exception as e:
        print(f"❌ Simple server test failed: {e}")
    
    # Test full MCP server if available
    print("\n--- Testing Full MCP Server ---")
    if sys.version_info >= (3, 10):
        try:
            mcp_result = subprocess.run([sys.executable, "src/blender_open_mcp/server.py", "--help"], 
                                      capture_output=True, text=True, timeout=5)
            if mcp_result.returncode == 0:
                print("✅ Full MCP server available")
            else:
                print("❌ Full MCP server has issues")
        except Exception as e:
            print(f"❌ Full MCP server test failed: {e}")
    else:
        print("⚠️  Python version too old for Full MCP server")

def main():
    """Run comprehensive tests"""
    print("🧪 Comprehensive Blender MCP Server Test")
    print("=" * 50)
    
    # Check Python compatibility
    mode = check_python_compatibility()
    
    # Test server detection
    detected_mode = test_server_detection()
    
    # Test both server modes
    test_server_modes()
    
    # Test health check (assumes server is running)
    print("\n" + "=" * 50)
    print("🏃 Live Server Tests (requires running server)")
    print("Run 'python main.py' in another terminal first!")
    
    # Wait for user to start server
    input("\nPress Enter when server is running...")
    
    health_ok = test_health_check(detected_mode)
    
    if health_ok:
        test_blender_commands(detected_mode)
    
    print("\n" + "=" * 50)
    print("📊 Test Summary")
    print(f"Python Mode: {mode}")
    print(f"Detected Server: {detected_mode}")
    print(f"Health Check: {'✅' if health_ok else '❌'}")
    
    if mode == "full_mcp":
        print("\n🎉 You have full MCP features available!")
    else:
        print("\n📱 Simple mode - upgrade to Python 3.10+ for full MCP")

if __name__ == "__main__":
    main() 