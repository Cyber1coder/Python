class Dog:
    species = "Canine"  

    def __init__(self, name, age):
        self.name = name  
        self.age = age  


dog1 = Dog("Buddy", 3)

print(dog1.name)  
print(dog1.species)

class Dog:
    def __init__(self, name, age):  
        self.name = name 
        self.age = age

    def bark(self): 
        print(f"{self.name} is barking!")


dog1 = Dog("Buddy", 3)
dog1.bark()




