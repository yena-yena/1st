student_tuple = (('191101', '홍길동', '010-123-45xx'), ('191102', '임꺽정', '010-223-45xx'), ('191103', '장길산', '010-323-45xx'))
student_dict = { num:name for num, name, tel in student_tuple }
print('학생 정보 : ', student_dict)

while True:
    grade = input("학번을 입력하세요 : ")

    if grade == student_dict:
        print('{}번 학생은 입니다.'.format(student_dict))


"""        elif int(grade) < 1:
            print("프로그램을 종료합니다.")
            break

        else:
            i = int(i) + 1 #191102가 입력된 경우. . ..
            if grade == i:
                print('{}번 학생은 {}입니다.'.format(i + 1, student_dict[i + 1]))


            else:
                i = int(i) + 1 #191103이 입력된 경우. . ..
                if grade == i:
                    print('{}번 학생은 {}입니다.'.format(i + 1, student_dict[i + 1]))

                else:
                    print("해당 학번의 학생이 없습니다.")
                    print("??")
"""