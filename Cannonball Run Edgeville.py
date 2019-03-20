# TODO: make a 2nd run for the other bank stand

import pyautogui as py
import random
import time
import sys
import tkinter
from tkinter import messagebox
import ctypes


py.FAILSAFE = True

# Variables for randomly clicking a tab (inv, skills, equip, etc.)
xleft = 1580
xright = 1890
yup = 523
ydown = 568
# ...down bank
xleft1 = 939
xright1 = 988
yup1 = 571
ydown1 = 574

# Variables for program information
iterations = 0 # Count how many iterations
start_time = time.time() # Calculate time passed
# TODO: make the starting number a user input
# TODO: make sure valid answers are given -> https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
checkpoint = input('Enter "y" to add a checkpoint: ')
tab = input('Enter "y" to tab after initiating making cannonballs: ')

x = 1 # Code loop
while True:
    # Variables for clock and time management
    clock1 = float(random.uniform(.762, .827)) # Standard move between clicks
    clock2 = float(random.uniform(.352, .427)) # Custom deviation of clock1
    clock3 = float(random.uniform(1.11, 3.77)) # selecting inv tab
    waitsteelbars = float(random.uniform(158, 163.1))

    topbar = float(random.uniform(400, 1244))
    n = random.uniform(0, 100)
    xtab = float(random.uniform(xleft, xright)) # selecting tab
    ytab = float(random.uniform(yup, ydown))
    xbank = float(random.uniform(xleft1, xright1)) # selecting tab
    ybank = float(random.uniform(yup1, ydown1))

    py.click(x = topbar, y = 0) # Click the top of a window
    time.sleep(1.3)
    py.moveTo(xbank, ybank, duration = clock1) # Click bank
    py.click()
    py.moveTo(514, 176, duration = clock1) # Options selecting an item in bank
    py.click(button = 'right')
    py.moveTo(553, 356, duration = clock1) # Select from options
    py.click()
    py.moveTo(1875, 132, duration = clock2) # Run to furnace
    py.click()
    time.sleep(5.76)
    py.moveTo(1070, 491, duration = clock2) # Click furnace
    py.click()
    time.sleep(1.24)
    py.press('space') # Initiate making cannonballs
    m = float(random.uniform(0, 1))
    if m > .70:
        py.moveTo(xtab, ytab, duration = clock1/2)
        py.click()
    if tab == 'y':
        py.hotkey('alt', 'tab')
    time.sleep(waitsteelbars) # Cannonballs cooking
    if checkpoint == 'y':
        ctypes.windll.user32.MessageBoxW(0, 'Proceed with cannonballs?', 'Checkpoint', 0)
    py.click(x = topbar, y = 0) # Click the top of a window
    py.moveTo(1718, 191, duration = clock1)
    py.click()
    time.sleep(5.01)

    # Progarm information
    iterations += 1
    profit = format(iterations * 6162, ',d')
    barsused = format(iterations * 26, ',d')
    elapsed_time = ((time.time() - start_time))/60
    print('Iterations:',iterations, '| Bars Used:',barsused, '| Profit:',profit, '| Minutes passed:',elapsed_time)

x += 1 # Repeat


########### END

# def waitbars(entertime):
#    for i in range(entertime,0,-1):
#        time.sleep(1)
#        print(i) # Print a countdown of time remaining

##  Styles: (~LINE 62)
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No
##  6 : Cancel | Try Again | Continue
