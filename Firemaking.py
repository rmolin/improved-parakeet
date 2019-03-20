import pyautogui as py
import time
import random
import keyboard


print('- bank')
print('= make fire')
while True: #making a loop
    try:
        if keyboard.is_pressed('-'):
            clock1 = float(random.uniform(.762, .827))
            py.moveTo(963, 482, duration=clock1) # Click bank
            py.click()
            py.moveTo(509, 234, duration=clock1) # Placehold c1r2 \
            py.click(button='right')
            py.moveTo(541, 424, duration=clock1) #
            py.click()
            py.moveTo(1117, 66, duration=clock1) #
            py.click()
        elif keyboard.is_pressed('='):
            clock1 = float(random.uniform(.93, .938))
            clock3 = float(random.uniform(1.67, 1.77))

            #row 1
            py.moveTo(1643, 615, clock1)
            py.click()
            py.moveTo(1705, 615, clock1)
            py.click()
            py.moveTo(1643, 615, clock3)
            py.click()
            py.moveTo(1770, 615, clock1)
            py.click()
            py.moveTo(1643, 615, clock1)
            py.click()
            py.moveTo(1830, 615, clock1)
            py.click()

            #row 2
            py.moveTo(1643, 615, clock1)
            py.click()
            py.moveTo(1643, 667, clock1)
            py.click()
            py.moveTo(1643, 615, clock1)
            py.click()
            py.moveTo(1705, 667, clock1)
            py.click()
            py.moveTo(1643, 615, clock1)
            py.click()
            py.moveTo(1770, 667, clock1)
            py.click()
            py.moveTo(1643, 615, clock1)
            py.click()
            py.moveTo(1830, 667, clock1)
            py.click()

            #row 3
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1643, 720, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1705, 720, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1770, 720, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1830, 720, duration = clock1)
            py.click()

            #row 4
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1643, 777, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1705, 777, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1770, 777, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1830, 777, duration = clock1)
            py.click()

            #row 5
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1643, 827, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1705, 827, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1770, 827, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1830, 827, duration = clock1)
            py.click()

            #row 6
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1643, 882, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1705, 882, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1770, 882, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1830, 882, duration = clock1)
            py.click()

            #row 7
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1643, 940, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1705, 940, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1770, 940, duration = clock1)
            py.click()
            py.moveTo(1643, 615, duration = clock1)
            py.click()
            py.moveTo(1830, 940, duration = clock1)
            py.click()
    except:
        break
