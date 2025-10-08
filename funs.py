def greet():
    print("Hello")
greet()


def welcome(name="User"):
    print("Welcome", name)
welcome("Alice")


add = lambda x, y: x + y
print(add(5, 7))
