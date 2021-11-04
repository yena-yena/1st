# 3.12
x, y = input("점의 좌표 x, y를 입력하세요 : ").split()
x, y = int(x), int(y)
if (x*x + y*y)**(1/2) <= 5:
    print("원의 내부에 있음")
else:
    print("원의 외부에 있음")

# 3.13

# 3.14
alphabet = input("알파벳을 입력하세요 : ")
if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
    print(alphabet, "은 모음입니다.")
else:
    print(alphabet, "은 자음입니다.")

# 3.15
a = 2
# way 1.
for i in range(1, 10):
    print(a, "*", i, "=", a*i)
    i += 1
print("\n")
# way2.
z = 1
while z < 10:
    print(a, "*", z, "=", a * z)
    z += 1

# 3.16
number = int(input("1에서 9까지의 수를 입력하세요 : "))
if number < 1 or number > 9:
    print("1에서 9까지의 수를 다시 입력하세요 : ")
# way1.
for i in range(1, 10):
    print(number, "*", i, "=", number*i)
    i += 1
print("\n")
# way2.
z = 1
while z < 10:
    print(number, "*", z, "=", number*z)
    z += 1

