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
    
def read_number(num):
    num = str(num)

    result = ''

    result += f"{read_single_digit(int(num[0]))} "

    if len(num) == 2:
        result += f"{read_single_digit(int(num[1]))}"

    elif len(num) == 3:
        result += f"{read_single_digit(int(num[1]))} "
        result += f"{read_single_digit(int(num[2]))}"

    return result

number = int(input('세 자리 정수 입력: '))
result = read_number(number)
print(result)