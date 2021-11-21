import random as r
import re

picklist = list()
numlist = list()


for i in range(10):
    pick = r.randint(1, 1000)
    picklist.append(pick)

# print(picklist)
picklist = list(map(int, picklist))



f = open("random_numbers.txt", "w")
f.write(str(picklist))
f.close()

# random_numbers 파일 읽기
fr = open("random_numbers.txt", "r")
temp = fr.readlines()

#,를 기준으로 문자열을 만들기
s = ",".join(temp)
#숫자만을 뽑아내서 리스트에 넣기
s = re.findall("\d+", s)
# print(s)

#문자열 타입의 리스트를 정수형으로 바꾸기
picklist = list(map(int,s))

# 짝수 구별하는 코드
for i in picklist:
    #i = int(i) # i의 type : str

    # 문자열 형식 지정 중에 변환되지 않은 인수도 있습니다.
    if i % 2 == 0:
        numlist.append(i)

    else:
        continue


# random_even 파일 쓰기
fw = open("random_even.txt", "w")
fw.write(str(numlist))
fw.close()

# 홀수 구별하는 코드
for i in picklist:
    #i = int(i) # i의 type : str
    # 문자열 형식 지정 중에 변환되지 않은 인수도 있습니다.
    if i % 2 == 0:
        continue

    else:
        numlist.append(i)

# random_odd 파일 쓰기
fw = open("random_odd.txt", "w")
fw.write(str(numlist))
fw.close()
