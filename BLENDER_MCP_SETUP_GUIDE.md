# 🎯 **Complete Blender MCP + Copilot Studio Integration Guide**

## 📋 **Table of Contents**
1. [Overview](#overview)
2. [Architecture](#architecture) 
3. [Prerequisites](#prerequisites)
4. [Installation & Setup](#installation--setup)
5. [Domain & Tunnel Management](#domain--tunnel-management)
6. [Copilot Studio Configuration](#copilot-studio-configuration)
7. [Usage Examples](#usage-examples)
8. [Troubleshooting](#troubleshooting)
9. [Advanced Features](#advanced-features)

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
- **Ollama** - Installed from [ollama.com](https://ollama.com)
- **Python 3.8+** - System installation
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
```bash
pip install fastapi uvicorn httpx
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

### **Step 5: Start Enhanced Server**
```bash
python enhanced_server.py
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

1. **Create Cloudflare Account**
   - Sign up at [cloudflare.com](https://cloudflare.com)
   - Add a domain (you can register one for $10-15/year)

2. **Setup Named Tunnel**
   ```bash
   # Login to Cloudflare
   .\cloudflared.exe login
   
   # Create named tunnel
   .\cloudflared.exe tunnel create blender-mcp
   
   # Configure tunnel
   .\cloudflared.exe tunnel route dns blender-mcp api.yourdomain.com
   
   # Run with custom domain
   .\cloudflared.exe tunnel run blender-mcp
   ```

3. **Benefits:**
   - ✅ **Your domain:** `api.yourdomain.com`
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
   OpenAPI URL: https://chicken-key-exclude-skating.trycloudflare.com/openapi.json
   Host: chicken-key-exclude-skating.trycloudflare.com
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
- ✅ **Verify Port:** Blender should listen on 9876
- ✅ **Restart Server:** Stop and restart enhanced_server.py

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
netstat -an | findstr "8000 9876 11434"

# Test local endpoints
curl http://localhost:8000/health
curl http://localhost:9876
curl http://localhost:11434/api/tags

# Check enhanced server status
python check_status.py
```

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
✅ Blender MCP Addon: Running (port 9876)
✅ Ollama AI Server: Running (port 11434) with llama3.2
✅ Enhanced Server: Running (port 8000)
✅ Cloudflare Tunnel: Active
✅ Public URL: https://chicken-key-exclude-skating.trycloudflare.com
✅ AI Integration: Functional
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

*Last Updated: June 10, 2025*
*Version: 2.0 Enhanced* 