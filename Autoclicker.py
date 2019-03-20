import pyautogui as py
import time
import random
import time

py.FAILSAFE = True

THISLOGPATH = "THISLOGPATH.TXT"

iterations = 0
start_time = time.time() # Calculate time passed
timestr = time.strftime("%Y-%m-%d %H%M%S") # String for the current date and time

z = 1
while z > 0:
    x = 1851
    y = 755
    t1 = random.uniform(1.31, 1.44)
    py.PAUSE = t1
    py.click(x, y)
    that = random.uniform(0, 1)
    if that >= .955:
        stop = random.uniform(3, 8)
        time.sleep(stop)
    py.PAUSE = t1
    py.click(x, y)

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
