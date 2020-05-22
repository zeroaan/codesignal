
def buildPalindrome(st):
    result = []
    for i in range(len(st)):
        palindrome = st + st[0:i][::-1]
        if palindrome == palindrome[::-1]:
            result.append(palindrome)
            
    return min(result, key=len)
