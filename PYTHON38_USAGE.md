# Python 3.8 Compatible Blender MCP Server

Due to Python 3.8 compatibility issues with the latest MCP packages (which require Python 3.10+), this project includes a simplified server implementation that works with Python 3.8.

## Quick Start

1. **Start the server:**
   ```bash
   python main.py
   ```
   
   Or directly:
   ```bash
   python src/blender_open_mcp/simple_server.py
   ```

2. **The server will start on http://localhost:8000**

## Usage

The server provides a simple HTTP API that communicates with Blender. You can send POST requests to `http://localhost:8000/` with JSON payloads.

### Available Commands

#### Health Check
```bash
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"command": "health_check"}'
```

#### Get Scene Info
```bash
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"command": "get_scene_info"}'
```

#### Create Object
```bash
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"command": "create_object", "params": {"type": "CUBE", "name": "MyCube"}}'
```

#### Get Object Info
```bash
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"command": "get_object_info", "params": {"object_name": "MyCube"}}'
```

### Python Usage

You can also use Python to interact with the server:

```python
import requests

# Health check
response = requests.post('http://localhost:8000/', 
                        json={'command': 'health_check'})
print(response.json())

# Create a cube
response = requests.post('http://localhost:8000/', 
                        json={'command': 'create_object', 
                              'params': {'type': 'CUBE', 'name': 'MyCube'}})
print(response.json())
```

## Requirements

- Python 3.8+
- Blender with the MCP addon running (for actual Blender communication)
- No additional packages required (uses only Python standard library)

## Blender Setup

1. Make sure Blender is running
2. Install and enable the Blender MCP addon
3. The addon should be listening on `localhost:9999` (default)

## Server Options

```bash
python main.py --help
python src/blender_open_mcp/simple_server.py --help
```

Available options:
- `--host`: Host to bind to (default: localhost)
- `--port`: Port to bind to (default: 8000)

## Upgrading to Full MCP

To use the full MCP server with all features:

1. **Upgrade Python to 3.10+**
2. **Install dependencies:**
   ```bash
   pip install fastmcp
   pip install -r requirements.txt
   ```
3. **Use the original server:**
   ```bash
   python src/blender_open_mcp/server.py
   ```

## Troubleshooting

### Server won't start
- Check if port 8000 is already in use
- Try a different port: `python main.py --port 8001`

### Can't connect to Blender
- Ensure Blender is running
- Check that the Blender MCP addon is enabled and listening on port 9999
- The server will still start even if Blender isn't available

### Commands return errors
- Make sure Blender is running with the addon
- Check the server logs for detailed error messages 