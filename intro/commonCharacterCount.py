def commonCharacterCount(s1, s2):
    # value = 0
    # set1 = set(s1) # 중복값 없애기 위해 set 사용
    # for i in set1:
    #     count1 = s1.count(i)
    #     count2 = s2.count(i)
    #     value += min(count1, count2)
    # return value
    
    return sum([min(s1.count(i), s2.count(i)) for i in set(s1)])
