# Python 3.12 Setup Instructions for PXT Web App

This guide will help you set up Python 3.12 and create a virtual environment for the PXT Web App project.

## Prerequisites

- A computer running macOS, Linux, or Windows
- Terminal/Command Prompt access
- Basic familiarity with command line operations

## Step 1: Install Python 3.12

### **macOS (Recommended Method - Using Homebrew)**

1. **Install Homebrew** (if you don't have it):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3.12**:
   ```bash
   brew install python@3.12
   ```

3. **Verify installation**:
   ```bash
   python3.12 --version
   # Should display: Python 3.12.x
   ```

### **macOS (Alternative - Direct Download)**

1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.12.x"
3. Run the installer and follow the prompts
4. Verify installation in Terminal:
   ```bash
   python3.12 --version
   ```

### **Windows**

1. Go to https://www.python.org/downloads/
2. Download Python 3.12.x for Windows
3. Run the installer
   - ✅ **IMPORTANT**: Check "Add Python to PATH"
   - ✅ Check "Install for all users" (optional)
4. Verify installation in Command Prompt:
   ```cmd
   python --version
   # or
   python3.12 --version
   ```

### **Linux (Ubuntu/Debian)**

```bash
# Update package list
sudo apt update

# Install Python 3.12
sudo apt install python3.12 python3.12-venv python3.12-pip

# Verify installation
python3.12 --version
```

## Step 2: Set Up the PXT Web App Virtual Environment

### **Navigate to Project Directory**

```bash
cd PXT_web_app
```

### **Remove Old Virtual Environment** (if it exists)

```bash
# Remove any existing PXT_app folder
rm -rf PXT_app
```

### **Create New Virtual Environment with Python 3.12**

**macOS/Linux:**
```bash
python3.12 -m venv PXT_app
```

**Windows:**
```cmd
python -m venv PXT_app
```
*Note: Use `python3.12` if you have multiple Python versions*

### **Activate the Virtual Environment**

**macOS/Linux:**
```bash
source PXT_app/bin/activate
```

**Windows (Command Prompt):**
```cmd
PXT_app\Scripts\activate
```

**Windows (PowerShell):**
```powershell
PXT_app\Scripts\Activate.ps1
```

### **Verify Virtual Environment**

After activation, you should see `(PXT_app)` at the beginning of your command prompt.

Verify Python version:
```bash
python --version
# Should show: Python 3.12.x
```

## Step 3: Install Project Dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- pandas (data processing)
- Werkzeug (web utilities)

**Expected output**: You should see successful installation messages for all packages.

## Step 4: Test the Installation

### **Run the Application**

```bash
cd app
python app.py
```

### **Test in Browser**

1. Open your web browser
2. Go to: `http://127.0.0.1:5000`
3. You should see the PXT Web App upload page

### **Test with Sample Data**

1. Upload the file: `../data/sample_peatland_data.csv`
2. Verify the data preview displays correctly

## Daily Workflow

### **Starting Work**

Every time you want to work on the project:

```bash
# Navigate to project
cd PXT_web_app

# Activate virtual environment
source PXT_app/bin/activate  # macOS/Linux
# or
PXT_app\Scripts\activate     # Windows

# Run the application
cd app
python app.py
```

### **Stopping Work**

When you're done:

```bash
# Stop the Flask server: Ctrl+C (Command+C on Mac)

# Deactivate virtual environment
deactivate
```

## Troubleshooting

### **"python3.12: command not found"**

**Solution**: Python 3.12 isn't installed or not in PATH
- Reinstall Python 3.12 following Step 1
- On Windows, make sure "Add Python to PATH" was checked

### **"No module named 'pandas'"**

**Solution**: Dependencies not installed or wrong environment
```bash
# Make sure virtual environment is activated (you should see (PXT_app))
source PXT_app/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **"Permission denied" errors**

**Solution**: Use appropriate permissions
- macOS/Linux: Add `sudo` if needed for system-wide installation
- Windows: Run Command Prompt as Administrator

### **Port already in use (5000)**

**Solution**: Another application is using port 5000
- Close other Flask applications
- Or modify `app.py` to use a different port:
  ```python
  app.run(debug=True, host="127.0.0.1", port=5001)
  ```

### **Virtual environment activation fails on Windows PowerShell**

**Solution**: Enable script execution
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## For Collaborators

### **First-time Setup**

If someone else set up the project, here's what you need to do:

1. **Clone/download the project** to your computer
2. **Follow Steps 1-3** above to install Python 3.12 and create your own virtual environment
3. **Don't commit the virtual environment** to version control (it should be in `.gitignore`)

### **Getting Updates**

When the project is updated:

```bash
# Activate your environment
source PXT_app/bin/activate

# Update dependencies
pip install -r requirements.txt

# Run the updated application
cd app
python app.py
```

## Project Structure After Setup

```
PXT_web_app/
├── PXT_app/                    # Virtual environment (don't commit to git)
│   ├── bin/ (or Scripts/)      # Python executables
│   ├── lib/                    # Installed packages
│   └── pyvenv.cfg             # Environment configuration
├── Documentation/              # Project documentation
├── app/                       # Web application code
├── data/                      # Sample data files
├── requirements.txt           # Python dependencies
└── README.md                  # Main project README
```

## Success Checklist

✅ Python 3.12 is installed and accessible  
✅ Virtual environment `PXT_app` is created  
✅ Virtual environment activates successfully (shows `(PXT_app)` in prompt)  
✅ Dependencies install without errors  
✅ Flask application runs at `http://127.0.0.1:5000`  
✅ Sample CSV data uploads and displays correctly  

## Getting Help

If you encounter issues not covered here:

1. **Check the main README.md** for additional troubleshooting
2. **Verify Python version**: `python --version` (should be 3.12.x)
3. **Verify virtual environment**: Should see `(PXT_app)` in terminal prompt
4. **Check installed packages**: `pip list` to see what's installed

---

**Next Steps**: Once setup is complete, see `README.md` for development workflow and project information.