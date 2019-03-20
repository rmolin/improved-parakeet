import pyautogui as py
import time
import random

py.FAILSAFE = True

# Clicks an x and y on screen
def clickSpot(x, y, time):
    py.moveTo(x, y, duration = time)
    py.click()

THISLOGPATH = "THISLOGPATH.TXT"

# Variables for program information
iterations = 0 # Count how many iterations
start_time = time.time() # Calculate time passed
timestr = time.strftime("%Y-%m-%d %H%M%S") # String for the current date and time

#indefinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
x = 1
while True:
    clock = float(random.uniform(3.30, 3.77))
    xtop = float(random.uniform(946, 990))
    ytop = float(random.uniform(405, 449))
    xright = float(random.uniform(1050, 1084))
    yright = float(random.uniform(508, 552))

    # Mine rock
    clickSpot(xtop, ytop, .01)
    time.sleep(clock)
    py.moveTo(1641, 661)
    py.PAUSE = .2
    py.keyDown('shift')
    py.click(button='left')
    py.keyUp('shift')
    clickSpot(xright, yright, .01)
    time.sleep(clock)
    py.moveTo(1711, 660)
    py.PAUSE = .2
    py.keyDown('shift')
    py.click(button='left')
    py.keyUp('shift')

    # Progarm information
    iterations += 1
    profit = format(iterations * 35, ',d')
    elapsed_time = ((time.time() - start_time))/60
    print('Iterations:',iterations, '| Total XP:',profit, '| Minutes passed:',elapsed_time)
    # Write program information to a text file
    if iterations >= 11:
        iiterations = 'Itarations: ' + str(iterations) + ' | xp: ' + str(profit) + ' | Minutes passed: ' + str(elapsed_time) + ' | Date: ' + str(timestr) + '\n'
        f = open(THISLOGPATH,"a")
        f.write(iiterations)

x += 1
