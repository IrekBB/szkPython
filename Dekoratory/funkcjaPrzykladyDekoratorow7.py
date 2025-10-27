<<<<<<< HEAD
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
=======
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
>>>>>>> 6aa862e50fd580ff4b4027d0f8357d09024e549b
