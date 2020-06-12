
def phoneCall(min1, min2_10, min11, s):
    if min1 <= s <= min1 + 9 * min2_10:
        return 1 + (s - min1) // min2_10
    return 10 + (s - min1 - 9 * min2_10) // min11
