# "cache", albo schowek, poczatkowo stowarzyszający 0 i 1 z fib(0) i fib(1) odpowiednio
# trzymanie cache w globalnym bloku to wada
cache = {0:0, 1:1}
def fib(n):
    if n not in cache: # wartość fib(n) jeszcze nie zapamiętana w schowku? Liczymy ją więc:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

print (fib(150))

"""
Używamy tu triku: uczyniliśmy z cache opcjonalny parametr fib z domyślną wartością będącą słownikiem
 - zmienialnym obiektem. Niektóre edytory ostrzegają przed takim działaniem: obiekt, który jest domyślną
wartością parametru jest tworzony przy definiowaniu funkcji, a nie przy każdym jej wywołaniu, i jego 
modyfikacje przenoszą się na następne wywołania, jak w przykładzie niżej:
"""
def fib_V1(n, cache={0: 0, 1: 1}):
    if n not in cache: # wartość fib(n) jeszcze nie zapamiętana w schowku? Liczmy ją więc:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n] # zwracamy wartość odczytaną ze schowka

print(fib_V1(150))
