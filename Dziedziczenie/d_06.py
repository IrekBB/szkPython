# Bardzo częstą sytuacją odwoływania się do metod z nadklas jest pisanie konstruktora podklasy. 
# Modyfikując przykład z poprzednieg pliku
class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    
    def do_something(self):
        print('obiekt Vehicle coś robi!')
    
class Car(Vehicle):
    def __init__(self, color, speed, n_wheels): # n_wheels - ile kół
        super().__init__(color, speed) # czyli tu: Vehicle.__init__(self, color, speed) - inicjalizuje atrybuty color i speed
        self.n_wheels = n_wheels # część specyficzna dla Car
    def do_something(self):
        super().do_something()
        print('obiekt Car coś robi!')

def main(args):
    car = Car("red", 250, 4)
    print(car.color)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

"""
- B jest podklasą A gdy B dziedziczy z A, bezpośrednio lub nie. Równoważnie, A jest wtedy nadklasą B.

- Klasa bazowa klasy A: w szerszym rozumieniu, to samo co nadklasa. W węższym rozumieniu: klasa, 
z której A dziedziczy bezpośrednio (czyli klasa podana w nawiasie w definicji A).

- Metoda: występuje w dwóch znaczeniach. Nieprzywiązana metoda to funkcja, zdefiniowana w treści 
danej klasy. Metoda przywiązana to atrybut obiektu (z reguły instancji danej klasy), której 
wywołanie wywołuje stosowną funkcję (nieprzywiązaną metodę) odpowiedniej klasy, podając ten obiekt 
jako pierwszy parametr self.

"""