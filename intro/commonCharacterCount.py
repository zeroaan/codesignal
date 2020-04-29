def commonCharacterCount(s1, s2):
    value = 0
    set1 = set(s1)
    for i in set1:
        count1 = s1.count(i)
        count2 = s2.count(i)
        value += min([count1, count2])
    return value
