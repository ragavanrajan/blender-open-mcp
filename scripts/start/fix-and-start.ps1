# Fix and Start Blender MCP Server
Write-Host "================================" -ForegroundColor Green
Write-Host "Fixing Blender MCP Server Setup" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green

# Clean up existing processes
Write-Host "Cleaning up existing processes..." -ForegroundColor Yellow
try {
    Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force
    Get-Process cloudflared -ErrorAction SilentlyContinue | Stop-Process -Force
} catch {
    Write-Host "No processes to clean up." -ForegroundColor Gray
}

Start-Sleep -Seconds 2

# Navigate to project directory
Set-Location "E:\MyDev\MyMCP\blender-open-mcp"

Write-Host "Starting MCP Server..." -ForegroundColor Yellow
# Start the server that works
Start-Process powershell -ArgumentList "-Command", "cd 'E:\MyDev\MyMCP\blender-open-mcp'; python main.py --host 0.0.0.0 --port 8000; pause" -NoNewWindow

Start-Sleep -Seconds 10

# Test if server is responding
Write-Host "Testing server..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/docs" -UseBasicParsing -TimeoutSec 5
    Write-Host "✅ Server is running! Status: $($response.StatusCode)" -ForegroundColor Green
} catch {
    Write-Host "❌ Server not responding yet. Check the other window." -ForegroundColor Red
}

Write-Host "================================" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Verify server shows 'Connected to Blender'" -ForegroundColor White
Write-Host "2. Your tunnel is already running" -ForegroundColor White
Write-Host "3. Test: https://blender-open-mcp-de.com/docs" -ForegroundColor White
Write-Host "4. Update Power Platform connector" -ForegroundColor White
Write-Host "================================" -ForegroundColor Green

pause 