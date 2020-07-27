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
my_cat = Cat('Catty')

for pet in [my_dog,my_cat]:
    print(type(pet))
    print(pet.speak())