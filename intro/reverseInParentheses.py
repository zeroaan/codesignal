def reverseInParentheses(inputString):
    for i in range(len(inputString)):
        if inputString[i] == "(":
            left = i
        elif inputString[i] == ")":
            right = i
            return reverseInParentheses(inputString[:left] \
            + inputString[left+1:right][::-1] + inputString[right+1:])
    return inputString
