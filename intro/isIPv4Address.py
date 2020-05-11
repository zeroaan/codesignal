def isIPv4Address(inputString):
    number = inputString.split('.')

    if len(number) != 4:
        return False

    for i in number:
        if i.isdigit() == False:
            return False
        if int(i) < 0 or int(i) > 255:
            return False
        if i == '00' or i == '01': return False
        
    return True
