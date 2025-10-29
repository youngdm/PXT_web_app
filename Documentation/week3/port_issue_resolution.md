# Port Issue Resolution Summary - PXT Web App

## Problem Identified
The PXT Web App was reporting "both ports 5000 and 5001 are unavailable" even when port 5001 was actually free. This was preventing the Flask application from starting properly.

## Root Cause Analysis

### Investigation Results
Using the port investigation tool (`investigate_ports.py`), we discovered:

1. **Port 5000**: Occupied by `ControlCenter` (PID varies)
   - This is macOS AirPlay Receiver service
   - Normal system service that enables screen mirroring functionality
   - Runs automatically when AirPlay Receiver is enabled in System Settings

2. **Port 5001**: Actually available
   - No processes were using this port
   - System commands confirmed it was free: `lsof -i :5001` returned nothing

### The Flask Debug Mode Issue
The real problem was **Flask's debug mode reloader mechanism**:

1. Main Flask process starts and checks ports → finds 5001 available
2. Flask starts on port 5001 successfully
3. Flask debug mode enables **automatic reloader**
4. Reloader process tries to restart the app
5. **During restart**, reloader runs port check again
6. Now port 5001 appears occupied (by the original Flask process)
7. Port checking logic incorrectly reports "both ports unavailable"
8. Application exits with error

## Solution Implemented

### Code Fix in `app.py`
Added detection for Flask's reloader process using the `WERKZEUG_RUN_MAIN` environment variable:

```python
# Check if we're running in Flask's reloader process
if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    # This is the reloader process - Flask already chose the port
    # Just run without port checking
    app.run(debug=True, host="127.0.0.1", port=int(os.environ.get("FLASK_PORT", 5001)))
else:
    # This is the main process - do port selection
    # [Original port selection logic here]
    os.environ["FLASK_PORT"] = str(port)
    app.run(debug=True, host="127.0.0.1", port=port)
```

### How the Fix Works
1. **Main Process**: Runs full port detection and selection logic
2. **Sets Environment Variable**: `FLASK_PORT` stores the chosen port
3. **Reloader Process**: Skips port detection, uses stored port from environment
4. **No Port Conflicts**: Reloader doesn't compete with main process

## Testing Results

### Before Fix
```
⚠️  Port 5000 is busy, using fallback port 5001
🚀 Starting PXT Web App on http://127.0.0.1:5001
 * Running on http://127.0.0.1:5001
 * Restarting with stat
❌ Both ports 5000 and 5001 are unavailable.
   Please stop other applications using these ports and try again.
```

### After Fix
```
⚠️  Port 5000 is busy, using fallback port 5001
🚀 Starting PXT Web App on http://127.0.0.1:5001
 * Running on http://127.0.0.1:5001
 * Restarting with stat
 * Debugger is active!
✅ Application running successfully
```

## Port Usage Summary

### Current System Status
- **Port 5000**: Occupied by macOS AirPlay Receiver (ControlCenter)
- **Port 5001**: Available for PXT Web App
- **Fallback mechanism**: Working correctly
- **Flask debug mode**: Compatible with port selection

### User Options
1. **Recommended**: Keep AirPlay, use port 5001 automatically
2. **Alternative**: Disable AirPlay to free port 5000
   - System Settings → General → AirDrop & Handoff → Turn off "AirPlay Receiver"
3. **Temporary**: Kill AirPlay process (will restart automatically)

## Tools Created for Troubleshooting

### `investigate_ports.py`
- Comprehensive port investigation tool
- Identifies processes using specific ports
- Works on macOS, Linux, and Windows
- Provides kill commands for process cleanup

### `demo_port_fallback.py`
- Demonstrates port selection logic
- Shows expected behavior for different scenarios
- Educational tool for understanding port conflicts

### Key Commands for Future Reference

#### Check Port Usage (macOS/Linux)
```bash
lsof -i :5000          # Check specific port
lsof -i -n -P          # All network connections
netstat -an | grep 5000 # Alternative method
```

#### Check Port Usage (Windows)
```cmd
netstat -ano | findstr 5000
tasklist /FI "PID eq <PID>"
```

#### Kill Process
```bash
kill <PID>              # Graceful termination
kill -9 <PID>           # Force kill (macOS/Linux)
taskkill /PID <PID>     # Windows
```

## Prevention Strategies

### For Development
1. **Always use debug mode carefully** - understand reloader behavior
2. **Check system services** that commonly use development ports
3. **Use port investigation tools** before troubleshooting
4. **Consider port ranges** (5000-5010) for multiple projects

### For Production
1. **Disable debug mode** - `debug=False` eliminates reloader issues
2. **Use specific ports** - avoid common conflict ranges
3. **Implement health checks** - verify port availability before deployment
4. **Document port assignments** - track which services use which ports

## Lessons Learned

1. **Debug Mode Complexity**: Flask's reloader creates additional processes that can interfere with port detection
2. **Environment Variables**: Useful for passing information between main and reloader processes  
3. **System Services**: macOS AirPlay commonly occupies port 5000, requiring fallback strategies
4. **Investigation Tools**: Essential for diagnosing port conflicts accurately
5. **User Experience**: Clear messaging about port selection improves developer experience

## Final Status
✅ **RESOLVED**: PXT Web App now starts successfully with automatic port fallback
✅ **TESTED**: Both port selection and Flask debug mode working correctly
✅ **DOCUMENTED**: Complete investigation and solution process recorded
✅ **TOOLS**: Port investigation utilities available for future troubleshooting

The application is now robust against common port conflicts and provides a smooth development experience.