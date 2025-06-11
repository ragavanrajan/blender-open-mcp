# 🚀 Scripts Directory

This directory contains all utility scripts for BlenderMCP, organized by purpose.

## 📁 Directory Structure

```
scripts/
├── 🚀 start/          # Startup scripts
├── 🧪 test/           # Test scripts  
└── 🔧 utils/          # Utility scripts
```

## 🚀 Startup Scripts (`start/`)

Scripts to start various components of BlenderMCP.

| Script | Description | Usage |
|--------|-------------|-------|
| **start-rest-server.ps1** | Start REST server (Option B) | `./scripts/start/start-rest-server.ps1` |
| **start-everything.ps1** | Start server + tunnel | `./scripts/start/start-everything.ps1` |
| **start-tunnel.bat** | Start tunnel only | `./scripts/start/start-tunnel.bat` |
| **start-server.bat** | Start server only | `./scripts/start/start-server.bat` |
| **fix-and-start.ps1** | Fix issues and start | `./scripts/start/fix-and-start.ps1` |

### 🌟 Recommended Startup
```bash
# For REST endpoints (recommended)
./scripts/start/start-rest-server.ps1

# For complete setup (server + tunnel)
./scripts/start/start-everything.ps1
```

## 🧪 Test Scripts (`test/`)

Scripts to test various components and functionality.

| Script | Description | Usage |
|--------|-------------|-------|
| **test_full_mcp_server.py** | Test full MCP server | `python scripts/test/test_full_mcp_server.py` |
| **test_simple_server.py** | Test simple HTTP server | `python scripts/test/test_simple_server.py` |
| **simple-test.py** | Quick API test | `python scripts/test/simple-test.py` |
| **verify_python_upgrade.py** | Verify Python upgrade | `python scripts/test/verify_python_upgrade.py` |

### 🧪 Quick Testing
```bash
# Test if everything is working
python scripts/test/simple-test.py

# Test the simple server
python scripts/test/test_simple_server.py
```

## 🔧 Utility Scripts (`utils/`)

General utility and helper scripts.

| Script | Description | Usage |
|--------|-------------|-------|
| **local_tunnel.py** | Local tunnel management | `python scripts/utils/local_tunnel.py` |
| **quick-start.py** | Quick development start | `python scripts/utils/quick-start.py` |

### 🔧 Common Utilities
```bash
# Quick development environment
python scripts/utils/quick-start.py

# Manage local tunnel
python scripts/utils/local_tunnel.py
```

## 🎯 Common Use Cases

### 🏁 First Time Setup
```bash
# 1. Start everything for the first time
./scripts/start/start-everything.ps1

# 2. Test that it's working
python scripts/test/simple-test.py
```

### 🚀 Daily Development
```bash
# Start REST server for development
./scripts/start/start-rest-server.ps1
```

### 🔧 Troubleshooting
```bash
# Fix issues and restart
./scripts/start/fix-and-start.ps1

# Verify Python setup
python scripts/test/verify_python_upgrade.py
```

### 🧪 Testing Changes
```bash
# Test the simple server
python scripts/test/test_simple_server.py

# Test full functionality
python scripts/test/test_full_mcp_server.py
```

## 📋 Prerequisites

Before running any scripts, ensure you have:

1. **Python 3.11+** installed
2. **Blender** running with socket server enabled
3. **Dependencies** installed: `pip install -r requirements.txt`
4. **Cloudflare tunnel** configured (for external access)

## 🆘 Script Issues?

If a script fails:

1. **Check prerequisites** (Python, Blender, dependencies)
2. **Review the logs** (scripts show detailed output)
3. **Try the fix script**: `./scripts/start/fix-and-start.ps1`
4. **Check troubleshooting docs**: [../docs/troubleshooting/](../docs/troubleshooting/)

---

**🚀 Start with `start-everything.ps1` for a complete setup, or `start-rest-server.ps1` for development!** 