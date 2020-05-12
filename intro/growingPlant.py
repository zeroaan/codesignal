def growingPlant(upSpeed, downSpeed, desiredHeight):
    plant, day = 0, 0
    while(True):
        day += 1
        plant += upSpeed
        if plant >= desiredHeight:
            return day
        plant -= downSpeed
