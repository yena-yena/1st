import random
import datetime

#1. 가위바위보 승패
def play():

    rsp=['가위','바위','보']
    user=input("가위, 바위, 보 중 하나를 입력하세요 : ")
    com=random.choice(rsp)

    print("플레이어 : {}".format(user))
    print("컴퓨터 : {}".format(com))

    if com=='가위':
        if user=='보':
            print("졌습니다")
        elif user=='가위':
            print("비겼습니다")
        elif user=='바위':
            print("이겼습니다")

    elif com == '바위':
        if user == '가위':
            print("졌습니다")
        elif user=='바위':
            print("비겼습니다")
        elif user=='보':
            print("이겼습니다")

    elif com == '보':
        if user == '바위':
            print("졌습니다")
        elif user == '가위':
            print("이겼습니다")
        elif user == '보':
            print("비겼습니다")

#2. 사칙연산 계산기
def cal():
    a = int(input("정수 a를 입력해주세요 : "))
    b = int(input("정수 b를 입력해주세요 : "))

    def plus(a,b):
        return a+b
    def minus(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b

    print("1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈")
    c=int(input("원하시는 숫자를 골라주세요 : "))

    if c==1:
        print(plus(a,b))
    elif c==2:
        print(minus(a,b))
    elif c==3:
        print(mul(a,b))
    elif c==4:
        print(div(a,b))
    else:
        print("1,2,3,4 중 하나를 입력해주세요")

#3. 현재시간 년, 월, 일 출력
def nowis():
    date=datetime.date.today()
    print("현재 시간은 {}년 {}월 {}일 입니다.".format(date.year,date.month,date.day))