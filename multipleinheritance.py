class Wheel:
    def show_wheel(self):
        print("Wheel")

class Rubber:
    def show_rubber(self):
        print("Rubber")

class Tyre(Wheel,Rubber):
    def show_tyre(self):
        print("Tyre")

t = Tyre()
t.show_wheel()
t.show_rubber()
t.show_tyre()

