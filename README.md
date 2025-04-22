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

🔹 This is often used to create a unique timestamp, which could be useful as a filename.

🟡 But in this case, the variable name is calculated but not used — a small inefficiency.

- `time.sleep(5)`-> This pauses the program for **5 seconds** before taking the screenshot. This gives you time to switch windows or get your screen ready.
- `img = pyautogui.screenshot('test.png')`
    - This takes a screenshot of the entire screen.
    - The image is saved as `'test.png'` in the current working directory.
    - The screenshot is also stored in the variable `img` as an image object (Pillow `Image` type).
- `img.show()` -> This opens the screenshot in the default image viewer on your system (Windows Photo Viewer, Preview on macOS, etc.).
- `screenshot()` -> This calls the `screenshot()` function, so the code actually runs.

🔍 Summary of Behavior:
1. It waits 5 seconds.
2. Captures a screenshot of the entire screen.
3. Saves it as 'test.png'.
4. Opens the image for preview.

This marks the end of the implementation of the Python Screenshot App (Note: This does not include the GUI. The app automatically takes a screenshot of the screen after 5 seconds.) Now let's look at how to improve this project to include a Graphics User Interface where the user can click on a button to take a screenshot rather than waiting for five seconds.

You can overwrite the `screenshot_app.py` and paste the following codes in the file.

```
import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/ibrah/Documents/LearnPythonProjects/screensnaps/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot)

button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text="Quit",
    command=quit)

close.pack(side=tk.LEFT)

root.mainloop()
```

### Explanation of the code:
#### ✅ Imports
```
import time
import pyautogui
import tkinter as tk
```

- `time` is used to generate a unique timestamp for naming the screenshot file.
- `pyautogui` is a module that can control the mouse and keyboard and also take screenshots.
- `tkinter` is a Python standard GUI toolkit, used to create graphical interfaces.

#### ✅ screenshot() Function
```
def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/ibrah/Documents/LearnPythonProjects/screensnaps/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()
```

- `time.time()` returns the current time in seconds since epoch.
- Multiplying by `1000` and rounding gives a millisecond-accurate timestamp to name the screenshot uniquely.
- The path `'C:/Users/ibrah/Documents/LearnPythonProjects/screensnaps/'` is formatted with this timestamp to save the screenshot. `{}.png` saves the screenshot in .png photo format.
- `pyautogui.screenshot(name)` takes a screenshot and saves it to the specified path.
- `img.show()` opens the saved image using the default image viewer.

#### ✅ Creating the GUI
```
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
```

- `root = tk.Tk()`: Creates the main application window.
- `tk.Frame(root)`: Creates a frame widget to hold the buttons.
- `frame.pack()`: Adds the frame to the main window.

#### ✅ "Take Screenshot" Button
```
button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot)
button.pack(side=tk.LEFT)
```

- A button is created with the label "Take Screenshot".
- When clicked, it calls the `screenshot()` function.
- `side=tk.LEFT`: Aligns the button to the left inside the frame.

#### ✅ "Quit" Button
```
close = tk.Button(
    frame,
    text="Quit",
    command=quit)
close.pack(side=tk.LEFT)
```

- Another button labeled "Quit" is created.
- When clicked, it exits the application.

#### ✅ Run the GUI Loop
```
root.mainloop()
```

- Starts the tkinter event loop, waiting for user interactions (like button clicks).


📝 Summary

This code opens a small window with two buttons:
- 📸 "Take Screenshot": Captures and saves a screenshot to a specific folder.
- ❌ "Quit": Closes the application.

▶️ [[Watch Demo Video](assets/video-thumbnail.png)](https://drive.google.com/file/d/169izlwK6HUbpvnXKuDunrLVAfKQCMYbQ/view?usp=sharing)

The full code is beginner-friendly and could be a great reference for anyone looking to dip their toes into automation and Python scripting.

🌟 Contributing
Feel free to fork, improve, and submit pull requests! This is a great project to start learning Python scripting and GUI automation.

📬 Contact
For questions, suggestions, or collaborations, connect with me on LinkedIn (https://www.linkedin.com/in/isiaq-ibrahim-468588156/).

⭐ Don't forget to give it a star if you find it helpful!
