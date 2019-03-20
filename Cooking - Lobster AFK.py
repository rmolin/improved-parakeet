import pyautogui
import time
import random

pyautogui.FAILSAFE = True

clock1 = float(random.uniform(.66, .79))
waitmapedge = float(random.uniform(13.7, 14.41)) 
waitscreenedge = float(random.uniform(10.7, 11.52)) 
waitamulet = float(random.uniform(65.1, 66.79)) 

#infinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
x = 1
while True:

    #click bank to left
    time.sleep(3)
    pyautogui.moveTo(858, 505, duration = clock1) #bank
    pyautogui.click()
    pyautogui.moveTo(1046, 734, duration = .9) #empty inv
    pyautogui.click()
    pyautogui.moveTo(587, 177, duration = clock1) #withdraw lobs
    pyautogui.click(button = "right")
    pyautogui.moveTo(734, 357)
    pyautogui.click()
    pyautogui.moveTo(1112, 63, duration = clock1) #exit
    pyautogui.click()
    pyautogui.moveTo(1815, 90, duration = clock1) #go into cooking building
    pyautogui.click()
    time.sleep(waitmapedge)
    pyautogui.moveTo(1708, 611, duration = clock1) #click inv spot
    pyautogui.click()
    pyautogui.moveTo(827, 557, duration = clock1) #click range
    pyautogui.click()
    pyautogui.moveTo(1201, 58, duration = 1.2) #burn time cause dont know more convenient code
    pyautogui.press('space')
    time.sleep(waitamulet)
    pyautogui.moveTo(1765, 233)
    pyautogui.click()
    time.sleep(18.8)
  
x += 1


