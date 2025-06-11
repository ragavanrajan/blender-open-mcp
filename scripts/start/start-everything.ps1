# BlenderMCP Complete Startup Script
# This script starts the server and tunnel in the correct order

Write-Host "BlenderMCP Complete Startup Script" -ForegroundColor Magenta
Write-Host "====================================" -ForegroundColor Magenta

# Step 1: Clean up any existing processes
Write-Host "`nStep 1: Cleaning up existing processes..." -ForegroundColor Yellow
taskkill /F /IM python.exe /T 2>$null
taskkill /F /IM cloudflared.exe /T 2>$null
Start-Sleep 3

# Step 2: Clear port 8000
Write-Host "Step 2: Clearing port 8000..." -ForegroundColor Yellow
$port8000Processes = netstat -ano | findstr ":8000" | ForEach-Object {
    $processId = ($_ -split '\s+')[-1]
    if($processId -ne "0" -and $processId -match '^\d+$') { 
        Write-Host "  Killing PID: $processId" -ForegroundColor Gray
        taskkill /F /PID $processId 2>$null 
    }
}
Start-Sleep 2

# Step 3: Verify Blender is running
Write-Host "Step 3: Checking Blender status..." -ForegroundColor Yellow
$blenderProcess = tasklist | findstr -i blender
if ($blenderProcess) {
    Write-Host "  Blender is running" -ForegroundColor Green
} else {
    Write-Host "  Blender is NOT running - Please start Blender first!" -ForegroundColor Red
    exit 1
}

# Step 4: Start the simple server
Write-Host "Step 4: Starting BlenderMCP REST Server..." -ForegroundColor Yellow
$serverJob = Start-Job -ScriptBlock {
    Set-Location "E:\MyDev\MyMCP\blender-open-mcp"
    python -c "import sys; sys.path.insert(0, 'src'); from blender_open_mcp.rest_server import run_rest_server; run_rest_server('0.0.0.0', 8000)"
}

# Wait for server to start
Write-Host "  Waiting for server to initialize..." -ForegroundColor Gray
Start-Sleep 8

# Step 5: Test local server
Write-Host "Step 5: Testing local server..." -ForegroundColor Yellow
try {
    $healthResponse = Invoke-WebRequest -Uri "http://localhost:8000/api/v2/health" -Method GET -UseBasicParsing
    if ($healthResponse.StatusCode -eq 200) {
        Write-Host "  Local REST server is working! Status: 200" -ForegroundColor Green
        Write-Host "  Response: $($healthResponse.Content)" -ForegroundColor Cyan
    }
} catch {
    Write-Host "  Local server failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Step 6: Start Cloudflare tunnel
Write-Host "Step 6: Starting Cloudflare tunnel..." -ForegroundColor Yellow
Write-Host "  Using tunnel ID: ff98000b-7cf0-4883-9f44-4c868867c6d4" -ForegroundColor Gray
$tunnelJob = Start-Job -ScriptBlock {
    Set-Location "E:\MyDev\MyMCP\blender-open-mcp"
    & ".\tools\cloudflared.exe" tunnel --config config\tunnel\tunnel-config.yml run
}

# Wait for tunnel to establish
Write-Host "  Waiting for tunnel to establish..." -ForegroundColor Gray
Start-Sleep 15

# Step 7: Test tunnel connection
Write-Host "Step 7: Testing tunnel connection..." -ForegroundColor Yellow
$maxRetries = 3
$retryCount = 0

while ($retryCount -lt $maxRetries) {
    try {
        $tunnelResponse = Invoke-WebRequest -Uri "https://blender-open-mcp-de.com/api/v2/health" -Method GET -UseBasicParsing
        if ($tunnelResponse.StatusCode -eq 200) {
            Write-Host "  Tunnel is working! Status: 200" -ForegroundColor Green
            Write-Host "  Public URL: https://blender-open-mcp-de.com/api/v2/health" -ForegroundColor Cyan
            break
        }
    } catch {
        $retryCount++
        Write-Host "  Tunnel attempt $retryCount failed: $($_.Exception.Message)" -ForegroundColor Yellow
        if ($retryCount -lt $maxRetries) {
            Write-Host "  Retrying in 10 seconds..." -ForegroundColor Gray
            Start-Sleep 10
        }
    }
}

if ($retryCount -eq $maxRetries) {
    Write-Host "  Tunnel failed after $maxRetries attempts" -ForegroundColor Red
    Write-Host "  Local server is still working on http://localhost:8000/api/v2/health" -ForegroundColor Blue
}

# Step 8: Final status report
Write-Host "`nSTARTUP COMPLETE!" -ForegroundColor Magenta
Write-Host "==================" -ForegroundColor Magenta
Write-Host "Local Server: http://localhost:8000/api/v2/health" -ForegroundColor Green
Write-Host "Public URL: https://blender-open-mcp-de.com/api/v2/health" -ForegroundColor Cyan
Write-Host "`nFor Copilot Studio:" -ForegroundColor Yellow
Write-Host "   Host URL: https://blender-open-mcp-de.com" -ForegroundColor White
Write-Host "   Method: GET" -ForegroundColor White
Write-Host "   Path: /api/v2/health" -ForegroundColor White
Write-Host "   Expected Response: 200 OK with success status" -ForegroundColor White

Write-Host "`nServer is running in background. Press Ctrl+C to stop." -ForegroundColor Blue 