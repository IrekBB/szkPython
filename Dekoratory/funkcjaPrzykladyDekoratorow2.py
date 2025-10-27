<<<<<<< HEAD
"""
Przykład 1. Dekorator print_arguments, który dla każdego wywołania udekorowanej funkcji wypisze na ekran
wartości przekazanych jej argumentów. Może być przydatny przy debugowaniu większej aplikacji, lub zbieraniu
danych dotyczących jej wykonywania. Implementacja polega na wtrąceniu jednej linijki w identity, przed wywołaniem
samej dekorowanej funkcji:
"""
def print_arguments(func):
    def new_func(*args, **kwargs):
        print('function {} called with {} {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return new_func

@print_arguments
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(10, 6))
=======
"""
Przykład 1. Dekorator print_arguments, który dla każdego wywołania udekorowanej funkcji wypisze na ekran
wartości przekazanych jej argumentów. Może być przydatny przy debugowaniu większej aplikacji, lub zbieraniu
danych dotyczących jej wykonywania. Implementacja polega na wtrąceniu jednej linijki w identity, przed wywołaniem
samej dekorowanej funkcji:
"""
def print_arguments(func):
    def new_func(*args, **kwargs):
        print('function {} called with {} {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return new_func

@print_arguments
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(10, 6))
>>>>>>> 04a243ce5a1b07f507b75f71b1dcf09ce156c7db
