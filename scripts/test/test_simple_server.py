#!/usr/bin/env python3
"""
Test script for the simple Blender MCP server
"""
import time
import json
from http.client import HTTPConnection

def test_server(host='localhost', port=8000):
    """Test the simple server"""
    print(f"Testing server at {host}:{port}")
    
    try:
        # Create connection
        conn = HTTPConnection(host, port, timeout=10)
        
        # Test 1: Health check
        print("\n1. Testing health check...")
        test_data = json.dumps({"command": "health_check"})
        headers = {"Content-Type": "application/json"}
        
        conn.request("POST", "/", test_data, headers)
        response = conn.getresponse()
        
        if response.status == 200:
            data = json.loads(response.read().decode())
            print(f"✅ Health check passed: {data}")
        else:
            print(f"❌ Health check failed: {response.status} {response.reason}")
        
        # Test 2: Invalid command
        print("\n2. Testing invalid command...")
        test_data = json.dumps({"command": "invalid_command"})
        
        conn.request("POST", "/", test_data, headers)
        response = conn.getresponse()
        
        if response.status == 200:
            data = json.loads(response.read().decode())
            if data.get("status") == "error":
                print(f"✅ Invalid command properly rejected: {data}")
            else:
                print(f"⚠️  Expected error for invalid command: {data}")
        else:
            print(f"❌ Invalid command test failed: {response.status}")
        
        conn.close()
        print("\n🎉 All tests completed!")
        
    except ConnectionRefusedError:
        print(f"❌ Could not connect to server at {host}:{port}")
        print("   Make sure the server is running with: python main.py")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")

if __name__ == "__main__":
    print("Simple Blender MCP Server Test")
    print("=" * 40)
    
    # Wait a moment for server to start if needed
    print("Waiting 2 seconds for server to be ready...")
    time.sleep(2)
    
    test_server() 