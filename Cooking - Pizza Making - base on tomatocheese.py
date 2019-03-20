import pyautogui
import random
import time

pyautogui.FAILSAFE = True

#misc variables
clock1 = float(random.uniform(.9, .99))
waitcombine = float(random.uniform(16.5, 18))
item1 = 586, 176
item2 = 657, 176

rdif = 36.7  #17.5 for inventory? Different for bank?
cdif = 69.3 #55 for inventory? Different for bank
ddif = 22

#inventory variables
ic1 = 1645 #this changes depending on screen size
ic2 = ic1+cdif
ic3 = ic2+cdif
ic4 = ic3+cdif
ir1 = 615 #this changes depending on screen size
ir2 = ir1+rdif
ir3 = ir2+rdif
ir4 = ir3+rdif
ir5 = ir4+rdif
ir6 = ir5+rdif
ir7 = ir6+rdif

#right click options
d2 = 66
d3 = d2+ddif
d4 = d3+ddif
d5 = d4+ddif
d6 = d5+ddif
d7 = d6+ddif

#infinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
x = 1
while True:
    
    #begin clicking
    pyautogui.moveTo(832, 494, duration = clock1) #bank
    pyautogui.click(button='right')
    time.sleep(clock1)
    pyautogui.moveRel(yOffset=d2, duration = clock1) #navigate bank options
    pyautogui.click()
    pyautogui.moveTo(1046, 734, duration = clock1) #empty inv
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(item1, duration = clock1) #withdraws INGREDIENT 1 (future left click)(this you change)
    pyautogui.click(button='right')
    pyautogui.moveRel(yOffset=d4, duration = clock1)
    pyautogui.click()
    pyautogui.moveTo(item2, duration = clock1) #withdraws INGREDIENT 2 (future right click)(this you change)
    pyautogui.click(button='right')
    pyautogui.moveRel(yOffset=d4, duration = clock1) 
    pyautogui.click()
    pyautogui.moveTo(1112, 63, duration = clock1) #exit bank
    pyautogui.click()
    pyautogui.moveTo(ic1, ir1, duration = clock1)
    pyautogui.click(button='left') #uses ingredient 1
    pyautogui.moveTo(ic4, ir7, duration = clock1)
    pyautogui.click()#...on ingredient 2
    time.sleep(1.81)
    pyautogui.press('space')
    time.sleep(waitcombine)
    
x += 1


