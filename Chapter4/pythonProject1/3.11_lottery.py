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
