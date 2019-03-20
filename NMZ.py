import pyautogui as py
import time
import random
import time

py.FAILSAFE = True

THISLOGPATH = "PATHTOLOGFILE.TXT"

iterations = 0
start_time = time.time() # Calculate time passed
timestr = time.strftime("%Y-%m-%d %H%M%S") # String for the current date and time

py.click(555, 0, duration=1.5)

z = 1
while z > 0:
    x = 1420
    x2=1421
    y = 656
    y2=677
    randX = random.uniform(x, x2)
    randY = random.uniform(y, y2)
    t1 = random.uniform(39, 58)
    t2 = random.uniform(.04, .11)

    py.PAUSE = t1
    py.click(randX, randY)
    py.PAUSE = t2
    py.click(randX, randY)
    py.PAUSE = t1
    py.click(randX, randY)
    py.PAUSE = t2
    py.click(randX, randY)

    # Progarm information
    iterations += 1
    xp = format(iterations * 65, ',d')
    # = format(iterations * 26, ',d')
    elapsed_time = ((time.time() - start_time))/60
    print('Iterations:',iterations, '| xp:',xp, '| Minutes passed:',elapsed_time)

    # Write program information to a text file
    if iterations >= 2:
        iiterations = 'Itarations: ' + str(iterations) + ' | xp: ' + str(xp) + ' | Minutes passed: ' + str(elapsed_time) + ' | Date: ' + str(timestr) + '\n'
        f = open(THISLOGPATH,"a")
        f.write(iiterations)
