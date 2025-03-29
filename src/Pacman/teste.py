from time import sleep
listLDR = []
listLDG = []
finalR = 18
posR = 0
finalG = 8
posG = 0

while True:
    sleep(0.5)
    if 17-posR < 17:
        listLDR.pop()
    listLDR.append(17-posR)
    posR = (posR + 1) % finalR
    if posR == 0:
        finalR -= 1
    print(listLDR)
    if finalR == 0:
        finalR = 18
        listLDR = []

    if 7-posG < 7:
        listLDG.pop()
    listLDG.append(7-posG)
    posG = (posG + 1) % finalG
    if posG == 0:
        finalG -= 1
    print(listLDG)
    if finalG == 0:
        finalG = 8
        listLDG = []