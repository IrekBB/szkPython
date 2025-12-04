"""
4. Handling infinite sequences 
Na koniec zauważmy, że generatory nadają się wyjątkowo  do reprezentowania nieskończonych ciągów, 
co jest po prostu niemożliwe w przypadku list. Dla przykładu rozważmy ciąg Fibonacciego.
"""
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main(args):
    fib = fibonacci()
    for _ in range(100):
        print(next(fib))

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))