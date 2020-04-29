def isLucky(n):
    """
    str_n = str(n)
    mid = len(str_n) // 2
    left = str_n[:mid]
    right = str_n[mid:]

    val_1, val_2 = 0, 0

    for i in left:
        val_1 += int(i)
        
    for j in right:    
        val_2 += int(j)
    
    if val_1 == val_2:
        return True
    return False
    """

    list_n = [int(i) for i in str(n)]
    mid = len(list_n) // 2
    left = list_n[:mid]
    right = list_n[mid:]
    
    if sum(left) == sum(right):
        return True
    return False
