#// mines 3 tin ores in barb villiage and dumps on infinite loop

import pyautogui
import time

pyautogui.FAILSAFE = True

clock = float(8.5)
xtop = float(968)
ytop = float(427)
xright = float(1072)
yright = float(530)
xbottom = float(965)
ybottom = float(632)

#indefinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
x = 1
while True:

#mine rock 28 tiles
	pyautogui.moveTo(xtop, ytop, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xright, yright, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xbottom, ybottom, duration= .35)
	pyautogui.click()
	time.sleep(clock)

	pyautogui.moveTo(xtop, ytop, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xright, yright, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xbottom, ybottom, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xtop, ytop, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xright, yright, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xbottom, ybottom, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xtop, ytop, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xright, yright, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xbottom, ybottom, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xtop, ytop, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xright, yright, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xbottom, ybottom, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xtop, ytop, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xright, yright, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xbottom, ybottom, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xtop, ytop, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xright, yright, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xbottom, ybottom, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xtop, ytop, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xright, yright, duration= .35)
	pyautogui.click()
	time.sleep(clock)
	pyautogui.moveTo(xbottom, ybottom, duration= .35)
	pyautogui.click()
	
	#row 1
	pyautogui.moveTo(1643, 615, duration=.44)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.PAUSE
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1705, 615, duration=.44)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1770, 615, duration=.44)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1830, 615, duration=.44)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	
	#row 2
	pyautogui.moveTo(1643, 667, duration=.44)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1705, 667, duration=.44)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	
	pyautogui.moveTo(1770, 667, duration=.44)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	
	pyautogui.moveTo(1830, 667, duration=.44)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	
	#row 3
	pyautogui.moveTo(1643, 720, duration=.43)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1705, 720, duration=.43)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1770, 720, duration=.43)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1830, 720, duration=.43)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')

	#row 4
	pyautogui.moveTo(1643, 777, duration=.41)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1705, 777, duration=.41)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1770, 777, duration=.41)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1830, 777, duration=.41)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	
	#row 5
	pyautogui.moveTo(1643, 827, duration=.40)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1705, 827, duration=.40)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1770, 827, duration=.40)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1830, 827, duration=.40)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	
	#row 6
	pyautogui.moveTo(1643, 882, duration=.29)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1705, 882, duration=.29)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1770, 882, duration=.29)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1830, 882, duration=.29)
	pyautogui.PAUSE = .2	
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	
	#row 7
	pyautogui.moveTo(1643, 940, duration=.25)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1705, 940, duration=.25)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1770, 940, duration=.25)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')
	pyautogui.moveTo(1830, 940, duration=.21)
	pyautogui.PAUSE = .2
	pyautogui.keyDown('shift')
	pyautogui.click(button='left')
	pyautogui.keyUp('shift')	

x += 1
