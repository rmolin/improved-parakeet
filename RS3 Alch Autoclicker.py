import pyautogui
import random

pyautogui.FAILSAFE = True

x = 1820
y = 635
t1 = random.uniform(1.13, 1.51)

#infinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
z = 1
while True:

    #alch clicks
    pyautogui.PAUSE = t1
    pyautogui.click(x, y)

z += 1
