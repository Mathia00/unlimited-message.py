import pyautogui
import time
message = 3
while True:
    time.sleep(4)
    pyautogui.typewrite("Hello ! How are you?")
    time.sleep(2)
    pyautogui.press('enter')
    message = message - (1)
