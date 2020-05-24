
def lineEncoding(s):
    s = s + ' '
    result = ''
    count = 1
    for v in range(len(s)-1):
        if s[v] == s[v+1]:
            count += 1
        else:
            if count == 1:
                result += s[v]
            else:
                result += str(count) + s[v]
            count = 1
    return result
