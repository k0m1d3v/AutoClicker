import pyautogui
import keyboard

isEnabled = False


def click():
    while isEnabled:
        pyautogui.click()


def stop():
    isEnabled = False


startKey = input("insert start key ")
keyboard.add_hotkey(startKey, click)
stopKey = input("insert stop key ")
keyboard.add_hotkey(stopKey, stop)
