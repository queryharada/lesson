def bubSorttest(listArrayParam):
    listArray = listArrayParam
    for i in range(0, len(listArray)):
        for j in range(i, len(listArray)):
            if listArray[i] > listArray[j]:
                temp = listArray[j]
                listArray[j] = listArray[i]
                listArray[i] = temp
    return listArray


listArray = [232, 454, 7, 9, 2, 5, 1, 0, 99]
print(bubSorttest(listArray))
listArray = [232, 454, 99, 9, 2, 5, 1, 0, 99, 0, 100, 101, 21, 5]
print(bubSorttest(listArray))
