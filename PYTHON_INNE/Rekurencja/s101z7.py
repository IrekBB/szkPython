def potega(n,p):
    res=1
    if p==0: return 1
    else:
        return n*potega(n, p-1)

def potega_p(n,p,res=1):
    if p==0: return res
    else:
        return potega_p(n,p-1, res=res*n)
    

def main(args):
    n = int(input("podstawa: "))
    p = int(input("wykładnik: "))
    print (f"{n}^{p}={potega(n,p)}")
    print (f"{n}^{p}={potega_p(n,p)}")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
