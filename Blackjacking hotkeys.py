import pyautogui as py
import random
import time
import keyboard

py.FAILSAFE = True

def rightClickSpot(x, y, time):
    py.moveTo(x, y, duration = time)
    py.rightClick()

while True: #making a loop
    try: #used try so that if user pressed other than the given key error will not be shown

        # Variables for clock and time manag ement
        clock1 = float(random.uniform(.05, .1)) # Standard move between clicks
        runToBank = float(random.uniform(6.32, 6.98))
        topbar = float(random.uniform(400, 1244))

        if keyboard.is_pressed(','): #if key is pressed
            py.rightClick()
            py.moveRel(yOffset=105, duration=clock1)
            py.click()
            py.moveRel(yOffset=-105, duration=clock1)
        elif keyboard.is_pressed('.'):
            py.rightClick()
            py.moveRel(yOffset=64, duration=clock1)
            py.click()
            py.moveRel(yOffset=-64, duration=clock1)
    except:
        break
