def isMAC48Address(inputString):
    mac = inputString.split('-')
    
    if len(mac) != 6:
        return False

    for m in mac:
        if len(m) != 2:
            return False

    mac_str = ''.join(mac)
    for s in mac_str:
        if s not in 'ABCDEF1234567890':
            return False
            
    return True
