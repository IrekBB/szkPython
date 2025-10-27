#  G. Jagiella
# Skrypt do wykładu Programowanie 2 (Python) Uniwersytet Wrocławski

import sys
"""
 Jest to "szkielet" lub atrapa klasy, reprezentującej bliżej niesprecyzowane zwierzę
 Omówimy dziedziczenie (tu w szczególnym znaczeniu - dziedziczenie klas): koncept programowania obiektowego
 pozwalający na definiowanie nowych klas w oparciu o istniejące, rozszerzając lub zmieniając ich funkcjonalność.
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

def main(args):
    dog = Animal("Dogmeat", 28.0)

    print(dog.get_name())    # tłumaczy się na: Animal.get_name(dog)
    print(dog.get_speed())   # tłumaczy się na: Animal.get_speed(dog)
    dog.eat("bone")   # tłumaczy się na: Animal.eat(dog, "bone")

    orca = Animal("Willy", 56.0)  # tworzy "anonimowy" i "surowy" obiekt x i tłumaczy się na
                              # Animal.__init__(x, "Willy", 56.0)
                              # (tu: utworzony obiekt x zostaje później nazwany orca)

    orca.eat('fish')  # tłumaczy się na: Animal.eat(orca, "fish")



if __name__=="__main__":
    sys.exit(main(sys.argv))
