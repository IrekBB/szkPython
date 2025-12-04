"""
Iteratory vs Generatory
Tradycyjne iteratory w Pythonie wymagały definiowania klas z jawnymi metodami __iter__() i __next__(), 
co znacznie komplikowało  ich tworzenie; funkcje generatora upraszczają ten proces,
automatycznie zachowując stan i eliminując potrzebę stosowania tych metod.

Why We Use Python Generators ?
1. Memory efficiency 
W przeciwieństwie do list i tablic, które przechowują w pamięci wszystkie elementy jednocześnie, 
generatory generują wartości na bieżąco, zatem przechowują w pamięci tylko jeden element na raz.
Rozważmy na przykład różnicę między funkcjami range() i xrange(). W Pythonie 2 range() utworzyła
listę w pamięci, co może być problematyczne w przypadku dużych zakresów. Funkcja xrange() działała 
jak generator, generując wartości leniwie. Ponieważ zachowanie xrange() było bardziej przydatne,
obecnie w Pythonie 3 funkcja range() również zachowuje się jak generator, więc pozwala uniknąć
obciążenia pamięci związanego z jednoczesnym przechowywaniem wszystkich wartości.   

"""
# Aby pokazać pomysł, porównajmy zużycie pamięci podczas generowania sekwencji 10 milionów liczb
def main(args):
    # Using a list
    numbers_list = [x for x in range(10_000_000)]
    print(f"Memory used by list: {sys.getsizeof(numbers_list) / 1_000_000:.2f} MB")

    # Using a generator
    numbers_gen = (x for x in range(10_000_000))
    print(f"Memory used by generator: {sys.getsizeof(numbers_gen)} bytes")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))