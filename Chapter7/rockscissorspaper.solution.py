import random

resStr = ['승리했습니다!!', '패배했습니다!!']
selStr = [['가위', '바위', '보'], ['찌', '묵', '빠']]


###################################################################
## 함수 :: 가위바위보 승패를 체크합니다.
###################################################################
def checkWin(user, com):
    if user == com:  # 비겼을때
        return 2
    elif user == 0 and com == 1:  # 가위 vs 바위
        return 1
    elif user == 1 and com == 2:  # 바위 vs 보
        return 1
    elif user == 2 and com == 0:  # 보 vs 가위
        return 1
    else:  # 나머지는 이겼을때
        return 0


###################################################################
## 함수 :: user의 입력이 잘못되었는지 확인
###################################################################
def checkUser(user):
    if user < 0 or user > 2:  # 잘못입력한 것에 대한 예외처리
        print('잘못입력하였습니다. 다시 입력하세요(0,1,2)')
        return False
    return True


###################################################################
## 가위바위보를 하여 누가 먼저 공격할지 정합니다.
###################################################################
print('\n## 안내 ## 누가 공격을 할지 정합니다.(가위 바위 보)\n')
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

###################################################################
## 묵찌빠를 시작합니다.
###################################################################
print('\n## 안내 ## 묵 찌 빠를 시작합니다.')

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