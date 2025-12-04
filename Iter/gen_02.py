"""
Funkcja generatora jest definiowana podobnie jak zwykła funkcja, ale return
zastępowane jest przez słowo kluczowe yield. Gdy ją wywołamy zwraca obiekt,
który jest iterowalny.
"""

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


def main(args):
    # Using the generator
    counter = count_up_to(5)
    for num in counter:
        print(num)

"""
Powyższy przykład demonstruje, że wywołanie funkcji count_up_to zwraca obiekt generatora.
Za każdym razem, gdy pętla for żąda wartości, funkcja zostaje wywołana zwracając,
za pomocą yield kolejną wygenerowaną wartość. Funkcja zachowuje stan pomiędzy kolejnymi
iteracjami dzięki czemu jest wstanie wznowić swoje działanie od miejsca, w którym została przerwana.
"""

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))