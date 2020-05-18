def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2

    result = 0
    if weight1 <= maxW:
        result = value1
    if weight2 <= maxW:
        result = max(value1, value2)
    return result
