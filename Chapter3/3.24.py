n = int(input("숫자를 입력하세요 : "))
x = 0
for i in range(1, n+1):
    x += (1/n)**2
print("결과는", x, "입니다.")