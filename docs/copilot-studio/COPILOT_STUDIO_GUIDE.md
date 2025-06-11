# 🤖 **BlenderMCP & Copilot Studio - Complete Integration Guide**

> **One comprehensive guide for integrating your BlenderMCP server with Microsoft Copilot Studio**

## ✅ **Current System Status**

### **Working Components**
- **Local Server**: WORKING on http://localhost:8000/
- **Blender Connection**: AVAILABLE on port 9876
- **Cloudflare Tunnel**: WORKING at https://blender-open-mcp-de.com/
- **Tunnel ID**: ff98000b-7cf0-4883-9f44-4c868867c6d4

### **API Options**
**Option A - Single Endpoint (Legacy)**:
- **Health Check**: `POST /` with `{"command": "health_check"}` returns `{"status": "success", "message": "..."}`
- **Swagger File**: `config/swagger/blender-mcp-swagger2.yaml`

**Option B - REST Endpoints (Recommended)**:
- **Health Check**: `GET /api/v2/health` returns `{"status": "success", "message": "...", "timestamp": "..."}`
- **Swagger File**: `config/swagger/blender-mcp-separate-endpoints.yaml`

### **Server API Specification**

**Option A - Single Endpoint API (Legacy)**:
- **Endpoint**: POST /
- **Commands**: health_check, get_scene_info, create_object, modify_object, remove_object, apply_material, execute_code, ai_prompt
- **Request Format**: `{"command": "command_name", "params": {...}}`
- **Response Format**: `{"status": "success/error", "message": "...", "data": {...}}`

**Option B - REST Endpoints API (Recommended)**:
- **Health**: `GET /api/v2/health`
- **Scene**: `GET /api/v2/scene`  
- **Objects**: `POST /api/v2/objects`, `GET /api/v2/objects/{name}`, `PUT /api/v2/objects/{name}`, `DELETE /api/v2/objects/{name}`
- **Materials**: `POST /api/v2/objects/{name}/material`
- **Execute**: `POST /api/v2/execute`
- **AI**: `POST /api/v2/ai/prompt`

## 💬 **Prompt Examples for Copilot Studio**

### **🎨 Creative Design Prompts**

#### **Basic Object Creation**
```
User: "Create a red cube in the center of my scene"
Copilot Action: CreateObject
Parameters:
- type: "CUBE"
- name: "RedCube"
- location: [0, 0, 0]

Follow-up: ApplyMaterial
Parameters:
- object_name: "RedCube"
- material_type: "Principled"
- base_color: [0.8, 0.2, 0.2, 1.0]
```

#### **Complex Scene Building**
```
User: "Build me a simple house scene with walls, roof, and door"
Copilot Sequence:
1. CreateObject(type="CUBE", name="WallLeft", location=[-2, 0, 1], scale=[0.2, 4, 2])
2. CreateObject(type="CUBE", name="WallRight", location=[2, 0, 1], scale=[0.2, 4, 2])
3. CreateObject(type="CUBE", name="WallBack", location=[0, -2, 1], scale=[4, 0.2, 2])
4. CreateObject(type="CUBE", name="Roof", location=[0, 0, 2.5], scale=[2.5, 2.5, 0.2])
5. CreateObject(type="CUBE", name="Door", location=[0, 2, 0.5], scale=[0.8, 0.2, 1.5])
```

### **🔧 Technical Animation Prompts**

#### **Object Movement**
```
User: "Move the cube 2 units up and rotate it 45 degrees"
Copilot Action: ModifyObject
Parameters:
- object_name: "Cube"
- location: [0, 0, 2]
- rotation: [0, 0, 45]
```

#### **Batch Operations**
```
User: "Create 5 spheres in a line, each one larger than the last"
Copilot Sequence:
1. CreateObject(type="SPHERE", name="Sphere1", location=[-4, 0, 0], scale=[0.5, 0.5, 0.5])
2. CreateObject(type="SPHERE", name="Sphere2", location=[-2, 0, 0], scale=[0.75, 0.75, 0.75])
3. CreateObject(type="SPHERE", name="Sphere3", location=[0, 0, 0], scale=[1, 1, 1])
4. CreateObject(type="SPHERE", name="Sphere4", location=[2, 0, 0], scale=[1.25, 1.25, 1.25])
5. CreateObject(type="SPHERE", name="Sphere5", location=[4, 0, 0], scale=[1.5, 1.5, 1.5])
```

### **🎭 Material & Lighting Prompts**

#### **Material Application**
```
User: "Make the cube look like gold metal"
Copilot Action: ApplyMaterial
Parameters:
- object_name: "Cube"
- material_type: "Principled"
- base_color: [1.0, 0.8, 0.2, 1.0]
- metallic: 0.9
- roughness: 0.1
```

