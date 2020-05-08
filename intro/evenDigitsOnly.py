def evenDigitsOnly(n):
    for i in set(str(n)): # list 로 해도 되지만 set으로 하면 중복값을 없애기 때문
        if int(i) % 2 != 0:
            return False
    return True
