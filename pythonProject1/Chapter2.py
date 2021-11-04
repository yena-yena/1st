# 2.14
"""거듭제곱 연산자 이용"""

for i in range(2, 11):
    print(i, "의 제곱근 =", i**(1/2))

# 2.15
"""피타고라스 정리 사용"""
a = int(input("밑변을 입력하세요 : "))
b = int(input("높이를 입력하세요 : "))
c = (a**2+b**2)**(1/2)
# c**2 = a**2+b**2  !할당연산자!

print("빗변의 길이 :", c)

# 지식인
"""1~1000까지의 약수 구하기"""
a = 1
for i in range(1, 1001):
    print(a)
    print(i, "의 약수 :", i % a == 0)
    a += 1

# 2.16
"""삼각함수 좌표 구하기"""
import math as m
space = 1+2j
sspace = (1+2j)
# nono = (5)

rotation = 1j
rrotation = m.sin(m.pi/2.0) * 1j

print("회전하기 전 :", space)
print("회전하기 전 :", sspace)
# print(nono)

print("90도 회전한 후 case1 :", space * rotation)
print("90도 회전한 후 case2 :", space * rrotation)

print("회전하기 전 :", space)
print("회전하기 전 :", sspace)


rotation2 = m.cos(m.pi/6.0) + m.sin(m.pi/6.0) * 1j
print("30도 회전한 후 :", space * rotation2)

# 2.18
"""짝수 판정기"""
n = int(input("정수를 입력하세요: "))
print("이 수가 짝수인가요?", n % 2 == 0)

# 2.19
"""0~100의 범위에 있는 짝수인지 판별"""
n = int(input("정수를 입력하세요: "))
print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", end=" ")
if 0 < n < 100:
    print("True")
else:
    print("False")

# 2.20
"""비트연산자 사용법 익히기"""
print(bin(5), "&", bin(6), "=", bin(5 & 6))
print(bin(5), "|", bin(6), "=", bin(5 | 6))
print(bin(5), "^", bin(6), "=", bin(5 ^ 6))

# 2.21
"""비트 부정 연산자 ~ 의 사용"""
n = int(input("정수를 입력하시오: "))
print(n, "의 2진수 값 :", bin(n))
print(n, "의 2진수 값에 대한 비트단위 부정값:", bin(~n))

# 2.22
"""%와 /의 사용"""
a = int(input("정수 a를 입력하시오 : "))
b = int(input("정수 b를 입력하시오 : "))
print("a / b의 몫 :", a // b)
print("a / b의 나머지:", a % b)

# 2.23, 2.24
"""과제로 대신함. //연산자와 %연산자의 사용"""
n = int(input('세 자리 정수를 입력하세요 : '))
print('백의 자리 : ', n // 100)
print('십의 자리 : ', n // 10 - (n//100) * 10)
print('일의 자리 : ', n % (n // 10))

