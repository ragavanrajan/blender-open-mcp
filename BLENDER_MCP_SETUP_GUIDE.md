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
pip install fastmcp httpx

# 3. Start the full MCP server (auto-detected)
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
pip install fastmcp
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

#### **Auto-Detected Start (Recommended)**
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
# Custom port and host
python main.py --port 8080 --host 0.0.0.0

# Get help
python main.py --help
```

#### **Verify Server is Running**
```bash
# Check server mode and test functionality
python verify_python_upgrade.py

# Test simple server (if in simple mode)
python test_simple_server.py

# Test manually (works for both modes)
curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"command": "health_check"}'
```

### **Step 6: Create Public Tunnel**
```bash
# Download cloudflared
Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile "cloudflared.exe"

# Start tunnel
.\cloudflared.exe tunnel --url http://localhost:8000
```

---

## 🌐 **Domain & Tunnel Management**

### **Current Setup: Temporary Domain**
- **URL:** `https://chicken-key-exclude-skating.trycloudflare.com`
- **Type:** Temporary (changes on restart)
- **Ownership:** Public, not owned by you
- **Duration:** Active while tunnel is running

### **Making It Permanent & Owned**

#### **Option 1: Cloudflare Named Tunnel (Recommended)**

1. **Setup Your Domain**
   - Your domain: `BLENDER-OPEN-MCP-DE.COM`
   - Ensure domain is added to your Cloudflare account
   - Domain DNS should be managed by Cloudflare

2. **Setup Named Tunnel**
   ```bash
   # Login to Cloudflare
   .\cloudflared.exe login
   
   # Create named tunnel
   .\cloudflared.exe tunnel create blender-mcp
   
   # Configure tunnel to route to your root domain
   .\cloudflared.exe tunnel route dns blender-mcp blender-open-mcp-de.com
   
   # Run with your custom domain
   .\cloudflared.exe tunnel run blender-mcp
   ```

3. **Your Setup Benefits:**
   - ✅ **Your domain:** `blender-open-mcp-de.com`
   - ✅ **Permanent:** Never changes
   - ✅ **Controlled:** Only you can manage it
   - ✅ **SSL Certificate:** Automatic HTTPS

#### **Option 2: ngrok Static Domain**

1. **Get ngrok Account**
   - Sign up at [ngrok.com](https://ngrok.com)
   - Upgrade to paid plan for static domains

2. **Use Your Static Domain**
   ```bash
   ngrok http 8000 --domain=your-static-domain.ngrok.app
   ```

#### **Option 3: Alternative Tunneling Services**

- **LocalTunnel:** Free with custom subdomains
- **Serveo:** SSH-based tunneling
- **PageKite:** Paid service with custom domains

---

## 🤖 **Copilot Studio Configuration**

### **Step 1: Create Custom Connector**

1. **Go to Copilot Studio**
   - Navigate to `Custom connectors`
   - Click `New custom connector`
   - Choose `Import from URL`

2. **Configure Connection**
   ```
   OpenAPI URL: https://blender-open-mcp-de.com/openapi.json
   Host: blender-open-mcp-de.com
   Base URL: /
   Authentication: None
   ```

### **Step 2: Create Copilot Agent**

1. **Create New Agent**
   - Name: "Blender Control Agent"
   - Description: "AI-powered Blender 3D control"

2. **Add Custom Connector**
   - Go to `Knowledge & Actions`
   - Add your BlenderMCP connector
   - Enable all operations

### **Step 3: Test Connection**
   - Go to connector `Test` tab
   - Create connection
   - Test `health` operation

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

#### **503 Service Unavailable**
- ✅ **Check Blender:** Ensure MCP addon is running
- ✅ **Verify Port:** Blender should listen on 9999 (default) or 9876
- ✅ **Restart Server:** Stop and restart with `python main.py`

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

| Endpoint | Method | Purpose | Example |
|----------|--------|---------|---------|
| `/health` | GET | System status | Health check |
| `/api/blender/scene` | GET | Scene info | Get objects list |
| `/api/blender/create` | POST | Create object | Add cube/sphere |
| `/api/blender/modify` | PUT | Modify object | Move/rotate/scale |
| `/api/blender/delete/{id}` | DELETE | Delete object | Remove by name |
| `/api/blender/material` | POST | Apply material | Set color/texture |
| `/api/blender/code` | POST | Execute Python | Run Blender script |
| `/api/ai/prompt` | POST | AI conversation | Ask questions |
| `/api/ai/command` | POST | AI→Blender | Natural language |

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
✅ Blender MCP Addon: Running (port 9999)
✅ MCP Server: Running (port 8000) - Auto-detected mode
✅ Ollama AI Server: Optional (port 11434) with llama3.2
✅ Cloudflare Tunnel: Optional - for external access
✅ Public URL: Available when tunnel is active
✅ Full Integration: Functional with all MCP features
✅ Copilot Studio: Ready for connection
```

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