import random as r
print("start")
score = 0
while True:
    s = input("start->enter / stop -> 0 : ")

    if s != "0":
        a = r.randint(1, 9)
        b = r.randint(1, 9)

        print(a, "x", b, "= ", end="")
        x = int(input())

        if a * b == x:
            score = score + 1
            print("score : ", score)
        else:
            print("failed!")

    else:
        print("stopped")
        break
