def deleteDigit(n):
    # result = []
    # s = str(n)
    # for i in range(len(s)):
    #     v = s[:i] + s[i+1:]
    #     result.append(v)
    # return int(max(result))

    s = str(n)
    return int(max([s[:i]+s[i+1:] for i in range(len(s))]))
