def sum_avg(*numbers):
    s = 0
    for i in numbers:
        s += i
    a = s / len(numbers)
    print("s ->", s, ",", "a -> ", a)


sum_avg(1.1, 2.2, 3.3, 4.4)
