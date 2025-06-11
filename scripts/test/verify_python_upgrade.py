#!/usr/bin/env python3
"""
Verify Python installation and MCP compatibility
"""
import sys
import subprocess

def check_python_version():
    """Check if Python version meets MCP requirements"""
    version = sys.version_info
    
    print(f"🐍 Python Version: {version.major}.{version.minor}.{version.micro}")
    print(f"📍 Python Path: {sys.executable}")
    
    if version >= (3, 10):
        print("✅ Python version is compatible with full MCP features!")
        return True
    elif version >= (3, 8):
        print("⚠️  Python version supports simple mode only (need 3.10+ for full MCP)")
        return False
    else:
        print("❌ Python version too old (need 3.8+ minimum)")
        return False

def check_pip():
    """Check if pip is available and working"""
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                               capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ pip is available: {result.stdout.strip()}")
            return True
        else:
            print("❌ pip is not working properly")
            return False
    except Exception as e:
        print(f"❌ Error checking pip: {e}")
        return False

def check_mcp_compatibility():
    """Check if we can install MCP packages"""
    compatible = check_python_version()
    pip_works = check_pip()
    
    if compatible and pip_works:
        print("\n🎉 Ready to install full MCP features!")
        print("Next steps:")
        print("1. pip install fastmcp")
        print("2. pip install -r requirements.txt")
        print("3. python src/blender_open_mcp/server.py")
        return True
    elif pip_works:
        print("\n📝 Currently using simple mode")
        print("Upgrade Python to 3.10+ for full MCP features")
        return False
    else:
        print("\n🔧 Need to fix pip installation first")
        return False

if __name__ == "__main__":
    print("🔍 Python & MCP Compatibility Check")
    print("=" * 40)
    
    check_mcp_compatibility() 