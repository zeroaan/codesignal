# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

def spiralNumbers(n):
    result = [[0] * n for i in range(n)]
    value = 1
    for i in range(n):
        for j in range(n):
            result[i][j] = value
            value += 1

    return result
