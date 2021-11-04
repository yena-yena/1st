cal = int(input(" 1 더하기 \n 2. 빼기\n 3. 곱하기 \n 4. 나누기 \n숫자를 입력하세요: "))
if 1>cal:
    print("1~4중 하나를 입력해주세요")
elif cal>4:
    print("1~4중 하나를 입력해주세요")
else:
    print("숫자 두 개를 입력하시오")
    a = int(input())
    b = int(input())

    def plus(a, b):
        result = a + b
        print(result)

    def minus(a, b):
        result = a - b
        print(result)

    def mul(a, b):
        result = a * b
        print(result)

    def div(a, b):
        result = a / b
        print(result)

    if cal == 1:
        plus(a, b)
    elif cal == 2:
        minus(a, b)
    elif cal == 3:
        mul(a, b)
    elif cal == 4:
        div(a, b)