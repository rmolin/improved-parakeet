
import pyautogui as py
import random
import time
import keyboard

py.FAILSAFE = True

def clickSpot(x, y, time):
    py.moveTo(x, y, duration = time)
    py.click()

while True: #making a loop
    try: #used try so that if user pressed other than the given key error will not be shown

        # Variables for clock and time manag ement
        clock1 = float(random.uniform(.22, .32)) # Standard move between clicks
        runToBank = float(random.uniform(6.32, 6.98))
        topbar = float(random.uniform(400, 1244))

        if keyboard.is_pressed(','): #if key is pressed
            clickSpot(843, 474, clock1)
        elif keyboard.is_pressed('.'):
            clickSpot(955, 582, clock1)
        elif keyboard.is_pressed('-'):
            clickSpot(1783, 113, clock1)
            time.sleep(runToBank)
            clickSpot(894, 532, clock1)
            clickSpot(1049, 733, 1.5)
            clickSpot(1701, 209, 1.5)
    except:
        break
