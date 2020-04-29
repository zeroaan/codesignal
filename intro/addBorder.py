def addBorder(picture):
    """
    result = []
    col = len(picture[0]) + 2
    row = len(picture) + 2
    result.append('*' * col)

    for i in range(len(picture)):
        value = '*'
        for j in range(len(picture[i])):
            value  += picture[i][j]
        value += '*'
        result.append(value)

    result.append('*' * col)
    return result
    """

    result = []
    col = len(picture[0]) + 2
    result.append('*' * col)

    for i in picture:
        result.append('*' + i + '*')

    result.append('*' * col)
    return result
