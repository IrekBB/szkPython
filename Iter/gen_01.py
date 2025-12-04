def generate_integers(n):  # generator jako funkcja (generator function)
    for i in range(n):
        yield i

def main(args):
    n = int(input("n="))
    for num in generate_integers(n):
        print(num)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))