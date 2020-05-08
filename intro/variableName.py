def variableName(name):
    value = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
    
    if name[0] in list('0123456789'):
        return False

    for i in name:
        if i not in value:
            return False
    return True
