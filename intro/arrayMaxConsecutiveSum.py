def arrayMaxConsecutiveSum(inputArray, k):
    max_value = sum(inputArray[:k])
    for i in range(1, len(inputArray) - k + 1):
        value = sum(inputArray[i:i+k])
        max_value = max(max_value, value)
    return max_value


    # max_value = value = sum(inputArray[:k])
    
    # for i in range(0, len(inputArray) - k):
    #     value += inputArray[i + k] - inputArray[i]
    #     max_value = max(max_value, value)

    # return max_value
