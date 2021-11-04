length=int(input('우물의 깊이를 입력해주세요 : '))
print('')
height = 7
day = 1

while True:
    if length < 7:
        print('day', day, ': 달팽이의 위치 : ', height, 'm')
        print("\n달팽이가 우물을 탈출하는데", day, '일 걸렸습니다. ')
    else :
        height = height - 3
        height = height + 7
        day = day + 1
        print('day', day, ': 달팽이의 위치 : ', height, 'm')
print("\n달팽이가 우물을 탈출하는데",day,'일 걸렸습니다. ' )

i=int(input('1. 시작 / 2. 종료 \n 다시 시작하시겠습니까? : '))
if i == 1:
    print('tlqkf')
elif i==2:
    print('종료합니다.')
