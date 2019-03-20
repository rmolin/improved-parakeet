import pyautogui as py
import time

py.FAILSAFE = True

clock1 = .75

x = 1
while True:
    time.sleep(1)
    py.moveTo(1644, 610, duration = clock1)
    py.click()
    py.moveTo(1706, 613, duration = clock1)
    py.click()
    time.sleep(1.5)
    py.press('space')
    time.sleep(9.5)

x += 1
