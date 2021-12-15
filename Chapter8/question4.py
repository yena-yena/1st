Americano = 3000
Ice_Americano = 3500
Cappuccino = 4000
Caffe_Latte = 4500
Espresso = 6000
pickup = input("메뉴를 골라주세요 : Americano = 3000 Ice_Americano = 3500 Cappuccino = 4000 Caffe_Latte = 4500 Espresso = 6000")

received2 = 0
received = int(input("돈을 넣어주세요 : "))
if pickup == "Americano":
    if received >= Americano:
        print("거스름돈", received - Americano, "원이 반환되었습니다.")

    else: #거스름돈을 받는경우
        received2 = received + received2
        print(Americano - received, "원을 더 넣어주세요.")

        while True:
            received3 = int(input("돈을 더 넣어주세요."))
            if received3 == Americano - received:
                print("커피값 결제 완료!")
                break
            elif received3 < Americano - received:
                print("돈을 더 넣어주세요")
                continue
