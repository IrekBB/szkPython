"""
G. Jagiella
Skrypt do wykładu Programowanie 2 (Python) Uniwersytet Wrocławski
"""
"""
Powiedzmy, że chcemy odziedziczyc po klasie Vehicle, która nie reprezentuje żadnego prawdziwego obiektu,
klasy Car, Train, Airplane, Ship, itp. Nie chcemy jednak dopuścic mozliwości utworzenia obiektu tej klasy (Vehicle)
Bo nie miało by to sensu. Jest to przecież klasa opisujaca pojazd całkowicie abstrakcyjny.

W programowaniu obiektowym, rozwiązaniem powyższego problemu są interfejsy. 
Interfejs to pewnego rodzaju konstrukcja (niekoniecznie klasa!), składająca się 
z deklaracji metod, ale nie ich implementacji (czyli tak zwanych metod abstrakcyjnych). 
Konkretne klasy mogą implementować interfejs poprzez implementowanie jego metod.

W Pythonie nie ma interfejsów per se, ale są sposoby emulowania ich: abstrakcyjne klasy bazowe 
(abstract base class, abc)
"""
import abc     # Wbudowany moduł abc zawiera klasę bazową ABC, oraz dekoratory, 
               # służące do oznaczenia metod klas z niej dziedziczących jako metody abstrakcyjne.
class Vehicle(abc.ABC):
    @abc.abstractmethod
    def get_domain(self):
        pass
    @abc.abstractmethod
    def get_speed(self):
        pass
    
class Car (Vehicle):
    def get_domain(self):
        return "land"
    def get_speed(self):
        return 100

class LandVehicle(Vehicle):  # w klasie brakuje nadpisania metody get_speed
    def get_domain(self):   
        return "land"    


def main(args):
    try:
        veh = Vehicle()
    except Exception as e:
        print ('Wyjatek:',type(e),' ' ,e)

    car = Car()
    print(isinstance(car, Vehicle)) # Car jest instancją Vehicle - czyli realizuje wymagany interfejs
    print(car.get_speed())    

    try:
        veh = LandVehicle()
    except Exception as e:
        print('Wyjątek:', type(e), e)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))