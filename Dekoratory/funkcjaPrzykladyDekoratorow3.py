<<<<<<< HEAD
"""
Przykład 2. Dekorator print_return, który dla każdego wywołania udekorowanej funkcji wypisze na ekran to, 
co dane wywołanie zwróciło. Ma podobne zastosowania, co print_arguments, implementacja też polega na
odpowiednim wtrąceniu:
"""
def print_return(func):
    def new_func(*args, **kwargs):
        ret = func(*args, **kwargs)
        print('{} returned {}'.format(func.__name__, ret))
        return ret
    return new_func

@print_return
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

@print_return
def Fibo(n):
   if n < 3:
       return 1
   return Fibo(n-1) + Fibo(n-2)

print(gcd(10, 6))
print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print (Fibo(10))
=======
"""
Przykład 2. Dekorator print_return, który dla każdego wywołania udekorowanej funkcji wypisze na ekran to, 
co dane wywołanie zwróciło. Ma podobne zastosowania, co print_arguments, implementacja też polega na
odpowiednim wtrąceniu:
"""
def print_return(func):
    def new_func(*args, **kwargs):
        ret = func(*args, **kwargs)
        print('{} returned {}'.format(func.__name__, ret))
        return ret
    return new_func

@print_return
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

@print_return
def Fibo(n):
   if n < 3:
       return 1
   return Fibo(n-1) + Fibo(n-2)

print(gcd(10, 6))
print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print (Fibo(10))
>>>>>>> 04a243ce5a1b07f507b75f71b1dcf09ce156c7db
