"""
Dekorator @classmethod jest używany, gdy chcemy tworzyć metody, które mają dostęp do klasy 
jako całości i mogą korzystać z jej atrybutów.

W tym przykładzie oblicz_obwod_okregu jest metodą klasy Kalkulator, oznaczoną jako @classmethod. 
Metoda ta używa stałej klasy PI, aby obliczyć obwód okręgu na podstawie podanego promienia. 
Przy użyciu @classmethod metoda ma dostęp do klasy jako swojego pierwszego argumentu, 
co pozwala jej korzystać z atrybutów klasy.
"""
class Kalkulator:
    PI = 3.14159
    
    @classmethod
    def oblicz_obwod_okregu(cls, promien):
        return 2 * cls.PI * promien

def main(args):
    promien = 5
    obwod = Kalkulator.oblicz_obwod_okregu(promien)
    print("Obwód koła o promieniu", promien, "wynosi:", obwod)    

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
