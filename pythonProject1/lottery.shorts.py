lottery1 = 2
lottery2 = 3
lottery3 = 9


n1, n2, n3 = input("세 복권번호를 입력하시오 : ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)

lottery_list = [lottery1, lottery2, lottery3]
input_list = [n1, n2, n3]
count = 0

for i in input_list:
    for x in lottery_list:
        if x == i:
            count = count + 1


if count == 0:
    print("꽝입니다.")
elif count == 1:
    print("1만원 당첨!")
elif count == 2:
    print("1천만원 당첨!")
elif count == 3:
    print("1억원 당첨!")
