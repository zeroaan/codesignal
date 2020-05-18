def bishopAndPawn(bishop, pawn):
    # if bishop[0] == pawn[0] or bishop[1] == pawn[1]:
    #     return False

    row = abs(ord(bishop[0]) - ord(pawn[0]))
    col = abs(int(bishop[1]) - int(pawn[1]))
    return row == col
