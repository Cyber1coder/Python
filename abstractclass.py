from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
dog.sleep()
cat.sound()
