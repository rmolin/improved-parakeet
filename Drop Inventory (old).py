import pyautogui as py  
import time
import random

py.FAILSAFE = True

#indefinite loop MAKE SURE FAILSAFE IS ON /
#end of script is "x += 1"
x = 1
while True:
#drop inventory
	#row 1
	py.moveTo(1643, 615, duration=.44)
	py.PAUSE = .2
	py.keyDown('shift')
	py.PAUSE
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1705, 615, duration=.44)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1770, 615, duration=.44)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1830, 615, duration=.44)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

	#row 2
	py.moveTo(1643, 667, duration=.44)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1705, 667, duration=.44)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

	py.moveTo(1770, 667, duration=.44)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

	py.moveTo(1830, 667, duration=.44)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

	#row 3
	py.moveTo(1643, 720, duration=.43)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1705, 720, duration=.43)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1770, 720, duration=.43)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1830, 720, duration=.43)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

	#row 4
	py.moveTo(1643, 777, duration=.41)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1705, 777, duration=.41)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1770, 777, duration=.41)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1830, 777, duration=.41)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

	#row 5
	py.moveTo(1643, 827, duration=.40)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1705, 827, duration=.40)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1770, 827, duration=.40)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1830, 827, duration=.40)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

	#row 6
	py.moveTo(1643, 882, duration=.29)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1705, 882, duration=.29)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1770, 882, duration=.29)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1830, 882, duration=.29)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

	#row 7
	py.moveTo(1643, 940, duration=.25)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1705, 940, duration=.25)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1770, 940, duration=.25)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')
	py.moveTo(1830, 940, duration=.21)
	py.PAUSE = .2
	py.keyDown('shift')
	py.click(button='left')
	py.keyUp('shift')

x += 1
