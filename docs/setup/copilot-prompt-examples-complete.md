# Blender MCP - Copilot Studio Prompt Examples

Transform your creative workflow with AI-powered Blender automation! This comprehensive guide provides inspiring prompt examples that showcase the full potential of your Blender MCP integration through Microsoft Copilot Studio.

## 🚀 Quick Start

**Your Blender MCP API is available at:** `https://blender-open-mcp-de.com`

Simply use these prompts in your Copilot Studio agent, and watch as AI creates stunning 3D content automatically!

---

## 📚 REST API Endpoint Prompts

This section provides a complete reference for all available REST API v2 endpoints, along with specific prompt examples for each one.

### 1. Health Check

- **Endpoint:** `GET /api/v2/health`
- **Description:** Checks if the Blender MCP server is running and accessible.
- **Prompt Example:**
  ```
  "Check the server status"
  ```
  or
  ```
  "Is the Blender server online?"
  ```

### 2. Get Scene Information

- **Endpoint:** `GET /api/v2/scene`
- **Description:** Retrieves a summary of the current Blender scene, including a list of all objects, materials, cameras, and lights.
- **Prompt Example:**
  ```
  "What's in the current scene?"
  ```
  or
  ```
  "Give me a list of all objects in the scene."
  ```

### 3. Create Object

- **Endpoint:** `POST /api/v2/objects`
- **Description:** Creates a new 3D object. Requires the object `type` and accepts optional parameters for `name`, `location`, `rotation`, and `scale`.
- **Prompt Examples:**
  - **Simple:**
    ```
    "Create a CUBE"
    ```
  - **Named:**
    ```
    "Create a SPHERE named 'MyPlanet'"
    ```
  - **With transform:**
    ```
    "Create a CYLINDER named 'Pillar' at location 1,2,3 with a scale of 1,1,5"
    ```

### 4. Get Object Information

- **Endpoint:** `GET /api/v2/objects/{objectName}`
- **Description:** Retrieves detailed information about a specific object by its name.
- **Prompt Example:**
  ```
  "Get info for the object named 'MyPlanet'"
  ```
  or
  ```
  "Show me the details of 'Pillar'"
  ```

### 5. Modify Object

- **Endpoint:** `PUT /api/v2/objects/{objectName}`
- **Description:** Modifies the properties of an existing object, such as its location, rotation, or scale.
- **Prompt Examples:**
  - **Move:**
    ```
    "Move 'MyPlanet' to 5,5,5"
    ```
  - **Rotate:**
    ```
    "Rotate 'Pillar' by 90 degrees on the Z axis"
    ```
  - **Scale:**
    ```
    "Scale 'MyPlanet' to double its size"
    ```

### 6. Delete Object

- **Endpoint:** `DELETE /api/v2/objects/{objectName}`
- **Description:** Removes an object from the scene.
- **Prompt Example:**
  ```
  "Delete the object named 'Pillar'"
  ```
  or
  ```
  "Remove 'MyPlanet' from the scene"
  ```

### 7. Apply Material

- **Endpoint:** `POST /api/v2/objects/{objectName}/material`
- **Description:** Applies a material to an object. You can specify a material name and properties like its color.
- **Prompt Example:**
  ```
  "Apply a new material to 'MyPlanet' with a blue color"
  ```
  or
  ```
  "Make the 'Pillar' object red"
  ```

### 8. Execute Python Code

- **Endpoint:** `POST /api/v2/execute`
- **Description:** Executes a raw Python script within Blender. This allows for complex operations not covered by other endpoints.
- **Prompt Example:**
  ```
  "Execute a script to add 10 random cubes to the scene"
  ```
  or
  ```
  "Run Python code to set up a camera pointing at the origin"
  ```

### 9. AI Assistant Prompt

- **Endpoint:** `POST /api/v2/ai/prompt`
- **Description:** Sends a natural language prompt to the AI assistant, which will interpret the command and execute the necessary actions in Blender.
- **Prompt Example:**
  ```
  "Create a snowman"
  ```
  or
  ```
  "Build a simple car model using basic shapes"
  ```
