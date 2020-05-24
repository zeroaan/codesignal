def chessKnight(cell):
    count = 0
    row = ord(cell[0]) - ord('a') + 1
    col = int(cell[1])
    move = [[1,2], [2,1], [1,-2], [2,-1], [-1,2], [-2,1], [-1,-2], [-2,-1]]
    
    for m in move:
        if 1 <= row + m[0] <= 8 and 1 <= col + m[1] <= 8:
            count +=1
    return count
