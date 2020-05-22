def buildPalindrome(st):
    for i in range(len(st)):
        palindrome = st + st[0:i][::-1]
        if palindrome == palindrome[::-1]:
            return palindrome
