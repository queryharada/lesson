def getcombs(a, combo=None):
    # initialize combo on first call of the function
    if combo == None:
        combo = []

    combosum = sum(combo)  # sum of numbers in the combo, note that sum([]) == 0
    # simple case: we have a valid combination of numbers, i.e. combosum == a
    if combosum == a:
        yield combo  # this simply gives us that combination, no recursion here!
    # recursive case: the combination of numbers does not sum to a (yet)
    else:
        for number in range(1, a + 1):  # try each number from 1 to a
            if combosum + number <= a:  # only proceed if we don't exceed a
                extcombo = combo + [number]  # append the number to the combo
                # give me all valid combinations c that can be built from extcombo
                for c in getcombs(a, extcombo):
                    yield c


def getMulMax(num):
    numDiv1 = 0
    numDiv2 = 0
    numDiv3 = int(num / 3)
    if numDiv3 == 1:
        numDiv3 = 0
        numMod3 = num
    else:
        numMod3 = num % 3
    if numMod3 != 0:
        numDiv2 = int(numMod3 / 2)
        numMod2 = numMod3 % 2
        if numMod2 == 1:
            numDiv1 = 1
    return numDiv1, numDiv2, numDiv3


if __name__ == "__main__":
    num = 13
    combos = getcombs(num)
    maxMul = 0
    maxCombo = None
    for combo in combos:
        print(combo)
        tempMul = 1
        for v in combo:
            tempMul = tempMul * v
        if maxMul < tempMul:
            maxMul = tempMul
            maxCombo = combo

    print('MAX Comb:', maxCombo, ' = ', maxMul)

    numDiv1, numDiv2, numDiv3 = getMulMax(num)
    numTot = 0
    if numDiv1 != 0:
        numTot += 1 ** numDiv1
    if numDiv2 != 0:
        numTot += 2 ** numDiv2
    if numDiv3 != 0:
        numTot += 3 ** numDiv3

    print('MAX Comb:', numDiv1, numDiv2, numDiv3, ' = ', numTot)
