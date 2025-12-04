"""
3. Simplicity and readability 
Generatory upraszczają implementację iteratorów, eliminując konieczność korzystania 
z szablonu kodu iteratora. Porównajmy iterator oparty na klasach z funkcją generatora
"""

# Iterator
class SquaresIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# Funkcja generatora 
def squares_generator(n):
    for i in range(n):
        yield i ** 2

def main(args):
    # Użycie iteratora
    print ("*** Użycie iteratora ***")
    squares = SquaresIterator(5)
    for square in squares:
        print(square)
    
    # Uzycie generator
    print ("*** Użycie generatora ***")
    squares = squares_generator(5)
    for square in squares:
        print(square)
    

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))