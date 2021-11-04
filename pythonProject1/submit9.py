while True:
    length = int(input('우물의 깊이를 입력해주세요 : '))
    height = 7
    day = 1
    print('day', day, ': 달팽이의 위치 : ', height, 'm')

    if length > height: #우물깊이>달팽위치
        height = height + 4
        day = day + 1

        if length < height:
            height = height + 3
            print('day', day, ': 달팽이의 위치 : ', height, 'm')
            print("\n달팽이가 우물을 탈출하는데", day, '일 걸렸습니다. ')

            i = int(input('1. 시작 / 2. 종료 \n 다시 시작하시겠습니까? : '))
            if i == 1:
                continue
            elif i == 2:
                print('종료합니다.')
            break
            print('day', day, ': 달팽이의 위치 : ', height, 'm')

##요기 한 줄

    elif length < height:
        print("\n달팽이가 우물을 탈출하는데", day, '일 걸렸습니다. ')
        i=int(input('1. 시작 / 2. 종료 \n 다시 시작하시겠습니까? : '))
        if i == 1:
            continue
        elif i==2:
            print('종료합니다.')
        break

