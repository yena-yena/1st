n = int(input("숫자를 입력하세요 : "))
a = 1
s = 0
for i in range(1, n+1):
    s = a ** 2 + s
    a += 1
print("결과는", s, "입니다.")
