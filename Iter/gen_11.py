"""
3. .close() Method
Metoda .close() zatrzymuje działanie generatora. Zgłasza wyjątek GeneratorExit. Jest to przydatne 
do czyszczenia zasobów lub zatrzymywania nieskończonych generatorów.

"""
def infinite_counter():
    count = 0
    try:
        while True:
            yield count
            count += 1
    except GeneratorExit:
        print("Generator closed!")


def main(args):
    # Using the generator
    counter = infinite_counter()
    print(next(counter))  # Output: 0
    print(next(counter))  # Output: 1
    counter.close()       # Output: "Generator closed!"

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))