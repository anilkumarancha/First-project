import time
import pyautogui

# Function to close all open tabs
def close_all_tabs():
    while True:
        pyautogui.hotkey('ctrl', 'w')  # Close the current tab
        time.sleep(0.1)  # Small delay to let the tab close
        # Add a condition to break the loop if necessary (e.g., check if no tabs are left)

# Call the function
close_all_tabs()