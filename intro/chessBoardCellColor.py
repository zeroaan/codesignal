def chessBoardCellColor(cell1, cell2):
    # black = list('ACEG')
    # white = list('BDFH')

    # if (cell1[0] in black and cell2[0] in black) or (cell1[0] in white and cell2[0] in white):
    #     return (int(cell1[1]) + int(cell2[1])) % 2 == 0
    # else:
    #     return (int(cell1[1]) + int(cell2[1])) % 2 != 0

    
    # print(ord("A")) # 65
    return (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0
