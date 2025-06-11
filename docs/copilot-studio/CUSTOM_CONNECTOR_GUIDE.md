# 🔌 Custom Connector Creation Guide for Copilot Studio

## What Are Custom Connectors?

Custom connectors in Copilot Studio are reusable API integrations that can be shared across multiple copilots and Power Platform solutions. They provide a professional way to wrap your REST APIs with proper documentation, authentication, and error handling.

## 🆚 Custom Connectors vs Direct API Actions

| Feature | Custom Connector | Direct API Action |
|---------|------------------|-------------------|
| **Reusability** | ✅ Use across multiple copilots | ❌ Configure for each copilot |
| **Maintenance** | ✅ Update once, applies everywhere | ❌ Update each copilot individually |
| **Documentation** | ✅ Rich OpenAPI documentation | ❌ Basic action descriptions |
| **Authentication** | ✅ Advanced auth options | ❌ Basic headers only |
| **Testing** | ✅ Built-in test console | ❌ External testing required |
| **Power Platform** | ✅ Works in all Power Platform apps | ❌ Copilot Studio only |
| **Enterprise Features** | ✅ Throttling, monitoring, sharing | ❌ Limited management |

## 🛠️ Step-by-Step Connector Creation

### Step 1: Create OpenAPI Specification

First, let's define your Blender MCP API properly. Save this as `blender-mcp-openapi.yaml`:

```yaml
openapi: 3.0.0
info:
  title: Blender MCP API
  description: AI-powered Blender automation through Model Context Protocol
  version: 1.0.0
servers:
  - url: https://blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net

paths:
  /health:
    get:
      summary: Health Check
      operationId: getHealth
      responses:
        '200':
          description: Server status
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  blender_connected:
                    type: boolean

  /api/blender/scene:
    get:
      summary: Get Scene Information
      operationId: getSceneInfo
      responses:
        '200':
          description: Scene information
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIResponse'

  /api/blender/create:
    post:
      summary: Create Object
      operationId: createObject
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [type, name]
              properties:
                type:
                  type: string
                  enum: [CUBE, SPHERE, CYLINDER, PLANE, CONE, TORUS]
                name:
                  type: string
                location:
                  type: array
                  items:
                    type: number
                  minItems: 3
                  maxItems: 3
                  default: [0, 0, 0]
                rotation:
                  type: array
                  items:
                    type: number
                  minItems: 3
                  maxItems: 3
                  default: [0, 0, 0]
                scale:
                  type: array
                  items:
                    type: number
                  minItems: 3
                  maxItems: 3
                  default: [1, 1, 1]
      responses:
        '200':
          description: Object created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIResponse'

  /api/blender/modify:
    put:
      summary: Modify Object
      operationId: modifyObject
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [name]
              properties:
                name:
                  type: string
                location:
                  type: array
                  items:
                    type: number
                  minItems: 3
                  maxItems: 3
                rotation:
                  type: array
                  items:
                    type: number
                  minItems: 3
                  maxItems: 3
                scale:
                  type: array
                  items:
                    type: number
                  minItems: 3
                  maxItems: 3
      responses:
        '200':
          description: Object modified
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIResponse'

  /api/blender/delete/{name}:
    delete:
      summary: Delete Object
      operationId: deleteObject
      parameters:
        - name: name
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Object deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIResponse'

  /api/blender/material:
    post:
      summary: Apply Material
      operationId: applyMaterial
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [object_name, material_name]
              properties:
                object_name:
                  type: string
                material_name:
                  type: string
                color:
                  type: array
                  items:
                    type: number
                  minItems: 3
                  maxItems: 3
                  default: [0.5, 0.5, 0.5]
      responses:
        '200':
          description: Material applied
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIResponse'

  /api/ai/prompt:
    post:
      summary: AI-Powered Operation
      operationId: aiPrompt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [prompt]
              properties:
                prompt:
                  type: string
                context:
                  type: string
      responses:
        '200':
          description: AI operation completed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AIResponse'

components:
  schemas:
    APIResponse:
      type: object
      properties:
        success:
          type: boolean
        message:
          type: string
        data:
          type: object

    AIResponse:
      type: object
      properties:
        success:
          type: boolean
        message:
          type: string
        analysis:
          type: string
        actions_taken:
          type: array
          items:
            type: string
```

