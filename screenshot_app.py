import time
import pyautogui
import tkinter as tk

def screenshot():
    #added to generate a random int number for the image
    name = int(round(time.time() * 1000))
    
    # this will save the screenshots in the folder screensnaps and in .png format
    name = 'C:/Users/ibrah/Documents/LearnPythonProjects/screensnaps/{}.png'.format(name)
    
    # time.sleep(5) was removed because I don't want the screenshot to be taken after 5 seconds rather I want it to be taken when I clicked on the 'Take Screenshot' button
    #removed 'test.png' and replaced with name
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# this function creates a button 'Take Screenshot' which allows the user to take a screenshot
button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot)

button.pack(side=tk.LEFT)

# this function creates a button 'Quit' which allows the user to close the GUI
close = tk.Button(
    frame,
    text="Quit",
    command=quit)

close.pack(side=tk.LEFT)

root.mainloop()