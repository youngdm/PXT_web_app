#!/usr/bin/env python3
"""
Port Investigation Tool for PXT Web App
Identifies what processes are using ports 5000 and 5001, plus other common development ports.
"""

import subprocess
import socket
import sys
import platform
import re


def is_port_available(port, host="127.0.0.1"):
    """Check if a port is available for use."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            return True
    except socket.error:
        return False


def get_port_info_unix(port):
    """Get process information for a port on Unix-like systems (macOS/Linux)."""
    try:
        # Use lsof to find what's using the port
        result = subprocess.run(
            ["lsof", "-i", f":{port}", "-n", "-P"],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.returncode == 0 and result.stdout.strip():
            lines = result.stdout.strip().split("\n")
            if len(lines) > 1:  # Skip header line
                processes = []
                for line in lines[1:]:  # Skip header
                    parts = line.split()
                    if len(parts) >= 2:
                        process_name = parts[0]
                        pid = parts[1]
                        user = parts[2] if len(parts) > 2 else "unknown"
                        processes.append(
                            {
                                "name": process_name,
                                "pid": pid,
                                "user": user,
                                "full_line": line,
                            }
                        )
                return processes
        return []
    except (
        subprocess.TimeoutExpired,
        subprocess.CalledProcessError,
        FileNotFoundError,
    ):
        # lsof might not be available or might fail
        return []


def get_port_info_windows(port):
    """Get process information for a port on Windows."""
    try:
        # Use netstat to find what's using the port
        result = subprocess.run(
            ["netstat", "-ano", "-p", "tcp"], capture_output=True, text=True, timeout=10
        )

        if result.returncode == 0:
            processes = []
            for line in result.stdout.split("\n"):
                if f":{port}" in line and "LISTENING" in line:
                    parts = line.split()
                    if len(parts) >= 5:
                        local_address = parts[1]
                        state = parts[3]
                        pid = parts[4]

                        # Get process name from PID
                        try:
                            tasklist_result = subprocess.run(
                                ["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV"],
                                capture_output=True,
                                text=True,
                                timeout=5,
                            )
                            if tasklist_result.returncode == 0:
                                lines = tasklist_result.stdout.strip().split("\n")
                                if len(lines) > 1:
                                    # Parse CSV output
                                    process_info = lines[1].strip('"').split('","')
                                    process_name = (
                                        process_info[0] if process_info else "unknown"
                                    )
                                else:
                                    process_name = "unknown"
                            else:
                                process_name = "unknown"
                        except:
                            process_name = "unknown"

                        processes.append(
                            {
                                "name": process_name,
                                "pid": pid,
                                "user": "unknown",
                                "local_address": local_address,
                                "state": state,
                                "full_line": line.strip(),
                            }
                        )
            return processes
        return []
    except (
        subprocess.TimeoutExpired,
        subprocess.CalledProcessError,
        FileNotFoundError,
    ):
        return []


def get_port_info_fallback(port):
    """Fallback method using Python's socket module."""
    try:
        # Try to connect to see if something is listening
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex(("127.0.0.1", port))
            if result == 0:
                return [
                    {
                        "name": "Unknown Process",
                        "pid": "unknown",
                        "user": "unknown",
                        "method": "socket_test",
                    }
                ]
        return []
    except:
        return []


def investigate_port(port):
    """Investigate what's using a specific port."""
    print(f"\n🔍 Investigating Port {port}")
    print("-" * 40)

    # Check if port is available first
    available = is_port_available(port)
    if available:
        print(f"✅ Port {port} is available (nothing using it)")
        return

    print(f"❌ Port {port} is occupied. Finding what's using it...")

    # Get system type
    system = platform.system().lower()

    # Try different methods based on OS
    processes = []
    if system in ["darwin", "linux"]:  # macOS or Linux
        processes = get_port_info_unix(port)
    elif system == "windows":
        processes = get_port_info_windows(port)

    # Fallback method if OS-specific methods fail
    if not processes:
        processes = get_port_info_fallback(port)

    if processes:
        print(f"📋 Found {len(processes)} process(es) using port {port}:")
        for i, proc in enumerate(processes, 1):
            print(f"   {i}. Process: {proc['name']}")
            print(f"      PID: {proc['pid']}")
            if "user" in proc:
                print(f"      User: {proc['user']}")
            if "local_address" in proc:
                print(f"      Address: {proc['local_address']}")
            if proc.get("method") != "socket_test":
                print(f"      Details: {proc.get('full_line', 'N/A')}")
    else:
        print(f"⚠️  Could not identify the process using port {port}")
        print(f"   This might be due to:")
        print(f"   - Insufficient permissions")
        print(f"   - Process running as different user")
        print(f"   - System-level service")


