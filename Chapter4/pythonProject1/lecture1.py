#3.18
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.\n')
print(' 1. 햄버거\n 2. 치킨 \n 3. 피자\n')
a=int(input('1에서 3까지의 메뉴를 선택하세요 : '))
if a==1 or a==2 or a==3:
    if a==1:
        print('햄버거')
    elif a==2:
        print('치킨')
    elif a==3:
        print('피자')
else:
    print('1~3까지의 메뉴를 선택하세요')

#2.19
num=int(input('정수를 입력하세요 : '))
print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? ')
if 0<=num<=100:
    if num%2==0:
        print('True')
    else:
        print('False')
else:
    print('False')