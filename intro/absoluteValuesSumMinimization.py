def absoluteValuesSumMinimization(a):
    result = []
    for i in a:
        value = 0
        for j in a:
            value += abs(j-i)
        result.append(value)
    return a[result.index(min(result))]
