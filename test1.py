import pyautogui as py
import time

time.sleep(2)
for i in range(100):
    py.write("Beti")
    time.sleep(1)
    py.press("enter")
