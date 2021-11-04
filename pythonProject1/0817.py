#9.1
class Cal:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def __add__(self,other):
        return Cal(self.a + self.b)

    def __sub__(self,other):
        return Cal(self.a - self.b)

    def __mul__(self,other):
        return Cal(self.a * self.b)

    def __truediv__(self,other):
        return Cal(self.a / self.b)

add = Cal(123,334)
sub = Cal(123, 334)
mul = Cal(123, 334)
true = Cal(123, 3)

print(add.__add__())
print(sub.__sub__(other))
print(mul.__mul__(other))
print(true.__truediv__(other))


'''
#9.5
a=1
b=1
c=2
d=3
e=3
alphaList = ['a','b','c','d','e']
compareList = [a,b,c,d,e]

for _ in range(4):
    print('{}와 {}는 같은 객체인가?'.format(alphaList[_],alphaList[_+1]), end=' ')
    if compareList[_] is compareList[_+1]:
        print("True")
    else:
        print("False")


#9.6 내가쓴건데 이해가 잘 안됨 ㅠㅠ 9.7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print('my_dog의 이름은 {} 이고, 나이는 {}살 입니다.'.format(self.name,self.age)) 9.6
    def __str__(self):
        return '이름은 {}이고, 나이는 {}살 입니다.'.format(self.name, self.age)
        pass
my_dog = Dog('Mango', '3')
print(my_dog) #9.7
'''


#9.8!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
class Counter:
    __number = 0

    def __init__(self, number = 0):
        self.number = number
        if number>=100 or number<=-1:
            self.number = 0

    def reset(self):
        self.number = 0

    def inc(self):
        self.number = number + 1
        if self.__number >= 100:
            number = 0

    def dec(self):
        number = number - 1
        if number<=-1:
            number = 0

    def __str__(self):
        return'{}'.format(self.__number)

c1 = Counter(10)
c1.inc()
print('c1 = ',c1)
'''

#------------9-9
"""
    def __str__(self, number):
        self.number = number
        if 
c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2 
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)
"""

#9-5
"""class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return 'Cat(name = '+self.name+', color = '+self.color+')'
nabi = Cat('나비', '검정색')
nero = Cat('네로', '흰색')

print(nabi)
print(nero)
"""
#9-6
"""
class Dog:
    name = 0
    def __int__(self, name):
        self.name = name
    def __str__(self):
        return ("my_dog의 정보 :{}".format(my_dog))
my_dog = Dog('Jindo')
"""

#9-4 연습문제
"""
class Dog:
    def bark(self):
        print('Bark Bark!')
    def my_dog_bark(self):
        print('멍멍!')
my_dog = Dog()
my_dog.bark()
my_dog.my_dog_bark()
"""
#9-4 코드
"""
class Cat:
    def __init__(self, name, color):
        self.name = name
        self. color = color
    def meow(self):
        print('내 이름은 {}, 색깔은 {}, 야옹 야옹~~'.format(self.name, self.color))
nabi = Cat('나비', '검정색')
nero = Cat('네로', '흰색')
mimi = Cat('미미', '갈색')

nabi.meow()
nero.meow()
mimi.meow()
"""

#lab 9-5
"""
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print('Bark Bark!!')
    def my_dog_bark(self):
        print('멍멍~!ㅋ')
my_dog = Dog(['Jindo'])
my_dog.bark()
my_dog.my_dog_bark()
"""
