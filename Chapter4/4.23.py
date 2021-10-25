import math as m
radius = int(input("반지름을 입력하시오: "))


def area_and_circumference(r):
    area = r * r * m.pi
    circumstance = 2 * r * m.pi
    print("넓이 : {0:7.3f}, 둘레 : {0:7.3f}".format(area, circumstance))
    while r > 0:
        r = int(input("반지름을 입력하시오: "))
    print("프로그램을 종료합니다.")


area_and_circumference(radius)
