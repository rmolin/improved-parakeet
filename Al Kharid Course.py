# (unfinished)

import pyautogui as py
import random
import time

py.FAILSAFE = True

clock1 = float(random.uniform(.31, .47))

py.moveTo(x = 954, y = 540, duration = clock1) # Initiate course
py.click()
py.moveTo(x = 1787, y = 224, duration = clock1) # Walk across tightrope
time.sleep(5)
py.click()
#4 seconds
py.moveTo(x = 949, y = 648, duration = clock1) # Halfway to cable
time.sleep(7.5)
py.click()
#7s
py.moveTo(x = 797, y = 942, duration = clock1) # Click on Cable
time.sleep(6)
py.click()
print("click on cable") # 864, 614
#3
py.moveTo(x = 864, y = 614, duration = clock1)
time.sleep(6)
py.click()
#6
py.moveTo(x = 1901, y = 165, duration = clock1)
time.sleep(7)
py.click()
#5
py.moveTo(x = 1093, y = 669, duration = clock1)
time.sleep(10)
py.click()
#10
py.moveTo(x = 1122, y = 291, duration = clock1)
time.sleep(7)
py.click()
#7
py.moveTo(x = 859, y = 185, duration = clock1)
time.sleep(5.5)
py.click()
#5.5
py.moveTo(x = 755, y = 211, duration = clock1)
time.sleep(12.7)
py.click()
#12.7
py.moveTo(x = 822, y = 234, duration = clock1)
time.sleep(7)
#py.click()
py.moveTo(x = 408, y = 471, duration = clock1)
time.sleep(7)
py.moveTo(x = 474, y = 489, duration = clock1)
time.sleep(7)
py.click()
py.moveTo(x = 389, y = 447, duration = clock1)
time.sleep(7)
py.click()
