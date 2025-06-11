# Simple startup script to run server and tunnel in current terminal for debugging
Write-Host "Starting BlenderMCP..." -ForegroundColor Green

# Clean up any existing processes first
Write-Host "Cleaning up existing processes..." -ForegroundColor Yellow
taskkill /F /IM python.exe /T 2>$null
taskkill /F /IM cloudflared.exe /T 2>$null
Start-Sleep 2

# 1. Start REST Server in background
Write-Host "Starting REST Server in background..." -ForegroundColor Cyan
$serverJob = Start-Job -ScriptBlock {
    Set-Location "E:\MyDev\MyMCP\blender-open-mcp"
    python -c "import sys; sys.path.insert(0, 'src'); from blender_open_mcp.rest_server import run_rest_server; run_rest_server('0.0.0.0', 8000)"
}

# Give the server a moment to initialize
Write-Host "Waiting for server to initialize..." -ForegroundColor Gray
Start-Sleep -Seconds 8

# Test the local server
Write-Host "Testing local server..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/v2/health" -UseBasicParsing
    Write-Host "✅ Local server is working! Status: $($response.StatusCode)" -ForegroundColor Green
    Write-Host "Response: $($response.Content)" -ForegroundColor Cyan
} catch {
    Write-Host "❌ Local server failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# 2. Start Cloudflare Tunnel in foreground for debugging
Write-Host "`nStarting Cloudflare Tunnel (foreground for debugging)..." -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop both server and tunnel" -ForegroundColor Yellow
Write-Host "=" * 50 -ForegroundColor Gray

# Run tunnel in foreground so we can see all output
& ".\tools\cloudflared.exe" tunnel --config ".\config\tunnel\tunnel-config.yml" run