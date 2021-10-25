a=input("가위바위보 중 입력하세요 : ")
b=input("가위바위보 중 입력하세요 : ")
if a=='가위':
    elif b=='바위':
        print("b가 이겼습니다")
    elif b=='가위':
        print("비겼습니다")
    else:
        print("a가 이겼습니다")

elif a=='바위':
    elif b=='바위':
        print("비겼습니다")
    elif b=='가위':
        print("a가 이겼습니다")
    else:
        print("b가 이겼습니다")

elif a=='보':
    elif b=='바위':
        print("a가 이겼습니다")
    elif b=='가위':
        print("b가 이겼습니다")
    else:
        print("비겼습니다")
