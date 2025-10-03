def fib(n, cache = [0,1]):
    for _ in range(n - len(cache)  + 1):
        cache.append(cache[-1] + cache[-2])
    return cache[n]
# Tutaj cache to lista, a nie słownik. Wartości fib w jej kolejnych indeksach konstruujemy metodą
#  wstępną (wstępującą, bottom-up). Pierwsze dwie linijki funkcji gwarantują, że długość cache będzie
#  większa, niż n, wykonując minimum potrzebnych do tego operacji (często zero iteracji pętli).

print(fib(150))