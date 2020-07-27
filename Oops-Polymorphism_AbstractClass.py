# How to use abstract class in polymorphism which never expect to create instance

class Animal():

    def __init__(self,name):
        self.name = name

    #Testing abstract class
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

#crating instance of base class

mypet = Animal('Tommy')

mypet.speak('Hello')