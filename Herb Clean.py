import pyautogui as py
import time
import random
import sys
import tkinter
from tkinter import messagebox
import ctypes


py.FAILSAFE = True

x = 1 # Code loop
while True:

    topbar = float(random.uniform(400, 1244))
    clock1 = float(random.uniform(.762, .827)) # Standard move between clicks

    py.click(x = topbar, y = 0) # Click the top of a window
    time.sleep(1.3)
    py.moveTo(985, 488, duration=clock1) # bank / wall toB north
    py.click()
    py.moveTo(1047, 733, duration=clock1) # empty inventory
    py.click()
    py.moveTo(514, 176, duration=clock1) # Options selecting an item in bank
    py.click(button = 'right')
    py.moveTo(553, 356, duration=clock1) # Select from options
    py.click()
    py.moveTo(1118, 68, duration=clock1)
    py.click()

    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1651, 612, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1710, 613, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1647, 665, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1707, 664, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1645, 719, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1714, 719, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1650, 769, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1709, 773, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1648, 832, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1711, 821, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1649, 879, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1711, 879, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1643, 935, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1710, 934, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1770, 615, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1836, 613, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1768, 661, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1835, 663, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1771, 718, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1840, 722, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1774, 772, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1834, 770, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1767, 826, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1836, 830, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1774, 884, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1835, 881, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1772, 934, duration=clock1)
    clock1 = float(random.uniform(.132, .382)) # Standard move between clicks
    py.click(1835, 935, duration=clock1)

x += 1 # Repeat
