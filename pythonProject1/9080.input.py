"""---------------------------------테스트 케이스 개수 입력받기---------------------------------"""
try:
    test_case = input("테스트 케이스의 개수를 입력하시오. (단 1~10이어야 함) : ")
    if 1 <= int(test_case) <= 10:
        print(test_case)
    else:
        raise ValueError

except ValueError:
    print("다시 입력해주세요.")
    quit()
"""---------------------------------게임 시작 시간 입력받기--------------------------------"""

pay = 0

# for i in test_case: (for문으로 오케쓰냐)


while True:
    HH, MM, D = map(int, input("현성이가 게임 시작하는 시간을 입력하세요. : ").split())
    if HH < 0 or HH > 23 or MM < 0 or MM > 59 or D < 1 or D > 4320:
        print("제대로 된 시간을 입력해주세요.")
        quit()

"""------------------------------------케이스 분류 : 시간계산-----------------------------------"""
if HH >= 22 or 0 <= HH <= 7:
    for i in (HH, 24):
        print(HH, "1")
        HH = HH + 1
        print(HH, "2")
    pay = pay + 5000

else:

    for i in (HH, 24):
        print(HH, "3이거이거")
        HH = HH + 1
        print(HH, "4욕어ㅛ거")
    pay = pay + 1000