def show_kill_instructions(port, processes):
    """Show instructions for stopping processes using the port."""
    if not processes:
        return

    print(f"\n🛑 To free up port {port}:")
    print("-" * 30)

    system = platform.system().lower()

    for proc in processes:
        pid = proc["pid"]
        name = proc["name"]

        if pid != "unknown":
            print(f"🎯 To stop {name} (PID {pid}):")

            if system in ["darwin", "linux"]:
                print(f"   kill {pid}")
                print(f"   # Or force kill: kill -9 {pid}")
            elif system == "windows":
                print(f"   taskkill /PID {pid}")
                print(f"   # Or force: taskkill /F /PID {pid}")
            else:
                print(f"   Use your system's process manager to stop PID {pid}")
        else:
            print(f"🎯 To stop {name}:")
            print(f"   Use your system's task manager or process monitor")

    print(f"\n⚠️  WARNING: Only stop processes you recognize!")
    print(f"   Some system services should not be stopped.")


def check_common_culprits():
    """Check for common processes that use port 5000."""
    print(f"\n🔍 Common Port 5000 Users")
    print("=" * 30)

    common_culprits = {
        5000: [
            "AirPlay Receiver (macOS) - Control Center > Screen Mirroring",
            "Other Flask development servers",
            "Node.js development servers",
            "Docker containers with port mapping",
            "Webpack dev server",
            "React development server (sometimes)",
        ],
        5001: [
            "Secondary Flask apps",
            "Alternative development servers",
            "Synology NAS admin interface",
            "Other web development tools",
        ],
    }

    for port, culprits in common_culprits.items():
        print(f"\n📍 Port {port} commonly used by:")
        for culprit in culprits:
            print(f"   • {culprit}")


def main():
    """Main function to investigate ports used by PXT Web App."""
    print("🌐 PXT Web App - Port Investigation Tool")
    print("=" * 50)
    print("This tool helps identify what's using ports 5000 and 5001")

    # Check system info
    print(f"\n💻 System Information:")
    print(f"   OS: {platform.system()} {platform.release()}")
    print(f"   Python: {sys.version.split()[0]}")

    # Investigate key ports
    ports_to_check = [5000, 5001, 8000, 8080, 3000]
    occupied_ports = {}

    for port in ports_to_check:
        investigate_port(port)
        if not is_port_available(port):
            # Get process info for kill instructions
            system = platform.system().lower()
            if system in ["darwin", "linux"]:
                processes = get_port_info_unix(port)
            elif system == "windows":
                processes = get_port_info_windows(port)
            else:
                processes = get_port_info_fallback(port)

            if processes:
                occupied_ports[port] = processes

    # Show kill instructions for occupied ports
    for port, processes in occupied_ports.items():
        show_kill_instructions(port, processes)

    # Show common culprits
    check_common_culprits()

    print(f"\n🎯 Quick Commands for macOS/Linux:")
    print(f"   View all port usage: lsof -i -n -P")
    print(f"   Check specific port: lsof -i :5000")
    print(f"   Kill by PID: kill <PID>")

    print(f"\n🎯 Quick Commands for Windows:")
    print(f"   View all port usage: netstat -ano")
    print(f"   Kill by PID: taskkill /PID <PID>")

    print(f"\n🚀 PXT Web App Port Status:")
    pxt_port_5000 = is_port_available(5000)
    pxt_port_5001 = is_port_available(5001)

    if pxt_port_5000:
        print(f"   ✅ Ready to run on port 5000 (primary)")
    elif pxt_port_5001:
        print(f"   ⚠️  Will fallback to port 5001 (port 5000 occupied)")
    else:
        print(f"   ❌ Both ports 5000 and 5001 are occupied")
        print(f"      You may need to free up one of these ports")

    print(f"\n📝 Next Steps:")
    if occupied_ports:
        print(f"   1. Review the processes using your desired ports above")
        print(f"   2. Stop any unnecessary processes using the kill commands")
        print(f"   3. Run 'cd app && python3 app.py' to start PXT Web App")
    else:
        print(f"   1. All ports are available!")
        print(f"   2. Run 'cd app && python3 app.py' to start PXT Web App")


if __name__ == "__main__":
    main()
