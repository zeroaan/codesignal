def palindromeRearranging(inputString):
    list1 = list(set(inputString))
    value = 0
    for i in list1:
        if inputString.count(i) % 2 == 1:
            value += 1
    return value <= 1
