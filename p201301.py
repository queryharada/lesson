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
    numDiv2 = 0
    numDiv3 = int(num / 3)
    numMod3 = num % 3
    if numMod3 != 0:
        if ((numMod3 + 3) % 2) == 0:
            numDiv2 = int(numMod3 + 3 / 2)
            numDiv3 -= 1
        else:
            numDiv2 = int(numMod3 / 2)

    return numDiv2, numDiv3


if __name__ == "__main__":
    for num in range(2,20):
        combos = getcombs(num)
        maxMul = 0
        maxCombo = None
        for combo in combos:
            # print(combo)
            tempMul = 1
            for v in combo:
                tempMul = tempMul * v
            if maxMul < tempMul:
                maxMul = tempMul
                maxCombo = combo
        print('Num:',num)
        print('MAX Comb:', maxCombo, ' = ', maxMul)
        numDiv2, numDiv3 = getMulMax(num)
        print('MAX Comb:', numDiv2, numDiv3, ' = ', (2 ** numDiv2) * (3 ** numDiv3))

    numDiv2, numDiv3 = getMulMax(2001)
    print('MAX Comb:', numDiv2, numDiv3, ' = ', (2 ** numDiv2) * (3 ** numDiv3))
