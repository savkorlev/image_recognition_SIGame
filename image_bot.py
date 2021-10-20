import pyautogui
import keyboard

def press():
    keyboard.press_and_release('ctrl')

while keyboard.is_pressed('q') == False:
    while keyboard.is_pressed('w') == True:
        if pyautogui.pixel(1555, 340)[0] == 255:
            press()