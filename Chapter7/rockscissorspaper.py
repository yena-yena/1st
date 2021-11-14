import random
rsp = ['가위', '바위', '보']
user = input("가위, 바위, 보 중 하나를 입력하세요 : ")
com = random.choice(rsp)

try:
    if user not in rsp:
        raise ValueError
except ValueError:
    print('잘못된 값을 입력하였습니다')

"while True:"
"if com == user:"



if com == '가위':
    if user == '보':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("졌습니다")
        print("컴퓨터가 선공을 시작하겠습니다.")
        com = random.choice(rsp)
        user = input("가위, 바위, 보 중 하나를 입력하세요 : ")
        print("컴퓨터 : {}".format(com))
        if com ==
    elif user == '가위':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("비겼습니다")
    elif user == '바위':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("이겼습니다")

elif com == '바위':
    if user == '가위':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("졌습니다")
    elif user == '바위':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("비겼습니다")
    elif user == '보':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("이겼습니다")

elif com == '보':
    if user == '바위':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("졌습니다")

    elif user == '가위':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("이겼습니다")
    elif user == '보':
        print("비겼습니다")
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