#### **Scene Lighting**
```
User: "Add dramatic lighting to my scene"
Copilot Action: ExecuteCode
Parameters:
- code: |
    import bpy
    # Add sun light
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    sun = bpy.context.object
    sun.data.energy = 3
    sun.rotation_euler = (0.785, 0, 0.785)
    
    # Add fill light
    bpy.ops.object.light_add(type='AREA', location=(-3, 2, 8))
    fill = bpy.context.object
    fill.data.energy = 1.5
- description: "Adding dramatic three-point lighting setup"
```

### **🤖 AI-Powered Creative Prompts**

#### **Natural Language Scene Description**
```
User: "Create a medieval castle scene with towers and walls"
Copilot Action: AI_Prompt
Parameters:
- prompt: "Generate a medieval castle with 4 corner towers, connecting walls, and a main keep. Use cubes and cylinders. Make towers 8 units tall, walls 4 units tall."
- model: "llama3.2"
```

#### **Style Transfer Requests**
```
User: "Make my scene look more sci-fi and futuristic"
Copilot Action: AI_Prompt
Parameters:
- prompt: "Transform current scene to sci-fi aesthetic: add blue/cyan materials, increase metallic properties, add emission shaders, create sleek angular shapes"
- model: "llama3.2"
```

### **📐 Procedural Generation Prompts**

#### **Geometric Patterns**
```
User: "Create a spiral pattern with 20 cubes"
Copilot Action: ExecuteCode
Parameters:
- code: |
    import bpy
    import math
    
    for i in range(20):
        angle = i * 0.5
        x = math.cos(angle) * (i * 0.5)
        y = math.sin(angle) * (i * 0.5)
        z = i * 0.2
        
        bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
        cube = bpy.context.object
        cube.name = f"SpiralCube_{i+1}"
        cube.scale = (0.3, 0.3, 0.3)
- description: "Creating spiral pattern with 20 cubes"
```

#### **Random Forest Generation**
```
User: "Generate a random forest with 15 trees of different heights"
Copilot Action: ExecuteCode  
Parameters:
- code: |
    import bpy
    import random
    
    for i in range(15):
        x = random.uniform(-10, 10)
        y = random.uniform(-8, 8)
        height = random.uniform(3, 8)
        
        # Tree trunk
        bpy.ops.mesh.primitive_cylinder_add(location=(x, y, height/2))
        trunk = bpy.context.object
        trunk.name = f"TreeTrunk_{i+1}"
        trunk.scale = (0.3, 0.3, height/2)
        
        # Tree top
        bpy.ops.mesh.primitive_uv_sphere_add(location=(x, y, height))
        top = bpy.context.object
        top.name = f"TreeTop_{i+1}"
        top.scale = (1.5, 1.5, 1.2)
- description: "Generating random forest with varied tree heights"
```

### **🎮 Interactive Conversation Templates**

#### **Guided Scene Building**
```yaml
Conversation Flow:
User: "I want to build a scene"
Copilot: "Great! What kind of scene would you like to create? I can help with:
• Architectural scenes (buildings, rooms, cities)
• Natural environments (forests, mountains, water)
• Abstract art (geometric patterns, sculptures)
• Character scenes (figures, animations)
• Product visualization (objects, materials)

What interests you?"

User Response Handler:
- If "architectural" → Ask for specific building type
- If "natural" → Ask for environment type
- If "abstract" → Ask for style preference
- If "character" → Ask for figure type
- If "product" → Ask for object type
```

#### **Troubleshooting Conversations**
```yaml
Error Handling:
User: "Something went wrong with my cube"
Copilot: "I'll help you troubleshoot! Let me check your scene first."

Action: GetSceneInfo()

Response Analysis:
- If no objects → "Your scene is empty. Would you like me to create a new cube?"
- If cube exists → "I found your cube. What specifically is wrong with it?"
- If error → "There seems to be a connection issue. Let me check if Blender is running."

Follow-up Actions:
- CreateObject if needed
- ModifyObject for fixes
- ExecuteCode for complex repairs
```

### **📊 Analytics & Reporting Prompts**

#### **Scene Statistics**
```
User: "Give me a report on my current scene"
Copilot Action: GetSceneInfo + ExecuteCode
Parameters:
- First get scene info
- Then execute analysis code:
  ```python
  import bpy
  
  objects = bpy.context.scene.objects
  mesh_count = len([o for o in objects if o.type == 'MESH'])
  light_count = len([o for o in objects if o.type == 'LIGHT'])
  camera_count = len([o for o in objects if o.type == 'CAMERA'])
  
  report = f"""
  Scene Analysis Report:
  - Total Objects: {len(objects)}
  - Mesh Objects: {mesh_count}
  - Lights: {light_count}
  - Cameras: {camera_count}
  - Active Object: {bpy.context.active_object.name if bpy.context.active_object else 'None'}
  """
  ```
```

