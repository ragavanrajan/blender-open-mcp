# 🤖 **BlenderMCP & Copilot Studio - Complete Integration Guide**

> **One comprehensive guide for integrating your BlenderMCP server with Microsoft Copilot Studio**

## ✅ **Current System Status**

### **Working Components**
- **Local Server**: WORKING on http://localhost:8000/
- **Blender Connection**: AVAILABLE on port 9876
- **Cloudflare Tunnel**: WORKING at https://blender-open-mcp-de.com/
- **Tunnel ID**: ff98000b-7cf0-4883-9f44-4c868867c6d4

### **API Options**
**Option A - Single Endpoint (Current)**:
- **Health Check**: `POST /` with `{"command": "health_check"}` returns `{"status": "success", "message": "..."}`
- **Swagger File**: `blender-mcp-swagger2.yaml`

**Option B - REST Endpoints (New & Recommended)**:
- **Health Check**: `GET /api/v2/health` returns `{"status": "success", "message": "...", "timestamp": "..."}`
- **Swagger File**: `blender-mcp-separate-endpoints.yaml`

### **Server API Specification**

**Option A - Single Endpoint API**:
- **Endpoint**: POST /
- **Commands**: health_check, get_scene_info, create_object, modify_object, remove_object, apply_material, execute_code, ai_prompt
- **Request Format**: `{"command": "command_name", "params": {...}}`
- **Response Format**: `{"status": "success/error", "message": "...", "data": {...}}`

**Option B - REST Endpoints API**:
- **Health**: `GET /api/v2/health`
- **Scene**: `GET /api/v2/scene`  
- **Objects**: `POST /api/v2/objects`, `GET /api/v2/objects/{name}`, `PUT /api/v2/objects/{name}`, `DELETE /api/v2/objects/{name}`
- **Materials**: `POST /api/v2/objects/{name}/material`
- **Execute**: `POST /api/v2/execute`
- **AI**: `POST /api/v2/ai/prompt`

## 🚨 **Common Issues & Solutions**

### **Issue 1: HTTP 501 "Unsupported method"**
**Problem**: Copilot Studio sending GET requests, server only accepts POST
**Solution**: Configure ALL actions to use POST method with JSON body

### **Issue 2: Schema Validation Error**  
**Problem**: Copilot expects `string` response, server returns `object`
**Solution**: Set response schema type to "object" with proper properties

### **Issue 3: 530 Tunnel Errors**
**Problem**: Cloudflare tunnel connectivity issues
**Solution**: Restart tunnel with correct tunnel ID (ff98000b-7cf0-4883-9f44-4c868867c6d4)

## 🔗 **Custom Connector Configuration**

### **Option A: Single Endpoint Configuration (Current)**

**Custom Connector Base Configuration**
```
Display Name: BlenderMCP
Host URL: https://blender-open-mcp-de.com
Base URL: /
Authentication Type: No authentication
```

### **Option B: REST Endpoints Configuration (Recommended)**

**Custom Connector Base Configuration**
```
Display Name: BlenderMCP REST
Host URL: https://blender-open-mcp-de.com
Base URL: /api/v2
Authentication Type: No authentication
```

**Import Swagger**: Use `blender-mcp-separate-endpoints.yaml`

---

## 📋 **Option A Configuration (Single Endpoint)**

### **Action 1: GetHealth - CORRECTED**
```
Summary: Health Check
Description: Check if Blender server is running
Operation ID: GetHealth
Visibility: Important

Request:
  URL: /
  Method: POST
  Headers:
    Content-Type: application/json
  
Body:
{
  "command": "health_check"
}

Response Schema:
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Status of the server"
    },
    "message": {
      "type": "string", 
      "description": "Server status message"
    }
  },
  "required": ["status", "message"]
}
```

### **Action 2: GetSceneInfo - CORRECTED**
```
Summary: Get Scene Info
Description: Get information about the current Blender scene
Operation ID: GetSceneInfo
Visibility: Important

Request:
  URL: /
  Method: POST
  Headers:
    Content-Type: application/json
    
Body:
{
  "command": "get_scene_info"
}

Response Schema:
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "data": {
      "type": "object"
    }
  }
}
```

### **Action 3: CreateObject - CORRECTED**
```
Summary: Create Object
Description: Create an object in Blender
Operation ID: CreateObject
Visibility: Important

Request:
  URL: /
  Method: POST
  Headers:
    Content-Type: application/json

Body Template:
{
  "command": "create_object",
  "params": {
    "type": "{ObjectType}",
    "name": "{ObjectName}",
    "location": ["{X}", "{Y}", "{Z}"]
  }
}

Parameters:
- ObjectType (string, required): CUBE, SPHERE, CYLINDER, PLANE, CONE
- ObjectName (string, optional): Name for the object
- X, Y, Z (number, optional): Position coordinates

Response Schema:
{
  "type": "object", 
  "properties": {
    "status": {"type": "string"},
    "message": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "object_name": {"type": "string"},
        "location": {
          "type": "array", 
          "items": {"type": "number"}
        }
      }
    }
  }
}
```

