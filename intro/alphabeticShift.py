def alphabeticShift(inputString):
    # print(ord('a')) # 97
    # print(ord('z')) # 122
    
    result = ""
    for i in range(len(inputString)):
        if inputString[i] == 'z':
            result += 'a'
        else:
            result += chr(ord(inputString[i]) + 1)
    return result
