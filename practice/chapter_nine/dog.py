'''
    -类：面向对象编程是最有效的软件编写方法之一。在面向对象编程中，
    你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。
    编写类时，你定义一大类对象都有的通用行
    -根据类来创建对象被称为实例化
    -根据约定，在Python中，首字母大写的名称指的是类
    -以self为前缀的变量都可供类中的所有方法使用
    ，我们还可以通过类的任何实例来访问这些变量。
    像这样可通过实例访问的变量称为属性
    -其中__init__()边上各有两个_
'''


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title()+".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
