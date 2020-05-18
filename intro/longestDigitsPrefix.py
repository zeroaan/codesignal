def longestDigitsPrefix(inputString):
    result = ''
    for i in inputString:
        if i.isdigit() == False: break
        result += i
    return result
