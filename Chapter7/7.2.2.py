import time as t


def sum1to1000000():
    countsum = 0
    for x in range(1, 1000001):
        countsum = countsum + x


start_time = t.time()

for i in range(100):
    sum1to1000000()

end_time = t.time()
gap = end_time - start_time
print("1,000,000까지의 합을 100번 반복해서 구하는 시간 : {}초".format(gap))
