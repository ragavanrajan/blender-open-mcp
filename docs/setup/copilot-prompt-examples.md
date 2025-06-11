# 🎨 Copilot Studio Prompt Examples for Blender MCP

Transform your creative workflow with AI-powered Blender automation! This guide provides inspiring prompt examples that showcase the full potential of your Blender MCP integration through Microsoft Copilot Studio.

## 🚀 Quick Start

**Your Blender MCP API is available at:** `https://blender-open-mcp-de.com`

Simply use these prompts in your Copilot Studio agent, and watch as AI creates stunning 3D content automatically!

## ⚠️ **Quick Reference - Object Types**
**Always use UPPERCASE for object types:**
- `CUBE` - Standard cube mesh
- `SPHERE` - UV sphere mesh  
- `CYLINDER` - Cylinder mesh
- `PLANE` - Flat plane mesh
- `CONE` - Cone mesh
- `TORUS` - Torus (donut) mesh
- `MONKEY` - Suzanne (Blender mascot) mesh

**❌ Common Error:** Using `"cube"` instead of `"CUBE"` will cause validation errors!

---

## 📋 Table of Contents

1. [Basic Object Creation](#-basic-object-creation)
2. [Scene Composition](#-scene-composition)
3. [Material & Styling](#-material--styling)
4. [Advanced Workflows](#-advanced-workflows)
5. [Creative Challenges](#-creative-challenges)
6. [Troubleshooting Prompts](#-troubleshooting-prompts)

---

## 🎯 Basic Object Creation

### Simple Object Creation
```
"Create a blue CUBE in Blender and place it at position (2, 0, 1)"
```

**⚠️ Important:** Always use uppercase object types: `CUBE`, `SPHERE`, `CYLINDER`, `PLANE`, `CONE`, `TORUS`, `MONKEY`

### Multiple Objects
```
"I need to create a basic scene with:
- A red SPHERE at the center
- A green CYLINDER to the left at (-3, 0, 0)  
- A yellow CONE to the right at (3, 0, 0)
Make them all the same size."
```

### Geometric Arrangements
```
"Create a circle of 6 CUBES around the origin. Each CUBE should be 4 units away from the center and have a different color (red, orange, yellow, green, blue, purple)."
```

---

## 🏗️ Scene Composition

### Architectural Mockup
```
"Help me create a simple building mockup:
1. Create a large cube as the base building (scale it to 4x4x6)
2. Add a smaller cube on top as a second floor (scale 2x2x3)
3. Place a cone on top as a roof
4. Add some cylinder pillars at the corners of the base
5. Use appropriate materials - gray for building, brown for pillars, red for roof"
```

### Product Display Scene
```
"Set up a product photography scene in Blender:
- Create a white plane as the background/floor (scale it large)
- Add a golden sphere as the main product in the center
- Place 3 small cubes around it as accent pieces
- Make the cubes different metallic colors (silver, copper, bronze)
- Position everything for a clean, professional look"
```

### Abstract Art Installation
```
"Create an abstract art piece with:
- 5 spheres of different sizes floating at different heights
- 3 twisted cylinders (rotate them at interesting angles)
- A large plane underneath as the base
- Use a gradient of colors from warm to cool across all objects
- Make it look like a modern sculpture installation"
```

---

## 🎨 Material & Styling

### Metallic Collection
```
"Create a materials showcase:
1. Make 4 cubes in a row
2. Apply different metallic materials:
   - First cube: Gold (RGB: 1.0, 0.8, 0.0)
   - Second cube: Silver (RGB: 0.9, 0.9, 0.9)
   - Third cube: Copper (RGB: 0.8, 0.4, 0.2)
   - Fourth cube: Bronze (RGB: 0.6, 0.4, 0.2)
3. Space them evenly along the X-axis"
```

### Color Palette Exploration
```
"I'm working on a brand identity. Create a color palette visualization:
- 6 spheres arranged in a hexagon pattern
- Each sphere represents a brand color:
  - Primary: Deep blue (0.1, 0.2, 0.8)
  - Secondary: Bright orange (1.0, 0.5, 0.0)
  - Accent 1: Lime green (0.5, 1.0, 0.2)
  - Accent 2: Purple (0.6, 0.2, 0.8)
  - Neutral 1: Light gray (0.8, 0.8, 0.8)
  - Neutral 2: Dark gray (0.3, 0.3, 0.3)
Make them glow and look professional."
```

---

## 🔥 Advanced Workflows

### Procedural City Block
```
"Generate a procedural city block:
1. Create a 5x5 grid of cubes as buildings
2. Vary the heights randomly (some 2 units tall, some 4, some 6)
3. Add cylinder 'antennas' on top of the tallest buildings
4. Create a large plane underneath as streets
5. Use gray materials for buildings, dark gray for streets
6. Add some colored accent cubes as 'signs' on random buildings"
```

### Molecular Structure Visualization
```
"Create a water molecule (H2O) visualization:
- One large red sphere for oxygen at the center
- Two smaller white spheres for hydrogen atoms
- Position the hydrogen atoms at the correct bond angle (104.5 degrees)
- Connect them with thin cylinders as bonds
- Scale everything appropriately for educational display
- Use scientific colors: red for oxygen, white for hydrogen, gray for bonds"
```

### Game Asset Prototype
```
"Design a fantasy game asset collection:
1. Create a treasure chest (use cubes and modify them)
2. Add magical crystals around it (use cones and spheres)
3. Create a pedestal underneath (cylinder)
4. Add particle-like small spheres floating around
5. Use fantasy colors: gold for chest, purple/blue for crystals, stone gray for pedestal
6. Arrange everything in an appealing composition"
```

---

## 🌟 Creative Challenges

### Minimalist Logo Recreation
```
"Help me recreate a minimalist logo concept:
- Create the letter 'A' using only basic shapes
- Use 2 cylinders for the legs of the A
- Use 1 thin cylinder for the crossbar
- Position everything precisely to form a clean 'A' shape
- Apply a gradient material from blue to purple
- Make it suitable for 3D logo animation"
```

### Seasonal Scene
```
"Create a winter wonderland scene:
1. Generate a snowy landscape with white planes at different levels
2. Add evergreen trees using cones stacked on cylinders
3. Create a snowman with 3 spheres of decreasing size
4. Add some icicles using stretched cones
5. Use appropriate winter colors: white for snow, dark green for trees, orange for snowman's nose
6. Make it feel cozy and festive"
```

### Abstract Data Visualization
```
"Transform data into 3D art:
- Create a bar chart using cubes of different heights representing sales data: [10, 25, 15, 30, 20, 35]
- Each bar should be a different color progressing through the rainbow
- Add a base plane underneath
- Include small spheres above each bar showing the exact values
- Make it look like a modern data sculpture
- Use clean, professional materials"
```

---

## 🔧 Troubleshooting Prompts

### Scene Inspection
```
"Show me what's currently in my Blender scene. List all objects, their positions, and materials."
```

### Cleanup Operations
```
"Clean up my scene by removing all objects except the default camera and light, then create a fresh workspace."
```

### Object Information
```
"Tell me detailed information about the object named 'Cube' - its position, rotation, scale, and material properties."
```

### Health Check
```
"Check if my Blender MCP server is running properly and show me the connection status."
```

---

## 💡 Pro Tips for Better Prompts

### ⚠️ **CRITICAL: Object Type Case Sensitivity**
**The most common error!** Object types MUST be uppercase:
- ✅ **Correct:** `CUBE`, `SPHERE`, `CYLINDER`, `PLANE`, `CONE`, `TORUS`, `MONKEY`
- ❌ **Wrong:** `cube`, `sphere`, `cylinder` (will cause "Invalid object type" error)

**Example Error:**
```json
{
  "status": "error",
  "message": "Invalid object type: 'cube'. Must be one of: CUBE, SPHERE, CYLINDER, PLANE, CONE, TORUS, MONKEY",
  "error_code": "INVALID_OBJECT_TYPE"
}
```

### 🎯 **Be Specific with Coordinates**
Instead of: *"Put it somewhere on the left"*  
Use: *"Place it at position (-3, 0, 0)"*

### 🎨 **Use Exact Color Values**
Instead of: *"Make it reddish"*  
Use: *"Apply red material with RGB values (0.8, 0.2, 0.1)"*

### 📐 **Specify Object Types Clearly**
Instead of: *"Add a round thing"*  
Use: *"Create a SPHERE object"*

### 🔄 **Break Complex Tasks into Steps**
Instead of: *"Make a complex building"*  
Use: *"First create the base structure, then add details, then apply materials"*

### 🎭 **Reference Real-World Examples**
Instead of: *"Make something cool"*  
Use: *"Create a scene inspired by modern architecture with clean lines and metallic materials"*

---

## 🚀 Advanced Integration Examples

### Batch Processing
```
"I need to create a product lineup visualization:
1. Create 5 different objects (cube, sphere, cylinder, cone, torus)
2. Arrange them in a line with 2 units spacing
3. Apply the same gold material to all of them
4. Scale each one slightly different to show size variations
5. Add a backdrop plane behind them
This will be used for our product catalog."
```

### Animation Preparation
```
"Set up a scene for animation:
- Create a sphere that will be our bouncing ball
- Position it at (0, 0, 5) - high up
- Create a plane below at (0, 0, 0) as the ground
- Apply a bright red material to the ball
- Apply a neutral gray to the ground
- Make sure everything is positioned for a bouncing animation"
```

### Architectural Visualization
```
"Create an architectural concept:
1. Build a modern house using cubes of different sizes
2. Main structure: large cube (6x4x3) as the base
3. Add a smaller cube (3x4x3) as an extension
4. Create a flat roof using a thin cube on top
5. Add window 'holes' using smaller cubes positioned as cutouts
6. Use white materials for walls, dark gray for roof
7. Add some landscaping cubes around as bushes"
```

---

## 🎓 Learning Exercises

### Exercise 1: Basic Shapes Mastery
```
"Teaching exercise: Create one of each basic shape (cube, sphere, cylinder, plane, cone, torus, monkey) and arrange them in a circle. Apply a different primary color to each one. This will help me learn all available object types."
```

### Exercise 2: Transformation Practice
```
"Help me practice transformations:
1. Create a cube at the origin
2. Move it to (2, 0, 0)
3. Rotate it 45 degrees around the Z-axis
4. Scale it to double size
5. Show me the final position and properties
This will help me understand coordinate systems."
```

### Exercise 3: Material Workflow
```
"Material practice session:
- Create 3 identical spheres in a row
- Apply different material approaches:
  - First: Pure red color
  - Second: Metallic gold
  - Third: Transparent blue
- Compare the visual differences and explain the material properties"
```

---

## 🌈 Inspiration Gallery

### Sci-Fi Scene
```
"Create a futuristic space station:
- Central hub: large sphere
- 4 connecting arms: cylinders extending in cardinal directions
- Docking ports: smaller cylinders at the ends
- Solar panels: thin planes attached to the arms
- Use metallic materials with blue accent lighting
- Position everything in a dramatic composition"
```

### Nature-Inspired Abstract
```
"Design an abstract representation of a forest:
- Tree trunks: various height cylinders with brown materials
- Canopy: green spheres of different sizes placed on top
- Ground: textured plane with earth-tone material
- Add some cone-shaped 'mountains' in the background
- Create depth with layered positioning"
```

### Geometric Art Piece
```
"Create a mathematical art installation:
- Generate a Fibonacci spiral using spheres of increasing size
- Each sphere should be positioned following the golden ratio
- Use a color gradient from purple to gold across the spiral
- Add a base platform underneath
- Make it look like a museum piece"
```

---

## 📞 Support & Community

**Need Help?** 
- Check the [Troubleshooting Guide](../troubleshooting/)
- Review the [API Documentation](../api/)
- Test your connection with: `"Check if my Blender server is running"`

**Share Your Creations!**
We'd love to see what you create with these prompts. Share your results and inspire others!

---

*Happy Creating! 🎨✨*

> **Note:** All prompts are designed to work with your Blender MCP REST API at `https://blender-open-mcp-de.com`. Make sure your server is running before trying these examples. 

## 🚨 Common Errors & Solutions

### Error 1: "Invalid object type"
**Problem:** Using lowercase object types  
**Solution:** Always use uppercase: `CUBE`, `SPHERE`, `CYLINDER`, `PLANE`, `CONE`, `TORUS`, `MONKEY`

**Wrong:**
```json
{"type": "cube", "name": "MyCube"}
```

**Correct:**
```json
{"type": "CUBE", "name": "MyCube"}
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
"Create a CUBE at position (0, 0, 0) to test the coordinate system"
```

### Error 4: Material application fails
**Problem:** Object doesn't exist or wrong object name  
**Solution:** Create object first, then apply material:
```
"First create a SPHERE named 'TestSphere', then apply a red material to it"
```

--- 