def allLongestStrings(inputArray):
    # value, result = [], []
    # for i in inputArray:
    #     value.append(len(i))
    # for j in range(len(inputArray)):
    #     if max(value) == value[j]:
    #         result.append(inputArray[j])
    # return result

    longest = max([len(i) for i in inputArray])
    return [j for j in inputArray if len(j) == longest]
