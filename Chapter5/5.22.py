n = int(input("n을 입력하시오: "))

snake_line = []

# list 요소 추가
for i in range(1, n * n + 1):
    snake_line.append(i)
print("snake_line의 요소 : ", snake_line)

# 변수 생성
for i in range(1, n + 1):
    snake = snake_line[n*(i-1):n*i]

    if i % 2 == 0:
        snake.reverse()
        print(*snake, sep='\t', end=" \n")

#        print('{:>}'.format(*snake), sep=' ', end="\t")

    else:
        print(*snake, sep='\t', end=" \n")
#        print('{:>}'.format(*snake), sep=' ', end="\t")


# 포맷팅 어케 하라고....
