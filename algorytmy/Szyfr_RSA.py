def klucze_RSA():

    def nwd(a, b):
        # obliczanie NWD
        while b:
            a, b = b, a % b
        return a

    def odwr_mod(a, n):
        # obliczanie odwróconego modulo
        p0, p1, a0, n0 = 0, 1, a, n
        q, r = n0 // a0, n0 % a0
        while r:
            t = p0 - q * p1
            if t >= 0:
                t = t % n
            else:
                t = n - ((-t) % n)
                p0, p1, n0, a0 = p1, t, a0, r
                q, r  = n0 // a0, n0 % a0
        return p1

    # zasadnicza część funkcji RSA
    from random import choice
    pierwsze = [11, 13, 17, 19, 23, 29, 31] #gotowa lista liczb pierwszych
    p = 0
    q = 0
    while p == q:
        p, q = choice(pierwsze), choice(pierwsze) # funkcja choice wybiera losową liczbę z listę liczb pierwszych
        phi, n = (p - 1) * (q - 1), p * q	#obliczenie n i wartości funkcji Eulera
        e = 3   # dobieramy możliwie małą wartość dla e
        d = odwr_mod(e, phi)   # obliczamy wartość d
        while nwd(e, phi) != 1:
            e += 2
            d = odwr_mod(e, phi)

    return (e, n), (d, n)		#zwracamy klucze

# przykładowe wykonanie
print(klucze_RSA())

# przykładowy wynik:
# ((5, 551), (101, 551))
