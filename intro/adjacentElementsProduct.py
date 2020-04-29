def adjacentElementsProduct(inputArray):
    value = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > value:
            value = inputArray[i] * inputArray[i+1]
    return value
