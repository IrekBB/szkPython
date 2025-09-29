epsilon= 0.00001

def f(x):
    return x*(x*(x-3)+2)-6

def pol_przedzialow_iter(a, b, precyzja=0.0001):
    if f(a) * f(b) >= 0:
        return None
    c = a
    while b - a >= precyzja:
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

def pol_przedzialow_rec(a,b):
    if f(a)==0: return 0
    if f(b)==0: return 0

    srodek = (a+b) /2
    if b-a<=epsilon: return srodek
    if f(a)*f(srodek)<0: return pol_przedzialow_rec(a,srodek)

    return pol_przedzialow_rec(srodek,b)
    

   
print(pol_przedzialow_iter(-10,10,0.00001))
print(pol_przedzialow_rec(-10,10))

