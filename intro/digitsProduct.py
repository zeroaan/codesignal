def digitsProduct(product):
    for i in range(1, 4000):
        digit = 1
        for j in str(i):
            digit *= int(j)
        if digit == product: 
            return i
    return -1
