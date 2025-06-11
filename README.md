# blender-open-mcp

`blender-open-mcp` is an open source project that integrates Blender with local AI models (via [Ollama](https://ollama.com/)) using the Model Context Protocol (MCP). This allows you to control Blender using natural language prompts, leveraging the power of AI to assist with 3D modeling tasks.

## Features

- **Control Blender with Natural Language:** Send prompts to a locally running Ollama model to perform actions in Blender.
- **Python Version Compatibility:** Works with Python 3.8+ (Simple Mode) and Python 3.10+ (Full MCP Mode) with automatic detection
- **Auto-Detection System:** Automatically selects the best server mode based on your Python version and available dependencies
- **MCP Integration:** Uses the Model Context Protocol for structured communication between the AI model and Blender.
- **Ollama Support:** Designed to work with Ollama for easy local model management.
- **Blender Add-on:** Includes a Blender add-on to provide a user interface and handle communication with the server.
- **PolyHaven Integration (Optional):** Download and use assets (HDRIs, textures, models) from [PolyHaven](https://polyhaven.com/) directly within Blender via AI prompts.
- **Basic 3D Operations:**
  - Get Scene and Object Info
  - Create Primitives
  - Modify and delete objects
  - Apply materials
- **Render Support:** Render images using the tool and retrieve information based on the output.

## Quick Start

### Prerequisites

1. **Blender:** Blender 3.0 or later. Download from [blender.org](https://www.blender.org/download/).
2. **Ollama:** Install from [ollama.com](https://ollama.com/), following OS-specific instructions.
3. **Python:** Python 3.8 or later (Python 3.10+ recommended for full MCP features).
4. **Git:** Required for cloning the repository.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/dhakalnirajan/blender-open-mcp.git
   cd blender-open-mcp
   ```

2. **Install Dependencies:**

   For **Python 3.10+** (Full MCP Mode):
   ```bash
   pip install -r requirements.txt
   ```

   For **Python 3.8-3.9** (Simple Mode):
   ```bash
   # No additional dependencies needed - uses Python standard library only
   ```

3. **Install the Blender Add-on:**

   - Open Blender.
   - Go to `Edit -> Preferences -> Add-ons`.
   - Click `Install...`.
   - Select the `addon.py` file from the `blender-open-mcp` directory.
   - Enable the "Blender MCP" add-on.

4. **Download an Ollama Model (if not already installed):**

   ```bash
   ollama run llama3.2
   ```

### Running the Server

**🚀 Automatic Mode (Recommended):**
```bash
python main.py
```

The system will automatically:
- Detect your Python version
- Check for FastMCP availability  
- Select Full MCP Server (Python 3.10+) or Simple Server (Python 3.8+)
- Display upgrade suggestions if applicable

**Manual Mode Options:**

For **Full MCP Server** (Python 3.10+):
```bash
python main.py --mode mcp --port 8000
```

For **Simple Server** (Python 3.8+):
```bash
python main.py --mode simple --port 8000
```

### Blender Setup

1. **Start the Blender Add-on Server:**
   - Open Blender and the 3D Viewport.
   - Press `N` to open the sidebar.
   - Find the "Blender MCP" panel.
   - Click "Start MCP Server".

## Server Modes Comparison

| Feature | Full MCP Server (Python 3.10+) | Simple Server (Python 3.8+) |
|---------|--------------------------------|------------------------------|
| **Basic Blender Integration** | ✅ Full Support | ✅ Full Support |
| **Ollama AI Integration** | ✅ Advanced Features | ✅ Basic Features |
| **Model Context Protocol** | ✅ Complete MCP Support | ❌ HTTP REST Only |
| **Production ASGI Deployment** | ✅ FastMCP/Uvicorn | ❌ HTTP Server Only |
| **Advanced Error Handling** | ✅ Enhanced | ✅ Basic |
| **Image Handling** | ✅ Full Support | ✅ Full Support |
| **Dependencies** | FastMCP, httpx, etc. | Python Standard Library Only |

## Usage

Interact with `blender-open-mcp` using the `mcp` command-line tool or HTTP requests:

### Example Commands

- **Basic Health Check:**

  ```bash
  curl http://localhost:8000/health_check
  ```

- **Get Scene Information:**

  ```bash
  curl -X POST http://localhost:8000/get_scene_info -H "Content-Type: application/json" -d "{}"
  ```

- **Create a Cube:**

  ```bash
  curl -X POST http://localhost:8000/create_object -H "Content-Type: application/json" -d '{"type": "CUBE", "name": "my_cube"}'
  ```

- **Using MCP (Full Mode Only):**

  ```bash
  mcp prompt "Hello BlenderMCP!" --host http://localhost:8000
  mcp tool get_scene_info --host http://localhost:8000
  ```

## Available Tools

| Tool Name                  | Description                            | Parameters                                            |
| -------------------------- | -------------------------------------- | ----------------------------------------------------- |
| `get_scene_info`           | Retrieves scene details.               | None                                                  |
| `get_object_info`          | Retrieves information about an object. | `object_name` (str)                                   |
| `create_object`            | Creates a 3D object.                   | `type`, `name`, `location`, `rotation`, `scale`       |
| `modify_object`            | Modifies an object's properties.       | `name`, `location`, `rotation`, `scale`, `visible`    |
| `delete_object`            | Deletes an object.                     | `name` (str)                                          |
| `set_material`             | Assigns a material to an object.       | `object_name`, `material_name`, `color`               |
| `render_image`             | Renders an image.                      | `file_path` (str)                                     |
| `execute_blender_code`     | Executes Python code in Blender.       | `code` (str)                                          |
| `get_polyhaven_categories` | Lists PolyHaven asset categories.      | `asset_type` (str)                                    |
| `search_polyhaven_assets`  | Searches PolyHaven assets.             | `asset_type`, `categories`                            |
| `download_polyhaven_asset` | Downloads a PolyHaven asset.           | `asset_id`, `asset_type`, `resolution`, `file_format` |
| `set_texture`              | Applies a downloaded texture.          | `object_name`, `texture_id`                           |
| `set_ollama_model`         | Sets the Ollama model.                 | `model_name` (str)                                    |
| `set_ollama_url`           | Sets the Ollama server URL.            | `url` (str)                                           |
| `get_ollama_models`        | Lists available Ollama models.         | None                                                  |

## Troubleshooting

If you encounter issues:

- Ensure Ollama and the `blender-open-mcp` server are running.
- Check Blender's add-on settings.
- Verify command-line arguments.
- Refer to logs for error details.

For further assistance, visit the [GitHub Issues](https://github.com/dhakalnirajan/blender-open-mcp/issues) page.

---

Happy Blending with AI! 🚀
