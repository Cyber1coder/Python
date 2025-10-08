with open('qwerty.txt','w') as file:
    file.write("Hi!! Welcome")

with open('qwerty.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.read(2))
    file.seek(6)
    print(file.read())


with open('qwerty.txt', 'r+') as file:
    file.write("Hello ")
    file.seek(0)
    print(file.read())
    file.seek(6)
    print(file.read())

with open('qwerty_w+.txt', 'w+') as file:
    file.write("Hi!! Welcome")
    file.seek(0)
    print(file.read())
    file.seek(0)
    print(file.read(2))
    file.seek(6)
    print(file.read())


