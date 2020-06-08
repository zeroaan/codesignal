def circleOfNumbers(n, firstNumber):
    mid = n // 2
    return firstNumber + mid if firstNumber < mid else firstNumber - mid
