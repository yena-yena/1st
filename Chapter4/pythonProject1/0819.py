class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        print('이 과일은 {}입니다. 색깔은 {}입니다.'.format(self.name, self.color))

melon = Fruit('멜론', '초록색')
grape = Fruit('포도','보라색' )
strawberry = Fruit('딸기', '빨강색')
melon.info()
grape.info()
strawberry.info()