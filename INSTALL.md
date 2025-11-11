# Install and Run

This project uses Python 3.13.9 and depends on Pillow. Tkinter is part of the Python standard library but depends on the system’s Tk. On macOS “Tahoe”, ensure a compatible Python/Tk combo is used.  

## Requirements
- Python 3.13.9
- Tk (for tkinter) available on your system
- pip

## macOS (Tahoe) setup

We recommend Homebrew Python to avoid Tk version issues.

```bash
# Install Python 3.13 via Homebrew
brew install python@3.13

# Create and activate a virtual environment
/opt/homebrew/bin/python3.13 -m venv .venv
source .venv/bin/activate

# Optionally ensure Tk is available (only if tkinter import fails)
# brew install tcl-tk
# export PATH="/opt/homebrew/opt/tcl-tk/bin:$PATH"
# export CPATH="/opt/homebrew/opt/tcl-tk/include"
# export LIBRARY_PATH="/opt/homebrew/opt/tcl-tk/lib"
```
If you hit a Tk version string mismatch, use the Homebrew Python above and ensure the environment variables point to Homebrew’s tcl-tk as shown.

## Linux
```
sudo apt-get update
sudo apt-get install -y python3.13 python3.13-venv python3-tk

python3.13 -m venv .venv
source .venv/bin/activate
```
## Windows
- Install Python 3.13.9 from python.org.
- During install, select “Install for all users” and “Add python to PATH”.
- Tkinter is included; if import fails, reinstall using the official installer.
### Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```
### Verify environment
```
python -c "import tkinter as tk; import PIL; print('Environment OK')"
```
### Run
```
python path/to/your_entrypoint.py
```
# Notes on dependencies
- tkinter is part of the stdlib and won’t appear in requirements.txt.
- requirements.txt only pins pip-managed packages (e.g., Pillow).
