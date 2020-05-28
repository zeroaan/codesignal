def messageFromBinaryCode(code):
    # result = ''
    # for i in range(0, len(code), 8):
    #     bit = code[i:i+8]
    #     asc = 0
    #     for j in range(0, 8):
    #         asc += int(bit[j]) * 2**(7-j)
    #     result += chr(asc)
    # return result

    # 위의 코드도 통과하긴 했지만 int 함수를 사용하여 다시 해보았다.
    # int() 함수의 2번째 인자는 디폴트값이 10이지만 2를 입력하여 값을 가져온다.
    
    return ''.join([chr(int(code[i:i+8], 2)) for i in range(0, len(code), 8)])
