    def amulet(self):
        pyautogui.FAILSAFE = True

        clock1 = float(random.uniform(.752, .827))
        clock2 = float(random.uniform(.70, 1.01))
        clock3 = float(random.uniform(1.11, 3.77)) #selecting inv tab
        waitmapedge = float(random.uniform(11.7, 12.1))
        waitmapedge2 = float(random.uniform(15.7, 18.1))
        waitscreenedge = float(random.uniform(10.7, 11.52))
        waitamulet = float(random.uniform(50.5, 52))

        #infinite loop MAKE SURE FAILSAFE IS ON /
        #end of script is "x += 1"
        x = 1
        while True:
            # RNG for which tab to open
            a = random.uniform(0, 100)
            b = 25
            c = 75
            d = 77.5
            e = 87.5
            f = 92.5

            # RNG for which route to run
            q = random.uniform(0, 1)
            w = .80

            if q > w:
                #click bank to left TODO change all the x's and y's
                pyautogui.moveTo(858, 505, duration = clock1) #bank
                pyautogui.click()
                pyautogui.moveTo(1046, 734, duration = clock1) #empty inv
                pyautogui.click()
                pyautogui.moveTo(513, 173, duration = clock1) #withdraw mold
                pyautogui.click()
                pyautogui.moveTo(589, 178, duration = clock1)
                pyautogui.click(button = 'right')
                pyautogui.moveTo(592, 348, duration = clock1)#withdraw bars
                pyautogui.click()
                pyautogui.moveTo(1112, 63, duration = clock1) #exit
                pyautogui.click()
                pyautogui.moveTo(1862, 84, duration = clock1) #halfway to furnace
                pyautogui.click()
                time.sleep(waitmapedge)
                pyautogui.moveTo(1739, 542, duration = clock1) #click inv tab
                pyautogui.click()
                pyautogui.moveTo(1708, 611, duration = clock1) #click inv spot
                pyautogui.click()
                pyautogui.moveTo(140, 122, duration = clock1) #click furnace
                pyautogui.click()
                time.sleep(waitscreenedge)
                pyautogui.moveTo(546, 482, duration = clock1)
                pyautogui.click(button = 'right')
                pyautogui.moveTo(558, 610)
                pyautogui.click()
                if a >= b:
                    pyautogui.moveTo(1639, 545, duration = clock3)
                    pyautogui.click()
                elif b < a < c:
                    pass
                elif c < a < d:
                    pyautogui.moveTo(1689, 545, duration = clock3)
                    pyautogui.click()
                elif d < a < e:
                    pyautogui.moveTo(1787, 546, duration = clock3)
                    pyautogui.click()
                elif e < a < f:
                    pyautogui.moveTo(1887, 543, duration = clock3)
                    pyautogui.click()
                else:
                    pyautogui.moveTo(1638, 993, duration = clock3)
                    pyautogui.click()
                time.sleep(waitamulet)
                pyautogui.moveTo(1765, 265)
                pyautogui.click()
                time.sleep(19.8)
            else:
                #click bank to left
                pyautogui.moveTo(858, 505, duration = clock1) #bank
                pyautogui.click()
                pyautogui.moveTo(1046, 734, duration = clock1) #empty inv
                pyautogui.click()
                pyautogui.moveTo(513, 173, duration = clock1) #withdraw mold
                pyautogui.click()
                pyautogui.moveTo(589, 178, duration = clock1)
                pyautogui.click(button = 'right')
                pyautogui.moveTo(592, 348, duration = clock1)#withdraw bars
                pyautogui.click()
                pyautogui.moveTo(1112, 63, duration = clock1) #exit
                pyautogui.click()
                pyautogui.moveTo(1827, 60, duration = clock1) #fullway to furnace
                pyautogui.click()
                time.sleep(waitmapedge2)
                pyautogui.moveTo(1739, 542, duration = clock1) #click inv tab
                pyautogui.click()
                pyautogui.moveTo(1708, 611, duration = clock1) #click inv spot
                pyautogui.click()
                pyautogui.moveTo(811, 496, duration = clock1) #click furnace
                pyautogui.click()
                pyautogui.moveTo(546, 482, duration = clock2)
                pyautogui.click(button = 'right')
                pyautogui.moveTo(558, 610)
                pyautogui.click()
                if a >= b:
                    pyautogui.moveTo(1639, 545, duration = clock3)
                    pyautogui.click()
                elif b < a < c:
                    pass
                elif c < a < d:
                    pyautogui.moveTo(1689, 545, duration = clock3)
                    pyautogui.click()
                elif d < a < e:
                    pyautogui.moveTo(1787, 546, duration = clock3)
                    pyautogui.click()
                elif e < a < f:
                    pyautogui.moveTo(1887, 543, duration = clock3)
                    pyautogui.click()
                else:
                    pyautogui.moveTo(1638, 993, duration = clock3)
                    pyautogui.click()
                time.sleep(waitamulet)
                pyautogui.moveTo(1765, 265)
                pyautogui.click()
                time.sleep(19.8)
            x += 1

########## END ##########

# Mine top & right + drop inventory
Label4 = Label(master, text="2 square powerminer", bg="black", fg="white")
Button4 = Button(master, text="GO", bg="red", fg="white", command=self.mine)

