import sys
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

"""
Mechanizm dziedziczenia pozwala nam zatem na tworzenie wyspecjalizowanych "wersji" istniejących klas, 
uzupełniając je o nowe operacje. Na początku podrozdziału wspomnieliśmy też jednak o możliwości modyfikacji
istniejących operacji. Instancje atrapowego Animal ze smakiem zjadają każde podane im jedzenie.
To zachowanie można zmienić w nowej klasie, dziedziczącej z Animal, poprzez zdefiniowanie na nowo metody eat"""

class Human(Animal):
    def eat(self, food):
        print(f'{self.name}: nie chce mi się jeść.')


def main(args):
    human = Human('Agata', 10.0)
    human.eat('fastfood') # Tłumaczy się na: Human.eat(human, 'fastfood')

if __name__=='__main__':
    sys.exit(main(sys.argv))

"""
Gdy metoda klasy zostaje zdefiniowana na nowo w jej podklasie, będziemy mówić, że została nadpisana. 
"""