# Inheritance
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

a = Animal()
a.speak()  # print: Some sound
d = Dog()
d.speak()   # print: Woof!
#Dog 继承自 Animal，但它重写（override）了 speak 方法。