# 🎯 **Complete Blender MCP + Copilot Studio Integration Guide**

## 📋 **Table of Contents**
1. [Overview](#overview)
2. [Python Version Compatibility](#python-version-compatibility)
3. [Architecture](#architecture) 
4. [Prerequisites](#prerequisites)
5. [Installation & Setup](#installation--setup)
6. [Domain & Tunnel Management](#domain--tunnel-management)
7. [Copilot Studio Configuration](#copilot-studio-configuration)
8. [Usage Examples](#usage-examples)
9. [Troubleshooting](#troubleshooting)
10. [Advanced Features](#advanced-features)

---

## 🔍 **Overview**

This guide sets up a complete integration between:
- **Blender 3D** (local installation)
- **Ollama AI** (local LLM server)
- **Enhanced MCP Server** (custom FastAPI server)
- **Cloudflare Tunnel** (public access)
- **Microsoft Copilot Studio** (cloud agent platform)

**End Result:** Control your local Blender installation using natural language through a Copilot Studio agent with AI-powered commands.

---

## 🐍 **Python Version Compatibility**

This project supports two modes depending on your Python version:

### **Python 3.8-3.9 (Simple Mode)**
- ✅ **Works out of the box** - No external dependencies required
- ✅ **Basic HTTP server** - Full Blender integration
- ✅ **All core features** - Object creation, modification, materials
- ⚠️ **Limited MCP features** - Uses simplified server implementation

### **Python 3.10+ (Full MCP Mode)**
- ✅ **Complete MCP protocol** - Full Model Context Protocol support
- ✅ **Advanced features** - FastMCP server with all capabilities
- ✅ **Better performance** - Optimized for production use
- ⚠️ **Requires upgrade** - Need to install Python 3.10+

**Current Detection:** The project automatically detects your Python version and uses the appropriate mode.

### **🚀 Quick Start (TL;DR)**

#### **For Python 3.10+ Users (Full MCP Features):**
```bash
# 1. Clone and enter directory
git clone https://github.com/dhakalnirajan/blender-open-mcp.git
cd blender-open-mcp

# 2. Install full MCP dependencies
pip install fastmcp httpx uvicorn

# 3. Start the full MCP server with uvicorn (recommended)
uvicorn src.blender_open_mcp.server:app --host 0.0.0.0 --port 8000

# OR use auto-detected method
python main.py

# 4. Verify everything works
python verify_python_upgrade.py

# 5. Install Blender addon and you're ready!
```

#### **For Python 3.8-3.9 Users (Simple Mode):**
```bash
# 1. Clone and enter directory  
git clone https://github.com/dhakalnirajan/blender-open-mcp.git
cd blender-open-mcp

# 2. Start the simple server (no dependencies needed)
python main.py

# 3. Test it works
python test_simple_server.py

# 4. Install Blender addon and you're ready!
```

**Auto-Detection:** The `main.py` script automatically detects your Python version and uses the appropriate server mode!

---

## 🏗️ **Architecture**

```
┌─────────────────┐    HTTPS     ┌─────────────────┐
│  Copilot Studio │ ──────────► │ Cloudflare      │
│     Agent       │              │ Tunnel (Public) │
└─────────────────┘              └─────────────────┘
                                          │
                                          │ HTTP
                                          ▼
┌─────────────────┐              ┌─────────────────┐
│ Ollama AI       │◄─────────────┤ Enhanced MCP    │
│ (llama3.2)      │   AI Queries │ Server          │
│ localhost:11434 │              │ localhost:8000  │
└─────────────────┘              └─────────────────┘
                                          │
                                          │ Socket
                                          ▼
                                 ┌─────────────────┐
                                 │ Blender MCP     │
                                 │ Addon           │
                                 │ localhost:9876  │
                                 └─────────────────┘
```

---

## ✅ **Prerequisites**

### **Software Requirements:**
- **Blender 3.0+** - Downloaded from [blender.org](https://blender.org)
- **Ollama** - Installed from [ollama.com](https://ollama.com) *(Optional for AI features)*
- **Python 3.8+** - System installation
  - **Python 3.8-3.9:** Simple mode (no extra dependencies)
  - **Python 3.10+:** Full MCP mode (requires fastmcp package)
- **Git** - For repository cloning

### **Accounts Required:**
- **Microsoft Copilot Studio** - For agent creation
- **Cloudflare Account** (optional) - For permanent domains

---

## 🚀 **Installation & Setup**

### **Step 1: Repository Setup**
```bash
git clone https://github.com/dhakalnirajan/blender-open-mcp.git
cd blender-open-mcp
```

### **Step 2: Install Dependencies**

#### **For Python 3.8-3.9 (Simple Mode)**
```bash
# No dependencies required! Uses Python standard library only
python --version  # Should show 3.8 or 3.9
```

#### **For Python 3.10+ (Full MCP Mode)**
```bash
# Install full MCP dependencies
pip install fastmcp uvicorn
pip install -r requirements.txt
```

#### **Optional AI Dependencies (All Python versions)**
```bash
# Only needed if you want AI features
pip install httpx  # For Ollama integration
```

### **Step 3: Install Blender Addon**
1. Open Blender
2. Go to `Edit → Preferences → Add-ons`
3. Click `Install...`
4. Select `addon.py` from the project directory
5. Enable "Blender MCP" addon
6. Click "Start MCP Server" in the addon panel

### **Step 4: Setup Ollama**
```bash
# Install llama3.2 model
ollama pull llama3.2

# Verify Ollama is running
curl http://localhost:11434/api/tags
```

### **Step 5: Start the Server**

#### **FastAPI/Uvicorn Method (Recommended for Production)**
```bash
# Start with uvicorn for full FastAPI features (Python 3.10+)
uvicorn app:app --host 0.0.0.0 --port 8000

# OR if you have FastMCP installed directly
uvicorn src.blender_open_mcp.server:app --host 0.0.0.0 --port 8000

# With reload for development
uvicorn src.blender_open_mcp.server:app --host 0.0.0.0 --port 8000 --reload
```

#### **Auto-Detected Start (Alternative)**
```bash
# Automatically detects Python version and uses the best available server
python main.py

# Check what server mode is being used
python verify_python_upgrade.py
```

#### **Manual Server Selection**

**Simple Server (Python 3.8+):**
```bash
python src/blender_open_mcp/simple_server.py
```

**Full MCP Server (Python 3.10+ with fastmcp installed):**
```bash
python src/blender_open_mcp/server.py
```

#### **Server Options**
```bash
# Custom port and host with uvicorn
uvicorn src.blender_open_mcp.server:app --host 0.0.0.0 --port 8080

# Custom options with main.py
python main.py --port 8080 --host 0.0.0.0

# Get help
python main.py --help
```

#### **🔄 Startup Method Comparison**

| Method | Best For | Features | Command |
|--------|----------|----------|---------|
| **Uvicorn** | Production, Development | FastAPI docs, hot reload, ASGI | `uvicorn src.blender_open_mcp.server:app --host 0.0.0.0 --port 8000` |
| **Python main.py** | Quick testing, Auto-detection | Version detection, fallback | `python main.py --host 0.0.0.0 --port 8000` |

**For Copilot Studio integration, we recommend using uvicorn** as it provides the full FastAPI experience with automatic OpenAPI documentation at `/docs`.

#### **Verify Server is Running**
```bash
# Check server mode and test functionality
python verify_python_upgrade.py

# Test simple server (if in simple mode)
python test_simple_server.py

# Test uvicorn FastAPI server
curl -X GET http://localhost:8000/docs  # FastAPI docs
curl -X GET http://localhost:8000/health  # Health check

# Test manually (works for both modes)
curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"command": "health_check"}'
```

### **Step 6: Create Public Tunnel & Batch Files**

#### **Create Startup Batch Files:**
```bash
# Create start-server.bat
echo '@echo off
echo ================================
echo Starting Blender MCP Server...
echo ================================
cd /d "E:\MyDev\MyMCP\blender-open-mcp"
python main.py --host 0.0.0.0 --port 8000
echo Server stopped.
pause' > start-server.bat

# Create start-tunnel.bat  
echo '@echo off
echo ================================
echo Starting Cloudflare Tunnel...
echo Domain: blender-open-mcp-de.com
echo ================================
cd /d "E:\MyDev\MyMCP\blender-open-mcp"
.\cloudflared.exe tunnel --config tunnel-config.yml run
echo Tunnel stopped.
pause' > start-tunnel.bat
```

#### **Setup Cloudflare Tunnel:**
```bash
# Download cloudflared (if not already done)
Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile "cloudflared.exe"

# Create tunnel (if not exists)
.\cloudflared.exe tunnel create blender-mcp-tunnel

# Configure tunnel-config.yml with your tunnel ID and credentials path
```

---

## 🌐 **Domain & Tunnel Management**

### **Current Setup: Your Custom Domain**
- **Your Domain:** `blender-open-mcp-de.com`
- **Type:** Custom domain with Cloudflare
- **Ownership:** Owned by you
- **SSL:** Automatic HTTPS with Cloudflare

### **Setting Up Your Permanent Domain (blender-open-mcp-de.com)**

#### **Step 1: Configure Cloudflare Tunnel**

1. **Install Cloudflared**
   ```bash
   # Windows
   Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile "cloudflared.exe"
   
   # OR download from: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/
   ```

2. **Authenticate with Cloudflare**
   ```bash
   # Login to your Cloudflare account
   .\cloudflared.exe tunnel login
   ```

3. **Create Named Tunnel**
   ```bash
   # Create a persistent tunnel
   .\cloudflared.exe tunnel create blender-mcp-tunnel
   
   # Note the tunnel ID from the output - you'll need it
   ```

4. **Configure DNS Routing**
   ```bash
   # Route your domain to the tunnel
   .\cloudflared.exe tunnel route dns blender-mcp-tunnel blender-open-mcp-de.com
   ```

5. **Create Configuration File**
   Create `config.yml` in your project directory:
   ```yaml
   tunnel: YOUR_TUNNEL_ID_HERE
   credentials-file: C:\Users\%USERNAME%\.cloudflared\YOUR_TUNNEL_ID_HERE.json
   
   ingress:
     - hostname: blender-open-mcp-de.com
       service: http://localhost:8000
     - service: http_status:404
   ```

6. **Run the Tunnel**
   ```bash
   # Run with configuration file
   .\cloudflared.exe tunnel --config config.yml run
   
   # OR run directly (simpler for testing)
   .\cloudflared.exe tunnel run blender-mcp-tunnel
   ```

#### **Step 2: Verify Domain Setup**
```bash
# Test your domain is working
curl https://blender-open-mcp-de.com/health

# Test from PowerShell
Invoke-WebRequest -Uri "https://blender-open-mcp-de.com/health" -Method GET
```

### **Benefits of Your Custom Domain Setup:**
- ✅ **Permanent URL:** Never changes, reliable for Copilot Studio
- ✅ **Professional:** Your own branded domain
- ✅ **SSL Secure:** Automatic HTTPS encryption
- ✅ **Fast:** Cloudflare CDN optimization
- ✅ **Controlled:** Only you can manage access

---

## 🤖 **Copilot Studio Configuration**

### **Step 1: Create Custom Connector**

1. **Access Copilot Studio**
   - Go to [Copilot Studio](https://copilotstudio.microsoft.com)
   - Navigate to `Custom connectors`
   - Click `New custom connector`

2. **Import from URL**
   - Choose `Import from OpenAPI URL`
   - **OpenAPI URL:** `https://blender-open-mcp-de.com/openapi.json`
   - Click `Import`

3. **Configure General Settings**
   ```
   Connector Name: BlenderMCP
   Description: AI-powered Blender 3D control through MCP
   Host: blender-open-mcp-de.com
   Base URL: /
   Scheme: HTTPS
   ```

4. **Security Configuration**
   - Authentication Type: `No authentication` (for now)
   - *Optional: Add API key authentication later for security*

### **Step 2: Define Key Actions**

Add these essential actions to your connector:

#### **Action 1: Send AI Prompt**
```
Name: SendPrompt
Summary: Send natural language commands to Blender via AI
Description: Uses AI to interpret and execute Blender commands

Operation ID: send_prompt
HTTP Method: POST
URL: /api/ai/prompt

Request Body:
{
  "prompt": {
    "type": "string",
    "description": "Natural language command for Blender",
    "required": true
  },
  "model": {
    "type": "string", 
    "description": "AI model to use",
    "default": "llama3.2"
  }
}

Response:
{
  "response": "string",
  "success": "boolean", 
  "blender_result": "object"
}
```

#### **Action 2: Get Scene Info**
```
Name: GetSceneInfo
Summary: Get current Blender scene information
Description: Retrieves list of objects and scene details

Operation ID: get_scene_info  
HTTP Method: GET
URL: /api/blender/scene

Response:
{
  "objects": "array",
  "active_object": "string",
  "scene_name": "string"
}
```

#### **Action 3: Create Object**
```
Name: CreateObject
Summary: Create 3D object in Blender
Description: Creates primitives like cubes, spheres, cylinders

Operation ID: create_object
HTTP Method: POST  
URL: /api/blender/create

Request Body:
{
  "type": {
    "type": "string",
    "description": "Object type (cube, sphere, cylinder, etc.)",
    "required": true
  },
  "name": {
    "type": "string", 
    "description": "Object name",
    "required": false
  },
  "location": {
    "type": "array",
    "description": "X,Y,Z coordinates [x,y,z]", 
    "required": false
  }
}
```

#### **Action 4: Execute Blender Code**
```
Name: ExecuteBlenderCode
Summary: Execute Python code in Blender
Description: Runs custom Python scripts in Blender

Operation ID: execute_code
HTTP Method: POST
URL: /api/blender/code

Request Body:
{
  "code": {
    "type": "string",
    "description": "Python code to execute",
    "required": true
  }
}
```

### **Step 3: Test Your Connector**

1. **Test Connection**
   - Go to `Test` tab in your connector
   - Create a new connection
   - Test each action:

2. **Test Health Check**
   ```
   Action: GET /health
   Expected Response: {"status": "healthy", "blender_connected": true}
   ```

3. **Test Scene Info**
   ```
   Action: GetSceneInfo
   Expected Response: List of current Blender objects
   ```

4. **Test Object Creation**
   ```
   Action: CreateObject
   Body: {"type": "cube", "name": "test_cube", "location": [0,0,0]}
   Expected Response: Object creation confirmation
   ```

### **Step 4: Create Your Copilot Agent**

1. **Create New Agent**
   - Name: `Blender 3D Assistant`
   - Description: `AI-powered assistant for controlling Blender 3D software`

2. **Add Your Connector**
   - Go to `Actions` → `Add an action`
   - Select your `BlenderMCP` connector
   - Enable all actions you want to use

3. **Configure Instructions**
   Add this system prompt to your agent:
   ```
   You are a Blender 3D assistant that can control Blender software through natural language commands. 
   
   You can:
   - Create and modify 3D objects (cubes, spheres, cylinders, etc.)
   - Get information about the current scene
   - Apply materials and colors to objects
   - Execute Python code for advanced operations
   - Help with Blender workflows and techniques
   
   When users ask you to create or modify objects, use the appropriate actions to control Blender directly.
   Always confirm what you've done and describe the results.
   
   Available object types: cube, sphere, cylinder, cone, torus, plane, monkey
   Default location is [0,0,0] if not specified.
   Use natural, helpful responses.
   ```

### **Step 5: Enhanced Prompt Examples**

Configure your agent to handle these types of requests:

#### **Basic Object Creation**
```
User: "Create a red cube"
Agent Action: CreateObject → {"type": "cube", "name": "red_cube"}
Then: SendPrompt → {"prompt": "Color the cube red"}
```

#### **AI-Powered Commands**
```
User: "Create a beautiful artistic scene"
Agent Action: SendPrompt → {"prompt": "Create an artistic scene with multiple objects, good lighting, and interesting composition"}
```

#### **Scene Information**
```
User: "What's in my Blender scene?"
Agent Action: GetSceneInfo
Agent Response: Lists all objects with positions and properties
```

#### **Complex Operations**
```
User: "Create 5 colored spheres in a circle"
Agent Action: ExecuteBlenderCode → {complex Python script for multiple spheres}
```

### **Step 6: Advanced Configuration**

#### **Add Error Handling**
Configure your agent to handle common errors:
- Server connection issues
- Invalid object types
- Blender not responding

#### **Add Security (Optional)**
```bash
# Add API key authentication to your server
python main.py --api-key YOUR_SECRET_KEY

# Update connector with API key header:
# Header: X-API-Key = YOUR_SECRET_KEY
```

#### **Add Rate Limiting**
Protect your server from overuse:
```python
# In your server configuration
RATE_LIMIT = "10/minute"  # 10 requests per minute
```

### **Step 7: Production Deployment**

#### **🚀 Complete Setup with Batch Files**

Create two batch files for easy startup:

**1. Create `start-server.bat`:**
```batch
@echo off
echo ================================
echo Starting Blender MCP Server...
echo ================================
cd /d "E:\MyDev\MyMCP\blender-open-mcp"
python main.py --host 0.0.0.0 --port 8000
echo Server stopped.
pause
```

**2. Create `start-tunnel.bat`:**
```batch
@echo off
echo ================================
echo Starting Cloudflare Tunnel...
echo Domain: blender-open-mcp-de.com
echo ================================
cd /d "E:\MyDev\MyMCP\blender-open-mcp"
.\cloudflared.exe tunnel --config tunnel-config.yml run
echo Tunnel stopped.
pause
```

**3. Update `tunnel-config.yml`:**
```yaml
tunnel: YOUR_TUNNEL_ID_HERE
credentials-file: C:\Users\YOUR_USERNAME\.cloudflared\YOUR_TUNNEL_ID.json

ingress:
  - hostname: blender-open-mcp-de.com
    service: http://localhost:8000
  - hostname: www.blender-open-mcp-de.com  
    service: http://localhost:8000
  - service: http_status:404
```

#### **🎯 Daily Startup Process**

**Step 1: Start MCP Server**
```bash
# Open first PowerShell window
.\start-server.bat
```

**Step 2: Start Cloudflare Tunnel** 
```bash
# Open second PowerShell window
.\start-tunnel.bat  
```

**Step 3: Verify Both Services**
```bash
# Test local server
Invoke-WebRequest -Uri "http://localhost:8000/docs" -UseBasicParsing

# Test public domain
Invoke-WebRequest -Uri "https://blender-open-mcp-de.com/docs" -UseBasicParsing
```

#### **⚡ Alternative: Install as Windows Service**
```bash
# Install tunnel as Windows service (optional)
.\cloudflared.exe service install

# OR run in background
Start-Process -FilePath ".\cloudflared.exe" -ArgumentList "tunnel", "--config", "tunnel-config.yml", "run" -WindowStyle Hidden
```

---

## 🎨 **Usage Examples**

### **Basic Blender Operations**

#### **Scene Information**
```
"Show me what's currently in my Blender scene"
```
**Expected Response:** List of objects with positions

#### **Object Creation**
```
"Create a red cube at position 2, 0, 1"
"Add a blue sphere with radius 1.5"
"Make a green cylinder at the origin"
```

#### **Object Modification**
```
"Move the cube to position 5, 5, 2"
"Scale the sphere to 150% of its current size"
"Rotate the cylinder by 45 degrees around Z axis"
```

#### **Material Application**
```
"Make the default cube metallic gold"
"Apply a glass material to the sphere with transparency 0.8"
"Color the cylinder bright red"
```

### **AI-Powered Commands**

#### **Natural Language Scene Creation**
```
"Use AI to create a beautiful artistic scene with 3 objects"
"Have AI design a simple living room layout"
"Ask AI to create an abstract sculpture"
```

#### **AI Assistance**
```
"What's the best way to create realistic materials in Blender?"
"How do I set up proper lighting for rendering?"
"Explain procedural modeling techniques"
```

### **Advanced Operations**

#### **Python Code Execution**
```
"Execute this Python code: bpy.ops.mesh.primitive_torus_add(location=(3, 3, 0))"
"Run a script to create 10 random cubes"
```

#### **Batch Operations**
```
"Delete all objects except the camera and light"
"Create a grid of 5x5 cubes with different colors"
```

---

## 🔧 **Troubleshooting**

### **Common Issues & Solutions**

#### **404 Errors in Copilot Studio**
- ✅ **Check OpenAPI URL:** Use `/openapi.json` not `/docs/openapi.json`
- ✅ **Verify Host:** Use domain only, no `https://`
- ✅ **Test Tunnel:** Manually test endpoints in browser

#### **503 Service Unavailable (Power Platform Connector)**
- ✅ **Check Local Server:** Ensure MCP server is running on port 8000
  ```bash
  netstat -an | findstr "8000"  # Should show LISTENING
  ```
- ✅ **Check Cloudflare Tunnel:** Ensure tunnel is connecting properly
  ```bash
  .\cloudflared.exe tunnel --config tunnel-config.yml run
  ```
- ✅ **Fix Credentials Path:** Update tunnel-config.yml with correct user path
  ```yaml
  credentials-file: C:\Users\YOUR_ACTUAL_USERNAME\.cloudflared\YOUR_TUNNEL_ID.json
  ```
- ✅ **Test Local First:** Verify local server responds before testing public domain
  ```bash
  Invoke-WebRequest -Uri "http://localhost:8000/docs" -UseBasicParsing
  ```
- ✅ **Clean Restart:** Kill all processes and restart both services
  ```bash
  taskkill /F /IM python.exe /T
  taskkill /F /IM cloudflared.exe /T
  .\start-server.bat  # In first window
  .\start-tunnel.bat  # In second window
  ```
- ✅ **Check Blender Connection:** Ensure MCP addon is running (port 9876)
- ✅ **Verify Domain:** Test `https://blender-open-mcp-de.com/docs` directly in browser

#### **AI Not Responding**
- ✅ **Check Ollama:** Ensure service is running on 11434
- ✅ **Test Model:** Run `ollama run llama3.2` manually
- ✅ **Check Logs:** Look for AI errors in server output

#### **Tunnel Connection Lost**
- ✅ **Restart Tunnel:** Stop and restart cloudflared.exe
- ✅ **Update Connector:** Change domain in Copilot Studio
- ✅ **Check Network:** Ensure internet connectivity

### **Diagnostic Commands**

```bash
# Check if all services are running
netstat -an | findstr "8000 9999 11434"

# Test local endpoints
curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d "{\"command\": \"health_check\"}"
curl http://localhost:11434/api/tags  # Only if Ollama is installed

# Test server with Python
python test_simple_server.py

# Check server status
python check_status.py  # If available
```

---

## 🎯 **Full MCP Mode Features (Python 3.10+)**

### **Enhanced Capabilities with FastMCP**

When running Python 3.10+ with FastMCP installed, you get additional features:

✅ **Complete MCP Protocol Support**
- Full Model Context Protocol compliance
- Advanced client-server communication
- Better error handling and logging

✅ **Enhanced Performance**
- Optimized server architecture  
- Better concurrency handling
- Improved resource management

✅ **Advanced Tool Features**
- Rich context passing
- Image handling capabilities
- Streaming responses
- Progress reporting

✅ **Production Ready**
- ASGI app support for deployment
- Better scaling capabilities
- Advanced authentication options

### **Feature Comparison**

| Feature | Simple Mode (3.8+) | Full MCP Mode (3.10+) |
|---------|---------------------|------------------------|
| Basic Blender Control | ✅ | ✅ |
| HTTP API | ✅ | ✅ |
| Ollama Integration | ✅ | ✅ |
| MCP Protocol | ❌ | ✅ |
| Advanced Tools | ❌ | ✅ |
| Image Support | ❌ | ✅ |
| Production Deploy | Basic | Advanced |
| Performance | Good | Excellent |

---

## 🚀 **Advanced Features**

### **Available API Endpoints**

#### **🔧 Option A: Single Endpoint (Legacy)**
| Endpoint | Method | Purpose | Request Body |
|----------|--------|---------|--------------|
| `/` | POST | All operations | `{"command": "health_check"}` |
| `/` | POST | Scene info | `{"command": "get_scene_info"}` |
| `/` | POST | Create object | `{"command": "create_object", "params": {...}}` |
| `/` | POST | Modify object | `{"command": "modify_object", "params": {...}}` |
| `/` | POST | Execute code | `{"command": "execute_code", "params": {...}}` |

#### **🚀 Option B: REST Endpoints (Recommended)**
| Endpoint | Method | Purpose | Example |
|----------|--------|---------|---------|
| `/api/v2/health` | GET | System status | Health check with timestamp |
| `/api/v2/scene` | GET | Scene info | Get objects list |
| `/api/v2/objects` | POST | Create object | Add cube/sphere |
| `/api/v2/objects/{name}` | GET | Get object info | Retrieve object details |
| `/api/v2/objects/{name}` | PUT | Modify object | Move/rotate/scale |
| `/api/v2/objects/{name}` | DELETE | Delete object | Remove by name |
| `/api/v2/objects/{name}/material` | POST | Apply material | Set color/texture |
| `/api/v2/execute` | POST | Execute Python | Run Blender script |
| `/api/v2/ai/prompt` | POST | AI conversation | Ask questions |

### **🔄 Starting the Correct Server**

#### **Option A: Single Endpoint (Legacy)**
```bash
# Start simple server (port 8000)
python scripts/start/start-simple-server.py

# OR start directly
python -c "import sys; sys.path.insert(0, 'src'); from blender_open_mcp.simple_server import run_server; run_server('0.0.0.0', 8000)"
```

#### **Option B: REST Endpoints (Recommended)**
```bash
# Start REST server (port 8000)
python scripts/start/start-rest-server.py

# OR start with PowerShell script
./scripts/start/start-rest-server.ps1

# OR start directly
python -c "import sys; sys.path.insert(0, 'src'); from blender_open_mcp.rest_server import run_rest_server; run_rest_server('0.0.0.0', 8000)"
```

### **📊 Testing Both API Approaches**

#### **Test Single Endpoint (Option A)**
```bash
# Health check
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"command": "health_check"}'

# Scene info  
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"command": "get_scene_info"}'

# Create object
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"command": "create_object", "params": {"type": "CUBE", "name": "TestCube"}}'
```

#### **Test REST Endpoints (Option B)**
```bash
# Health check
curl -X GET http://localhost:8000/api/v2/health

# Scene info
curl -X GET http://localhost:8000/api/v2/scene

# Create object
curl -X POST http://localhost:8000/api/v2/objects \
  -H "Content-Type: application/json" \
  -d '{"type": "CUBE", "name": "TestCube", "location": [0, 0, 0]}'

# Get object info
curl -X GET http://localhost:8000/api/v2/objects/TestCube

# Modify object
curl -X PUT http://localhost:8000/api/v2/objects/TestCube \
  -H "Content-Type: application/json" \
  -d '{"location": [2, 2, 2], "rotation": [0, 0, 45]}'

# Delete object
curl -X DELETE http://localhost:8000/api/v2/objects/TestCube
```

### **🌐 Public Access via Tunnel**

#### **Option A URLs (Legacy)**
```bash
# Base URL: https://blender-open-mcp-de.com/
curl -X POST https://blender-open-mcp-de.com/ \
  -H "Content-Type: application/json" \
  -d '{"command": "health_check"}'
```

#### **Option B URLs (Recommended)**
```bash
# Base URL: https://blender-open-mcp-de.com/api/v2/
curl -X GET https://blender-open-mcp-de.com/api/v2/health
curl -X GET https://blender-open-mcp-de.com/api/v2/scene
curl -X POST https://blender-open-mcp-de.com/api/v2/objects \
  -H "Content-Type: application/json" \
  -d '{"type": "SPHERE", "name": "TestSphere"}'
```

### **Server Configuration**

The enhanced server supports these features:

```python
Features:
- Direct Blender socket connection (port 9876)
- Ollama AI integration (llama3.2 model)  
- Natural language command processing
- Standard REST API endpoints
- CORS enabled for web access
- Automatic error handling and retries
```

### **Extending Functionality**

#### **Adding New Models**
```bash
# Install additional Ollama models
ollama pull codellama
ollama pull mistral

# Update server configuration
python enhanced_server.py --ollama-model codellama
```

#### **Custom Endpoints**
Edit `enhanced_server.py` to add custom functionality:

```python
@app.post("/api/blender/custom")
async def custom_operation(request: CustomRequest):
    # Your custom Blender operations
    pass
```

---

## 📊 **Current Setup Status**

```
✅ Python Version: 3.11+ (Full MCP Mode) / 3.8+ (Simple Mode)
✅ FastMCP Package: Installed (for Python 3.10+)
✅ Blender MCP Addon: Running (port 9876)
✅ MCP Server: Running (port 8000) - Auto-detected mode
✅ Ollama AI Server: Optional (port 11434) with llama3.2
✅ Cloudflare Tunnel: Configured with static domain
✅ Static Domain: blender-open-mcp-de.com (permanent)
✅ Batch Files: start-server.bat & start-tunnel.bat created
✅ Tunnel Config: tunnel-config.yml with proper credentials path
✅ Full Integration: Functional with all MCP features
✅ Power Platform: Ready for connector testing
```

### **🎯 Quick Daily Startup:**
1. **Double-click** `start-server.bat` → Wait for "Connected to Blender"
2. **Double-click** `start-tunnel.bat` → Wait for tunnel connection
3. **Test:** Open `https://blender-open-mcp-de.com/docs` in browser
4. **Configure:** Power Platform connector with your domain

---

## 🎯 **Next Steps**

1. **Set up permanent domain** for production use
2. **Create more sophisticated prompts** in Copilot Studio
3. **Explore advanced AI features** with different models
4. **Build custom Blender operations** for specific workflows
5. **Share your setup** with team members

---

## 📞 **Support & Resources**

- **Original Repository:** [dhakalnirajan/blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)
- **Cloudflare Docs:** [Cloudflare Tunnel Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps)
- **Ollama Models:** [Available Models List](https://ollama.com/library)
- **Copilot Studio:** [Microsoft Documentation](https://docs.microsoft.com/en-us/microsoft-copilot-studio/)

---

**🎉 Congratulations! You now have a complete AI-powered Blender control system through Copilot Studio! 🎨🤖**

*Last Updated: June 11, 2025*
*Version: 2.2 - Auto-Detecting Python 3.8-3.11+ Compatible* 