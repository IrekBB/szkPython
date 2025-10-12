epsilon = 0.00000001 

def wart(x,yn):
    yn1 = 2 * yn - x * yn * yn
    if abs(yn-yn1) < epsilon:
        return yn1
    return wart(x, yn1)

def main(args):
    x = eval(input("x="))
    print (f"Wartość funkcji y=1/x dla x={x} wynosi {wart(x,00.1):.25}")

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
