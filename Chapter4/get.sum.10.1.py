def get_digit_sum_10_1():
    n = int(input('정수 입력: '))
    n %= 100
    return n // 10 + n % 10
print(get_digit_sum_10_1())
