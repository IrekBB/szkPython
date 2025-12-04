"""
Generator expressions 

Wyrażenia generatora to kompaktowy sposób tworzenia generatorów. Są podobne do wyrażeń listowych, 
ale zawierają nawiasy zamiast nawiasów kwadratowych.

"""


def main(args):
    # List comprehension (eager evaluation)
    squares_list = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

    # Generator expression (lazy evaluation)
    squares_gen = (x**2 for x in range(5))

    # Using the generator
    for square in squares_gen:
        print(square)

"""
Jaka jest zatem różnica między comprehension expression a wyrażeniem generatora? W przypadku 
comprehensive expression cała lista tworzona jest bezpośrednio w pamięci komputera, 
podczas gdy wyrażenie generatora tworzy wartości pojedynczo, oszczędzając tym samym pamięć.
"""

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))