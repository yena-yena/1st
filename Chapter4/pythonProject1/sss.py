hour=int(input("시간을 입력하세요"))
min=int(input("분을 입력하세요"))
if hour>0:
    if hour>23:#4부터 9까지는 수정요함
        print("0시부터 23시까지 입력해주세요")
    if min<45:
        print(hour-1,(min+60)-45)
    elif min>=45:
        if min < 0:
            print("0분부터 59분까지 입력해주세요")
        if min > 59:
            print("0분부터 59분까지 입력해주세요")
    else:
        print(hour,min-45)

elif hour==0:
    if hour > 23:  # 4부터 9까지는 수정요함
        print("0시부터 23시까지 입력해주세요")
    if min < 45:
        print(23, (min + 60) - 45)
    elif min >= 45:
        if min < 0:
            print("0분부터 59분까지 입력해주세요")
        if min > 59:
            print("0분부터 59분까지 입력해주세요")
    else:
        print(hour, min - 45)