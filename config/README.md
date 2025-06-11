# ⚙️ Configuration Directory

This directory contains all configuration files for BlenderMCP, organized by type.

## 📁 Directory Structure

```
config/
├── 🌐 tunnel/         # Cloudflare tunnel configurations
└── 📋 swagger/        # API specifications (OpenAPI/Swagger)
```

## 🌐 Tunnel Configuration (`tunnel/`)

Cloudflare tunnel configuration for external access.

| File | Description | Purpose |
|------|-------------|---------|
| **tunnel-config.yml** | Main tunnel configuration | Routes external traffic to local server |

### Tunnel Configuration Details

The tunnel configuration supports both API approaches:

```yaml
# REST API endpoints (Option B - Recommended)
- hostname: blender-open-mcp-de.com
  path: /api/v2
  service: http://localhost:8000

# Single endpoint API (Option A - Legacy)  
- hostname: blender-open-mcp-de.com
  service: http://localhost:8000
```

**Key Settings:**
- **Tunnel ID**: `ff98000b-7cf0-4883-9f44-4c868867c6d4`
- **Domain**: `blender-open-mcp-de.com`
- **Local Port**: `8000`

## 📋 API Specifications (`swagger/`)

OpenAPI/Swagger specifications for both API approaches.

| File | Description | API Type |
|------|-------------|----------|
| **blender-mcp-separate-endpoints.yaml** | REST endpoints specification | Option B (Recommended) |
| **blender-mcp-swagger2.yaml** | Single endpoint specification | Option A (Legacy) |
| **blender-mcp-swagger2-no-auth.yaml** | No-auth version | Option A variant |
| **swagger_2_0_spec.json** | JSON format specification | Option A (JSON) |

### API Specifications Overview

#### Option B: REST Endpoints (Recommended) ⭐
**File**: `blender-mcp-separate-endpoints.yaml`

- **Base Path**: `/api/v2/`
- **Design**: RESTful with proper HTTP methods
- **Endpoints**:
  - `GET /api/v2/health` - Health check
  - `GET /api/v2/scene` - Scene information
  - `POST /api/v2/objects` - Create objects
  - `GET /api/v2/objects/{name}` - Get object info
  - `PUT /api/v2/objects/{name}` - Modify objects
  - `DELETE /api/v2/objects/{name}` - Remove objects
  - More...

#### Option A: Single Endpoint (Legacy)
**File**: `blender-mcp-swagger2.yaml`

- **Base Path**: `/`
- **Design**: Command-based single endpoint
- **Format**: `POST /` with `{"command": "command_name", "params": {...}}`
- **Commands**: `health_check`, `get_scene_info`, `create_object`, etc.

## 🛠️ Using the Configurations

### For Development
```bash
# Use local paths in scripts
./tools/cloudflared.exe tunnel --config config/tunnel/tunnel-config.yml run
```

### For API Documentation
```bash
# Import into Postman, Insomnia, or similar
# Use: config/swagger/blender-mcp-separate-endpoints.yaml
```

### For Copilot Studio
1. **Option B (Recommended)**: Import `blender-mcp-separate-endpoints.yaml`
2. **Option A (Legacy)**: Import `blender-mcp-swagger2.yaml`

## 🔧 Customizing Configurations

### Tunnel Configuration
To modify tunnel settings:

1. Edit `config/tunnel/tunnel-config.yml`
2. Update hostname, paths, or service URLs
3. Restart tunnel: `./tools/cloudflared.exe tunnel --config config/tunnel/tunnel-config.yml run`

### API Specifications
To modify API specs:

1. Edit the appropriate YAML file in `config/swagger/`
2. Validate using online Swagger editor
3. Reimport into your API client or Copilot Studio

## 🌐 External Access URLs

Based on current configuration:

- **Base URL**: https://blender-open-mcp-de.com
- **REST API**: https://blender-open-mcp-de.com/api/v2/
- **Legacy API**: https://blender-open-mcp-de.com/

## 🔍 Configuration Validation

### Test Tunnel Configuration
```bash
# Check tunnel status
./tools/cloudflared.exe tunnel info ff98000b-7cf0-4883-9f44-4c868867c6d4

# Test external access
curl https://blender-open-mcp-de.com/api/v2/health
```

### Validate Swagger Files
```bash
# Use online validator: https://editor.swagger.io/
# Or swagger-codegen validate command
```

## 🆘 Troubleshooting

### Tunnel Issues
1. **Check tunnel status**: Ensure tunnel is running
2. **Verify configuration**: Check YAML syntax
3. **Test local server**: Ensure server is running on port 8000
4. **Check credentials**: Verify tunnel credentials file

### API Specification Issues
1. **Validate YAML**: Check syntax and structure
2. **Check paths**: Ensure paths match server implementation
3. **Verify parameters**: Ensure parameter definitions are correct

---

**⚙️ All configurations are pre-configured for the current setup. Modify as needed for your environment!** 