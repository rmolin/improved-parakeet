mport pyautogui
import random
import time

pyautogui.FAILSAFE = True

#misc variables
#x = screen x
#y = screen y
rdif = 36.7  #17.5 for inventory? Different for bank?
cdif = 69.3 #55 for inventory? Different for bank
ddif = 22
clock1 = float(random.uniform(.9, .99))
waitcombine = float(random.uniform(16.5, 18))

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

#bank variables
c1 = 514 #this changes depending on screen size
c2 = c1+cdif
c3 = c2+cdif
c4 = c3+cdif
c5 = c4+cdif
c6 = c5+cdif
c7 = c6+cdif
c8 = c7+cdif
r1 = 175 #this changes depending on screen size
r2 = r1+rdif
r3 = r2+rdif

#right click options
d2 = 66
d3 = d2+ddif
d4 = d3+ddif
d5 = d4+ddif
d6 = d5+ddif
d7 = d6+ddif

#list of ingredients
tomato = c6, r1
cheese = c7, r1
anchovies = c8, r1
zabase = c5, r1
incompleteza = c1, r2
uncooked = c2, r2
plainza = c3, r2


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
    pyautogui.moveTo(zabase, duration = clock1) #selects INGREDIENT 1 (future left click)(this you change)
    pyautogui.click(button='right')
    pyautogui.moveRel(yOffset=d4, duration = clock1)
    pyautogui.click()
    pyautogui.moveTo(tomato, duration = clock1) #selects INGREDIENT 2 (future right click)(this you change)
    pyautogui.click(button='right')
    pyautogui.moveRel(yOffset=d4, duration = clock1)
    pyautogui.click()
    pyautogui.moveTo(1112, 63, duration = clock1) #exit bank
    pyautogui.click()
    pyautogui.moveTo(ic1, ir1, duration = clock1)
    pyautogui.click(button='left') #uses ingredient 1
 #   pyautogui.moveRel(yOffset=d2)
  #  pyautogui.click()
    pyautogui.moveTo(ic4, ir7, duration = clock1)
    pyautogui.click()#...on ingredient 2
    time.sleep(clock1)
    pyautogui.press('space')
    time.sleep(waitcombine)

x += 1
