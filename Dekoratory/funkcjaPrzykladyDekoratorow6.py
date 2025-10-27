<<<<<<< HEAD
"""
Przykład 6. Dekorator check_args() sprawdzający, czy wszystkie argumenty podane dekorowanej funkcji są instancjami zadanego typu
"""
def check_args(t):
    def decorator_function(func):
        def new_func(*args, **kwargs):
            for a in args:
                if not isinstance(a, t):
                    raise TypeError('{} is not an instance of {}'.format(a, t))
            for a in kwargs.values():
                if not isinstance(a, t):
                    raise TypeError('{} is not an instance of {}'.format(a, t))
            return func(*args, **kwargs)
        return new_func
    return decorator_function

@check_args(int)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(10, 6)) # ok
try:
    print(gcd(10, "kalosze")) # wyjątek!
except Exception as e:
    print(e)

=======
"""
Przykład 6. Dekorator check_args() sprawdzający, czy wszystkie argumenty podane dekorowanej funkcji są instancjami zadanego typu
"""
def check_args(t):
    def decorator_function(func):
        def new_func(*args, **kwargs):
            for a in args:
                if not isinstance(a, t):
                    raise TypeError('{} is not an instance of {}'.format(a, t))
            for a in kwargs.values():
                if not isinstance(a, t):
                    raise TypeError('{} is not an instance of {}'.format(a, t))
            return func(*args, **kwargs)
        return new_func
    return decorator_function

@check_args(int)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(10, 6)) # ok
try:
    print(gcd(10, "kalosze")) # wyjątek!
except Exception as e:
    print(e)

>>>>>>> 6aa862e50fd580ff4b4027d0f8357d09024e549b
