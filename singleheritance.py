class Animal:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("Name : ",self.name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def getname(self):
        print("The dogs name is : " ,self.name)

d = Dog("Tommy")
d.display()
d.getname()