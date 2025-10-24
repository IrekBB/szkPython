import sys

def main(args):
    def do_twice(func):
        def new_func():
            func()
            func()
        return new_func

    def f():
        print('!')

    def g(): # tego nie podwajamy
        print('?')

    def h():
        print('.')


    f = do_twice(f) # od teraz f nazywa podwojenie tego, co f nazywało przed tą linijką
    h = do_twice(h)
    f()
    g()
    h()

if __name__ == "__main__": 
    main(sys.argv)