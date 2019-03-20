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
time.sleep(1)
py.moveTo(1009, 520, duration=.7)
z = 1
while z > 0:
    x = 1009
    y = random.uniform(541, 498)
    t1 = random.uniform(.65, .77)
    py.PAUSE = t1
    py.click(x, y)
    that = random.uniform(0, 1)
    if that <= .11:
        time.sleep(.55)
        py.moveTo(1705, 607, duration=.5)
        py.click()
        py.moveTo(x, y)
        time.sleep(1)
    if that >= .988:
        stop = random.uniform(3, 8)
        time.sleep(stop)
    py.PAUSE = t1
    py.click(x, y)

    # Progarm information
    iterations += 1
    xp = iterations * 84.5,',d'
    # = format(iterations * 26, ',d')
    elapsed_time = ((time.time() - start_time))/60
    print('Iterations:',iterations, '| xp:',xp, '| Minutes passed:',elapsed_time)

    # Write program information to a text file
    if iterations >= 10:
        iiterations = 'Itarations: ' + str(iterations) + ' | xp: ' + str(xp) + ' | Minutes passed: ' + str(elapsed_time) + ' | Date: ' + str(timestr) + '\n'
        f = open(THISLOGPATH,"a")
        f.write(iiterations)
