"""
Dekorator lru_cache ze standardowej biblioteki functools, przerabiający funkcję na taką, 
która używa schowka, podobnego jak w przykładach do rekurencji ze spamiętywaniem. Przykładowe użycie:
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n in range(2):
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))

"""
Argument maxsize oznacza maksymalną ilość zapamiętanych, ostatnio użytych argumentów, 
z którymi została wywołana funkcja (dla None jest to ilość nieograniczona). 
Gdy funkcja zostaje wywołana z danym argumentem, zwracana wartość jest zapamiętywana 
i następne wywołania z takim argumentem nie prowadzą do wykonania funkcji, a tylko 
zwrócenia wartości ze schowka.
"""
