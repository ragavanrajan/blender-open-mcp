# Local Blender MCP Setup for Copilot Studio

This guide helps you run your Blender MCP server locally and make it accessible to Copilot Studio via ngrok tunnel.

## Why Local Setup?

The Blender MCP server needs to communicate with a running Blender instance, which requires:
- Blender installed and running
- Blender MCP addon active
- Socket connection to Blender

Azure Web Apps don't have Blender installed, so we run it locally and expose it via tunnel.

## Prerequisites

1. **Blender** installed on your local machine
2. **Python 3.8+** with pip
3. **ngrok account** (free tier works fine)

## Setup Steps

### 1. Install Dependencies
```bash
pip install pyngrok uvicorn fastapi
```

### 2. Install Blender Addon
1. Copy `addon.py` to your Blender scripts folder
2. Enable the addon in Blender preferences
3. Make sure the socket server is running (port 9876)

### 3. Setup ngrok (Optional but Recommended)
1. Sign up at https://ngrok.com
2. Get your auth token
3. Set it in the tunnel script:
```python
ngrok.set_auth_token("your_auth_token_here")
```

### 4. Run Local Server with Tunnel
```bash
python local_tunnel.py
```

You'll see output like:
```
🔧 Blender MCP Local Tunnel Setup
========================================
🔗 Setting up ngrok tunnel...
✅ Tunnel created!
🌐 Public URL: https://abc123.ngrok.io
📝 Use this URL in your Copilot Studio custom connector

📋 Update your connector with:
   Base URL: https://abc123.ngrok.io
   OpenAPI/Swagger: https://abc123.ngrok.io/docs
```

### 5. Update Copilot Studio Connector
1. Go to your Copilot Studio
2. Edit your custom connector
3. Update the **Base URL** to the ngrok URL (e.g., `https://abc123.ngrok.io`)
4. Save the connector

## Testing Your Setup

Now you can test with these prompts in Copilot Studio:

### Basic Tests
- "Check if the Blender server is running"
- "Show me the current scene information"
- "Create a cube named 'TestCube'"

### Advanced Tests  
- "Create a red sphere and move it above the default cube"
- "Make a scene with three objects: a blue cube, a green cylinder, and a yellow sphere arranged in a triangle"

## Troubleshooting

### "MCP not available" Error
- Make sure Blender is running
- Check that the MCP addon is enabled
- Verify socket server is on port 9876

### Connection Timeout
- Restart Blender
- Restart the local server
- Check firewall settings

### ngrok Issues
- Make sure you have a valid auth token
- Check your ngrok usage limits
- Try restarting the tunnel

## Production Considerations

For production use, consider:
- **VPS/Cloud VM** with Blender installed
- **Persistent tunnel** service
- **Authentication** for your endpoints
- **Rate limiting** and monitoring

## Alternative: Cloud VM Setup

If you want a more permanent solution:
1. Set up a cloud VM (Azure, AWS, GCP)
2. Install Blender on the VM
3. Run your MCP server there
4. Use the VM's public IP instead of ngrok

This gives you a always-on solution without tunneling. 