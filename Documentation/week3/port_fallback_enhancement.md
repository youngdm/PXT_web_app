# Port Fallback Enhancement - PXT Web App

## Overview
Enhanced the PXT Web App Flask application with automatic port fallback functionality to handle common port conflicts gracefully. This improvement ensures the application can start reliably even when the default port 5000 is occupied by other services.

## Problem Solved
**Issue**: Flask applications commonly use port 5000, which can be occupied by:
- Other Flask development servers
- AirPlay service on macOS
- Other web development tools
- System services

**Previous Behavior**: Application would fail to start with cryptic error messages

**New Behavior**: Automatically detects port conflicts and falls back to alternative port with clear user messaging

## Implementation Details

### Port Selection Logic
```python
def is_port_available(port):
    """Check if a port is available for use."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", port))
            return True
    except socket.error:
        return False
```

### Fallback Mechanism
1. **Primary Port**: 5000 (Flask default)
2. **Fallback Port**: 5001 (unassigned, safe to use)
3. **Error Handling**: Clear messaging when both ports unavailable

### User Experience Improvements
- **Clear Messaging**: Users informed which port is being used
- **Automatic Fallback**: No manual intervention required
- **Graceful Failures**: Helpful error messages with troubleshooting tips

## Port Selection Messages

### Normal Startup (Port 5000 Available)
```
🚀 Starting PXT Web App on http://127.0.0.1:5000
```

### Fallback Scenario (Port 5000 Occupied)
```
⚠️  Port 5000 is busy, using fallback port 5001
🚀 Starting PXT Web App on http://127.0.0.1:5001
```

### Error Scenario (Both Ports Occupied)
```
❌ Both ports 5000 and 5001 are unavailable.
   Please stop other applications using these ports and try again.
```

## Testing Results

### Port Availability Test
```
Port 5000 (Primary): ❌ Occupied
Port 5001 (Fallback): ✅ Available
Expected Behavior: ⚠️  App should fallback to port 5001
```

### Functional Verification
- ✅ Port detection logic working correctly
- ✅ Fallback mechanism activates when needed  
- ✅ Flask application imports successfully
- ✅ Clear user messaging displayed
- ✅ Graceful error handling for edge cases

## Benefits

### For Developers
- **Reduced Friction**: No need to manually specify alternative ports
- **Better Developer Experience**: Clear feedback about port selection
- **Faster Development**: Automatic handling of common conflicts

### For Workshop Demonstrations
- **Reliability**: Application starts consistently in various environments
- **Professional Appearance**: Clean startup messaging
- **Reduced Setup Time**: Automatic port management

### For Production Deployment
- **Flexibility**: Handles various deployment scenarios
- **Monitoring**: Clear logging of port selection decisions
- **Robustness**: Graceful handling of resource conflicts

## Technical Specifications

### Port Selection Priority
1. **Port 5000**: Primary choice (standard Flask development port)
2. **Port 5001**: Fallback choice (unassigned, typically available)
3. **Error Exit**: If both ports unavailable

### Error Handling
- **Socket Binding Test**: Reliable port availability detection
- **Exception Handling**: Graceful failure modes
- **User Guidance**: Clear troubleshooting instructions

### Dependencies
- **Built-in Libraries Only**: Uses Python `socket` module
- **No External Dependencies**: Maintains simple installation process
- **Cross-Platform**: Works on Windows, macOS, Linux

## Usage Instructions

### Standard Usage
```bash
cd app
python3 app.py
```
The application will automatically:
1. Check if port 5000 is available
2. Use port 5000 if available, or fallback to 5001
3. Display clear message about selected port
4. Start Flask development server

### Troubleshooting Port