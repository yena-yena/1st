student_tuple = (('191101', '홍길동', '010-123-45xx'), ('191102', '임꺽정', '010-223-45xx'), ('191103', '장길산', '010-323-45xx'))
student_dict = { num:name for num, name, tel in student_tuple }
print('학생 정보 : ', student_dict)

while True:

    for i in student_dict:
        grade = input("학번을 입력하세요 : ")
        if grade == i:
            print('{}번 학생은 {}입니다.'.format(i, student_dict[i]))
            print("1번 문장")
            continue

        elif int(grade) < 1:
            print("프로그램을 종료합니다.")
            quit()

            """2번 문장과 3번 문장에 도달하지 못함"""
        else:
            i = int(i) + 1
            if grade == i:
                print('{}번 학생은 {}입니다.'.format(i + 1, student_dict[i + 1]))
                print("2번 문장")
            else:
                i = int(i) + 1
                if grade == i:
                    print('{}번 학생은 {}입니다.'.format(i + 1, student_dict[i + 1]))
                    print("3번 문장")
                else:
                    print("해당 학번의 학생이 없습니다.")

    break