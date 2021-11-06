menu = {"Americano": "3,000원", "Ice Americano": "3,500원", "Cappuccino": "4,000원", "Caffe Latte": "4,500원", "Espresso": "3,600원"}
for key in menu:
    print('{:<20} 가격 : {}'.format(key, menu[key]))

order = input("위의 메뉴 중 하나를 선택하세요 : ")
if order in menu:
    print('{}는 {} 입니다. 결제를 부탁합니다.'.format(order, menu[order]))
