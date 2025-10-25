"""
Przykład 7. Dekorator repeating, który dodaje dekorowanej funkcji nowy parametr opcjonalny repeat.
 Jego wartość (domyślnie 1) mówi, ile razy funkcja ma być powtórzona
"""
def repeating(func):
    def new_func(*args, repeat=1, **kwargs):
        for i in range(repeat):
            func(*args, **kwargs)
    return new_func

@repeating
def f(x, y):
    print(x, y, ":)")
    
f("a", "b", repeat=5)
