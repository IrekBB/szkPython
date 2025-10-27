import sys
"""
Dziedziczenie klas to mechanizm pozwalający na definiowanie nowych klas w oparciu o istniejące tak,
aby poszerzać lub zmieniać ich funkcjonalność. Pozwoli nam na rozwiązanie problemu ze wstępu,
jednak jego zastosowanie znacznie wykracza poza ten szczególny przykład.

Klasy w Pythonie można definiować, podając w ich definicji nazwę istniejącej klasy - tzw. klasę bazową,
z której nowa klasa będzie dziedziczyć (tę nową klasę będziemy też nazywać podklasą klasy bazowej):
"""
class Animal:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed

    def eat(self, food):
        print(f'{self.name}: Yum!')

class Fish(Animal): # Fish dziedziczy z klasy bazowej Animal 
    def swim(self):
        print(f'{self.name}: is swimming!')


class Bird(Animal):
    def fly(self):
        print(f'{self.name}: is flying!')

class Dog(Animal):
    def bark(self):
        print(f'{self.name}: WOOF!')


def main(args):
# Nowoutworzone obiekty typu Fish zostaną wtedy wyposażone w metody 
# zdefiniowane zarówno w Fish, jak i te z klasy bazowej Animal
    nemo = Fish('Nemo', 5.0)
    nemo.swim()           # tłumaczy się na Fish.swim(nemo)
    nemo.eat('fishfood')  # tłumaczy się na Animal.eat(nemo, 'fishfood')

    dog = Dog('Dogmeat', 28.0)
    sparrow = Bird('Elemelek', 46.0)
    dog.bark()
    sparrow.fly()

    # Wciąż możemy też tworzyć instancje bazowej klasy Animal
    orca = Animal('Willy', 56.0)
    orca.eat('tasty fish')

if __name__=="__main__":
    sys.exit(main(sys.argv))