def silnia_i(x, res=1):
    while x!=0:
        res = x * res
        x = x -1
    return res
    

def silnia(n):
    silnia=1
    if n==0: return 1
    else:
        for i in range(1,n+1):
            silnia = silnia * i
    return silnia

def main(args):
    n = int(input("n="))
    print(f"{n}!={silnia(n)}")
    print(f"{n}!={silnia_i(n)}")
    

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
