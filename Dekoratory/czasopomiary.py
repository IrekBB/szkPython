import time
import sys

def startstop(func):
     print("Starting...")
     start = time.time()
     def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
     end = time.time()
     print ("Finishing...")
     print (f"Czas wykonania: {end-start:.20f}s")
     return wrapper

@startstop
def silnia(n):
    if n<=1: return 1
    else: return n * silnia(n-1)

@startstop
def silnia_it(n, res=1):
    while n!=0:
        res = n * res
        n = n - 1
    return res

print (silnia(67))  
print (silnia_it(67))