import pyautogui

pyautogui.FAILSAFE = True
time1 = 8
time2 = 8
time3 = 8

#go to top right of dock, cook food
pyautogui.PAUSE = time1
pyautogui.click(1828, 119)
pyautogui.click(1707, 614)
pyautogui.click(1643, 615)
pyautogui.click(1833, 933)
pyautogui.click(1050, 530)
pyautogui.press('space')

input("Ready to continue?")

#top right part of dock to general store
pyautogui.PAUSE = time2
pyautogui.click(1783, 264)
pyautogui.click(1720, 226)
pyautogui.click(421, 701)

input("Ready to continue?")

#from store between two posts to logs to dock
pyautogui.PAUSE = time3
pyautogui.click(1902, 149)
pyautogui.click(1890, 189)
pyautogui.click(1427, 275)
pyautogui.click(1692, 134)
pyautogui.click(1741, 73)
pyautogui.click(1851, 74)

print("done!")









