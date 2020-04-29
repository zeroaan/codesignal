def sortByHeight(a):
    copy_a = sorted(a)
    while -1 in copy_a:
        copy_a.remove(-1)
    
    result = []
    for i in range(len(a)):
        if a[i] == -1:
            result.append(-1)
        else:
            result.append(min(copy_a))
            copy_a.remove(min(copy_a))

    return result
