print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("1) 햄버거""\n""2) 치킨""\n" "3) 피자""\n")
menu = int(input("1에서 3까지의 메뉴를 선택하세요 : "))

while menu > 3 or menu < 0:
    menu = int(input("1에서 3까지의 메뉴를 선택하세요 : "))

if menu == 1:
    print("햄버거를 선택하셨습니다.")
elif menu == 2:
    print("치킨을 선택하셨습니다.")
elif menu == 3:
    print("피자를 선택하셨습니다.")


