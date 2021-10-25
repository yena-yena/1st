print("세 수를 입력하세요 :")
n1 = int(input())
n2 = int(input())
n3 = int(input())

a = []


def sort3(num1, num2, num3):
    a.append(num1)
    a.append(num2)
    a.append(num3)
    a.sort()
    print("정렬된 리스트는 다음과 같습니다: {} {} {}".format(a[0], a[1], a[2]))


sort3(n1, n2, n3)
