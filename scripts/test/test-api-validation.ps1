#!/usr/bin/env pwsh
# BlenderMCP API Validation Test Script
# Tests all the validation features of the REST API

Write-Host "🧪 BlenderMCP API Validation Test Suite" -ForegroundColor Magenta
Write-Host "=" * 50 -ForegroundColor Gray

$baseUrl = "http://localhost:8000/api/v2"
$headers = @{"Content-Type" = "application/json"}

function Test-ApiCall {
    param(
        [string]$TestName,
        [string]$Url,
        [string]$Method = "POST",
        [string]$Body,
        [string]$ExpectedStatus = "success",
        [string]$ExpectedError = ""
    )
    
    Write-Host "🔍 Testing: $TestName" -ForegroundColor Cyan
    
    try {
        $response = Invoke-WebRequest -Uri $Url -Method $Method -Headers $headers -Body $Body -ErrorAction Stop
        $json = $response.Content | ConvertFrom-Json
        
        if ($json.status -eq $ExpectedStatus) {
            Write-Host "   ✅ PASSED" -ForegroundColor Green
            if ($ExpectedStatus -eq "success") {
                Write-Host "   📄 Response: $($json.message)" -ForegroundColor Gray
            }
        } elseif ($ExpectedStatus -eq "error" -and $json.status -eq "error") {
            if ($ExpectedError -eq "" -or $json.message -like "*$ExpectedError*") {
                Write-Host "   ✅ PASSED (Expected Error)" -ForegroundColor Green
                Write-Host "   📄 Error: $($json.message)" -ForegroundColor Gray
            } else {
                Write-Host "   ❌ FAILED (Wrong Error)" -ForegroundColor Red
                Write-Host "   📄 Expected: $ExpectedError" -ForegroundColor Yellow
                Write-Host "   📄 Got: $($json.message)" -ForegroundColor Yellow
            }
        } else {
            Write-Host "   ❌ FAILED" -ForegroundColor Red
            Write-Host "   📄 Expected: $ExpectedStatus, Got: $($json.status)" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "   ❌ FAILED (Exception)" -ForegroundColor Red
        Write-Host "   📄 Error: $($_.Exception.Message)" -ForegroundColor Yellow
    }
    
    Write-Host ""
}

# Test 1: Valid Object Creation
Write-Host "📋 VALID OBJECT CREATION TESTS" -ForegroundColor Yellow
Write-Host "-" * 30 -ForegroundColor Gray

Test-ApiCall -TestName "Create valid CUBE" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "TestCube1"}' -ExpectedStatus "success"

Test-ApiCall -TestName "Create valid SPHERE with location" -Url "$baseUrl/objects" -Body '{"type": "SPHERE", "name": "TestSphere", "location": [1, 2, 3]}' -ExpectedStatus "success"

Test-ApiCall -TestName "Create valid CYLINDER with all params" -Url "$baseUrl/objects" -Body '{"type": "CYLINDER", "name": "TestCylinder", "location": [0, 0, 1], "rotation": [0, 0, 1.57], "scale": [1, 1, 2]}' -ExpectedStatus "success"

# Test 2: Invalid Object Types
Write-Host "📋 INVALID OBJECT TYPE TESTS" -ForegroundColor Yellow
Write-Host "-" * 30 -ForegroundColor Gray

Test-ApiCall -TestName "Natural language type" -Url "$baseUrl/objects" -Body '{"type": "Create a red cube", "name": "BadCube1"}' -ExpectedStatus "error" -ExpectedError "Invalid object type"

Test-ApiCall -TestName "Lowercase type" -Url "$baseUrl/objects" -Body '{"type": "cube", "name": "BadCube2"}' -ExpectedStatus "error" -ExpectedError "Invalid object type"

Test-ApiCall -TestName "Descriptive type" -Url "$baseUrl/objects" -Body '{"type": "CUBE object", "name": "BadCube3"}' -ExpectedStatus "error" -ExpectedError "Invalid object type"

