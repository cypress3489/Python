import time

stoneMat = ("Collect Stone? (yes/no) ")
woodMat = ("Collect Stone? (yes/no) ")
goldMat = ("Collet Gold? (yes/no) ")
stoneAmt = 0
woodAmt = 0
goldAmt = 0
secondStone = 0
secondWood = 0
secondGold = 0
stoneConform = ""
woodConform = ""
goldConform = ""
bootTime = 0.3
answer = ""

def printMats(): 
    print("Stone:", stoneAmt, "Wood:", woodAmt, "Gold:", goldAmt)


answer = input("Run Game? ")

if answer.lower().strip() == "yes":
    print("booting Up Game. Please Wait")
    time.sleep(bootTime)
    print("1")
    time.sleep(bootTime)
    print("2")
    time.sleep(bootTime)
    print("3")
    time.sleep(bootTime)
    print("4")
    time.sleep(bootTime)
    print("5")
    time.sleep(bootTime)
    print("6")
    time.sleep(bootTime)
    print("7")
    time.sleep(bootTime)
    print("8")
    time.sleep(bootTime)
    print("9")
    time.sleep(bootTime)
    print("10")
    print("The Untitled Game - Version 1.0")
    print("by: Cypress")
    play = input("What Shall we start with, How to play (htp) or the game itself (play)? ")

if play == "play":
    printMats()
    matCollection = input("What do you do? (Stone/Gold/Wood) ")

#Stone
if matCollection.lower().strip() == "stone":
    stoneConform = input(stoneMat)
if stoneConform.lower().strip() == "yes":
    print("collecting Wait 10s...")
    print(0)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(5)
    time.sleep(1)
    print(6)
    time.sleep(1)
    print(7)
    time.sleep(1)
    print(8)
    time.sleep(1)
    print(9)
    time.sleep(1)
    print("You collected 20 stone!")
    stoneAmt += 20
    time.sleep(0.5)
    printMats()
    matCollection = input("What do you do? (Stone/Gold/Wood) ")

#Wood
if matCollection.lower().strip() == "wood":
    woodConform = input(woodMat)
if woodConform.lower().strip() == "yes":
    print("collecting Wait 10s...")
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(5)
    time.sleep(1)
    print(6)
    time.sleep(1)
    print(7)
    time.sleep(1)
    print(8)
    time.sleep(1)
    print(9)
    time.sleep(1)
    print("You collected 20 wood!")
    woodAmt += 20


#Gold
if matCollection.lower().strip() == "gold":
    goldConform = input(goldMat)
if goldConform.lower().strip() == "yes":
    print("collecting Wait 10s...")
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(5)
    time.sleep(1)
    print(6)
    time.sleep(1)
    print(7)
    time.sleep(1)
    print(8)
    time.sleep(1)
    print(9)
    time.sleep(1)
    print("You collected 50 gold!")
    goldAmt += 50