### **🚀 Advanced Workflow Prompts**

#### **Animation Setup**
```
User: "Set up a simple rotation animation for my cube"
Copilot Action: ExecuteCode
Parameters:
- code: |
    import bpy
    
    # Get the cube
    cube = bpy.context.scene.objects.get('Cube')
    if cube:
        # Clear existing animation data
        cube.animation_data_clear()
        
        # Set keyframes for rotation
        cube.rotation_euler = (0, 0, 0)
        cube.keyframe_insert(data_path="rotation_euler", frame=1)
        
        cube.rotation_euler = (0, 0, 6.28319)  # 360 degrees in radians
        cube.keyframe_insert(data_path="rotation_euler", frame=120)
        
        # Set interpolation to linear
        for fcurve in cube.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'LINEAR'
    
    # Set frame range
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 120
- description: "Setting up 360-degree rotation animation over 120 frames"
```

#### **Render Setup**
```
User: "Prepare my scene for high-quality rendering"
Copilot Action: ExecuteCode
Parameters:
- code: |
    import bpy
    
    # Set render engine to Cycles
    bpy.context.scene.render.engine = 'CYCLES'
    
    # Set high quality settings
    bpy.context.scene.cycles.samples = 256
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    
    # Enable denoising
    bpy.context.scene.cycles.use_denoising = True
    
    # Set output format
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = '/tmp/render_'
- description: "Configuring scene for high-quality Cycles rendering"
```

### **💡 Best Practices for Prompt Design**

#### **Clear Intent Specification**
```
❌ Bad: "Make it look better"
✅ Good: "Increase the metallic property to 0.8 and decrease roughness to 0.2 for a chrome finish"

❌ Bad: "Add some lights"
✅ Good: "Add a sun light at position (5, 5, 10) with energy 3.0 for key lighting"
```

#### **Context Preservation**
```
✅ Reference previous actions: "Modify the red cube I just created"
✅ Use scene context: "Move all spheres up by 2 units"
✅ Chain operations: "After creating the cube, apply a blue material to it"
```

#### **Error Recovery Patterns**
```yaml
Error Handling Patterns:
1. Check Connection: GetHealth() → Verify Blender connection
2. Validate Object: GetSceneInfo() → Confirm object exists
3. Retry Logic: "If that didn't work, let me try a different approach"
4. User Feedback: "I encountered an issue. Could you check if Blender is running?"
```

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

---

## 📋 **Option B Configuration (REST Endpoints - Recommended)**

### **Action 1: REST Health Check**
```
Summary: Health Check (REST)
Description: Check if Blender REST server is running
Operation ID: GetHealthREST
Visibility: Important

Request:
  URL: /api/v2/health
  Method: GET
  Headers: (none required)

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
    },
    "timestamp": {
      "type": "string",
      "description": "Current server timestamp"
    }
  },
  "required": ["status", "message", "timestamp"]
}
```

### **Action 2: REST Get Scene Info**
```
Summary: Get Scene Info (REST)
Description: Get information about the current Blender scene
Operation ID: GetSceneInfoREST
Visibility: Important

Request:
  URL: /api/v2/scene
  Method: GET
  Headers: (none required)

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
      "type": "object",
      "properties": {
        "objects": {
          "type": "array",
          "items": {"type": "string"}
        },
        "active_object": {"type": "string"},
        "scene_name": {"type": "string"}
      }
    }
  }
}
```

### **Action 3: REST Create Object**
```
Summary: Create Object (REST)
Description: Create an object in Blender using REST API
Operation ID: CreateObjectREST
Visibility: Important

Request:
  URL: /api/v2/objects
  Method: POST
  Headers:
    Content-Type: application/json

Body Template:
{
  "type": "{ObjectType}",
  "name": "{ObjectName}",
  "location": ["{X}", "{Y}", "{Z}"],
  "rotation": ["{RX}", "{RY}", "{RZ}"],
  "scale": ["{SX}", "{SY}", "{SZ}"]
}

Parameters:
- ObjectType (string, required): CUBE, SPHERE, CYLINDER, PLANE, CONE, TORUS
- ObjectName (string, optional): Name for the object
- X, Y, Z (number, optional): Position coordinates
- RX, RY, RZ (number, optional): Rotation in degrees  
- SX, SY, SZ (number, optional): Scale factors

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
        },
        "rotation": {
          "type": "array",
          "items": {"type": "number"}
        },
        "scale": {
          "type": "array",
          "items": {"type": "number"}
        }
      }
    }
  }
}
```

