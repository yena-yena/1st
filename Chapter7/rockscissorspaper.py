import random #random 모듈 import

resStr = ['승리했습니다!!', '패배했습니다!!']
selStr = [['가위', '바위', '보'], ['찌', '묵', '빠']]


# rsp = ['가위', '바위', '보'] #rsp list에 가위 바위 보 저장 --> com이 낼 거임
user = input("가위, 바위, 보 중 하나를 입력하세요 : ") #가위 바위 보 중 하나를 user라는 변수에 input 받음
com = random.choice(rsp) # random.choice를 사용하여 rsp 중 무작위로 com의 수 정함


"""잘못된 값 입력 시 예외처리 구문"""
try:
    if user not in rsp:
        raise ValueError
except ValueError:
    print('잘못된 값을 입력하였습니다')


result = 0
while True:
    user = int(input("가위(0), 바위(1), 보(2)를 선택하세요: "))
    if checkUser(user):
        com = random.randint(0, 2)
        print(f'\t결과 => 사용자 ({selStr[0][user]}) 컴퓨터 ({selStr[0][com]})')
        result = checkWin(user, com)
        if result == 2:
            print('\t비겼습니다. 가위 바위 보 다시합니다.')
        else:
            break



"""가위바위보 코드 짜기"""
if com == '가위':
    if user == '보':
        print("플레이어 : {}".format(user))
        print("컴퓨터 : {}".format(com))
        print("졌습니다")

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


print('\n묵 찌 빠를 시작합니다.')

attack = 0
while True:
    print()
    if result == 0:
        print('[공격하세요] : ', end='')
        attack = 0
    elif result == 1:
        print('[수비하세요] : ', end='')
        attack = 1
    else:
        print('[다시하세요] : ', end='')

    user = int(input("묵(0), 찌(1), 빠(2)를 선택하세요 : "))
    if checkUser(user):
        # checkWin함수를 사용하기 위해 가위바위보 순으로 변경해줍니다.
        if user == 0:  # 묵
            user = 1
        elif user == 1:  # 찌
            user = 0

        com = random.randint(0, 2)
        print(f'\t결과 => 사용자 ({selStr[1][user]}) 컴퓨터 ({selStr[1][com]})')

        result = checkWin(user, com)

        if result == 2:
            print('\n', resStr[attack])
            break

        if attack == 0:
            if result == 1:  # 컴퓨터에게 공격권이 넘어갑니다.
                attack = 1
        else:
            if result == 0:  # 유저에게 공격권이 넘어갑니다.
                attack = 0