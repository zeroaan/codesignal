def arrayReplace(inputArray, elemToReplace, substitutionElem):
    # for i in range(len(inputArray)):
    #     if inputArray[i] == elemToReplace:
    #         inputArray[i] = substitutionElem
    # return inputArray

    return [substitutionElem if i == elemToReplace else i for i in inputArray]
