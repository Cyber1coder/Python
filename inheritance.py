class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print("Name : ",self.name , "Age : ",self.age)

class Student(Person):
    def __init__(self, name, age,rollno):
        super().__init__(name, age)
        self.rollno = rollno

    def display(self):
        print("Roll no : ",self.rollno)

s1 = Student("Revatee",20,34)
s1.show()
s1.display()

        