def isBeautifulString(inputString):
    # 잘못된 방법
    # result = [inputString.count(i) for i in sorted(set(inputString))]
    # for j in range(len(result)-1):
    #     if result[j] < result[j+1]:
    #         return False
    # return True

    result = [inputString.count(i) for i in 'abcdefghijklmnopqrstuvwxyz']
    return result == sorted(result, reverse=True)
