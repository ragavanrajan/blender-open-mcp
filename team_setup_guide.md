# 🏢 **Team Collaboration Setup Guide**

## 🎯 **Problem Solved**
Enable multiple team members to use the same Copilot Studio agent while controlling their own local Blender installations.

---

## 🔄 **Option 1: Individual Setup (Simplest)**

### **Architecture:**
```
Team Member A    Team Member B    Team Member C
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Blender     │  │ Blender     │  │ Blender     │
│ Ollama      │  │ Ollama      │  │ Ollama      │
│ Server      │  │ Server      │  │ Server      │
│ Tunnel      │  │ Tunnel      │  │ Tunnel      │
│ Agent A     │  │ Agent B     │  │ Agent C     │
└─────────────┘  └─────────────┘  └─────────────┘
```

### **Steps for Each Team Member:**
1. **Install the complete setup** (Blender + Ollama + Enhanced Server)
2. **Create their own Cloudflare tunnel**
3. **Set up their own Copilot Studio agent**

### **Pros & Cons:**
✅ **Pros:** Independent, secure, full control, no network dependencies  
❌ **Cons:** Multiple agents to maintain, duplicated setup work

---

## 🌐 **Option 2: Centralized Server (Recommended)**

### **Architecture:**
```
Team Members                    Cloud Server (AWS/Azure)
┌─────────────┐                ┌─────────────────────────┐
│ Member A    │                │ Team Server             │
│ Blender     │◄──────────────►│ Multi-tenant            │
│ (local)     │   VPN/Network  │ Authentication          │
└─────────────┘                │ Ollama AI               │
┌─────────────┐                │ api.company.com         │
│ Member B    │◄──────────────►│                         │
│ Blender     │                └─────────────────────────┘
│ (local)     │                            ▲
└─────────────┘                            │
┌─────────────┐                    ┌───────────────┐
│ Member C    │◄──────────────────►│ Copilot Studio│
│ Blender     │                    │ Single Agent  │
│ (local)     │                    └───────────────┘
└─────────────┘
```

### **Implementation Steps:**

#### **A. Deploy Team Server to Cloud**
```bash
# 1. Choose cloud provider (AWS, Azure, DigitalOcean)
# 2. Create VM with public IP
# 3. Install dependencies
sudo apt update
sudo apt install python3 python3-pip
pip3 install fastapi uvicorn httpx

# 4. Upload team_server_setup.py
# 5. Configure team members in the file
# 6. Run server
python3 team_server_setup.py
```

#### **B. Configure Team Member Access**
Each team member needs to:

1. **Set up VPN/Network access** to reach each other's machines
2. **Configure their machine** in the team server:
```python
TEAM_MEMBERS = {
    "alice": {
        "name": "Alice Smith",
        "blender_url": "http://192.168.1.100:9876",  # Alice's IP
        "api_key": "alice-secret-key"
    },
    "bob": {
        "name": "Bob Johnson", 
        "blender_url": "http://192.168.1.101:9876",  # Bob's IP
        "api_key": "bob-secret-key"
    }
}
```

3. **Install Blender + MCP addon** locally
4. **Install Ollama** locally (optional, or use central AI)

#### **C. Copilot Studio Configuration**
1. **Single agent** connects to `api.company.com`
2. **Authentication** via API headers
3. **User identification** built into requests

### **Pros & Cons:**
✅ **Pros:** Single agent, centralized management, shared AI  
❌ **Cons:** Network setup required, central point of failure

---

## 🔄 **Option 3: Hybrid Approach (Most Flexible)**

### **Architecture:**
```
Each Member Runs Locally       Shared Copilot Studio
┌─────────────────────────┐    ┌───────────────────┐
│ Member A:               │    │ Single Agent      │
│ • Blender (local)       │◄──►│ Smart Routing     │
│ • Enhanced Server       │    │ User Detection    │
│ • Personal Tunnel       │    └───────────────────┘
└─────────────────────────┘
┌─────────────────────────┐
│ Member B:               │◄──┐
│ • Blender (local)       │   │
│ • Enhanced Server       │   │
│ • Personal Tunnel       │   │
└─────────────────────────┘   │
```

### **Implementation:**

#### **A. Each Member Sets Up Locally**
```bash
# 1. Each member installs complete stack
git clone <repository>
pip install fastapi uvicorn httpx

# 2. Each member starts their server
python enhanced_server.py

# 3. Each member creates tunnel with user ID
./cloudflared.exe tunnel --url http://localhost:8000 --name alice-blender
```

#### **B. Smart Copilot Studio Agent**
Configure the agent to route requests based on user context:

```
1. Agent detects user (via conversation context)
2. Routes to appropriate tunnel:
   - Alice → alice-blender.trycloudflare.com
   - Bob → bob-blender.trycloudflare.com
   - Carol → carol-blender.trycloudflare.com
```

### **Pros & Cons:**
✅ **Pros:** Local control, shared agent, no central server needed  
❌ **Cons:** Complex routing logic, multiple tunnels to manage

---

## 🛠️ **Quick Setup for Teams (Option 2 - Recommended)**

### **For Team Lead:**
1. **Deploy team server** to cloud provider
2. **Configure team members** in `TEAM_MEMBERS` dict
3. **Set up permanent domain** with Cloudflare
4. **Create single Copilot Studio agent**

### **For Team Members:**
1. **Install Blender + MCP addon**
2. **Get API key** from team lead
3. **Test connection** to team server
4. **Share tunnel access** with Copilot Studio

### **Authentication in Copilot Studio:**
Add API key header to all requests:
```
Headers:
  X-API-Key: team-member-secret-key
```

---

## 🔧 **Networking Requirements**

### **Option 2 (Centralized) Requirements:**
- **VPN or direct network access** between team members
- **Firewall rules** allowing port 9876 access
- **Cloud server** with public IP and domain

### **Security Considerations:**
- ✅ **API key authentication** for team server
- ✅ **VPN tunneling** for secure connections  
- ✅ **Firewall restrictions** on Blender ports
- ✅ **HTTPS encryption** via Cloudflare

---

## 🎯 **Recommendation**

**For Small Teams (2-5 people):** Use **Option 2 (Centralized Server)**
- Single point of management
- Shared AI resources
- Professional setup

**For Large Teams (5+ people):** Use **Option 1 (Individual Setup)** 
- Better scalability
- Independent operation
- No single point of failure

**For Distributed Teams:** Use **Option 3 (Hybrid)**
- Works across different networks
- Flexible user management
- Shared experience

---

## 📞 **Support & Next Steps**

1. **Choose your preferred option** based on team size and network setup
2. **Follow the implementation steps** for your chosen approach  
3. **Test with one team member** before rolling out to everyone
4. **Configure Copilot Studio** authentication and routing
5. **Train team** on using the AI-powered Blender commands

The centralized server approach (Option 2) provides the best balance of functionality and manageability for most teams. 