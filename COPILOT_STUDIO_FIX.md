# 🔧 **Copilot Studio Custom Connector - COMPLETE FIX**

## 🎯 **The Problem**
Your **create object endpoint** returns errors because Copilot Studio isn't sending parameters correctly to your server.

## ✅ **The Solution**

### **Step 1: Update Custom Connector URLs**
```
❌ Old (WRONG): 
   - Host: chicken-key-exclude-skating.trycloudflare.com
   - OpenAPI: /docs/openapi.json

✅ New (CORRECT):
   - Host: [YOUR_NEW_TUNNEL_URL]
   - OpenAPI: /openapi.json
```

### **Step 2: Get Your New Tunnel URL**
Run in terminal (already running):
```bash
.\cloudflared.exe tunnel --url http://localhost:8000
```

**Look for output like:**
```
Your quick Tunnel has been created! Visit it at:
https://[NEW-TUNNEL-URL].trycloudflare.com
```

### **Step 3: Update Copilot Studio Connector**

1. **Open Copilot Studio** → Custom Connectors
2. **Edit your Blender connector**
3. **Update these settings:**

```yaml
General:
  Host: [YOUR_NEW_TUNNEL_URL].trycloudflare.com
  
OpenAPI:
  URL: https://[YOUR_NEW_TUNNEL_URL].trycloudflare.com/openapi.json
  
Test Connection:
  URL: https://[YOUR_NEW_TUNNEL_URL].trycloudflare.com/health
```

### **Step 4: Test Each Endpoint**

#### ✅ **Working Endpoints** (already confirmed):
- **Health Check**: `/health`
- **Scene Info**: `/api/blender/scene`  
- **AI Prompts**: `/api/ai/prompt`
- **Code Execution**: `/api/blender/code`

#### 🔧 **Create Object Fix**:
The create endpoint **should work** once the connector is properly configured.

### **Step 5: Alternative - Use Code Execution**

If create endpoint still has issues, use the **code execution endpoint** which works:

**Instead of:** Create Object → cube
**Use:** Execute Code → `bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))`

## 🚀 **Test Commands for Copilot Studio**

### **1. Health Check**
```
"Check Blender connection"
```

### **2. Get Scene Info**  
```
"Show me my current Blender scene"
```

### **3. Create Objects via Code**
```
"Execute this Python code: bpy.ops.mesh.primitive_cube_add(location=(2, 2, 2))"
```

### **4. AI-Powered Commands**
```
"Create a sphere at position 5, 5, 5"
"Add a cube to my scene"
"Make a cylinder"
```

## 🎯 **Expected Results**

After fixing the connector configuration:
- ✅ All endpoints should work properly
- ✅ Create object should work via both direct API and AI commands
- ✅ No more 404 or 503 errors
- ✅ Proper parameter passing from Copilot Studio to Blender

## 🐛 **Troubleshooting**

### **If create endpoint still fails:**
1. Check server logs for exact error
2. Use code execution as alternative
3. Verify Blender MCP addon is running
4. Test direct API calls vs Copilot Studio calls

### **Common Issues:**
- **Tunnel expired**: Restart cloudflared
- **Blender not connected**: Check port 9876
- **Parameter mismatch**: Use exact JSON format

## ✅ **Success Indicators**

You'll know it's working when:
- Health check shows `blender_connected: true`
- Scene endpoint returns your Blender objects
- Create endpoint adds objects to Blender
- No error messages in Copilot Studio

---

**🎯 Next Steps:** Update your connector with the new tunnel URL and test! 