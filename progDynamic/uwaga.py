"""
Używamy tu triku: uczyniliśmy z cache opcjonalny parametr fib z domyślną wartością będącą słownikiem - zmienial
nym obiektem. Niektóre edytory ostrzegają przed takim działaniem: obiekt, który jest domyślną wartością 
parametru jest tworzony przy definiowaniu funkcji, a nie przy każdym jej wywołaniu, i jego modyfikacje 
przenoszą się na następne wywołania, jak w przykładzie niżej:
"""
def f(lst=[]):
    lst.append(1)
    print(lst)
f()
f()
f()