### Step 2: Create Custom Connector in Power Platform

#### 2.1 Access Power Platform
1. Go to [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/)
2. Select your environment
3. Go to **Resources** → **Connectors**
4. Click **+ New custom connector**

#### 2.2 Basic Configuration
```yaml
Connector Name: Blender MCP API
Description: AI-powered Blender automation
Icon: Upload a Blender logo (optional)
Host: blender-open-mcp-gphpdbg7cccdcsf8.newzealandnorth-01.azurewebsites.net
Base URL: /
```

#### 2.3 Import OpenAPI
1. Click **Import from OpenAPI**
2. Upload or paste your OpenAPI specification
3. Review imported actions
4. Click **Continue**

### Step 3: Configure Security (Optional)

For production use, add API key authentication:

```yaml
Authentication Type: API Key
API Key:
  Parameter label: API-Key
  Parameter name: X-API-Key
  Parameter location: Header
```

### Step 4: Test Your Connector

#### 4.1 Create Test Connection
1. Go to **Test** tab
2. Click **+ New connection**
3. If using API key, enter your key
4. Click **Create connection**

#### 4.2 Test Each Operation
Test key operations:

```json
// Test Health Check
Operation: GetHealth
Expected: {"status": "ok", "blender_connected": true}

// Test Create Object
Operation: CreateObject
Body: {
  "type": "CUBE",
  "name": "TestCube",
  "location": [1, 0, 1]
}

// Test AI Prompt
Operation: AiPrompt  
Body: {
  "prompt": "Create a red sphere",
  "context": "Test operation"
}
```

### Step 5: Publish Connector

1. Review all configurations
2. Click **Create connector**
3. Test in the connector console
4. When satisfied, click **Publish**

## 🎯 Using Your Custom Connector in Copilot Studio

### Step 1: Add Connector to Copilot

1. In Copilot Studio, open your copilot
2. Go to **Actions** → **Add an action**
3. Choose **Connectors**
4. Find "Blender MCP API" connector
5. Select actions you want to use

### Step 2: Create Topics Using Connector

#### Example Topic: Create Objects

**Trigger Phrases:**
- "Create a {objectType}"
- "Add {objectType} named {objectName}"
- "Make a new {objectType}"

**Topic Flow:**
```yaml
Node 1: Parse Input
- Extract objectType (CUBE, SPHERE, etc.)
- Extract objectName (optional)
- Set default name if not provided

Node 2: Call Connector
- Connector: Blender MCP API
- Action: Create Object
- Parameters:
  - type: {Topic.objectType}
  - name: {Topic.objectName}
  - location: [0, 0, 0]
  - scale: [1, 1, 1]

Node 3: Handle Response
- Condition: {ConnectorResponse.success} = true
  - Success: "✅ Created {objectName} successfully!"
  - Failed: "❌ Error: {ConnectorResponse.message}"
```

#### Example Topic: AI Assistant

**Trigger Phrases:**
- "Help me with {request}"
- "I want to {action}"
- "Can you {task}"

**Topic Flow:**
```yaml
Node 1: Capture Request
- Variable: userRequest (from trigger)

Node 2: Call AI Connector
- Connector: Blender MCP API
- Action: AI-Powered Operation
- Parameters:
  - prompt: {Topic.userRequest}
  - context: "Copilot Studio integration"

Node 3: Present Results  
- Message: "I analyzed your request: {AIResponse.analysis}"
- Message: "Actions taken: {AIResponse.actions_taken}"
- Condition: Check if successful and offer follow-ups
```

## 🔧 Advanced Connector Features

### Dynamic Parameter Values

Set up smart parameter suggestions:

```yaml
# In connector designer
objectType parameter:
  - Static values: [CUBE, SPHERE, CYLINDER, PLANE, CONE, TORUS]
  - Default: CUBE
  - Required: true

materialName parameter:
  - Dynamic values from: /api/blender/materials (if you add this endpoint)
  - Fallback: [Metal, Glass, Plastic, Wood]
```

