cal=int(input("1. 더하기\n 2. 빼기\n 3. 곱하기\n 4. 나누기\n숫자를 입력해주세요:"))

a=input()
b=input()

if cal==1:
    print("숫자 두 개를 입력하세요")
    def two(a,b):
        result=a+b
        print(result)
two(a,b)

elif cal==2:
    print("숫자 두 개를 입력하세요")
    def two(a,b):
        result=a-b
        print(result)
two(a,b)

elif cal==3:
    print("숫자 두 개를 입력하세요")
    def two(a,b):
        result=a*b
        print(result)
two(a,b)

elif cal==4:
    print("숫자 두 개를 입력하세요")
    def two(a,b):
        result=a/b
        print(result)
two(a,b)

else:
    print("1~4 중 하나를 입력해주세요")