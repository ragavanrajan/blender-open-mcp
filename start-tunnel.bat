@echo off
echo ================================
echo Starting Cloudflare Tunnel...
echo Domain: blender-open-mcp-de.com
echo ================================
cd /d "E:\MyDev\MyMCP\blender-open-mcp"
.\cloudflared.exe tunnel --config tunnel-config.yml run
echo Tunnel stopped.
pause 