### Error Handling Configuration

```yaml
# Configure specific error responses
Error Handling:
  400: "Bad request - check your parameters"
  404: "Object not found in scene"  
  500: "Blender connection error - is Blender running?"
  503: "Server temporarily unavailable"
```

### Response Transformation

Transform API responses for better use in copilots:

```yaml
# Transform complex responses to simple values
Response Mapping:
  - success: {body.success}
  - message: {body.message}
  - objectCount: {body.data.objects.length}
  - activeObject: {body.data.active_object.name}
```

## 📊 Monitoring Your Connector

### Built-in Analytics
Power Platform provides:
- Usage metrics (calls per day)
- Success/failure rates
- Performance data
- User adoption

### Custom Monitoring
Add to your Azure application:

```json
{
  "applicationInsights": {
    "instrumentationKey": "your-key",
    "samplingSettings": {
      "isEnabled": true
    }
  }
}
```

## 🚀 Best Practices

### 1. Design Principles
- **Descriptive Names**: Clear action and parameter names
- **Consistent Responses**: Same format across all operations
- **Rich Documentation**: Help users understand each action
- **Error Messages**: Meaningful, actionable error messages

### 2. Performance Optimization
- **Response Caching**: Cache static data like object types
- **Batch Operations**: Combine related operations
- **Async Support**: For long-running operations
- **Compression**: Enable gzip compression

### 3. Security Best Practices
- **API Keys**: Use authentication for production
- **Input Validation**: Validate all parameters
- **Rate Limiting**: Prevent API abuse
- **HTTPS Only**: Secure all communications

## 🛠️ Troubleshooting Common Issues

### OpenAPI Import Validation Errors

**Issue: "Operation ID does not start with upper case letter"**
```yaml
Solutions:
1. Check all operationId fields in your OpenAPI spec
2. Ensure they start with uppercase letters (e.g., "GetHealth" not "getHealth")
3. Use PascalCase for operation IDs (GetSceneInfo, CreateObject, etc.)
4. Re-import the corrected OpenAPI specification
```

**Issue: "Parameter in path: [name] - Type not defined"**
```yaml
Solutions:
1. Check the parameter structure in your OpenAPI spec
2. Ensure parameters follow this order:
   - name: parameter_name
   - in: path
   - required: true
   - description: "Parameter description"
   - schema:
       type: string
3. Move 'description' before 'schema' if needed
4. Re-import the corrected specification
```

### Connection Test Failures
```yaml
Issue: "Cannot connect to host"
Solutions:
1. Verify Azure app is running
2. Check URL spelling
3. Test endpoint with curl/Postman
4. Check firewall settings
```

### Parameter Problems
```yaml
Issue: "Required parameter missing"
Solutions:
1. Check parameter names match OpenAPI spec
2. Verify required vs optional parameters
3. Test with minimal required parameters
4. Check data types (string vs number)
```

### Response Parsing Errors
```yaml
Issue: "Cannot read property of undefined"
Solutions:
1. Check response schema matches actual API
2. Handle null/empty responses
3. Add default values for optional fields
4. Test all success and error scenarios
```

## 🎉 Next Steps

1. **Create your OpenAPI specification** using the template above
2. **Set up the custom connector** in Power Platform
3. **Test all operations** thoroughly
4. **Create sample copilot topics** to test integration
5. **Add authentication** for production deployment
6. **Monitor usage** and optimize based on feedback
7. **Share with your team** and gather requirements

## 📚 Additional Resources

- [Power Platform Custom Connectors Documentation](https://docs.microsoft.com/en-us/connectors/custom-connectors/)
- [OpenAPI Specification Guide](https://swagger.io/specification/)
- [Copilot Studio Actions Documentation](https://docs.microsoft.com/en-us/power-virtual-agents/advanced-flow)
- [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

Your custom connector will provide a professional, reusable integration that works across all your Power Platform solutions! 🚀 