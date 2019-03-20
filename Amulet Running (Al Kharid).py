import pyautogui as py
import time
import random

py.FAILSAFE = True

# Variables for program information
iterations = 0 # Count how many iterations
start_time = time.time() # Calculate time passed

loadPerInv = 26
xpPerRaw = 30
priceOfRaw = 80
priceOfFinished = 124
profit = priceOfFinished - priceOfRaw

def clickSpot(x, y, time):
    py.moveTo(x, y, duration = time)
    py.click()

# Generates a random number
def getRandomNumber(x, y):
    return float(random.uniform(x, y))
# Puts a random number in a variable
rn = getRandomNumber(1, 6)

#infinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
x = 1
while True:
    # Time management variables
    clock1 = float(random.uniform(.57, .75))
    runToFurnace = float(random.uniform(10.23, 12.5))
    runToBank = float(random.uniform(14.02, 15))
    waitamulet = float(random.uniform(50.5, 52))
    topbar = float(random.uniform(400, 1244))

    # Start by having the bank to your left
    py.moveTo(topbar, 0, duration=.25)
    time.sleep(1.7)
    py.click()
    clickSpot(865, 514, clock1) # Clicks bank
    clickSpot(1042, 729, clock1) # Clicks the empty inventory button
#    clickSpot(515, 179, clock1) # Withdraw mould r2c2
    clickSpot(589, 178, clock1) # Withdraw bars from r1c1
    clickSpot(1770, 53, clock1) # Click minimap, run to furnace
    time.sleep(runToFurnace)
    clickSpot(1708, 611, clock1) # Click use gold bar inv r1c1
    clickSpot(855, 519, clock1) # Click furnace
    py.moveTo(545, 486, duration = clock1) # Right click make amulet
    py.click(button = 'right')
    clickSpot(535, 617, clock1) # Click make all option
    time.sleep(waitamulet)
    clickSpot(1620, 227, clock1) # Toggle run
    clickSpot(1711, 267, clock1) # Run back to Bank
    time.sleep(runToBank)
    clickSpot(1618, 225, clock1) # Toggle run

    # Progarm information
    iterations += 1
    barsused = format(iterations * loadPerInv, ',d')
    profit2 = profit * iterations * loadPerInv
    xpGainz = iterations * xpPerRaw * loadPerInv
    elapsed_time = ((time.time() - start_time))/60
    print('Iterations:',iterations, '| Raw Used:',barsused, '| Profit:',profit2, '| XP gainz:',xpGainz, '| Minutes passed:',elapsed_time)

x += 1
