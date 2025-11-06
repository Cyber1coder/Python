class A:
    def displayA(self):
        print("Class A")

class B(A):
        def displayB(self):
            print("Class B")

obj = B()
obj.displayA()
obj.displayB()

class X:
    def displayX(self):
        print("Class X")

class Y:
    def displayY(self):
        print("Class Y")

class Z(X, Y):
    def displayZ(self):
        print("Class Z")

obj2 = Z()
obj2.displayX()
obj2.displayY()
obj2.displayZ()

class Parent:
    def displayParent(self):
        print("Parent")

class Child1(Parent):
    def displayChild1(self):
        print("Child1")

class Child2(Parent):
    def displayChild2(self):
        print("Child2")

class GrandChild(Child1, Child2):
    def displayGrandChild(self):
        print("GrandChild")

obj3 = GrandChild()
obj3.displayParent()
obj3.displayChild1()
obj3.displayChild2()
obj3.displayGrandChild()
