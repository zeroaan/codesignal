def sumUpNumbers(inputString):
    a = [i if i.isdigit() else '/' for i in inputString]
    b = ''.join(a)
    c = b.split('/')

    return sum([int(i) for i in c if i.isdigit()])
