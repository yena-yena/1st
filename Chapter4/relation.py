
def fa(n):
    if number == 1:
        return 1
#        print("a(1) = 1")
    else:
        a = 1
        for i in range(2, number + 1):
            a = a + i
        print("a(" + str(i) + ") =", a)


number = int(input("항 번호 입력 : "))

fa(number)
