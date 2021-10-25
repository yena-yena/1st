import new_module
print("1. 가위바위보 게임")
print("2. 계산기(사칙연산)")
print("3. 현재 날짜 알리미")

func=int(input("원하는 기능을 선택하세요 : "))
if func==1:
    new_module.play()
elif func==2:
    new_module.cal()
elif func==3:
    new_module.nowis()
else:
    print("1,2,3 중 하나를 입력해주세요")