### **Action 4: REST Get Object Info**
```
Summary: Get Object Info (REST)
Description: Get information about a specific object
Operation ID: GetObjectInfoREST
Visibility: Important

Request:
  URL: /api/v2/objects/{ObjectName}
  Method: GET
  Headers: (none required)

URL Parameters:
- ObjectName (string, required): Name of the object to query

Response Schema:
{
  "type": "object",
  "properties": {
    "status": {"type": "string"},
    "message": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "type": {"type": "string"},
        "location": {"type": "array", "items": {"type": "number"}},
        "rotation": {"type": "array", "items": {"type": "number"}},
        "scale": {"type": "array", "items": {"type": "number"}},
        "visible": {"type": "boolean"}
      }
    }
  }
}
```

### **Action 5: REST Modify Object**
```
Summary: Modify Object (REST)
Description: Modify properties of an existing object
Operation ID: ModifyObjectREST
Visibility: Important

Request:
  URL: /api/v2/objects/{ObjectName}
  Method: PUT
  Headers:
    Content-Type: application/json

URL Parameters:
- ObjectName (string, required): Name of object to modify

Body Template:
{
  "location": ["{X}", "{Y}", "{Z}"],
  "rotation": ["{RX}", "{RY}", "{RZ}"],
  "scale": ["{SX}", "{SY}", "{SZ}"],
  "visible": "{Visible}"
}

Parameters:
- X, Y, Z (number, optional): New position coordinates
- RX, RY, RZ (number, optional): Rotation in degrees
- SX, SY, SZ (number, optional): Scale factors
- Visible (boolean, optional): Object visibility

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
        "location": {"type": "array", "items": {"type": "number"}},
        "rotation": {"type": "array", "items": {"type": "number"}},
        "scale": {"type": "array", "items": {"type": "number"}}
      }
    }
  }
}
```

### **Action 6: REST Delete Object**
```
Summary: Delete Object (REST)
Description: Remove an object from the scene
Operation ID: DeleteObjectREST
Visibility: Important

Request:
  URL: /api/v2/objects/{ObjectName}
  Method: DELETE
  Headers: (none required)

URL Parameters:
- ObjectName (string, required): Name of object to delete

Response Schema:
{
  "type": "object",
  "properties": {
    "status": {"type": "string"},
    "message": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "deleted_object": {"type": "string"}
      }
    }
  }
}
```

### **Action 7: REST Apply Material**
```
Summary: Apply Material (REST)
Description: Apply material properties to an object
Operation ID: ApplyMaterialREST
Visibility: Important

Request:
  URL: /api/v2/objects/{ObjectName}/material
  Method: POST
  Headers:
    Content-Type: application/json

URL Parameters:
- ObjectName (string, required): Name of object to apply material to

Body Template:
{
  "material_name": "{MaterialName}",
  "material_type": "{MaterialType}",
  "base_color": ["{R}", "{G}", "{B}", "{A}"],
  "metallic": "{Metallic}",
  "roughness": "{Roughness}",
  "emission_strength": "{EmissionStrength}"
}

Parameters:
- MaterialName (string, optional): Name for the material
- MaterialType (string, optional): Type of material (Principled, Emission, etc.)
- R, G, B, A (number, optional): RGBA color values (0.0-1.0)
- Metallic (number, optional): Metallic property (0.0-1.0)
- Roughness (number, optional): Roughness property (0.0-1.0)
- EmissionStrength (number, optional): Emission strength for glowing materials

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
        "material_name": {"type": "string"},
        "material_properties": {"type": "object"}
      }
    }
  }
}
```

### **Action 8: REST Execute Code**
```
Summary: Execute Code (REST)
Description: Execute custom Python code in Blender
Operation ID: ExecuteCodeREST
Visibility: Important

Request:
  URL: /api/v2/execute
  Method: POST
  Headers:
    Content-Type: application/json

Body Template:
{
  "code": "{PythonCode}",
  "description": "{Description}"
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
    "data": {
      "type": "object",
      "properties": {
        "code_executed": {"type": "string"},
        "execution_result": {"type": "string"},
        "execution_time": {"type": "number"}
      }
    }
  }
}
```

### **Action 9: REST AI Prompt**
```
Summary: AI Prompt (REST)
Description: Send natural language commands to AI for Blender operations
Operation ID: AIPromptREST
Visibility: Important

Request:
  URL: /api/v2/ai/prompt
  Method: POST
  Headers:
    Content-Type: application/json

Body Template:
{
  "prompt": "{UserPrompt}",
  "model": "{AIModel}",
  "execute": "{ExecuteDirectly}"
}

Parameters:
- UserPrompt (string, required): Natural language command
- AIModel (string, optional): AI model to use (default: llama3.2)
- ExecuteDirectly (boolean, optional): Whether to execute the generated code immediately

Response Schema:
{
  "type": "object",
  "properties": {
    "status": {"type": "string"},
    "message": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "ai_response": {"type": "string"},
        "generated_code": {"type": "string"},
        "executed": {"type": "boolean"},
        "execution_result": {"type": "string"}
      }
    }
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