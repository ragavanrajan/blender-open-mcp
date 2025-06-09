# 🤖 Copilot Studio Integration Guide

## Overview
This guide shows how to integrate your Azure-deployed BlenderMCP server with Microsoft Copilot Studio to create AI-powered Blender automation chatbots.

## 🌐 Your API Endpoints

**Base URL:** `https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net`

### Available Endpoints

| Method | Endpoint | Description | Use Case |
|--------|----------|-------------|----------|
| GET | `/health` | Health check | System monitoring |
| GET | `/api/blender/scene` | Get scene info | Scene analysis |
| POST | `/api/blender/create` | Create objects | Object creation |
| PUT | `/api/blender/modify` | Modify objects | Object editing |
| DELETE | `/api/blender/delete/{name}` | Delete objects | Object removal |
| POST | `/api/blender/material` | Apply materials | Material assignment |
| POST | `/api/blender/code` | Execute Python code | Custom operations |
| POST | `/api/ai/prompt` | AI-powered operations | Natural language |

## 🛠️ Copilot Studio Setup

### Step 1: Create a New Copilot
1. Go to [Copilot Studio](https://copilotstudio.microsoft.com)
2. Click **"Create"** → **"New copilot"**
3. Name it "Blender Assistant" or similar
4. Choose your preferred language and publish settings

### Step 2: Add Custom Actions

#### Action 1: Get Scene Information
```yaml
Name: GetBlenderScene
Description: Get current Blender scene information
Method: GET
URL: https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/api/blender/scene
Headers:
  Content-Type: application/json
```

#### Action 2: Create Objects
```yaml
Name: CreateBlenderObject
Description: Create objects in Blender
Method: POST
URL: https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/api/blender/create
Headers:
  Content-Type: application/json
Body:
{
  "type": "{ObjectType}",
  "name": "{ObjectName}",
  "location": [0, 0, 0],
  "rotation": [0, 0, 0],
  "scale": [1, 1, 1]
}
```

#### Action 3: Modify Objects
```yaml
Name: ModifyBlenderObject
Description: Modify objects in Blender
Method: PUT
URL: https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/api/blender/modify
Headers:
  Content-Type: application/json
Body:
{
  "name": "{ObjectName}",
  "location": ["{X}", "{Y}", "{Z}"],
  "rotation": ["{RX}", "{RY}", "{RZ}"],
  "scale": ["{SX}", "{SY}", "{SZ}"]
}
```

#### Action 4: Delete Objects
```yaml
Name: DeleteBlenderObject
Description: Delete objects from Blender
Method: DELETE
URL: https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/api/blender/delete/{ObjectName}
Headers:
  Content-Type: application/json
```

#### Action 5: Apply Materials
```yaml
Name: ApplyBlenderMaterial
Description: Apply materials to Blender objects
Method: POST
URL: https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/api/blender/material
Headers:
  Content-Type: application/json
Body:
{
  "object_name": "{ObjectName}",
  "material_name": "{MaterialName}",
  "color": ["{R}", "{G}", "{B}"]
}
```

#### Action 6: Execute Custom Code
```yaml
Name: ExecuteBlenderCode
Description: Execute Python code in Blender
Method: POST
URL: https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/api/blender/code
Headers:
  Content-Type: application/json
Body:
{
  "command": "{PythonCode}",
  "description": "{Description}"
}
```

### Step 3: Create Topics and Conversations

#### Topic: Create Objects
```
Trigger phrases:
- "Create a cube"
- "Add a sphere"
- "Make a cylinder"
- "Create {ObjectType}"

Conversation flow:
1. Extract object type from user input
2. Call CreateBlenderObject action
3. Respond with success/error message
```

#### Topic: Move Objects
```
Trigger phrases:
- "Move {object} to {location}"
- "Position {object} at {coordinates}"
- "Relocate {object}"

Conversation flow:
1. Extract object name and coordinates
2. Call ModifyBlenderObject action
3. Confirm the operation
```

#### Topic: Apply Materials
```
Trigger phrases:
- "Make {object} {color}"
- "Apply {material} to {object}"
- "Color {object} {color}"

Conversation flow:
1. Extract object name and material/color
2. Call ApplyBlenderMaterial action
3. Confirm material application
```

## 💬 Example Conversations

### Creating Objects
**User:** "Create a blue cube at position 2, 0, 1"
**Copilot:** 
1. Calls CreateBlenderObject with type="CUBE", location=[2,0,1]
2. Calls ApplyBlenderMaterial with color=[0,0,1] (blue)
3. Responds: "I've created a blue cube at position (2, 0, 1) in your Blender scene!"

### Scene Analysis
**User:** "What's in my scene?"
**Copilot:**
1. Calls GetBlenderScene
2. Analyzes the returned data
3. Responds: "Your scene contains: 3 cubes, 1 sphere, and 2 lights. The active object is 'Cube.001'."

### Complex Operations
**User:** "Create a ring of 8 cubes around the origin"
**Copilot:**
1. Uses ExecuteBlenderCode to run a Python script
2. Responds with the results of the operation

## 🔧 Advanced Integration

### Variables to Set Up in Copilot Studio

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `ObjectType` | Choice | Object types | CUBE, SPHERE, CYLINDER, PLANE |
| `MaterialName` | Text | Material names | Metal, Glass, Plastic |
| `ColorValue` | Text | Color descriptions | red, blue, green |
| `Position` | Text | 3D coordinates | "2,0,1" |

### Error Handling

Add condition nodes to check API responses:
```
If API response.success = true:
  - Show success message
  - Continue conversation
Else:
  - Show error message: API response.message
  - Offer to try again
```

## 🎯 Sample Use Cases

1. **Architectural Design Assistant**
   - "Create a house foundation"
   - "Add windows to the walls"
   - "Apply brick texture to the building"

2. **Product Design Helper**
   - "Design a phone case"
   - "Make it transparent plastic"
   - "Add a logo on the back"

3. **Animation Setup**
   - "Create a character rig"
   - "Set up a camera path"
   - "Add lighting for dramatic effect"

## 🚨 Important Notes

### Prerequisites
1. **Blender must be running** with the BlenderMCP addon installed
2. **Blender must be accessible** to your Azure server (same network/VPN)
3. **MCP components must be available** (check /health endpoint)

### Authentication
- Current setup has no authentication
- Consider adding API keys for production use
- Monitor usage through Azure App Service logs

### Rate Limiting
- Azure may impose rate limits
- Consider implementing request queuing for heavy operations
- Monitor server response times

## 🔍 Testing Your Integration

### Quick Tests
1. Visit your server: `https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net`
2. Check health: `https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/health`
3. View API docs: `https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/docs`

### Test API Calls
Use tools like Postman or curl to test:
```bash
# Test scene info
curl -X GET "https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/api/blender/scene"

# Test object creation
curl -X POST "https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net/api/blender/create" \
  -H "Content-Type: application/json" \
  -d '{"type": "CUBE", "name": "TestCube", "location": [1, 2, 3]}'
```

## 🎉 Next Steps

1. **Deploy the updated server** (already done!)
2. **Set up Copilot Studio** following the steps above
3. **Configure your Blender addon** to connect to the server
4. **Test the integration** with simple commands
5. **Expand with more complex operations** as needed

Your BlenderMCP server is now ready for Copilot Studio integration! 🚀 