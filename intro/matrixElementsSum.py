def matrixElementsSum(matrix):
    value = 0
    zero = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero.append(j)
            if j not in zero:
                value += matrix[i][j]
    return value
