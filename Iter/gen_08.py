"""
Advanced Python Generator Concepts  

1. Chaining generators together
Generatory można łączyć. Dane można przekształcać, filtrować i przetwarzać modułowo, łącząc generatory w łańcuch. 

"""
# Załóżmy, że masz nieskończoną sekwencję liczb i chcesz podnieść każdą liczbę do kwadratu i odfiltrować wyniki nieparzyste
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
def square_numbers(sequence):
    for num in sequence:
        yield num ** 2
def filter_evens(sequence):
    for num in sequence:
        if num % 2 == 0:
            yield num

def main(args):
    # Compose the generators
    numbers = infinite_sequence()
    squared = square_numbers(numbers)
    evens = filter_evens(squared)
    for _ in range(10):
        print(next(evens))

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))