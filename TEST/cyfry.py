def main(args):
    cyfry = [1,2,3,4,5,6,7,8,9,0]
    for x in range(len(cyfry)):
        print (f"({cyfry[x]})", end=" ")
    print()
    print(*cyfry)
    print(*cyfry, sep="-")

if __name__=="__main__": 
    import sys
    sys.exit(main(sys.argv))