def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

nterms = int(input("몇 개의 피보나치 수를 원하세요?"))

if nterms <= 0:
    print("오류 : 양수를 입력하세요.")
else:
    print("Fibonacci 수열 : ", end="")
    for i in range(nterms):
        print(fibonacci(i), end="")