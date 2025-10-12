def nwd(a,b):
    if b==0:
        return a
    else:
        return nwd(b,a%b)
    

def gcd(a,b):
    if a==b: return a
    else:
        if a > b:
            return gcd(a-b,b)
        else:
            return gcd(b-a,a)
            

def main(args):
    a = int(input("a="))
    b = int(input("b="))
    print (f"gcd(great common divisor) dla liczb {a}, {b}: {gcd(a,b)}")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
