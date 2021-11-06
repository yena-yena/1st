name = input("이름을 입력하세요 : ")
if name[-3:] == 'vic':
    print('안녕하세요? {} 님. 발칸 반도에서 오셨나요?'.format(name))
else:
    print('안녕하세요? {} 님.'.format(name))
