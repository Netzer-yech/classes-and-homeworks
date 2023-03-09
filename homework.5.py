# A
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# B
# 3

# C

class Husky(Dog):
    def __init__(self, name, age, color):
        Dog.__init__(self, name, age)

    def howl(self):
        print('ahooooo')

# D
class BlackHusky(Husky):
    def return_color(self):
        return 'black'

# E
# a no age argument defined 'stevie = Shark(3)

def main():
    rexi = Dog('rexi', 3)
    print(rexi.name, rexi.age)
    netzer = Husky('netzer', 31, 'brown')
    netzer.howl()
    willy = BlackHusky('willy', 4, 'black')
    print(willy.return_color())

main()

# F
uno = Dog('uno', 6)
yuka = Dog('yoka', 3)
ana = Dog('ana', 1)
list_dogs = [uno, yuka, ana]
for x in list_dogs:
    print(x.name)
# x is a variable only for starting the loop and callig name argument




