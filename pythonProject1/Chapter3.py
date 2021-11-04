# 3.2
"""if문 사용(숫자 범위)"""
name = input("이름을 입력하시오 : ")
height = int(input("키를 입력하세요 (단위 cm) : "))
if height >= 140:
    print(name, "님은 놀이기구를 탈 수 있습니다.")
else:
    print(name, "님은 놀이기구를 탈 수 없습니다.")

# 3.3
age = int(input("나이를 입력하시오 : "))
height = int(input("키를 입력하시오(단위 cm) : "))
if age >= 19 and height >= 150:
    print("입장할 수 있습니다.")
else:
    print("입장할 수 없습니다.")

# 3.4
age = int(input("나이를 입력하시오 : "))
if age >= 20:
    print("Adult")
elif 10 <= age < 20:
    print("Youth")
else:
    print("Kid")

# 3.5
# way 1
"""스플릿 그냥 쓰자!!"""
# input 받는순간 걍 줄바꿈이 됨
print("두 정수를 입력하시오 :", end=" ")
n1 = int(input())
print(end="")
n2 = int(input())
if n1 > n2:
    print(n2, n1, end="")
else:
    print(n1, n2)

# way 2
n1, n2 = input("두 정수를 입력하시오 :").split()
n1, n2 = int(n1), int(n2)
if n1 > n2:
    print(n2, n1, end="")
else:
    print(n1, n2)

# 3.6
"""작은 거부터 나열, 근데 숫자가 세개인.."""
n1, n2, n3 = input("세 정수를 입력하시오 : ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 > n2:
    if n3 > n1:
        if n3 > n2:
            print(n2, n1, n3, end="")
        else:
            print(n3, n2, n1, end="")

    elif n3 < n1:
        if n3 > n2:
            print(n2, n3, n1, end="")
        else:
            print(n3, n2, n1, end="")

else:
    if n3 > n2:
        if n3 > n1:
            print(n1, n2, n3, end="")
        else:
            print(n3, n1, n2, end="")

    elif n3 < n2:
        if n3 > n1:
            print(n1, n3, n2, end="")
        else:
            print(n3, n1, n2, end="")

# 3.7
game_score = int(input("게임 점수를 입력하시오 : "))
if game_score >=1000:
    print("고수입니다.")
else:
    print("입문자입니다.")

# 3.8
x, y = input("점의 좌표 x, y를 입력하시오 : ").split()
x, y = int(x), int(y)
if x > 0:
    if y > 0:
        print("1사분면에 있음")
    elif y < 0:
        print("4사분면에 있음")
    else:
        print("점은 축 위에 놓여 있습니다.")

elif x < 0:
    if y > 0:
        print("2사분면에 있음")
    elif y < 0:
        print("3사분면에 있음")
    else:
        print("점은 축 위에 놓여 있습니다.")

else:
    print("점은 축 위에 놓여 있습니다.")

# 3.9
n = int(input("정수를 입력하시오 : "))
if n % 2 == 0:
    print(n, "은 2로 나누어집니다.")

    if n % 3 == 0:
        print(n, "은 3으로 나누어집니다.")
        print(n, "은 2와 3 모두로 나누어집니다.")
    else:
        print(n, "은 3으로 나누어지지 않습니다.")
else:
    print(n, "은 2로 나누어지지 않습니다.")

    if n % 3 == 0:
        print(n, "은 3으로 나누어집니다.")

    else:
        print(n, "은 3으로 나누어지지 않습니다.")
        print(n, "은 2와 3 모두로 나누어지지 않습니다.")

# 3.10
a, b = input("두 정수를 입력하시오 : ").split()
a, b = int(a), int(b)
if a % b == 0:
    print(a, "는", b, "의 배수입니다.")
else:
    print(a, "는", b, "의 배수가 아닙니다.")


# 3.11
lottery1 = 2
lottery2 = 3
lottery3 = 9
n1, n2, n3 = input("세 복권번호를 입력하시오 : ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 == lottery1:

    if n2 == lottery2:
        if n3 == lottery3:
            print("축하합니다! 1억원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")

    elif n2 == lottery3:
        if n3 == lottery2:
            print("축하합니다! 1억원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")

    else:
        if n3 == lottery2:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        elif n3 == lottery3:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")


elif n1 == lottery2:

    if n2 == lottery1:
        if n3 == lottery3:
            print("축하합니다! 1억원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")

    elif n2 == lottery3:
        if n3 == lottery1:
            print("축하합니다! 1억원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")

    else:
        if n3 == lottery1:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        elif n3 == lottery3:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")


elif n1 == lottery3:
    if n2 == lottery1:
        if n3 == lottery2:
            print("축하합니다! 1억원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
    elif n2 == lottery2:
        if n3 == lottery1:
            print("축하합니다! 1억원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
    else:
        if n3 == lottery2:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        elif n3 == lottery1:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")


else:
    if n2 == lottery1:
        if n3 == lottery2:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        elif n3 == lottery3:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")

    elif n2 == lottery2:
        if n3 == lottery1:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        elif n3 == lottery3:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")

    elif n2 == lottery3:
        if n3 == lottery1:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        elif n3 == lottery2:
            print("축하합니다! 1천만원 상금의 주인공이 되셨습니다!")
        else:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")

    else:
        if n3 == lottery1:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")
        elif n3 == lottery2:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")
        elif n3 == lottery3:
            print("축하합니다! 1만원 상금의 주인공이 되셨습니다!")
        else:
            print("꽝입니다.")