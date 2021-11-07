student_tuple = (('191101', '홍길동', '010-123-45xx'), ('191102', '임꺽정', '010-223-45xx'), ('191103', '장길산', '010-323-45xx'))
student_dict = { num:name for num, name, tel in student_tuple }
print('학생 정보 : ', student_dict)

while True:

    grade = input("학번을 입력하세요 : ")

    if int(grade) >= 1:
        if grade == '191101':
            print(student_dict[191101], '번 학생은 입니다.')
            continue

        elif grade == '191102':
            print('{}번 학생은 입니다.'.format(student_dict[1]))
            print("2번 문장")

        elif grade == '191103':
            print('{}번 학생은 입니다.'.format(student_dict[2]))

        else:
            print("해당 학번의 학생이 없습니다.")

    elif int(grade) < 1:
        print("프로그램을 종료합니다.")
        quit()


