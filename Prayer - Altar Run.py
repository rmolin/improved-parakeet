# TODO: make a 2nd run for the other bank stand

import pyautogui as py
import time
import random
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

# Bank dimensions
xleft1 = 1038
xright1 = 1071
yup1 = 477
ydown1 = 516
# Portable dimensions
xleft2 = 811
xright2 = 936
yup2 = 278
ydown2 = 365
# "Go to friends house" option menu
xleft3 = 273
xright3 = 504
yup3 = 895
ydown3 = 908
# left to right portal
xleft7 = 1724
xright7 = 1758
yup7 = 527
ydown7 = 562

#
xleft4 = 1724
xright4 = 1758
yup4 = 527
ydown4 = 562
# Select r1c1 randomly
xleft5 = 1633
xright5 = 1657
yup5 = 594
ydown5 = 617
# Select portal leaving
xleft5 = 1008
xright5 = 1014
yup5 = 545
ydown5 = 694
# r1c1
xleft6 = 1631
xright6 = 1659
yup6 = 596
ydown6 = 616


# Variables for program information
iterations = 0 # Count how many iterations
start_time = time.time() # Calculate time passed
# TODO: make the starting number a user input
# TODO: make sure valid answers are given -> https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

# Financials
#buysteelbar =
#sellcannonball =
#invprofit =

x = 1 # Code loop
while True:
    # Variables for clock and time management
    clock1 = float(random.uniform(.762, .827)) # Standard move between clicks
    clock2 = float(random.uniform(.352, .427)) # Custom deviation of clock1
    waitsteelbars = float(random.uniform(158, 163.1))
    runsleep = float(random.uniform(7.2, 7.4)) # Run = 6 | Walk = 12
    walksleep = float(random.uniform(11.4, 12.6)) # Run = 6 | Walk = 12
    processsleep = float(random.uniform(.98, 1.51))

    # Click objects in game randomly
    n = random.uniform(0, 100)
    topbar = float(random.uniform(400, 1244))
    xtab = float(random.uniform(xleft, xright)) # selecting tab
    ytab = float(random.uniform(yup, ydown))
    xinvtab = float(random.uniform(xleft4, xright4)) # selecting tab
    yinvtab = float(random.uniform(yup4, ydown4))
    xbank = float(random.uniform(xleft1, xright1)) # selecting tab
    ybank = float(random.uniform(yup1, ydown1))
    xportable = float(random.uniform(xleft2, xright2)) # selecting tab
    yportable = float(random.uniform(yup2, ydown2))
    xportoptions = float(random.uniform(xleft3, xright3)) # selecting tab
    yportoptions = float(random.uniform(yup3, ydown3))
    xr1c1 = float(random.uniform(xleft6, xright6)) # selecting tab
    yr1c1 = float(random.uniform(yup6, ydown6))
    xportal2 = float(random.uniform(xleft5, xright5)) # selecting tab
    yportal2 = float(random.uniform(yup5, ydown5))

    py.click(x = topbar, y = 0) # Click the top of a window
    time.sleep(1.3)
    py.moveTo(xbank, ybank, duration=clock1) # Click bank
    py.click()
    py.moveTo(514, 176, duration=clock1) # Options selecting an item in bank r1c1
    py.click(button = 'right')
    py.moveTo(553, 356, duration=clock1) # Select all but one from options
    py.click()
    # Begin run
    py.moveTo(1687, 149, duration=clock2)
    py.click()
    time.sleep(walksleep)
    py.moveTo(1697, 181, duration=clock2)
    py.click()
    time.sleep(walksleep)
    py.moveTo(1689, 169, duration=clock2)
    py.click()
    time.sleep(walksleep)
    py.moveTo(1707, 142, duration=clock2)
    py.click()
    time.sleep(walksleep)
    py.moveTo(xportable, yportable, duration=clock1) # Click the portal
    py.click()
    time.sleep(processsleep)
    py.moveTo(xportoptions, yportoptions, duration=clock1) # Select friends house from options
    py.click()
    time.sleep(processsleep)
    if iterations == 0:
         input('enter portal, then press ANY KEY')
    #    playerhouse = input('enter POH name: ')
    #    py.press(playerhouse) # Enter poh name
    #    time.sleep(processsleep)
    #    py.press('enter')
    else:
        py.moveTo(445, 812, duration=clock1)
        py.click()
    time.sleep(1)
    py.moveTo(1677, 228, duration=clock1) # Toggle run
    py.click()
    py.moveTo(xinvtab, yinvtab, duration=clock1) # Click inventory tab
    py.click()
    py.moveTo(xr1c1, yr1c1, duration=clock1)
    py.click(button = 'right')
    py.moveRel(xOffset=None, yOffset=62, duration=clock1)
    py.click()
    py.moveTo(897, 153, duration=clock1) # Click altar
    py.click()
    time.sleep(66)
    m = float(random.uniform(0, 1))
    if m > .70:
        py.moveTo(xtab, ytab, duration=clock1/2)
        py.click()
    py.click(x = topbar, y = 0) # Click the top of a window
    # Begin run back to bank
    time.sleep(processsleep)
    py.moveTo(1796, 197, duration=clock1) # Go to portal in house
    py.click()
    time.sleep(runsleep)
    py.moveTo(996, 613, duration=clock1)
    py.click()
    time.sleep(runsleep)
    py.moveTo(1904, 196, duration=clock1)
    py.click()
    time.sleep(runsleep)
    py.moveTo(1908, 142, duration=clock1)
    py.click()
    time.sleep(runsleep)
    py.moveTo(1908, 142, duration=clock1)
    py.click()
    time.sleep(runsleep)
    py.moveTo(1877, 173, duration=clock1)
    py.click()
    time.sleep(runsleep)       
    py.moveTo(1677, 228, duration=clock1) # Toggle run
    py.click() 

    # Progarm information
    iterations += 1
    profit = format(iterations * 252, ',d') 
    barsused = format(iterations * 28, ',d')
    elapsed_time = ((time.time() - start_time))/60
    print('Iterations:',iterations, '| Bones Used:',barsused, '| XP Gained:',profit, '| Minutes passed:',elapsed_time)

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
