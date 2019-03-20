import pyautogui as py
import time
import random


py.FAILSAFE = True

# Variables for randomly clicking a tab (inv, skills, equip, etc.)
xleft = 1580
xright = 1890
yup = 523
ydown = 568
# ...down bank
xleft1 = 940
xright1 = 999
yup1 = 572
ydown1 = 575

def rand(low, high):
    n = random.uniform(low, high)
    print(n)

#infinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
x = 1
while True:

    # Time
    clock1 = float(random.uniform(.74, .93))
    clock2 = float(random.uniform(1.10, 1.37))
    clock3 = float(random.uniform(1.11, 3.77)) #selecting inv tab
    wait1 = float(random.uniform(50.5, 50.98))

    # Local variables / need to change each time
    n = random.uniform(0, 100)
    topbar = float(random.uniform(400, 1244))
    xtab = float(random.uniform(xleft, xright)) # selecting tab
    ytab = float(random.uniform(yup, ydown))
    xbank = float(random.uniform(xleft1, xright1)) # selecting tab
    ybank = float(random.uniform(yup1, ydown1))

    py.click(x = topbar, y = 0) # Click the top of a window
    time.sleep(1.3)
    py.moveTo(985, 488, duration = clock1) # bank / wall toB north
    py.click()
    py.moveTo(1047, 733, duration = clock1) # empty inventory
    py.click()
    py.moveTo(506, 182, duration = clock1) # withdraw placeholder knife
    py.click()
    py.moveTo(586, 177, duration = clock1) # withdraw all but 1 Logs
    py.click(button = "right")
    py.moveTo(588, 350, duration = clock1)
    py.click()
    py.moveTo(1112, 63, duration = clock1) # exit bank screen
    py.click()
 #   py.moveTo(1739, 542, duration = clock1) #click inv tab
  #  py.click()
    py.moveTo(1642, 611, duration = clock1) # click inv spot r1c1
    py.click()
    py.moveTo(1708, 610, duration = clock1) # click inv spot r1c2
    py.click()
    time.sleep(1.2) # just to burn time before pressing space
    py.press('3')
    # 1 arrows, 2 shortbow, 3 longbow, 3 crossbow stock, 4 shield
   # m = float(random.uniform(0, 1))
   # if m > .85:
    #    py.moveTo(xtab, ytab, duration = clock1/2)
     #   py.click()
    time.sleep(wait1)
    time.sleep(1)

x += 1
