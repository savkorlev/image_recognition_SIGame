import pyautogui
import keyboard


def press():
    keyboard.press_and_release('ctrl')


while keyboard.is_pressed('q') is False:
    if keyboard.is_pressed('w') is True:
        if pyautogui.pixel(1555, 340)[0] == 255:
            press()
