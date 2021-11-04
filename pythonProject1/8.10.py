import random as r
F_rand = open('randint30.txt','w') # 파일쓰기
for i in range(30):
    num = str(r.randint(1,10))
    F_rand.write(num)
    F_rand.write(' ')
F_rand.close() # 닫아줘야 또다른 모드로 파일을 오픈할 수 있음.

with open ('randint30.txt', 'r') as f: # 파일읽어 list 저장
    randint_list = list(f.readline().split(' '))

cnt_dic = {} # 숫자의 횟수 저장해줄 딕셔너리 생성
for i in range(1,11):
    cnt_dic[i] = 0

for i in range(30): # 딕셔너리에 숫자의 횟수 저장
    for cnt in range(1,11):
        if int(randint_list[i]) == cnt:
            cnt_dic[cnt] += 1

for i in range(10): # 출력
    print('{} : {}개'.format(i+1, cnt_dic[i+1]))