cnt = 0
while True:
    pwd = input("관리자 암호를 입력하세요 : ")

    if pwd == "hanbitac":
        print("로그인 됐습니다.")
        break

    else:
        cnt = cnt + 1
        print("암호를 다시 확인하세요.")


        if cnt >= 5:
            print("횟수 초과로 로그인에 실패하셨습니다.")
            break