def mine(self):
    pyautogui.FAILSAFE = True

    clock = float(random.uniform(4.4, 4.67))
    time1 = .35
    time2 = float(random.uniform(.29,.41))
    xtop = float(968)
    ytop = float(427)
    xright = float(1072)
    yright = float(530)

    #indefinite loop MAKE SURE FAILSAFE IS ON /
    #end of script is "x += 1"
    x = 1
    while True:

    #mine rock
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)

      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xright, yright, duration= time1)
      pyautogui.click()
      time.sleep(clock)
      pyautogui.moveTo(xtop, ytop, duration= time1)
      pyautogui.click()

    #drop inventory
      #row 1
      pyautogui.moveTo(1643, 615, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.PAUSE
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1705, 615, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1770, 615, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1830, 615, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

      #row 2
      pyautogui.moveTo(1643, 667, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1705, 667, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

      pyautogui.moveTo(1770, 667, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

      pyautogui.moveTo(1830, 667, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

      #row 3
      pyautogui.moveTo(1643, 720, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1705, 720, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1770, 720, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1830, 720, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

      #row 4
      pyautogui.moveTo(1643, 777, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1705, 777, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1770, 777, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1830, 777, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

      #row 5
      pyautogui.moveTo(1643, 827, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1705, 827, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1770, 827, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1830, 827, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

      #row 6
      pyautogui.moveTo(1643, 882, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1705, 882, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1770, 882, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1830, 882, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

      #row 7
      pyautogui.moveTo(1643, 940, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1705, 940, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1770, 940, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')
      pyautogui.moveTo(1830, 940, duration=time2)
      pyautogui.PAUSE = .2
      pyautogui.keyDown('shift')
      pyautogui.click(button='left')
      pyautogui.keyUp('shift')

    x += 1

########## END ##########

    #DOES NOT DROP THE FIRST 2 INVENTORY SPACES FOR SOME REASON, WHEN COMMENTED
    # OUT IT DOES NOT DROP THE NEXT FIRST 2 INVENTORY SPACES
    # ^^ CAUTION, IT REGULARLY CLICKS THE FIRST SPACE AND USES ON SECOND
def dropinv(self):

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

    ########## END ##########

    def firemaking(self):

        clock1 = float(random.uniform(.93, .935))
        clock2 = clock1
        clock3 = float(random.uniform(1.67, 1.77))

        #row 1
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 615, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock3)
        pyautogui.click()
        pyautogui.moveTo(1770, 615, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 615, clock1)
        pyautogui.click()

        #row 2
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 667, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 667, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 667, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 667, clock1)
        pyautogui.click()

        #row 3
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 720, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 720, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 720, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 720, duration = clock1)
        pyautogui.click()

        #row 4
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 777, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 777, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 777, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 777, duration = clock1)
        pyautogui.click()

        #row 5
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 827, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 827, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 827, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 827, duration = clock1)
        pyautogui.click()

        #row 6
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 882, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 882, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 882, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 882, duration = clock1)
        pyautogui.click()

        #row 7
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 940, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 940, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 940, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 940, duration = clock1)
        pyautogui.click()

# (old)Drop Inventory
Label2 = Label(master, text="Drop Inventory", bg="black", fg="white")
Button2 = Button(master, text="GO", bg="red", fg="white", command=self.dropinv)

########## END ##########

# In gui in master currently
def firemaking(self):

        clock1 = float(random.uniform(.93, .935))
        clock2 = clock1
        clock3 = float(random.uniform(1.67, 1.77))

        #row 1
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 615, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock3)
        pyautogui.click()
        pyautogui.moveTo(1770, 615, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 615, clock1)
        pyautogui.click()

        #row 2
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 667, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 667, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 667, clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 667, clock1)
        pyautogui.click()

        #row 3
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 720, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 720, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 720, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 720, duration = clock1)
        pyautogui.click()

        #row 4
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 777, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 777, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 777, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 777, duration = clock1)
        pyautogui.click()

        #row 5
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 827, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 827, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 827, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 827, duration = clock1)
        pyautogui.click()

        #row 6
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 882, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 882, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 882, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 882, duration = clock1)
        pyautogui.click()

        #row 7
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1643, 940, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1705, 940, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1770, 940, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(1643, 615, duration = clock2)
        pyautogui.click()
        pyautogui.moveTo(1830, 940, duration = clock1)
        pyautogui.click()

######## End ###########

def baseontomatocheese(self):
    # Pixels between each row/column/down options
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

    pyautogui.FAILSAFE = True

    #misc variables
    clock1 = float(random.uniform(.9, .99))
    waitcombine = float(random.uniform(16.5, 18))
    item1 = 586, 176
    item2 = 657, 176

    #infinite loop MAKE SURE FAILSAFE IS ON /
    #end of script is "x += 1"
    x = 1
    while True:

        #begin clicking
        pyautogui.moveTo(948, 457, duration = clock1) #bank
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

########### End ###########

def anchoviesonplainza(self):
    # TODO: make these variables the same throughout all def's
    # Pixels between each row/column/down options
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

    pyautogui.FAILSAFE = True

    #misc variables
    clock1 = float(random.uniform(.9, .99))
    waitcombine = float(random.uniform(16.5, 18))
    item1 = 586, 176
    item2 = 657, 176

    #infinite loop MAKE SURE FAILSAFE IS ON /
    #end of script is "x += 1"
    x = 1
    while True:

        #begin clicking
        pyautogui.moveTo(948, 457, duration = clock1) #bank
        pyautogui.moveTo(1046, 734, duration = 1.24) #empty inv
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
      #  pyautogui.moveTo(ic1, ir1, duration = clock1)
      #  pyautogui.click(button='left') #uses ingredient 1

        pyautogui.moveTo(ic1, ir1, duration = clock1) #selects INGREDIENT 2 (future right click)(this you change)
        pyautogui.click(button='right')
        pyautogui.moveRel(yOffset=d2, duration = clock1)
        pyautogui.click()

        pyautogui.moveTo(ic4, ir7, duration = clock1)
        pyautogui.click()#...on ingredient 2
        time.sleep(clock1)
        pyautogui.press('space')
        time.sleep(waitcombine)

    x += 1
