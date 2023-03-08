class Shark:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress



    def swim(self):
        print('the shark is swimming')

    def eat(self):
        print('the shark is eating')

    def bite(self):
        print(5 + 5)

def main():
    netzer = Shark('netzer', 31, 'metzer')
    # definition of object netzer

    netzer.eat()
    netzer.swim()
    netzer.bite()

    print(netzer.age)

    noa = Shark('noa', 31, 'metzer')
    # definition of object noa


    gil = Shark('gil', 2, 'metzer')
    gil.adress = 'metzer'
    print(gil.adress)

main()

class Reef(Shark):
    def __init__(self, name, age, adress, type, depth):
        Shark.__init__(self, name, age, adress)
        self.type = type
        self.depth = depth
# definition of child calss named 'Reef'
# definition of constructor with the new properties
# must calling function of first constructor

def main_2():
    nevo = Reef('nevo', 0, 'metzer', 'rock', 30)

    print(nevo.type)

    karin = Reef('karin', 63, 'metzer', 'grandma', 40)
    karin.swim()
    karin.bite()


main_2()

# a = 1
# b = 2

# for x in range(100):
    # print(x)
# debug check

