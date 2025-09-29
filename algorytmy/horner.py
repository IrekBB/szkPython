def horner_rec(wsp,st,x):
    if st==0: return wsp[0]
    return x*horner_rec(wsp,st-1,x)+wsp[st]

def horner_iter(wsp,x):
    wynik = 0
    for i in wsp:
        wynik = wynik*x + i
    return wynik

L=[3,3,-2,11]
print (horner_rec(L,3,2))
print (horner_iter(L,2))
