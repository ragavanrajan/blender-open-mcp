#!/usr/bin/env python3
"""Test script to verify both array and string formats work"""

import requests
import json

def test_formats():
    print("=== Testing Array Format (Backward Compatibility) ===")
    data1 = {
        'type': 'CUBE', 
        'name': 'ArrayCube', 
        'location': [1, 2, 3],
        'rotation': [0, 0, 1.57],
        'scale': [2, 1, 1]
    }
    
    try:
        r1 = requests.post('http://localhost:8000/api/v2/objects', json=data1, timeout=10)
        print(f'Array Status: {r1.status_code}')
        print(f'Array Response: {r1.text}')
    except Exception as e:
        print(f'Array Test Error: {e}')
    
    print("\n=== Testing String Format (Copilot Studio Compatible) ===")
    data2 = {
        'type': 'SPHERE', 
        'name': 'StringSphere', 
        'location': '4,5,6',
        'rotation': '0,0,1.57', 
        'scale': '2,1,1'
    }
    
    try:
        r2 = requests.post('http://localhost:8000/api/v2/objects', json=data2, timeout=10)
        print(f'String Status: {r2.status_code}')
        print(f'String Response: {r2.text}')
    except Exception as e:
        print(f'String Test Error: {e}')
    
    print("\n=== Testing Minimal Format (Type Only) ===")
    data3 = {'type': 'CYLINDER'}
    
    try:
        r3 = requests.post('http://localhost:8000/api/v2/objects', json=data3, timeout=10)
        print(f'Minimal Status: {r3.status_code}')
        print(f'Minimal Response: {r3.text}')
    except Exception as e:
        print(f'Minimal Test Error: {e}')

    print("\n=== Testing Public Endpoint ===")
    try:
        r4 = requests.post('https://blender-open-mcp-de.com/api/v2/objects', json={'type': 'CONE'}, timeout=10)
        print(f'Public Status: {r4.status_code}')
        print(f'Public Response: {r4.text}')
    except Exception as e:
        print(f'Public Test Error: {e}')

if __name__ == "__main__":
    test_formats() 