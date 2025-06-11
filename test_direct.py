#!/usr/bin/env python3
"""
Direct Blender Connection Test
Test Blender connection without MCP framework
"""
import socket
import json
import sys

def test_blender_connection():
    """Test direct connection to Blender"""
    host = "localhost"
    port = 9876
    
    print(f"🔌 Connecting to Blender at {host}:{port}...")
    
    try:
        # Create socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.settimeout(10.0)
        
        print("✅ Connected to Blender!")
        
        # Test scene info command
        command = {"type": "get_scene_info", "params": {}}
        sock.sendall(json.dumps(command).encode('utf-8'))
        
        print("📤 Sent get_scene_info command...")
        
        # Receive response
        response_data = sock.recv(8192)
        response = json.loads(response_data.decode('utf-8'))
        
        print("📥 Received response:")
        print(json.dumps(response, indent=2))
        
        if response.get("status") == "success":
            result = response.get("result", {})
            scene_name = result.get("name", "Unknown")
            object_count = result.get("object_count", 0)
            print(f"🎬 Scene: {scene_name}")
            print(f"📦 Objects: {object_count}")
            
            # List some objects
            objects = result.get("objects", [])
            if objects:
                print("📋 Scene objects:")
                for obj in objects[:5]:  # Show first 5
                    print(f"   - {obj.get('name', 'Unknown')} ({obj.get('type', 'Unknown')})")
        
        sock.close()
        print("✅ Test completed successfully!")
        return True
        
    except ConnectionRefusedError:
        print("❌ Connection refused - Is Blender running with MCP addon enabled?")
        return False
    except socket.timeout:
        print("❌ Connection timeout - Blender not responding")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON response: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_create_object():
    """Test creating an object"""
    host = "localhost"
    port = 9876
    
    print(f"\n🎨 Testing object creation...")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.settimeout(10.0)
        
        # Test create cube command
        command = {
            "type": "create_object", 
            "params": {
                "type": "CUBE",
                "name": "TestCube",
                "location": [2, 0, 1],
                "scale": [1.5, 1.5, 1.5]
            }
        }
        sock.sendall(json.dumps(command).encode('utf-8'))
        
        print("📤 Sent create_object command...")
        
        # Receive response
        response_data = sock.recv(8192)
        response = json.loads(response_data.decode('utf-8'))
        
        print("📥 Create object response:")
        print(json.dumps(response, indent=2))
        
        sock.close()
        return response.get("status") == "success"
        
    except Exception as e:
        print(f"❌ Create object error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Blender MCP Direct Connection Test")
    print("=" * 40)
    
    # Test basic connection
    if test_blender_connection():
        # Test object creation
        test_create_object()
    else:
        print("\n💡 Make sure:")
        print("   1. Blender is running")
        print("   2. MCP addon is enabled")
        print("   3. Socket server is started (click 'Connect to Local AI')")
        sys.exit(1) 