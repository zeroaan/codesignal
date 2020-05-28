def fileNaming(names):
    result = []

    for n in names:
        if n not in result:
            result.append(n)
        else:
            # for i in range(1, len(names)):
            #     value = n + '(' + str(i) +')'
            #     if n + '(' + str(i) +')' not in result:
            #         result.append(value)
            #         break
            # for 문으로도 가능하지만 통과하고 나서 다른 사람 정답을 보니
            # while문으로 한 코드가 많아서 한번 해보았다.

            i = 1
            while n + '(' + str(i) +')' in result:
                i += 1
            result.append(n + '(' + str(i) + ')')
    return result
