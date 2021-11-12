num = int(input("정수 입력 : "))
maximum = num
print("초기 최대값 = ", maximum)

while num != 0:
    if num > maximum:
        maximum = num
        print("바뀐 최대값 =", maximum)

    else:
        num = int(input("정수를 입력해 : "))
print("최종 최대값 = ", maximum)
