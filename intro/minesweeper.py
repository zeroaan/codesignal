def minesweeper(matrix):
    result = []
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        value = []
        for j in range(col):
            mine = 0
            if i > 0:
                if matrix[i-1][j]:
                    mine += 1
            if j > 0:
                if matrix[i][j-1]:
                    mine += 1
            if i > 0 and j > 0:
                if matrix[i-1][j-1]:
                    mine += 1
            if i < row - 1:
                if matrix[i+1][j]:
                    mine += 1
            if j < col - 1:
                if matrix[i][j+1]:
                    mine += 1
            if i < row - 1 and j < col - 1:
                if matrix[i+1][j+1]:
                    mine += 1
            if i > 0 and j < col - 1:
                if matrix[i-1][j+1]:
                    mine += 1
            if i < row - 1 and j > 0:
                if matrix[i+1][j-1]:
                    mine += 1
            value.append(mine)
        result.append(value)
    
    return result
            
