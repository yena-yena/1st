list=[]
n=int(input("리스트의 길이 : ")) #리스트의 길이 입력받기 근데 n으로
if n<=1:
    print("n는 1이거나 1을 넘지 않는 정수입니다")
else:
    print("n개의 정수를 입력해주세요 : ")
    for i in range(0,n):
        add=int(input())
        list.append(add)
    print("리스트의 요소 :{}".format(list))

    m=int(input("정수 m을 입력해주세요 : "))
    for i in range(0,m):
        if m>list[i]:
            print(list[i])
