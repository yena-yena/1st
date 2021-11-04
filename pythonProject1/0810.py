#4. 1994년 5.5일 태어난 사람이 현재 며칠째 살고 있는지 계산하는 프로그램 작성하기 -->module
import time
tm=(1994,5,5,0,0,0,0,0,0)  #해당 날짜에 대해 튜플을 생성하고 mktime 함수를 사용해서 tm을 에폭시로 바꾼다.
birth=time.mktime(tm)
today=time.time()
gone=(today-birth)/(60*60*24)
print("태어난 지 {}일 지났습니다.".format(gone))

#5. 10에서 20사이의 난수 10개를 뽑아 출력하라. 끝 수인 20도 포함된다.  -->module
import random
for i in range(10):
    print(random.randint(10,20))

#5. domain 변수는 임의의 웹 주소를 가지고 있다. 이 도메인이 .kr로 끝나는 한국 도메인인지 확인하는 코드를 작성하라.-->function
domain='http://www.hihi.kr'
if domain.endswith('.kr'):
    print('한국 도메인입니당')

#6. sosi 문자열에 '태연, 서현, 수영' 이름이 저장돼 있다. 각 가수의 이름을 추출하여 '사랑해'와 함께 출력하라.-->function
sosi='태연,서현,수영'
singer=sosi.split(',')  ##쉼표 기준으로 자름
for s in singer:
    print(s,'사랑해')



#6.9
tup=(1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)
print(tup)
set1=set(tup)
print(set1)
set2=tuple(set1)
print(set2)

#6.7
#record=(100,121,120,130,140,120,122,123,190,125)
#record[1:]
#for i in record[1:]:
    #if record[i]>record[i+1]:
        #print(i)
tup = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)

print('일일 매출 기록:', tup)

n = 0

for i in range(1, 10):
    if tup[i] < tup[i-1]:
        n += 1

print('지난 10일 동안 전일대비 매출이 감소한 날은 {}일입니다.'.format(n))
#6.26
#mylist=[(1,2),(4,5),(4,2),(3,1),(9,4)]
#user=tuple(input('a,b 두 값을 입력하시오 : '))
#if user in mylist:
    #print('x a,b')

mylist = [(1,2), (4,5), (4,2), (3,1), (9,4)]
user_list = list(map(int,input("두 정수를 입력하시오: ").split()))
unum1 = user_list[0]
unum2 = user_list[1]

for i in range(5):
    mynum1 = mylist[i][0]
    mynum2 = mylist[i][1]

    if unum1 == mynum1 and unum2 == mynum2:
        print("{} 번째에 ({},{}) 요소가 있습니다.".format(i+1, unum1, unum2))
        break
    elif unum1 == mynum2 and unum2 == mynum1:
        print("({0},{1}) 요소가 없으나, {2} 번째에 ({1},{0})요소가 있습니다.".format(unum1, unum2, i+1))
        break

if unum1 != mynum1 and unum2 != mynum2:
    print("이 요소는 없습니다.")
#7.6
import math