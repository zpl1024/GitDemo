"""自己写一个面向对象的例子：

比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】"""
# from python import decorator_test

class AnimalDemo:
    def __init__(self, name, color, age, sex):
        self.animals_name = name
        self.animals_color = color
        self.animals_age = age
        self.animals_sex = sex

    # @decorator_test.log_decoratorDemo
    def sing(self):
        print(f"{self.animals_name} can singing")

    def running(self):
        print(f"{self.animals_name} can running")


if __name__ == '__main__':
    animals = AnimalDemo('xiaobai', 'white', '2', 'male')
    # animals = AnimalDemo()
    animals.sing()
