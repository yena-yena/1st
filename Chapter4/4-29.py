def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
number = int((input("정수를 입력하세요 : ")))

print("{}! = {}".format(number, factorial(number)))