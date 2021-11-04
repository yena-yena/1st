#8.1(3)
a_list = [200, 300, 400]
try:
    print('a_list : ', a_list)
    idx=int(input("구하고자 하는 값의 인덱스를 0,1,2 중에서 입력하시오 : "))
    result = a_list[idx]
    print('결과 : ', result)
except:#Value Error(문자 사용했을때,a), Index Error(범위 벗어남, 5같은)
    print('0,1,2 중 하나를 입력해주세요')
    print('끝입니다')

