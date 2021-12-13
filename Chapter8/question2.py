alist = []

while True:

    a = int(input("1. 추가 2. 삭제 3. 전체검색 4. 종료 \n"))

    if a == 1:
        b = input("추가할 이름 : ")
        alist.append(b)

    if a == 2:
        b = input("추가할 이름 : ")

        if b not in alist:
            print("삭제할 이름이 없습니다.ㅠㅠ")
        else:
            alist.remove(b)

    if a == 3:
        print(alist)


    if a == 4:
        break

