import time

# initialize stoneConform and woodConform with empty strings
stoneConform = ""
woodConform = ""

stoneMat = ("Collect Stone? (yes/no) ")
woodMat = ("Collect Stone? (yes/no) ")
goldMat = ("Collet Gold? (yes/no) ")
stoneAmt = 0
woodAmt = 0
goldAmt = 0
secondStone = 0
secondWood = 0
secondGold = 0

print("The Untitled Game - Version 0.1")
answer = input("Run the game? (yes/no): ")

if answer.lower().strip() == "yes":
    matCollection = input("What do you do? (Stone/Gold/Wood/Bag) ")

#Stone
if matCollection.lower().strip() == "stone":
    stoneConform = input(stoneMat)
if stoneConform.lower().strip() == "yes":
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
    print("You collected 20 stone!")
    stoneAmt += 20
    print("You now have", stoneAmt, "stone!")

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
    print("You now have", woodAmt, "wood!")
