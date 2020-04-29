def makeArrayConsecutive2(statues):
    value = 0

    for i in range(min(statues), max(statues)+1):
        if i not in statues:
            value += 1
    return value
