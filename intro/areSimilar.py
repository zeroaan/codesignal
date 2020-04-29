def areSimilar(a, b):
    if a == b:
        return True

    value = []

    for i in range(len(a)):
        if a[i] != b[i]:
            value.append(i)
            
    a[value[0]], a[value[1]] = a[value[1]], a[value[0]]
    return a == b
