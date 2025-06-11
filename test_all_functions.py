#!/usr/bin/env python3
"""
Comprehensive MCP Function Tests
Test all Blender MCP functionality
"""
import socket
import json
import time

def send_command(command_type, params=None):
    """Send command to Blender and return response"""
    host = "localhost"
    port = 9876
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.settimeout(15.0)
        
        command = {"type": command_type, "params": params or {}}
        sock.sendall(json.dumps(command).encode('utf-8'))
        
        response_data = sock.recv(8192)
        response = json.loads(response_data.decode('utf-8'))
        
        sock.close()
        return response
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

def test_scene_info():
    """Test getting scene information"""
    print("📋 Testing scene information...")
    response = send_command("get_scene_info")
    
    if response.get("status") == "success":
        result = response.get("result", {})
        print(f"   ✅ Scene: {result.get('name')}")
        print(f"   ✅ Objects: {result.get('object_count')}")
        return True
    else:
        print(f"   ❌ Failed: {response.get('message')}")
        return False

def test_create_objects():
    """Test creating different object types"""
    print("\n🎨 Testing object creation...")
    
    objects_to_create = [
        {"type": "CUBE", "name": "MyCube", "location": [0, 0, 2]},
        {"type": "SPHERE", "name": "MySphere", "location": [3, 0, 0]},
        {"type": "CYLINDER", "name": "MyCylinder", "location": [-3, 0, 0]},
        {"type": "CONE", "name": "MyCone", "location": [0, 3, 0]},
        {"type": "PLANE", "name": "MyPlane", "location": [0, -3, 0]},
    ]
    
    success_count = 0
    for obj in objects_to_create:
        response = send_command("create_object", obj)
        if response.get("status") == "success":
            print(f"   ✅ Created {obj['type']}: {obj['name']}")
            success_count += 1
        else:
            print(f"   ❌ Failed to create {obj['type']}: {response.get('message')}")
    
    return success_count == len(objects_to_create)

def test_modify_objects():
    """Test modifying objects"""
    print("\n✏️  Testing object modification...")
    
    modifications = [
        {"name": "MyCube", "location": [1, 1, 3], "scale": [2, 2, 2]},
        {"name": "MySphere", "rotation": [0, 0, 1.57], "scale": [0.5, 0.5, 0.5]},
    ]
    
    success_count = 0
    for mod in modifications:
        response = send_command("modify_object", mod)
        if response.get("status") == "success":
            print(f"   ✅ Modified {mod['name']}")
            success_count += 1
        else:
            print(f"   ❌ Failed to modify {mod['name']}: {response.get('message')}")
    
    return success_count == len(modifications)

def test_materials():
    """Test applying materials"""
    print("\n🎨 Testing materials...")
    
    materials = [
        {"object_name": "MyCube", "material_name": "RedMaterial", "color": [1.0, 0.0, 0.0]},
        {"object_name": "MySphere", "material_name": "BlueMaterial", "color": [0.0, 0.0, 1.0]},
        {"object_name": "MyCylinder", "material_name": "GreenMaterial", "color": [0.0, 1.0, 0.0]},
    ]
    
    success_count = 0
    for mat in materials:
        response = send_command("set_material", mat)
        if response.get("status") == "success":
            print(f"   ✅ Applied {mat['material_name']} to {mat['object_name']}")
            success_count += 1
        else:
            print(f"   ❌ Failed to apply material to {mat['object_name']}: {response.get('message')}")
    
    return success_count == len(materials)

def test_execute_code():
    """Test executing Python code"""
    print("\n🐍 Testing Python code execution...")
    
    code_tests = [
        "print('Hello from Blender!')",
        "bpy.context.scene.frame_current = 10",
        "len(bpy.context.scene.objects)"
    ]
    
    success_count = 0
    for i, code in enumerate(code_tests):
        response = send_command("execute_code", {"code": code})
        if response.get("status") == "success":
            print(f"   ✅ Code {i+1} executed successfully")
            success_count += 1
        else:
            print(f"   ❌ Code {i+1} failed: {response.get('message')}")
    
    return success_count == len(code_tests)

def test_delete_objects():
    """Test deleting objects"""
    print("\n🗑️  Testing object deletion...")
    
    objects_to_delete = ["MyCone", "MyPlane"]
    
    success_count = 0
    for obj_name in objects_to_delete:
        response = send_command("delete_object", {"name": obj_name})
        if response.get("status") == "success":
            print(f"   ✅ Deleted {obj_name}")
            success_count += 1
        else:
            print(f"   ❌ Failed to delete {obj_name}: {response.get('message')}")
    
    return success_count == len(objects_to_delete)

def final_scene_check():
    """Final scene state check"""
    print("\n📊 Final scene state...")
    response = send_command("get_scene_info")
    
    if response.get("status") == "success":
        result = response.get("result", {})
        objects = result.get("objects", [])
        print(f"   📦 Total objects: {len(objects)}")
        print("   📋 Objects in scene:")
        for obj in objects:
            name = obj.get("name", "Unknown")
            obj_type = obj.get("type", "Unknown")
            loc = obj.get("location", [0, 0, 0])
            print(f"      - {name} ({obj_type}) at {loc}")
        return True
    else:
        print(f"   ❌ Failed to get final scene info: {response.get('message')}")
        return False

def main():
    """Run all tests"""
    print("🧪 Comprehensive Blender MCP Function Tests")
    print("=" * 50)
    
    tests = [
        ("Scene Info", test_scene_info),
        ("Create Objects", test_create_objects),
        ("Modify Objects", test_modify_objects),
        ("Apply Materials", test_materials),
        ("Execute Code", test_execute_code),
        ("Delete Objects", test_delete_objects),
        ("Final Check", final_scene_check),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔄 Running: {test_name}")
        try:
            if test_func():
                print(f"✅ {test_name} - PASSED")
                passed += 1
            else:
                print(f"❌ {test_name} - FAILED")
        except Exception as e:
            print(f"❌ {test_name} - ERROR: {e}")
        
        time.sleep(0.5)  # Small delay between tests
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Your MCP server is working perfectly!")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")

if __name__ == "__main__":
    main() 