def hanoi(n, a, b):
    if n==1:
        print(f"Przesuń dysk nr {n} z {a} na {b}")
    else:
        hanoi(n-1,a,3-a-b)
        print(f"Przesuń dysk nr {n} z {a} na {b}")
        hanoi(n-1,3-a-b,b)

def main(args):
    print("Testujemy dla 3 krążków")
    hanoi(3, 0, 1)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
