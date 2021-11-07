student_tuple = (('191101', '홍길동', '010-123-45xx'), ('191102', '임꺽정', '010-223-45xx'), ('191103', '장길산', '010-323-45xx'))
student_dict = { num:name for num, name, tel in student_tuple }
print('학생 정보 : ', student_dict)

while True:

    grade = int(input("학번을 입력하세요 : "))

    if grade == 191101:
        print('191101번 학생은 홍길동입니다.')

    elif grade == 191102:
        print('191102번 학생은 임꺽정입니다.')

    elif grade == 191103:
        print('191103번 학생은 장길산입니다.')

    elif grade < 1:
        print("프로그램을 종료합니다.")
        break

    else:
        print("해당 학번의 학생이 없습니다.")

