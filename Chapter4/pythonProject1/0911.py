x = int(input('-100에서 100 사이의 정수 x를 입력하시오 : '))
if -100<=x<=100:
    print(x)
    if 0<x:
        print(x,'는 자연수입니다.')
else:
    print('x =',x)