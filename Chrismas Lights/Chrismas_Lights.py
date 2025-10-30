
lights = []

i = 0
while i < 1000:
    sublist = []
    j = 0
    while j < 1000:
        sublist.append(0)
        j+=1
    i+=1

    lights.append(sublist)

def TurnOn(x, y):
    lights[x][y] += 1

def TurnOff(x, y):
    if lights[x][y] > 0:
        lights[x][y] -= 1

def Toggle(x,y):
    lights[x][y] += 2

def TurnOnRange(xStart, yStart, xEnd, yEnd):
    while xStart < xEnd:
        currentY = yStart
        while currentY < yEnd:
            TurnOn(xStart, currentY)
            currentY+=1
        xStart+=1

def TurnOffRange(xStart, yStart, xEnd, yEnd):
    while xStart < xEnd:
        currentY = yStart
        while currentY < yEnd:
            TurnOff(xStart, currentY)
            currentY+=1
        xStart+=1

def ToggleRange(xStart, yStart, xEnd, yEnd):
    while xStart < xEnd:
        currentY = yStart
        while currentY < yEnd:
            Toggle(xStart, currentY)
            currentY+=1
        xStart+=1

def CountLightsOn():
    amount = 0;
    i = 0
    while(i < 1000):
        j = 0
        while (j < 1000):
            amount+= lights[i][j]
            j+=1
        i+=1
    print("Total brightness is : " + str(amount) + ".")

start = input("Welcome to Santa's lights controller, press any key to start.")

TurnOnRange(887, 9, 959, 629)
TurnOnRange(454, 398, 844, 448)
TurnOffRange(539, 243, 559, 965)
TurnOffRange(370, 819, 676, 868)
TurnOffRange(145, 40, 370, 997)
TurnOffRange(301, 3, 808, 453)
TurnOnRange(351, 678, 951, 908)
ToggleRange(720, 196, 897, 994)
ToggleRange(831, 394, 904, 860)

CountLightsOn()