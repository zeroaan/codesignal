def longestWord(text):
    # english = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # value = ''
    # for w in text:
    #     if w in english:
    #         value += w
    #     else:
    #         value += '/'
    # result = value.split("/")
    # return max(result, key=len)

    # list comprehension 으로 짧게 만들기

    english = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = ''.join([w if w in english else '/' for w in text])
    result = value.split('/')
    return max(result, key=len)
