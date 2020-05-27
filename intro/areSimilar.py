def areSimilar(a, b):
    if a == b:
        return True

    value = []

    for i in range(len(a)):
        if a[i] != b[i]:
            value.append(i)
            
    # 13 ~ 14줄은 없어도 문제 통과는 되지만
    # 만약 a = [1, 2, 2], b = [2, 2, 2] 일 경우
    # 16줄에서 인덱스 에러가 나기 때문에 해당 줄을 추가해주었다.
    if len(value) != 2:
        return False
    
    a[value[0]], a[value[1]] = a[value[1]], a[value[0]]
    return a == b
