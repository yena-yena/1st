import random as r

picklist = list()
numlist = list()


for i in range(10):
    pick = r.randint(1, 1000)
    picklist.append(pick)

print(picklist)
# picklist = list(map(int, picklist))   --->요거 잘못됨 그래서 이중 리스트 씌워진듯

# print(type(picklist))


f = open("random_numbers.txt", "w")
f.write(str(picklist))
f.close()
# print(type(picklist))

# random_numbers 파일 읽기
fr = open("random_numbers.txt", "r")
reading = fr.readline()


# 짝수 구별하는 코드
for i in reading:
    # 문자열 형식 지정 중에 변환되지 않은 인수도 있습니다.
    if int(i) % 2 == 0:
        numlist.append(i)

    else:
        continue


# random_even 파일 쓰기
fw = open("random_even.txt", "w")
fw.write(str(numlist))
fw.close()

# 홀수 구별하는 코드
for i in picklist:

    # 문자열 형식 지정 중에 변환되지 않은 인수도 있습니다.
    if i % 2 == 0:
        continue

    else:
        numlist.append(i)

# random_odd 파일 쓰기
fw = open("random_odd.txt", "w")
fw.write(str(numlist))
fw.close()
