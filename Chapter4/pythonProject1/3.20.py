n = int(input("숫자를 입력하세요 : "))
for i in range(1, n + 1):
    for z in range(10 - i):
        print(" ", end='')
    for z in range(i):
        print('*', end='')
    print()
