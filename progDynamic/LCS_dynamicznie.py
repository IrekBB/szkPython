import numpy as np # dla macierzy

def lcs(a, b):
    n = len(a)
    m = len(b)
    cache = np.zeros((n + 1, m + 1), dtype=int)

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if a[x - 1] == b[y - 1]:
                cache[x, y] = 1 + cache[x - 1, y - 1]
            else:
                cache[x, y] = max(cache[x, y - 1], cache[x - 1, y])
    return cache[n, m]

print(lcs('ALGORYTM', 'GRAMOTY'))