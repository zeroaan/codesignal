def lateRide(n):
    minute = n // 60
    second = n % 60
    
    return minute // 10 + minute % 10 + second // 10 + second % 10
