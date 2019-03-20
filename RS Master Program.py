from tkinter import *
import pyautogui
import random
import time

# entry1 = Entry(root)
class Autoclickbox: # Need 2 blank lines above class

    def __init__(self, master): # This stands for initialize and it gets called automatically whenever you create an object so you dont have to call any variables or functions
        frame = Frame(master) # We want to put the frame in the main winow but the main window is not "master"

        # Autoclicker
        Label1 = Label(master, text="RS3 Autoclicker", bg="black", fg="white")
        Button1 = Button(master, text="GO", bg="red", fg="white", command=self.autoclick)

        # firemaking
    #    Label2 = Label(master, text="Firemaking", bg="black", fg="white")
    #    Button2 = Button(master, text="GO", bg="red", fg="white", command=self.firemaking)

        # Drop Inventory
    #    Label2 = Label(master, text="Drop Inventory", bg="black", fg="white")
    #    Button2 = Button(master, text="GO", bg="red", fg="white", command=self.dropinv)
        # Gnome Villiage Agility
        Label2 = Label(master, text="Gnome Vill Run", bg="black", fg="white")
        Button2 = Button(master, text="GO", bg="red", fg="white", command=self.gnomevillrun)



        # Amulet Running / Bank Stand on Left side
    #    Label3 = Label(master, text="Amulet Running", bg="black", fg="white")
    #    Button3 = Button(master, text="GO", bg="red", fg="white", command=self.amulet)

        # Fletching Arrows / Keep knife in r1c1, continuously pulls logs from Bank
        Label3 = Label(master, text="Fletching Arrows", bg="black", fg="white")
        Button3 = Button(master, text="GO", bg="red", fg="white", command=self.fletchingarrows)

    #    Label5 = Label(master, text="Base on ingredien", bg="black", fg="white")
    #    Button5 = Button(master, text="GO", bg="red", fg="white", command=self.baseontomatocheese)

        # Base on tomato / GE Wall on top
        Label5 = Label(master, text="Base on ingredient", bg="black", fg="white")
        Button5 = Button(master, text="GO", bg="red", fg="white", command=self.baseontomatocheese)

        # Anchovies on plainza / GE Wall on top
        Label6 = Label(master, text="Ingredient on plainza", bg="black", fg="white")
        Button6 = Button(master, text="GO", bg="red", fg="white", command=self.anchoviesonplainza)

        # Cooking (Al Kharid Method) / Bank Stand on Left side
        Label7 = Label(master, text="Cooking (Al Kharid)", bg="black", fg="white")
        Button7 = Button(master, text="GO", bg="red", fg="white", command=self.cookingalkharid)

        # Grid
        Label1.grid(row=0)
        Label2.grid(row=1)
        Label3.grid(row=2)
        Label5.grid(row=4)
        Label6.grid(row=5)
        Label7.grid(row=6)
        Button1.grid(row=0, column=2)
        Button2.grid(row=1, column=2)
        Button3.grid(row=2, column=2)
        Button5.grid(row=4, column=2)
        Button6.grid(row=5, column=2)
        Button7.grid(row=6, column=2)

    def autoclick(self):
        pyautogui.FAILSAFE = True

        x = 1820 # TODO: make this a future input on the gui
        y = 635
        t1 = random.uniform(1.13, 1.51)

        #infinite loop MAKE SURE FAILSAFE IS ON /
        #end of script is "x += 1"
        z = 1
        while True:

            #alch clicks
            pyautogui.PAUSE = t1
            pyautogui.click(x, y)

        z += 1 # $$$ make a keybind that stops instead of using failsafe

    def fletchingarrows(self):
        pyautogui.FAILSAFE = True

        #infinite loop MAKE SURE FAILSAFE IS ON /
        #end of script is "x += 1"
        x = 1
        while True:

            clock1 = float(random.uniform(.95, 1.12))
            clock2 = float(random.uniform(1.10, 1.37))
            clock3 = float(random.uniform(1.11, 3.77)) #selecting inv tab
            wait1 = float(random.uniform(35.5, 36.1))

            # RNG for which tab to open
            a = random.uniform(0, 100)
            b = 25
            c = 75
            d = 77.5
            e = 87.5
            f = 92.5

            time.sleep(2)
            #click bank to left
            pyautogui.moveTo(985, 488, duration = clock1) # bank / wall toB north
            pyautogui.click()
            pyautogui.moveTo(587, 177, duration = clock1) # withdraw lobs
            pyautogui.click(button = "right")
            pyautogui.moveTo(587, 357, duration = clock1)
            pyautogui.click()
            pyautogui.moveTo(1112, 63, duration = clock1) # exit
            pyautogui.click()
            pyautogui.moveTo(1739, 542, duration = clock1) #click inv tab
            pyautogui.click()
            pyautogui.moveTo(1776, 611, duration = clock1) # click inv spot r1c3
            pyautogui.click()
            pyautogui.moveTo(1644, 609, duration = clock1) # click inv spot r1c1
            pyautogui.click()
            time.sleep(1.2) # just to burn time before pressing space
            pyautogui.press('1')
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

            time.sleep(wait1)
            time.sleep(1)

        x += 1

    def gnomevillrun(self):
        clock1 = float(random.uniform(4.4, 4.67))

        # time.sleep(clock)

        pyautogui.moveTo(x = 341, y = 627, duration =clock1)
        pyautogui.click()
        pyautogui.moveTo(x = 948, y =781, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(x = 950, y =589, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(x = 1239, y =541, duration = clock1)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(x = 874, y = 201, duration = clock1)
        pyautogui.click()
        pyautogui.moveTo(x = 892, y =346, duration = clock1)
        pyautogui.click()
        # Back at the start at the end of the left tube

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

    def cookingalkharid(self):
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
                time.sleep(2)
                pyautogui.moveTo(858, 505, duration = clock1) #bank
                pyautogui.click()
                pyautogui.moveTo(1046, 734, duration = 1.24) #empty inv
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

root = Tk() #root goes after any classes and variables
root.title("RS UI Bot Scripts")
b = Autoclickbox(root) #This is root becuase "master" is in the class

# ***** Status Bar *****
status = Label(root, text="havent learned how to make this change", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=7, columnspan=2)

root.mainloop()
