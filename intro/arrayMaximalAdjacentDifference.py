def arrayMaximalAdjacentDifference(inputArray):
    abs_list = []
    for i in range(len(inputArray)-1):
        abs_list.append(abs(inputArray[i]-inputArray[i+1]))
    return max(abs_list)