Test-ApiCall -TestName "Random text type" -Url "$baseUrl/objects" -Body '{"type": "blender object mesh", "name": "BadCube4"}' -ExpectedStatus "error" -ExpectedError "Invalid object type"

Test-ApiCall -TestName "Missing type field" -Url "$baseUrl/objects" -Body '{"name": "BadCube5"}' -ExpectedStatus "error" -ExpectedError "Missing required field: type"

# Test 3: Invalid Location Arrays
Write-Host "📋 INVALID LOCATION TESTS" -ForegroundColor Yellow
Write-Host "-" * 30 -ForegroundColor Gray

Test-ApiCall -TestName "Location with 2 elements" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube6", "location": [1, 2]}' -ExpectedStatus "error" -ExpectedError "Location must be an array of 3 numbers"

Test-ApiCall -TestName "Location with 4 elements" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube7", "location": [1, 2, 3, 4]}' -ExpectedStatus "error" -ExpectedError "Location must be an array of 3 numbers"

Test-ApiCall -TestName "Location with string values" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube8", "location": ["1", "2", "3"]}' -ExpectedStatus "error" -ExpectedError "Location values must be numbers"

Test-ApiCall -TestName "Location as string" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube9", "location": "1,2,3"}' -ExpectedStatus "error" -ExpectedError "Location must be an array of 3 numbers"

# Test 4: Invalid Rotation Arrays  
Write-Host "📋 INVALID ROTATION TESTS" -ForegroundColor Yellow
Write-Host "-" * 30 -ForegroundColor Gray

Test-ApiCall -TestName "Rotation with 2 elements" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube10", "rotation": [0, 1.57]}' -ExpectedStatus "error" -ExpectedError "Rotation must be an array of 3 numbers"

Test-ApiCall -TestName "Rotation with string values" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube11", "rotation": ["0", "1.57", "0"]}' -ExpectedStatus "error" -ExpectedError "Rotation values must be numbers"

# Test 5: Invalid Scale Arrays
Write-Host "📋 INVALID SCALE TESTS" -ForegroundColor Yellow
Write-Host "-" * 30 -ForegroundColor Gray

Test-ApiCall -TestName "Scale with 2 elements" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube12", "scale": [1, 2]}' -ExpectedStatus "error" -ExpectedError "Scale must be an array of 3 numbers"

Test-ApiCall -TestName "Scale with zero values" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube13", "scale": [0, 1, 1]}' -ExpectedStatus "error" -ExpectedError "Scale values must be positive numbers"

Test-ApiCall -TestName "Scale with negative values" -Url "$baseUrl/objects" -Body '{"type": "CUBE", "name": "BadCube14", "scale": [-1, 1, 1]}' -ExpectedStatus "error" -ExpectedError "Scale values must be positive numbers"

# Test 6: Valid All Object Types
Write-Host "📋 ALL VALID OBJECT TYPES TEST" -ForegroundColor Yellow
Write-Host "-" * 30 -ForegroundColor Gray

$validTypes = @("CUBE", "SPHERE", "CYLINDER", "PLANE", "CONE", "TORUS", "MONKEY")
$counter = 1

foreach ($type in $validTypes) {
    Test-ApiCall -TestName "Create $type" -Url "$baseUrl/objects" -Body "{`"type`": `"$type`", `"name`": `"Test$type$counter`"}" -ExpectedStatus "success"
    $counter++
}

# Test 7: Health Check
Write-Host "📋 HEALTH CHECK TEST" -ForegroundColor Yellow
Write-Host "-" * 30 -ForegroundColor Gray

Test-ApiCall -TestName "Health Check" -Url "$baseUrl/health" -Method "GET" -Body "" -ExpectedStatus "success"

Write-Host "🏁 API Validation Test Suite Complete!" -ForegroundColor Magenta
Write-Host "=" * 50 -ForegroundColor Gray 