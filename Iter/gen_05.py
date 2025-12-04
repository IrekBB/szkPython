"""
2. Performance improvements 

Wartości są obliczane tylko wtedy, gdy są potrzebne. Oznacza to, że możesz natychmiast 
rozpocząć przetwarzanie danych, bez czekania na wygenerowanie całej sekwencji.
"""

def main(args):
    # Wyobraź sobie na przykład sumowanie kwadratów pierwszych 1 miliona liczb:
    # Using a list (eager evaluation)
    sum_of_squares_list = sum([x**2 for x in range(1_000_000)])

    # Using a generator (lazy evaluation)
    sum_of_squares_gen = sum(x**2 for x in range(1_000_000))
"""
Chociaż oba podejścia dają ten sam wynik, wersja generatora pozwala uniknąć tworzenia
ogromnej listy, dzięki czemu wynik uzyskujemy szybciej.
"""

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))