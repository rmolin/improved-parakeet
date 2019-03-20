import pyautogui

x = 1
while True:

    pyautogui.PAUSE = 42.1
    pyautogui.moveTo(1682, 482, duration = .55)
    pyautogui.click()
    pyautogui.moveTo(1747, 489, duration = .47)
    pyautogui.click()

x += 1
