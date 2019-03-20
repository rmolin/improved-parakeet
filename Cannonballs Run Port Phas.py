import pyautogui as py
import time
import random
import sys
import tkinter
from tkinter import messagebox


py.FAILSAFE = True

clock1 = float(random.uniform(.752, .827)) # Standard move between clicks
clock2 = float(random.uniform(.352, .427)) # Custom deviation of clock1
clock3 = float(random.uniform(1.11, 3.77)) # selecting inv tab
waitsteelbars = float(random.uniform(161, 162.1))

# RNG for which tab to open
# Random variable needs to be local otherwise it wont change each run
combat = 9 #.09
skills = 18 #.09
quests = 23 #.05
inv = 73 #.5
equip = 86 #.13
pray = 91 #.05
spells = 94.5 #.035
friends = 98.5 #.035

# Variables for randomly clicking a tab
xleft = 1580
xright = 1890
yup = 523
ydown = 568


def waitbars(entertime):
    for i in range(entertime,0,-1):
        time.sleep(1)
        print(i) # Print a countdown of time remaining


#infinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
x = 1
while True:

    # Variables that need to change each iteration
    n = random.uniform(0, 100)
    topbar = float(random.uniform(400, 1244))
    xswish = float(random.uniform(xleft, xright)) # selecting tab
    yswish = float(random.uniform(yup, ydown))

    py.click(x = topbar, y = 0) # Click the top of a window
    time.sleep(1.3)
    py.moveTo(970, 612, duration = clock1) # Click bank
    py.click()
    py.moveTo(514, 176, duration = clock1) # Options selecting an item in bank
    py.click(button = 'right')
    py.moveTo(553, 356, duration = clock1) # Select from options
    py.click()
    py.moveTo(1109, 66, duration = clock2) # Exit bank
    py.click()
    py.moveTo(1780, 83, duration = clock2) # Run to furnace
    py.click()
    time.sleep(6.35)
    py.moveTo(1080, 490, duration = clock2) # Click furnace
    py.click()
    time.sleep(1.323)
    py.press('space') # Initiate making cannonballs

    m = float(random.uniform(0, 1))
    if m > .50:
        py.moveTo(xswish, yswish, duration = clock1/2)
        py.click()
        print('Switch')
    else:
        print('No Switch')
    time.sleep(waitsteelbars) # Cannonballs cooking
    py.click(x = topbar, y = 0) # Click the top of a window
    py.moveTo(1816, 250, duration = clock1)
    py.click()
    time.sleep(5.6)

# repeat
x += 1
