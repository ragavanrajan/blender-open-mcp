#!/usr/bin/env pwsh

Write-Host "🌟 Starting BlenderMCP REST Server (Separate Endpoints)" -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found! Please install Python first." -ForegroundColor Red
    exit 1
}

# Check if Blender is running (optional check)
Write-Host "🔍 Checking Blender connection on port 9876..." -ForegroundColor Yellow
try {
    $tcpTest = Test-NetConnection -ComputerName localhost -Port 9876 -WarningAction SilentlyContinue
    if ($tcpTest.TcpTestSucceeded) {
        Write-Host "✅ Blender is running on port 9876" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Blender not detected on port 9876 (will try to connect when needed)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "⚠️  Could not check Blender connection (will try to connect when needed)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🚀 Starting REST Server on http://localhost:8000..." -ForegroundColor Green
Write-Host "📋 Available REST Endpoints:" -ForegroundColor Cyan
Write-Host "   GET    /api/v2/health                    - Health check" -ForegroundColor White
Write-Host "   GET    /api/v2/scene                     - Get scene info" -ForegroundColor White
Write-Host "   POST   /api/v2/objects                   - Create object" -ForegroundColor White
Write-Host "   GET    /api/v2/objects/{name}            - Get object info" -ForegroundColor White
Write-Host "   PUT    /api/v2/objects/{name}            - Modify object" -ForegroundColor White
Write-Host "   DELETE /api/v2/objects/{name}            - Remove object" -ForegroundColor White
Write-Host "   POST   /api/v2/objects/{name}/material   - Apply material" -ForegroundColor White
Write-Host "   POST   /api/v2/execute                   - Execute Python code" -ForegroundColor White
Write-Host "   POST   /api/v2/ai/prompt                 - AI assistant" -ForegroundColor White
Write-Host ""
Write-Host "🌐 External URL: https://blender-open-mcp-de.com/api/v2/" -ForegroundColor Magenta
Write-Host "📖 Swagger File: config/swagger/blender-mcp-separate-endpoints.yaml" -ForegroundColor Magenta
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start the REST server
try {
    python -c "import sys; sys.path.insert(0, 'src'); from blender_open_mcp.rest_server import run_rest_server; run_rest_server('0.0.0.0', 8000)"
} catch {
    Write-Host "❌ Failed to start server: $_" -ForegroundColor Red
    exit 1
} 