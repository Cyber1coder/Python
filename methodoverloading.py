class MethodOverloading:
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print("Two arguments:", a, b)
        elif a is not None:
            print("One argument:", a)
        else:
            print("No arguments")

obj = MethodOverloading()
obj.show()
obj.show(10)
obj.show(10, 20)