---

## 🚨 **CRITICAL: Copilot Studio Connector Issues**

### **Missing Input Fields Problem**
If your Copilot Studio connector only shows the `type` field and is missing `name`, `location`, `rotation`, and `scale` fields:

**🔧 Solution Steps:**
1. **Delete the existing connector** in Copilot Studio
2. **Re-import the connector** using the same Swagger URL: `https://blender-open-mcp-de.com/config/swagger/blender-mcp-separate-endpoints.yaml`
3. **Verify all fields appear**: You should see 5 input fields total
4. **Test the connection** before using in prompts

**📋 Expected Input Fields:**
- `type` (String, Required) - Object type: CUBE, SPHERE, etc.
- `name` (String, Optional) - Custom object name
- `location` (String, Optional) - Position as "X,Y,Z" (e.g., "1,2,3")
- `rotation` (String, Optional) - Rotation as "RX,RY,RZ" (e.g., "0,0,1.57")
- `scale` (String, Optional) - Scale as "SX,SY,SZ" (e.g., "2,1,1")

**⚠️ Important Notes:**
- Use **comma-separated strings** for coordinates (not arrays)
- Object types must be **UPPERCASE** (CUBE, not cube)
- Empty fields will use Blender defaults

---

## ⚠️ **Quick Reference - Object Types**

**Valid Object Types (MUST be UPPERCASE):**
- `CUBE` - Standard cube mesh
- `SPHERE` - UV sphere mesh  
- `CYLINDER` - Cylinder mesh
- `PLANE` - Flat plane mesh
- `CONE` - Cone mesh
- `TORUS` - Torus (donut) mesh
- `MONKEY` - Suzanne (Blender mascot) mesh

---

## 📋 Table of Contents

