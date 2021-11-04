# 3.11


# 3.12
x, y = input("점의 좌표 x, y를 입력하세요 : ").split()
x, y = int(x), int(y)
if abs((x*x + y*y)**1/2) <= 5:
    print("원의 내부에 있음")
else:
    print("원의 외부에 있음")

# 3.25
well = 30
snail = 7
i = 1
while snail < well:
    print("day :", i, " 달팽이의 위치 :", snail, "미터")
    snail += 2
    i += 1
print("day :", i, " 달팽이의 위치 :", snail, "미터", "\n")
print("우물을 탈출하는 데 걸린 날은", i, "일 입니다.")

depth, m, day = 30, 7, 1

while True:
    print("day :", day, " 달팽이의 위치 :", m, "미터")
    day += 1
    m += 2
    if depth <= m:
        print("day :", day, " 달팽이의 위치 :", m, "미터")
        break

print("우물을 탈출하는 데 걸린 날은 {}일 입니다.".format(day))

day = 0
m = 0
while True:
    day = day + 1
    m = m + 7
    print("day1 :", day, "달팽이의 위치 :", m, "미터")
    if m >= 30:
        break
    m = m - 5
print("우물을 탈출하는데 걸린 날은 ", day, "일 입니다.")
