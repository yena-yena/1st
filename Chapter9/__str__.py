class Human():
    '''인간'''
    def __init__(self, name, weight):
        '''초기화 함수'''
        self.name = name
        self.weight = weight

    def __str__(self):
        '''문자열화 함수'''
        return "{} (몸무게 : {}kg)".format(self.name, self.weight)

person = Human("사람", 60.5) # 초기화 함수 사용
print(person) # 문자열화 함수 사용