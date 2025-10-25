"""
Funkcje zwracające dekoratory i dalsze przykłady
Wyrażenie pojawiające się po @ przed definicją funkcji nie musi być nazwą samego dekoratora. 
Może być również wywołaniem funkcji, która zwraca dekoratory.

Funkcja która zwraca dekoratory to, fundamentalnie:
 funkcja, która zwraca funkcję, która bierze funkcję i która zwraca funkcję. 
 Funkcja zwracająca dekoratory może przyjmować dowolne argumenty i używać ich 
 w definicji zwracanych dekoratorów.
"""

# Przykład 5. Dekorator powtarzania repeat(), działający jak `do_twice' (tym razem dla funkcji o dowolnych parametrach), 
# ale o dowolnej zadanej ilości powtórzeń:

def repeat(n):
    def decorator_function(func):
        def new_func(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return new_func
    return decorator_function

@repeat(4)
def f():
    print('!')
    
@repeat(2)
def g(x):
    print(x, '!')
    
f()
g(1)
