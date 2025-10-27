import sys
import time

def main(args):
    def timer(func):
        print (f'Czas rozpoczęcia to:{time.time()}s')
        def wrapper(*args, **kwargs):
            print('function {} called with {} {}'.format(func.__name__, args, kwargs))
            return func(*args, **kwargs)
        print (f'Czas zakończenia to:{time.time()}s')
        return wrapper  
        
    @timer
    def fib(n):
        if n<2: return 1
        else: return fib(n-2) + fib (n-1)

    print(fib(10))
if __name__ == "__main__":
    sys.exit(main(sys.argv))

