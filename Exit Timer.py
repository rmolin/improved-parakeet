
import time
import pyautogui as py

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
countdown(1800) # 3600 = 1 hr
py.moveTo(x=0, y=0)
