import requests
import json

# Test data with correct CUBE format
test_data = {
    "type": "CUBE",
    "name": "TestCube", 
    "location": [0, 0, 0]
}

print("Testing Create Object endpoint...")
print(f"Request data: {test_data}")

# Test local endpoint
try:
    response = requests.post('http://localhost:8000/api/v2/objects', json=test_data)
    print(f"\nLocal Status: {response.status_code}")
    print(f"Local Response: {response.text}")
except Exception as e:
    print(f"Local Error: {e}")

# Test public endpoint  
try:
    response = requests.post('https://blender-open-mcp-de.com/api/v2/objects', json=test_data)
    print(f"\nPublic Status: {response.status_code}")
    print(f"Public Response: {response.text}")
except Exception as e:
    print(f"Public Error: {e}") 