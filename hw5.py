def read_single_digit(integer):
    if integer == 0:
        return '영'
    elif integer == 1:
        return '일'
    elif integer == 2:
        return '이'
    elif integer == 3:
        return '삼'
    elif integer == 4:
        return '사'
    elif integer == 5:
        return '오'
    elif integer == 6:
        return '육'
    elif integer == 7:
        return '칠'
    elif integer == 8:
        return '팔'
    elif integer == 9:
        return '구'
    
def read_number(integer):
    print(read_single_digit(int(integer[0])), end=' ')
    print(read_single_digit(int(integer[1])), end=' ')
    print(read_single_digit(int(integer[2])))

number = input('세 자리 정수 입력: ')
read_number(number)