import pyautogui

# Test screenshot
screenshot = pyautogui.screenshot()
screenshot.save("test_screen.png")

# Move mouse to top-left corner
pyautogui.moveTo(100, 100, duration=1)

# Display screen size
print("Screen size:", pyautogui.size())