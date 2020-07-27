class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' Says woof'

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' Says MeoW'

my_dog = Dog('Tommy')
print(my_dog)
print(my_dog.name)
print(my_dog.speak())
my_cat = Cat('Catty')
print(my_cat)
print(my_cat.name)
print(my_cat.speak())