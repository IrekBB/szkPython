"""
Special generator methods  
Generatory wyposażone zostały w metody pozwalajace na obustronną komunikację i kontrolę 
zakończenia działania.

Metoda send()
Metoda .send() umożliwia przekazanie wartości z powrotem do generatora, zamieniając go na program współbierzny.
Jest to przydatne podczas tworzenia generatorów interaktywnych lub stanowych.
"""

def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

def main(args):
    acc = accumulator()
    next(acc)  # Start the generator
    print(acc.send(10))  # Output: 10
    print(acc.send(5))   # Output: 15
    print(acc.send(20))  # Output: 35
"""
Oto jak to działa: 
Działanie generatora zaczyna się od next(acc) (inicjalizacja generatora).
Każde wywołanie .send(value) przekazuje wartość spowrotem do generatora, gzie jest przypisywana 
do zmiennej value w instrukcji yield.  Generator aktualizuje swój stan (zmienna total) i zwraca nowy wynik.

"""


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))