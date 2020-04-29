def checkPalindrome(inputString):
    value = ''
    for i in range(len(inputString)-1, -1, -1):
       value += inputString[i]
    if inputString == value:
        return True
    return False
