def extractEachKth(inputArray, k):
    # result = []
    # for i in range(1, len(inputArray) + 1):
    #     if i % k != 0:
    #         result.append(inputArray[i-1])
    # return result

    return [inputArray[i-1] for i in range(1, len(inputArray)+1) if i % k != 0]
