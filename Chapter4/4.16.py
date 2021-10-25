inputStr = input("쉼표로 구분된 정수를 여러 개 입력하시오 : ")
inputList = inputStr.split(',')
intList = []
for e in inputList:
    intList.append(int(e))
print("입력된 정수의 리스트 : ", intList)


intList.sort()
print("정렬된 정수의 리스트 : ", end="")
for i in intList:
    print(i, end=" ")
