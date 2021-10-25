n = int(input("숫자를 입력하세요 : "))

for i in range(1, n):
    i += 1
    if n % i == 0:
        print(n, "은 소수가 아닙니다.")

