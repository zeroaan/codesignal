def differentSquares(matrix):
    result = []
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row-1):
        for j in range(col-1):
            a = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
            if a not in result:
                result.append(a)

    return len(result)
