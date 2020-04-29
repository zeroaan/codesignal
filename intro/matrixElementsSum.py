def matrixElementsSum(matrix):
    value = 0
    zero_room = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_room.append(j)
        for k in range(len(matrix[0])):
            if k not in zero_room:
                value += matrix[i][k]
    return value
