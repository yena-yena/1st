# 1.10
"""반복문을 이용, 1~10까지 합"""


# way 1
List = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
t = 0
for x in List:
    t = t+x
print(t)


# way 2
for i in (1, 11):  # 이렇게 쓰면 그냥 i가 1 그리고 11일 때로 인식함. 따라서 두 개의 결괏값이 출력됨
    print('zz')
    print(i)



"""------------------------------------------------------------------------------------------------"""

# 1.14
"""n!"""
n = int(input('팩토리얼 연산할 숫자를 입력하세용 : '))
x = 1
for i in range(1, n+1):
    x = x * i
print(x)

# int(input())! 왕중요!
