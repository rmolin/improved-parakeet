# Clicks an x and y on screen
def clickSpot(x, y, time):
    py.moveTo(x, y, duration = time)
    py.click()

# Finds a random number between two numbers
def getRandomNumber(x, y):
    return float(random.uniform(x, y))

# print(getRandomNumber(1, 9))
