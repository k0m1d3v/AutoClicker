import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

ToggleKey = KeyCode(char="cc")

isClicking = False
mouse = Controller()

def clicker():
    while True:
        if isClicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)

def toggle_listener(key):
    if key == ToggleKey:
        global isClicking
        isClicking = not isClicking

clickThread = threading.Thread(target=clicker)
clickThread.start()

with Listener(on_press=toggle_listener) as listener:
    listener.join()