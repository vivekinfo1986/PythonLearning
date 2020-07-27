#Define a base class with abstract method and using inheritence overwrite it.
class Animal():

    def __init__(self,name):
        self.name = name

    #Testing abstract class
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

class Dog(Animal):
    def speak(self):
        return self.name + " Says woof!!"

class Cat(Animal):
    def speak(self):
        return self.name + " Says MeaW!!"

Pet1 = Dog('Tommy')
Pet2 = Cat('Catty')

print(Pet1.speak())
print(Pet2.speak())

