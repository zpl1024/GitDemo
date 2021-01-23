"""自己写一个面向对象的例子：

比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】"""

from Animal_test import AnimalDemo

class CatDemo(AnimalDemo):
    def __init__(self,name,color,age,sex):
        super().__init__(name,color,age,sex)
        self.hair = "shorthair"

    def actions(self):
        print(f"{self.animals_name} can catch mouses")

    def sing(self):
        print(f"{self.animals_name} can sing 'miaomiao'")


if __name__ == '__main__':
    cats = CatDemo('xiaohei', 'black', '1', 'female')
    cats.sing()
    cats.actions()
    print(f'{cats.animals_name} has {cats.animals_color} {cats.hair}')

