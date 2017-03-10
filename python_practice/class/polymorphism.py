class User:
    def __init__(self, name):
        self.name = name

    def eat_something(self, item):
        item.eat()

class Food:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('{}를 먹었다. 배가부르다.'.format(self.name))

class Drink:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('{}를 마셨다. 갈증이 해소된다.'.format(self.name))

user = User('이한영')
food1 = Food('햄버거')
drink1 = Drink('포카리 스웨트')

user.eat_something(food1)
user.eat_something(drink1)