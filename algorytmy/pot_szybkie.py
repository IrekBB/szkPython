def pot_szybkie_iter(podstawa, n):
    w = 1
    while n>0:
        if n%2==1:
            w = w * podstawa
        podstawa=podstawa**2
        n=n//2
    return w


def pot_szybkie_rec(podstawa, n):
    if n==0:
        return 1
    if (n%2==1):
        return podstawa * pot_szybkie_rec(podstawa, n-1)
    w = pot_szybkie_rec(podstawa,n//2)
    return w**2

print(pot_szybkie_iter(2,10))
print(pot_szybkie_rec(2,10))

        
