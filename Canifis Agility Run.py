import pyautogui as py
import time
import random


py.FAILSAFE = True

# Variables for clock and time management
clock1 = float(random.uniform(.35, .55)) # Standard move between clicks
clock2 = float(random.uniform(.352, .427)) # Custom deviation of clock1
clock3 = float(random.uniform(1.11, 3.77)) # selecting inv tab
waitsteelbars = float(random.uniform(158, 163.1))
topbar = float(random.uniform(400, 1244))


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
    py.click(x = topbar, y = 0) # Click the top of a window
    time.sleep(1.25)
    py.moveTo(911, 490, duration=clock1) # climb tree
    py.click()
    time.sleep(8.5)
    py.moveTo(927, 396, duration=clock1) # jump gap
    py.click()
    time.sleep(6.5)
    py.moveTo(810, 531, duration=clock1) # jump 2nd gap
    py.click()
    time.sleep(6.5)
    py.moveTo(775, 643, duration=clock1) # jump 3rd gap
    py.click()
    time.sleep(6.5)
    py.moveTo(909, 707, duration=clock1) # jump 4th gap
    py.click()
    time.sleep(6.5)
    py.moveTo(978, 591, duration=clock1) # pole vault
    py.click()
    time.sleep(9.5)
    py.moveTo(1262, 542, duration=clock1) # jump gap
    py.click()
    time.sleep(9.5)
    py.moveTo(930, 387, duration=clock1) # jump 2nd gap
    py.click()
    time.sleep(8.5)
    py.moveTo(885, 468, duration=clock1) # go to start point
    py.click()
    time.sleep(4.5)

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
