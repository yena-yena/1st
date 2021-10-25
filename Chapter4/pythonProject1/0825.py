class Car():
    def __init__(self, name):
        self.name = name

    def Run(self):
        print('차가 달립니다.')

class Truck(Car):
    def __init__(self, name, capacity):
        super().__init__(name)
        self. capacity = capacity
    def speak(self):
        print('이 트럭은 {}톤 트럭입니다.'.format(self.capacity))

name = input('트럭의 이름은? ')
capacity = input('몇 톤입니까? ')
truck = Truck(name, capacity)
#name = Truck()
#capacity = Truck()
truck.speak()
truck.Run()
#capacity.speak()