### **Action 4: ModifyObject (Object Modification)**
```
Summary: Modify Object
Description: Modify properties of an existing object
Operation ID: ModifyObject
Visibility: Important

Request:
  URL: /
  Method: POST
  Headers:
    Content-Type: application/json

Body Template:
{
  "command": "modify_object",
  "params": {
    "object_name": "{ObjectName}",
    "location": ["{X}", "{Y}", "{Z}"],
    "rotation": ["{RX}", "{RY}", "{RZ}"],
    "scale": ["{SX}", "{SY}", "{SZ}"]
  }
}

Parameters:
- ObjectName (string, required): Name of object to modify
- X, Y, Z (number, optional): New position
- RX, RY, RZ (number, optional): Rotation in degrees
- SX, SY, SZ (number, optional): Scale factors

Response Schema:
{
  "type": "object",
  "properties": {
    "status": {"type": "string"},
    "message": {"type": "string"},
    "data": {"type": "object"}
  }
}
```

### **Action 5: ExecuteCode (Custom Python Code)**
```
Summary: Execute Code
Description: Execute custom Python code in Blender
Operation ID: ExecuteCode
Visibility: Important

Request:
  URL: /
  Method: POST
  Headers:
    Content-Type: application/json

Body Template:
{
  "command": "execute_code",
  "params": {
    "code": "{PythonCode}",
    "description": "{Description}"
  }
}

Parameters:
- PythonCode (string, required): Python code to execute
- Description (string, optional): Description of operation

Response Schema:
{
  "type": "object",
  "properties": {
    "status": {"type": "string"},
    "message": {"type": "string"},
    "data": {"type": "object"}
  }
}
```

## 🧪 **Testing & Validation**

### **Pre-Integration Tests**

#### **1. Local Server Test**
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/" -Method POST -Body '{"command": "health_check"}' -ContentType "application/json"
```
**Expected**: `{"status": "success", "message": "Simple Blender server is running!"}`

#### **2. Tunnel Test**
```powershell
Invoke-WebRequest -Uri "https://blender-open-mcp-de.com/" -Method POST -Body '{"command": "health_check"}' -ContentType "application/json" -UseBasicParsing
```
**Expected**: Same as local test

### **Copilot Studio Testing Steps**

#### **Step 1: Test Health Check**
In Copilot Studio's test pane:
```
Test Action: GetHealth
Expected Response: {"status": "success", "message": "Simple Blender server is running!"}
```

#### **Step 2: Test Scene Info**
```
Test Action: GetSceneInfo
Expected Response: Scene information with object count and names
```

#### **Step 3: Test Object Creation**
```
Test Action: CreateObject
Parameters:
- ObjectType: CUBE
- ObjectName: TestCube
- X: 0, Y: 0, Z: 0
```

## 🎯 **Advanced Integration**

### **Sample Copilot Studio Prompts**

Add these conversation topics to your Copilot:

```yaml
Topic: Basic Commands
Trigger phrases:
- "Check if Blender is running"
- "What's in my scene?"
- "Create a cube"
- "Make a sphere"

Actions:
- GetHealth() for "check running"
- GetSceneInfo() for "what's in scene"
- CreateObject(type="CUBE") for "create cube"
- CreateObject(type="SPHERE") for "make sphere"
```

### **Error Handling in Copilot Studio**

Add condition nodes to check API responses:
```yaml
If response.status = "success":
  - Show success message
  - Continue conversation
Else:
  - Show error: response.message
  - Offer retry option
```

## 🔧 **Troubleshooting**

### **Connection Issues**

#### **530 Errors (Tunnel Problems)**
```powershell
# Restart tunnel
taskkill /F /IM cloudflared.exe /T
.\cloudflared.exe tunnel --config tunnel-config.yml run
```

#### **501 Errors (Method Issues)**
- **Cause**: Using GET instead of POST
- **Fix**: Change all actions to POST method
- **Check**: Ensure Content-Type is application/json

### **Schema Validation Issues**

#### **String vs Object Response**
- **Problem**: Copilot expects string, gets object
- **Fix**: Set response schema type to "object"
- **Schema**: Include "status" and "message" properties

## 🚀 **Quick Start Checklist**

### **Before Copilot Studio Setup**
- [ ] Local server running on port 8000
- [ ] Blender running with MCP addon
- [ ] Cloudflare tunnel working
- [ ] Health check returns 200 status

### **Copilot Studio Configuration**
- [ ] Host URL set to https://blender-open-mcp-de.com
- [ ] All actions use POST method
- [ ] All actions target "/" endpoint
- [ ] Content-Type header set to application/json
- [ ] Response schemas set to "object" type

### **Testing Verification**
- [ ] Health check works
- [ ] Scene info returns data
- [ ] Object creation works in Blender
- [ ] Error handling displays proper messages

## 🎉 **Success Indicators**

You'll know the integration is working when:
- ✅ Health check shows `{"status": "success", "message": "Simple Blender server is running!"}`
- ✅ Scene info returns your Blender objects
- ✅ Object creation actually adds objects to Blender
- ✅ No 501 or 530 errors in logs
- ✅ Copilot Studio test console shows 200 responses

---

**🎯 Your BlenderMCP integration with Copilot Studio is now complete! Test each action and start building amazing AI-powered Blender automations!** 🚀 