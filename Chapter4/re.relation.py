def fa(n):
    if n == 1:
        return 1
#        print("a(1) = 1")
    else:
        return (fa(n-1) + n)
#        a = 1
#        for i in range(2, number + 1):
#            a = a + i
#

number = int(input("항 번호 입력 : "))

if number < 1:
    print("수열 an은 1항부터 시작합니다.")
else:
    print("a(" + str(number) + ") =", fa(number))