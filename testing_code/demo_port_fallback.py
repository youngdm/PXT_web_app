#!/usr/bin/env python3
"""
Demonstration script for PXT Web App port fallback mechanism.
This script shows how the Flask app automatically selects available ports.
"""

import socket
import time
import subprocess
import sys
import os


def is_port_available(port):
    """Check if a port is available for use."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", port))
            return True
    except socket.error:
        return False


def check_port_status():
    """Display current status of Flask app ports."""
    print("🔍 Checking Port Availability...")
    print("-" * 40)

    ports = {5000: "Primary", 5001: "Fallback"}

    for port, description in ports.items():
        available = is_port_available(port)
        status_icon = "✅ Available" if available else "❌ Occupied"
        print(f"   Port {port} ({description}): {status_icon}")

    return is_port_available(5000), is_port_available(5001)


def demonstrate_flask_startup():
    """Demonstrate Flask app startup with port selection."""
    print("\n🚀 Flask App Port Selection Demonstration")
    print("=" * 50)

    port_5000_free, port_5001_free = check_port_status()

    print(f"\n📋 Expected Behavior:")
    if port_5000_free:
        print(f"   ✅ App should start on port 5000 (primary)")
        expected_port = 5000
    elif port_5001_free:
        print(f"   ⚠️  App should fallback to port 5001")
        expected_port = 5001
    else:
        print(f"   ❌ App should exit with error (both ports occupied)")
        expected_port = None

    print(f"\n🎯 To test the Flask app:")
    print(f"   1. Run: cd app && python3 app.py")
    print(f"   2. Look for startup message indicating which port is used")

    if expected_port:
        print(f"   3. Visit: http://127.0.0.1:{expected_port}")

    return expected_port


def simulate_port_occupation():
    """Simulate occupying port 5000 to demonstrate fallback."""
    print(f"\n🧪 Port Fallback Simulation")
    print("=" * 40)

    if is_port_available(5000):
        print(f"💡 Tip: To test fallback behavior:")
        print(
            f"   1. Start any service on port 5000 (e.g., 'python3 -m http.server 5000')"
        )
        print(f"   2. Then run the PXT Web App")
        print(f"   3. App will automatically use port 5001 instead")
    else:
        print(f"✅ Port 5000 is currently occupied - perfect for testing!")
        print(f"   The Flask app will automatically use port 5001")


def show_port_management_tips():
    """Display helpful tips for port management."""
    print(f"\n💡 Port Management Tips")
    print("=" * 30)
    print(f"🔧 If you need to free up ports:")
    print(f"   • Find processes: lsof -i :5000")
    print(f"   • Kill process: kill -9 <PID>")
    print(f"   • Or use different port: python3 app.py --port 8080")

    print(f"\n🌐 Common Port Conflicts:")
    print(f"   • Port 5000: Other Flask apps, AirPlay on macOS")
    print(f"   • Port 5001: Usually free (good fallback choice)")
    print(f"   • Port 8080: Alternative web development port")

    print(f"\n✅ PXT Web App Handles:")
    print(f"   • Automatic port detection")
    print(f"   • Graceful fallback to port 5001")
    print(f"   • Clear error messages")
    print(f"   • User-friendly startup notifications")


def main():
    """Run the complete port fallback demonstration."""
    print("🌐 PXT Web App - Port Fallback Demonstration")
    print("=" * 55)

    # Show current port status
    expected_port = demonstrate_flask_startup()

    # Show simulation tips
    simulate_port_occupation()

    # Show management tips
    show_port_management_tips()

    print(f"\n🎯 Quick Test:")
    print(f"   Run 'cd app && python3 app.py' to see the port selection in action!")

    if expected_port:
        print(f"   Expected URL: http://127.0.0.1:{expected_port}")

    print(f"\n📝 The app.py file now includes:")
    print(f"   ✅ Port availability checking")
    print(f"   ✅ Automatic fallback from 5000 to 5001")
    print(f"   ✅ Clear user messaging about port selection")
    print(f"   ✅ Graceful error handling")


if __name__ == "__main__":
    main()
