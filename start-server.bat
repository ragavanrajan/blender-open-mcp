@echo off
echo ================================
echo Starting Blender MCP Server...
echo ================================
cd /d "E:\MyDev\MyMCP\blender-open-mcp"
python main.py --host 0.0.0.0 --port 8000
echo Server stopped.
pause 