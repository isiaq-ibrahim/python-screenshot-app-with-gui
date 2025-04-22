# python-screenshot-app

Python Screenshot App is an application I have developed using Python. The application allows users to take a screenshot of their screen and save it as an image file format, e.g., .jpeg, .png, .jpg, etc. It saves the image into a folder named screensnaps (this can be modified in the Python file).


## How to install and run this project
1. First, you must download Python (python.org) and install it on your machine. Install Python 3.10 - 3.11 due to compatibility issues with PyAutoGUI.

✅ Recommended Python Versions for PyAutoGUI
PyAutoGUI and its dependencies (like pyscreeze, pillow, etc.) are best supported on:
- Python 3.6 → 3.11

🟢 Python 3.10 and 3.11 are currently the most stable for PyAutoGUI.

⚠️ Python 3.12+ Issues

Some versions of Pillow, which is used by pyscreeze (and indirectly by pyautogui), had compatibility issues with Python 3.12 in earlier releases.

PyAutoGUI hasn't been officially updated to declare Python 3.12 support in all cases.

2. After successfully installing Python, launch your command prompt and verify that it has been successfully installed and also to check the current version.

```
python --version
```

If you’re using Python 3.12 or newer, some packages (like Pillow) might not be fully compatible depending on the version.

3. Start the command prompt again, but this time as an administrator. We need to install a library package called PyAutoGUI. To install this, run the following script in your terminal:

```
pip install virtualenv
```

This script allows us to create multiple virtual environment for our other projects.



4. 






🚀 Features
- Capture full-screen screenshots with a single command
- Automatically saves screenshots with random integer filenames
- Cross-platform support (Windows, macOS, Linux)
- Simple and beginner-friendly Python codebase

🛠️ Built with
- Python 3.10.7
- PyAutoGUI

📂 Installation
```
pip install pyautogui
```

📷 Usage
```
python screenshot_app.py
```
