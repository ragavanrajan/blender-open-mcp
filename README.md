# 🎨 BlenderMCP - Blender Model Communication Protocol

A comprehensive solution for controlling Blender remotely via REST API and MCP protocol, with full Copilot Studio integration.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-green.svg)]()

## 🚀 Quick Start

### Option A: Complete Start (Recommended)
```bash
# Start everything (server + tunnel) - Recommended
./scripts/start/start-everything.ps1

# Or start REST server only (for development without tunnel)
./scripts/start/start-rest-server.ps1
```

### Option B: Manual Start
```bash
# 1. Start the REST server
python -c "import sys; sys.path.insert(0, 'src'); from blender_open_mcp.rest_server import run_rest_server; run_rest_server('0.0.0.0', 8000)"

# 2. Start the tunnel (in another terminal)
./tools/cloudflared.exe tunnel --config config/tunnel/tunnel-config.yml run
```

## 📁 Project Structure

```
blender-open-mcp/
├── 📖 docs/                          # Documentation
│   ├── 🛠️  setup/                    # Setup guides
│   ├── 📋 api/                       # API documentation  
│   ├── 🔧 troubleshooting/           # Troubleshooting guides
│   └── 🤖 copilot-studio/            # Copilot Studio integration
├── 🐍 src/                           # Source code
│   └── blender_open_mcp/             # Main package
├── 🚀 scripts/                       # Utility scripts
│   ├── start/                        # Startup scripts
│   ├── test/                         # Test scripts
│   └── utils/                        # Utility scripts
├── ⚙️  config/                        # Configuration files
│   ├── tunnel/                       # Tunnel configurations
│   └── swagger/                      # API specifications
├── 📝 examples/                      # Example usage
├── 🛠️  tools/                        # External tools
└── 🏗️  .github/                      # GitHub workflows
```

## 🌟 Features

- **🎯 Two API Approaches**: Single endpoint (legacy) and REST endpoints (recommended)
- **🌐 Public Access**: Cloudflare tunnel for external access
- **🤖 Copilot Studio**: Full integration with Microsoft Copilot Studio
- **🔄 Live Blender Control**: Real-time object creation, modification, and scene management
- **📊 Comprehensive API**: Health checks, scene info, object manipulation, material application
- **🛡️ CORS Support**: Cross-origin resource sharing enabled
- **📋 OpenAPI Documentation**: Complete Swagger/OpenAPI specifications

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **Setup Guides** |
| [📖 Setup Guide](docs/setup/BLENDER_MCP_SETUP_GUIDE.md) | Complete setup instructions |
| [🏠 Local Setup](docs/setup/LOCAL_SETUP_GUIDE.md) | Local development setup |
| [👥 Team Setup](docs/setup/team_setup_guide.md) | Team collaboration setup |
| **API Documentation** |
| [📊 API Comparison](docs/api/API_COMPARISON.md) | Single vs REST endpoints |
| [📋 Swagger Files](config/swagger/) | OpenAPI specifications |
| **Copilot Studio** |
| [🤖 Copilot Guide](docs/copilot-studio/COPILOT_STUDIO_GUIDE.md) | Complete integration guide |
| [🔌 Custom Connector](docs/copilot-studio/CUSTOM_CONNECTOR_GUIDE.md) | Custom connector setup |
| **Troubleshooting** |
| [🐛 Python Upgrade](docs/troubleshooting/PYTHON311_UPGRADE_SUMMARY.md) | Python 3.11 upgrade notes |

## 🛠️ API Options

### Option A: Single Endpoint (Legacy)
- **Endpoint**: `POST /`
- **Format**: `{"command": "command_name", "params": {...}}`
- **Swagger**: [config/swagger/blender-mcp-swagger2.yaml](config/swagger/blender-mcp-swagger2.yaml)

### Option B: REST Endpoints (Recommended) ⭐
- **Health**: `GET /api/v2/health`
- **Scene**: `GET /api/v2/scene`
- **Objects**: `POST /api/v2/objects`, `GET /api/v2/objects/{name}`, etc.
- **Swagger**: [config/swagger/blender-mcp-separate-endpoints.yaml](config/swagger/blender-mcp-separate-endpoints.yaml)

## 🌐 Access URLs

- **Local**: http://localhost:8000
- **Public**: https://blender-open-mcp-de.com
- **REST API**: https://blender-open-mcp-de.com/api/v2/

## 🧪 Testing

```bash
# Health check (REST)
curl https://blender-open-mcp-de.com/api/v2/health

# Health check (Legacy)
curl -X POST https://blender-open-mcp-de.com/ \
  -H "Content-Type: application/json" \
  -d '{"command": "health_check"}'

# Create a cube
curl -X POST https://blender-open-mcp-de.com/api/v2/objects \
  -H "Content-Type: application/json" \
  -d '{"type": "CUBE", "name": "MyCube"}'
```

## 🔧 Development

### Prerequisites
- Python 3.11+
- Blender 4.0+ (running with socket server enabled)
- Cloudflare tunnel (for external access)

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python scripts/test/test_simple_server.py

# Start development server
python -c "import sys; sys.path.insert(0, 'src'); from blender_open_mcp.rest_server import run_rest_server; run_rest_server()"
```

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/blender-open-mcp.git
   cd blender-open-mcp
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Blender**: Follow the [setup guide](docs/setup/BLENDER_MCP_SETUP_GUIDE.md)

4. **Start the server**: Use one of the startup scripts in `scripts/start/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/blender-open-mcp/issues)
- **Documentation**: [docs/](docs/)
- **Troubleshooting**: [docs/troubleshooting/](docs/troubleshooting/)

## 🙏 Acknowledgments

- Blender Foundation for the amazing 3D software
- Cloudflare for tunnel technology
- Microsoft for Copilot Studio integration capabilities

---

**🎯 Ready to control Blender remotely? Start with our [Setup Guide](docs/setup/BLENDER_MCP_SETUP_GUIDE.md)!** 