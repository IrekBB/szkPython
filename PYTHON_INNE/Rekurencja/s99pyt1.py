def odwroc_bin(n):
    if n!=0:
        odwroc_bin(n//2)
        print(n%2,end="")
    

def main(args):
    n = int(input("n="))
    odwroc_bin(n)
    print("\n",bin(n))

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
