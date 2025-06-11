# 🔄 **BlenderMCP API Comparison - Single vs Separate Endpoints**

## 📋 **Overview**

You now have **two different API approaches** for your BlenderMCP server:

1. **Single Endpoint Approach** (Current) - One POST endpoint with command types
2. **Separate Endpoints Approach** (New) - Dedicated REST endpoints for each operation

---

## 🎯 **Single Endpoint Approach (Current)**

### **Files:**
- `blender-mcp-swagger2.yaml` 
- `src/blender_open_mcp/simple_server.py`

### **Characteristics:**
- **URL**: `https://blender-open-mcp-de.com/`
- **Method**: `POST` only
- **All operations** go through the same endpoint
- **Command-based** with JSON body containing `{"command": "...", "params": {...}}`

### **Example Requests:**

```bash
# Health Check
curl -X POST https://blender-open-mcp-de.com/ \
  -H "Content-Type: application/json" \
  -d '{"command": "health_check"}'

# Create Object
curl -X POST https://blender-open-mcp-de.com/ \
  -H "Content-Type: application/json" \
  -d '{"command": "create_object", "params": {"type": "CUBE", "name": "MyCube"}}'

# Get Scene Info
curl -X POST https://blender-open-mcp-de.com/ \
  -H "Content-Type: application/json" \
  -d '{"command": "get_scene_info"}'
```

### **Pros:**
✅ **Already working** with your current Copilot Studio setup  
✅ **Simple tunnel configuration** - only one endpoint to expose  
✅ **Single operation** to configure in Copilot Studio  
✅ **Consistent method** (POST) for all operations  

### **Cons:**
❌ **Not RESTful** - doesn't follow REST principles  
❌ **Hard to cache** - all requests look the same to proxies  
❌ **Poor discoverability** - endpoints not self-documenting  
❌ **Copilot Studio confusion** - might try to call non-existent operations  

---

## 🌟 **Separate Endpoints Approach (New)**

### **Files:**
- `blender-mcp-separate-endpoints.yaml` 
- `src/blender_open_mcp/rest_server.py`

### **Characteristics:**
- **Base URL**: `https://blender-open-mcp-de.com/api/v2/`
- **RESTful methods**: `GET`, `POST`, `PUT`, `DELETE`
- **Dedicated endpoints** for each operation
- **Resource-based** URLs following REST conventions

### **Example Requests:**

```bash
# Health Check
curl -X GET https://blender-open-mcp-de.com/api/v2/health

# Create Object
curl -X POST https://blender-open-mcp-de.com/api/v2/objects \
  -H "Content-Type: application/json" \
  -d '{"type": "CUBE", "name": "MyCube"}'

# Get Scene Info
curl -X GET https://blender-open-mcp-de.com/api/v2/scene

# Get Object Info
curl -X GET https://blender-open-mcp-de.com/api/v2/objects/MyCube

# Modify Object
curl -X PUT https://blender-open-mcp-de.com/api/v2/objects/MyCube \
  -H "Content-Type: application/json" \
  -d '{"location": [2.0, 0.0, 1.0]}'

# Delete Object
curl -X DELETE https://blender-open-mcp-de.com/api/v2/objects/MyCube

# Apply Material
curl -X POST https://blender-open-mcp-de.com/api/v2/objects/MyCube/material \
  -H "Content-Type: application/json" \
  -d '{"material_name": "Gold", "color": [1.0, 0.8, 0.0]}'
```

### **Pros:**
✅ **RESTful design** - follows HTTP and REST best practices  
✅ **Better caching** - GET requests can be cached properly  
✅ **Self-documenting** - URLs clearly indicate what they do  
✅ **Easier testing** - can test individual endpoints separately  
✅ **Better error handling** - specific HTTP status codes  
✅ **More intuitive** for developers familiar with REST APIs  

### **Cons:**
❌ **Requires tunnel update** - need to expose `/api/v2/*` paths  
❌ **More complex** Copilot Studio configuration  
❌ **Multiple operations** to set up in Copilot Studio  
❌ **Mixed HTTP methods** - Copilot Studio might not handle all methods  

---

## 🚀 **Endpoint Comparison Table**

| Operation | Single Endpoint | Separate Endpoints |
|-----------|----------------|-------------------|
| Health Check | `POST /` + `{"command": "health_check"}` | `GET /api/v2/health` |
| Scene Info | `POST /` + `{"command": "get_scene_info"}` | `GET /api/v2/scene` |
| Create Object | `POST /` + `{"command": "create_object", "params": {...}}` | `POST /api/v2/objects` |
| Get Object | `POST /` + `{"command": "get_object_info", "params": {...}}` | `GET /api/v2/objects/{name}` |
| Modify Object | `POST /` + `{"command": "modify_object", "params": {...}}` | `PUT /api/v2/objects/{name}` |
| Remove Object | `POST /` + `{"command": "remove_object", "params": {...}}` | `DELETE /api/v2/objects/{name}` |
| Apply Material | `POST /` + `{"command": "apply_material", "params": {...}}` | `POST /api/v2/objects/{name}/material` |
| Execute Code | `POST /` + `{"command": "execute_code", "params": {...}}` | `POST /api/v2/execute` |
| AI Prompt | `POST /` + `{"command": "ai_prompt", "params": {...}}` | `POST /api/v2/ai/prompt` |

---

## 🛠️ **How to Switch to Separate Endpoints**

### **1. Update Tunnel Configuration**
Update your `tunnel-config.yml` to expose both approaches:

```yaml
tunnel: ff98000b-7cf0-4883-9f44-4c868867c6d4
credentials-file: C:\Users\ragavan.rajan\.cloudflared\ff98000b-7cf0-4883-9f44-4c868867c6d4.json

ingress:
  - hostname: blender-open-mcp-de.com
    path: /api/v2
    service: http://localhost:8000
  - hostname: blender-open-mcp-de.com
    service: http://localhost:8000
  - service: http_status:404
```

### **2. Start the REST Server**
```bash
# Start the new REST server on port 8000 (same as current server)
python -c "import sys; sys.path.insert(0, 'src'); from blender_open_mcp.rest_server import run_rest_server; run_rest_server('0.0.0.0', 8000)"
```

### **3. Update Copilot Studio**
- **Base URL**: `https://blender-open-mcp-de.com/api/v2`
- **Import the new swagger**: `blender-mcp-separate-endpoints.yaml`
- **Configure each operation** separately in your custom connector

---

## 💡 **Recommendation**

### **For Current Use (Immediate):**
**Stick with the Single Endpoint approach** since it's already working and configured.

### **For Future Development:**
**Consider migrating to Separate Endpoints** because:
- More maintainable and scalable
- Better for API documentation and testing
- Easier for other developers to understand
- Follows industry standards

### **Migration Strategy:**
1. **Test the REST server** locally first
2. **Update tunnel configuration** to support both approaches
3. **Create new Copilot Studio connector** with separate endpoints
4. **Gradually migrate** operations one by one
5. **Deprecate** the single endpoint approach when ready

---

## 📁 **File Summary**

### **Current (Single Endpoint):**
- `blender-mcp-swagger2.yaml` - Current swagger definition
- `src/blender_open_mcp/simple_server.py` - Current server (port 8000)

### **New (Separate Endpoints):**
- `blender-mcp-separate-endpoints.yaml` - REST swagger definition  
- `src/blender_open_mcp/rest_server.py` - REST server (port 8000)

Both approaches can run simultaneously if needed! 🎉 