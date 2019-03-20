import pyautogui as py
import time
import random


py.FAILSAFE = True
while True:
    try:
        x = 1851
        y = 755
        t1 = random.uniform(.58, .801)
        py.PAUSE = t1
        py.click(x, y)
        py.PAUSE = t1
        py.click(x,y)
        py.PAUSE = t1
        py.press('space')
        py.press('1')
        that = random.uniform(0, 1)
        if that >= .915:
            this = random.uniform(3, 8)
            time.sleep(this)


    except:
        break