1. [Basic Object Creation](#-basic-object-creation)
2. [Scene Building Examples](#-scene-building-examples)
3. [Creative & Artistic Examples](#-creative--artistic-examples)
4. [Architectural & Technical Examples](#-architectural--technical-examples)
5. [Game & Entertainment Scenes](#-game--entertainment-scenes)
6. [Scientific & Educational Examples](#-scientific--educational-examples)
7. [Commercial & Retail Examples](#-commercial--retail-examples)
8. [Common Errors & Solutions](#-common-errors--solutions)
9. [Pro Tips](#-pro-tips-for-better-results)

---

## 🎯 **Basic Object Creation**

### Simple Object Creation
```
"Create a CUBE named 'MyFirstCube'"
```

### Object with Position
```
"Create a SPHERE at position 2,0,3 and name it 'FloatingSphere'"
```

### Object with Full Transform
```
"Create a CYLINDER named 'TallPipe' at position 0,0,1 with rotation 0,0,1.57 and scale 1,1,3"
```

### Multiple Objects
```
"Create three objects: a CUBE at 0,0,0, a SPHERE at 2,0,0, and a CONE at 4,0,0"
```

---

## 🏗️ **Scene Building Examples**

### Simple Room Layout
```
"Build a simple room with these objects:
- Create a PLANE named 'Floor' at position 0,0,0 with scale 10,10,1
- Create a CUBE named 'WallNorth' at position 0,5,2 with scale 10,0.2,4
- Create a CUBE named 'WallSouth' at position 0,-5,2 with scale 10,0.2,4
- Create a CUBE named 'WallEast' at position 5,0,2 with scale 0.2,10,4
- Create a CUBE named 'WallWest' at position -5,0,2 with scale 0.2,10,4"
```

### Furniture Setup
```
"Create a living room scene:
- Create a CUBE named 'Table' at position 0,0,0.4 with scale 2,1,0.1
- Create a CUBE named 'Chair1' at position 0,1.5,0.5 with scale 0.5,0.5,1
- Create a CUBE named 'Chair2' at position 0,-1.5,0.5 with scale 0.5,0.5,1
- Create a CYLINDER named 'Lamp' at position 2,2,1.5 with scale 0.2,0.2,2"
```

### Garden Scene
```
"Create a garden layout:
- Create a PLANE named 'Ground' with scale 15,15,1
- Create a CYLINDER named 'Tree1' at position 3,3,1 with scale 0.5,0.5,2
- Create a SPHERE named 'TreeTop1' at position 3,3,2.5 with scale 1.5,1.5,1.5
- Create a CYLINDER named 'Tree2' at position -4,2,1 with scale 0.4,0.4,1.8
- Create a SPHERE named 'TreeTop2' at position -4,2,2.3 with scale 1.2,1.2,1.2
- Create a CUBE named 'Bench' at position 0,0,0.3 with scale 2,0.4,0.6"
```

---

## 🎨 **Creative & Artistic Examples**

### Abstract Sculpture
```
"Create an abstract sculpture:
- Create a TORUS named 'Ring1' at position 0,0,2 with rotation 1.57,0,0
- Create a SPHERE named 'Core' at position 0,0,2 with scale 0.8,0.8,0.8
- Create a CYLINDER named 'Pillar' at position 0,0,1 with scale 0.3,0.3,2
- Create a CONE named 'Top' at position 0,0,3.5 with scale 0.6,0.6,1"
```

### Geometric Pattern
```
"Create a geometric pattern with 5 spheres in a circle:
- Create a SPHERE named 'Center' at position 0,0,0
- Create a SPHERE named 'Point1' at position 2,0,0 with scale 0.8,0.8,0.8
- Create a SPHERE named 'Point2' at position 1.2,1.6,0 with scale 0.8,0.8,0.8
- Create a SPHERE named 'Point3' at position -1.2,1.6,0 with scale 0.8,0.8,0.8
- Create a SPHERE named 'Point4' at position -2,0,0 with scale 0.8,0.8,0.8
- Create a SPHERE named 'Point5' at position 0,-2,0 with scale 0.8,0.8,0.8"
```

### Spiral Tower
```
"Create a spiral tower:
- Create a CUBE named 'Base' at position 0,0,0.5 with scale 3,3,1
- Create a CYLINDER named 'Level1' at position 0,0,1.5 with scale 1,1,1
- Create a CYLINDER named 'Level2' at position 0.5,0,2.5 with scale 0.8,0.8,1
- Create a CYLINDER named 'Level3' at position 0,0.5,3.5 with scale 0.6,0.6,1
- Create a CONE named 'Spire' at position 0,0,4.8 with scale 0.4,0.4,1.5"
```

---

## 🏭 **Architectural & Technical Examples**

### Bridge Structure
```
"Build a simple bridge:
- Create a CUBE named 'Support1' at position -3,0,1 with scale 0.5,0.5,2
- Create a CUBE named 'Support2' at position 3,0,1 with scale 0.5,0.5,2
- Create a CUBE named 'Deck' at position 0,0,2.2 with scale 7,2,0.2
- Create a CUBE named 'Railing1' at position 0,1,2.8 with scale 7,0.1,0.6
- Create a CUBE named 'Railing2' at position 0,-1,2.8 with scale 7,0.1,0.6"
```

### Industrial Layout
```
"Create an industrial facility:
- Create a CUBE named 'MainBuilding' at position 0,0,3 with scale 8,6,6
- Create a CYLINDER named 'Smokestack' at position 3,2,6 with scale 0.8,0.8,4
- Create a CUBE named 'Warehouse' at position -6,0,2 with scale 4,8,4
- Create a CYLINDER named 'Tank1' at position 6,3,1.5 with scale 1.5,1.5,3
- Create a CYLINDER named 'Tank2' at position 6,-3,1.5 with scale 1.5,1.5,3"
```

### Playground Design
```
"Design a playground:
- Create a PLANE named 'PlayArea' with scale 12,12,1
- Create a CYLINDER named 'Slide' at position 3,3,1 with scale 1,1,2 and rotation 0.5,0,0
- Create a CUBE named 'SwingSet' at position -3,3,1.5 with scale 3,0.3,3
- Create a SPHERE named 'ClimbingDome' at position 0,0,1 with scale 2,2,1
- Create a CUBE named 'Sandbox' at position -3,-3,0.2 with scale 2,2,0.4"
```

---

## 🎮 **Game & Entertainment Scenes**

### Medieval Castle
```
"Build a medieval castle:
- Create a CUBE named 'KeepBase' at position 0,0,2 with scale 4,4,4
- Create a CYLINDER named 'Tower1' at position 2,2,3 with scale 1,1,4
- Create a CYLINDER named 'Tower2' at position -2,2,3 with scale 1,1,4
- Create a CYLINDER named 'Tower3' at position 2,-2,3 with scale 1,1,4
- Create a CYLINDER named 'Tower4' at position -2,-2,3 with scale 1,1,4
- Create a CUBE named 'Gate' at position 0,2.5,1 with scale 1.5,0.5,2"
```

### Space Station
```
"Create a space station:
- Create a TORUS named 'MainRing' at position 0,0,0 with scale 5,5,1
- Create a CYLINDER named 'CentralHub' at position 0,0,0 with scale 1,1,3
- Create a CYLINDER named 'DockingPort1' at position 0,6,0 with scale 0.5,0.5,2
- Create a CYLINDER named 'DockingPort2' at position 0,-6,0 with scale 0.5,0.5,2
- Create a SPHERE named 'CommArray' at position 0,0,2 with scale 0.8,0.8,0.8"
```

### Racing Track
```
"Design a racing track:
- Create a TORUS named 'Track' at position 0,0,0 with scale 8,8,0.2
- Create a CUBE named 'StartLine' at position 8,0,0.1 with scale 0.2,2,0.1
- Create a CYLINDER named 'Pylon1' at position 6,6,0.5 with scale 0.2,0.2,1
- Create a CYLINDER named 'Pylon2' at position -6,6,0.5 with scale 0.2,0.2,1
- Create a CYLINDER named 'Pylon3' at position -6,-6,0.5 with scale 0.2,0.2,1
- Create a CUBE named 'Grandstand' at position 12,0,2 with scale 2,8,4"
```

---

## 🔬 **Scientific & Educational Examples**

### Solar System Model
```
"Create a solar system model:
- Create a SPHERE named 'Sun' at position 0,0,0 with scale 2,2,2
- Create a SPHERE named 'Mercury' at position 3,0,0 with scale 0.2,0.2,0.2
- Create a SPHERE named 'Venus' at position 4,0,0 with scale 0.3,0.3,0.3
- Create a SPHERE named 'Earth' at position 5,0,0 with scale 0.4,0.4,0.4
- Create a SPHERE named 'Mars' at position 6,0,0 with scale 0.3,0.3,0.3
- Create a SPHERE named 'Jupiter' at position 8,0,0 with scale 1,1,1"
```

### Molecular Structure
```
"Create a water molecule model:
- Create a SPHERE named 'Oxygen' at position 0,0,0 with scale 1,1,1
- Create a SPHERE named 'Hydrogen1' at position 1.5,1,0 with scale 0.5,0.5,0.5
- Create a SPHERE named 'Hydrogen2' at position 1.5,-1,0 with scale 0.5,0.5,0.5
- Create a CYLINDER named 'Bond1' at position 0.75,0.5,0 with scale 0.1,0.1,1 and rotation 0,0,0.5
- Create a CYLINDER named 'Bond2' at position 0.75,-0.5,0 with scale 0.1,0.1,1 and rotation 0,0,-0.5"
```

### Geometric Demonstration
```
"Create geometric shapes for math education:
- Create a CUBE named 'Cube_Example' at position -3,0,0.5
- Create a SPHERE named 'Sphere_Example' at position -1,0,0.5
- Create a CYLINDER named 'Cylinder_Example' at position 1,0,0.5
- Create a CONE named 'Cone_Example' at position 3,0,0.5
- Create a PLANE named 'Reference_Grid' with scale 8,8,1"
```

---

## 🏪 **Commercial & Retail Examples**

### Store Layout
```
"Design a retail store:
- Create a PLANE named 'FloorSpace' with scale 15,10,1
- Create a CUBE named 'Checkout' at position 6,4,0.8 with scale 2,1,1.6
- Create a CUBE named 'Shelf1' at position -5,0,1 with scale 1,8,2
- Create a CUBE named 'Shelf2' at position -3,0,1 with scale 1,8,2
- Create a CUBE named 'Shelf3' at position -1,0,1 with scale 1,8,2
- Create a CUBE named 'Display' at position 2,0,0.5 with scale 3,3,1"
```

### Restaurant Layout
```
"Create a restaurant floor plan:
- Create a PLANE named 'DiningArea' with scale 12,8,1
- Create a CUBE named 'Table1' at position 2,2,0.4 with scale 1.5,1.5,0.1
- Create a CUBE named 'Table2' at position 2,-2,0.4 with scale 1.5,1.5,0.1
- Create a CUBE named 'Table3' at position -2,2,0.4 with scale 1.5,1.5,0.1
- Create a CUBE named 'Table4' at position -2,-2,0.4 with scale 1.5,1.5,0.1
- Create a CUBE named 'Kitchen' at position -5,0,1 with scale 2,6,2"
```

---

## 🚨 **Common Errors & Solutions**

### Error 1: "Invalid object type"
**Problem:** Using lowercase object types  
**Solution:** Always use uppercase: `CUBE`, `SPHERE`, `CYLINDER`, `PLANE`, `CONE`, `TORUS`, `MONKEY`

**Wrong:**
```
"Create a cube named 'test'"
```

**Correct:**
```
"Create a CUBE named 'test'"
```

### Error 2: "Connection refused" or "502 Bad Gateway"
**Problem:** Server not running or tunnel disconnected  
**Solution:** Check server status with health check prompt:
```
"Check if my Blender MCP server is running properly and show me the connection status."
```

### Error 3: Objects not appearing as expected
**Problem:** Incorrect coordinate system understanding  
**Solution:** Use specific coordinates and test with simple positions first:
```
"Create a CUBE at position 0,0,0 to test the coordinate system"
```

### Error 4: Coordinate format errors
**Problem:** Using wrong format for coordinates  
**Solution:** Use comma-separated strings without spaces:

**Wrong:**
```
"Create a CUBE at position [1, 2, 3]"
"Create a CUBE at position 1 2 3"
```

**Correct:**
```
"Create a CUBE at position 1,2,3"
```

---

## 💡 **Pro Tips for Better Results**

### 1. **Start Simple**
Begin with basic objects before creating complex scenes:
```
"Create a CUBE named 'TestCube' to verify the connection"
```

### 2. **Use Descriptive Names**
Give objects meaningful names for easier management:
```
"Create a CYLINDER named 'MainPillar' instead of just 'Cylinder'"
```

### 3. **Plan Your Coordinates**
Think about object placement in 3D space:
- X-axis: Left (-) to Right (+)
- Y-axis: Back (-) to Front (+)  
- Z-axis: Down (-) to Up (+)

### 4. **Build Incrementally**
Create scenes step by step rather than all at once:
```
"First create the floor, then add walls, then furniture"
```

### 5. **Use Reference Objects**
Create a reference grid or marker objects:
```
"Create a PLANE named 'Grid' with scale 10,10,1 as a reference"
```

---

## 📞 **Support & Community**

**Need Help?** 
- Check the [Troubleshooting Guide](../troubleshooting/)
- Review the [API Documentation](../api/)
- Test your connection with: `"Check if my Blender server is running"`

**Share Your Creations!**
We'd love to see what you create with these prompts. Share your results and inspire others!

---

*Happy Creating! 🎨✨*

> **Note:** All prompts are designed to work with your Blender MCP REST API at `https://blender-open-mcp-de.com`. Make sure your server is running before trying these examples. 