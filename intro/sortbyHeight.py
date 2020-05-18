def sortByHeight(a):
    height = [i for i in a if i > 0]
    
    result = []
    for i in range(len(a)):
        if a[i] == -1:
            result.append(-1)
        else:
            result.append(min(height))
            height.remove(min(height))

    return result
