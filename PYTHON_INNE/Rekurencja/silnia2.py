def silnia2(x, tmp=1):
    if x==0:
        return tmp
    else:
        return silnia2(x-1, x*tmp)

def main(args):
    n = int(input("n="))
    print (f"{n}!={silnia2(n)}")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
