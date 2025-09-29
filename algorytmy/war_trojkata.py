def trojkat(a,b,c):
    return a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a;


def main(args):
    a = eval(input("bok a = "))
    b = eval(input("bok b = "))
    c = eval(input("bok c = "))
    if trojkat(a,b,c):
        print (f"Trójkąt o bokach {a}, {b}, {c} istnieje.")
    else:
        print(f"Trójkąta o bokach {a}, {b}, {c} nie istnieje.")

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
