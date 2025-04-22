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

3. Start the command prompt again, but this time as an administrator. You need to install a library package called PyAutoGUI. To install this, run the following script in your terminal:

```
pip install virtualenv
```
The command pip install virtualenv installs the virtualenv package using Python's package manager, pip.

🔍 What is virtualenv?

virtualenv is a tool used to create isolated Python environments. Each virtual environment has its own installation directories, separate from the global Python environment. This is useful for:
- Avoiding conflicts between dependencies of different projects.
- Working on projects with different Python versions or packages.
- Keeping your system’s Python environment clean and stable.

✅ What happens when you run pip install virtualenv?

When you run the command:
```
pip install virtualenv
```

- pip connects to the Python Package Index (PyPI).
- It downloads the latest version of the virtualenv package.
- It installs the package into your current Python environment (usually system-wide or in an existing virtual environment, depending on how pip is configured).

🛠️ After installing, you can create a virtual environment like this:

```
virtualenv [myenv]
```
In my case, I use 'virtualenv pyautoenv' (you will find this in the repository with others I had previously created, like projectsenv and pythonprojects). I ran this script in the command prompt while in the directory where I am going to write my Python code. Then activated it by running:

```
pyautoenv\Scripts\activate
```
After completing all these steps, navigate to the folder you will be working with and create a Python file (screenshot_app.py). Alternatively, you can create this in your text code editor like VSCode, Sublime Text, or Notepad++.

4. Download and install VSCode (code.visualstudio.com), open the folder on your computer in VSCode, and then open the screenshot_app.py file in VSCode. Copy and paste this:

```
import time
import pyautogui

def screenshot():
    time.sleep(5)
    img = pyautogui.screenshot('test.png')
    img.show()

screenshot()
```

To run this code, go to the terminal and run 'python screenshot_app.py'. A screenshot of your screen will be taken after five seconds (this is because I have specified 5 in the code. Of course, you can modify this.) If you run the program one more time, it overrides the file 'test.png'. To solve this problem of file overwrite, I added the following line of code under 'def screenshot()'

```
import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    time.sleep(5)
    img = pyautogui.screenshot('test.png')
    img.show()

screenshot()
```
Summary of the code:
- `import pyautogiu` -> This imports the pyautogui library, which is used for GUI automation. It can control the mouse and keyboard, and also take screenshots.
- `import time` -> This imports Python's built-in `time` module, which allows you to work with time-related functions, like delays (`sleep`) or getting the current timestamp (`time()`).
- `def screenshot():` -> This defines a function named `screenshot`. Everything indented below it belongs to this function.
- `name = int(round(time.time() * 1000))`:
    - `time.time()` returns the current time in seconds since the Unix epoch.
    - Multiplying by `1000` converts it to milliseconds.
    - `round()` rounds the number to the nearest integer.
    - `int(...)` ensures it’s an integer.

