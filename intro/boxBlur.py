def boxBlur(image):
    result = []
    row = len(image)
    col = len(image[0])

    for i in range(1, row-1):
        value = []
        for j in range(1, col-1):
            pixel = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    pixel += image[x][y]
            value.append(pixel//9)
        result.append(value)

    return result
