
"""
Przykład 3. Połączenie obu poprzednich przykładów - bez pisania nowego kodu. Do funkcji możemy zaaplikować więcej, niż jeden dekorator:
"""
def print_return(func):
    def new_func(*args, **kwargs):
        ret = func(*args, **kwargs)
        print('{} returned {}'.format(func.__name__, ret))
        return ret
    return new_func

def print_arguments(func):
    def new_func(*args, **kwargs):
        print('function {} called with {} {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return new_func

@print_arguments
@print_return
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
"""
Przykład 3. Połączenie obu poprzednich przykładów - bez pisania nowego kodu. Do funkcji możemy zaaplikować więcej, niż jeden dekorator:
"""
def print_return(func):
    def new_func(*args, **kwargs):
        ret = func(*args, **kwargs)
        print('{} returned {}'.format(func.__name__, ret))
        return ret
    return new_func

def print_arguments(func):
    def new_func(*args, **kwargs):
        print('function {} called with {} {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return new_func

@print_arguments
@print_return
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

>>>>>>> 04a243ce5a1b07f507b75f71b1dcf09ce156c7db
gcd(10,6)