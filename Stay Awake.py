import pyautogui as py
import time
import random


py.FAILSAFE = True

x = 1
while True:

    z = float(random.uniform(60.1, 180))
    py.click(1601, 679)
    time.sleep(z)

x += 1
