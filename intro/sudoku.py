def sudoku(grid):
    col = len(grid)
    row = len(grid[0])

    # 가로가 만족하지 않을 경우 False
    for r in grid:
        if sorted(list(set(r))) != sorted(r):
            return False

    # 세로가 만족하지 않을 경우 False
    for i in range(row):
        c = []
        for j in range(col):
            c.append(grid[j][i])
        if sorted(list(set(c))) != sorted(c):
            return False

    # 3 X 3이 만족하지 않을 경우 False
    for i in range(0, col, 3):
        for j in range(0, row, 3):
            g = [grid[i][j], grid[i][j+1], grid[i][j+2], \
                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], \
                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
            if sorted(list(set(g))) != sorted(g):
                return False

    return True
