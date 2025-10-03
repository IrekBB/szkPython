def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

def silnia_dyn(n):
    sTab  = [0] * (n+1)
    if n<2:
        return [1,1]
    sTab[1] = 1
    for i in range(2, n+1):
        sTab[i] = i*sTab[i-1]

    return sTab

def main(args):
    N = 12
    f = silnia_dyn(N)
    print(f)
    print("Wyniki:")
    for i in range(N+1):
        print(f"silnia({i:2})={f[i]:>10} \t metoda klasyczna: {silnia(i):>10}")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))