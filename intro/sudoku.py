def sudoku(grid):
    col = len(grid)
    row = len(grid[0])

    # 가로가 만족하지 않을 경우 False
    for g in grid:
        if sorted(list(set(g))) != sorted(g):
            return False

    # 세로가 만족하지 않을 경우 False
    for j in range(row):
        a = []
        for i in range(col):
            a.append(grid[i][j])
        if sorted(list(set(a))) != sorted(a):
            return False

    # 3 X 3이 만족하지 않을 경우 False
    for i in range(0, col, 3):
        for j in range(0, row, 3):
            b = [grid[i][j], grid[i][j+1], grid[i][j+2], \
                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], \
                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
            if sorted(list(set(b))) != sorted(b):
                return False

    return True
