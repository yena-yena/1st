n = int(input("n을 입력하세요 : "))

slist = list(range(1, n * n + 1))

for i in range(n):
    tmp = slist[i*n:(i+1)*n]

    if i % 2 == 1:
        tmp.reverse()
    slist[i*n:(i+1)*n] = tmp

k = 0
for i in slist:
    k = k + 1
    print('{:4d}'.format(i), end='')
    if k % n == 0:
        print()
