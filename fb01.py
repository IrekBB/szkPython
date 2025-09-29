'''
def silnia(n):
    if n<2: return 1
    else: return n * silnia(n-1)

n = int(input("n="))
print (f'{n}!= {silnia(n)} ')

def odwroc(napis, nr):
   print(napis[nr], end='') # wypisz literę na pozycji nr
   if nr > 0: # jeśli nie wypisaliśmy wszystkich liter
       odwroc(napis, nr - 1) # to wywołaj rekurencyjnie funkcję odwroc wskazującą na literę stojącą tuż przed wyświetlaną

# --------blok główny programu -----------
napis = input() 
odwroc(napis, len(napis) - 1)

p = int(input('p='))
q = int(input('q='))

def potega(p,q):
    if q==0: return 1
    else: return p*potega(p,q-1)

print(potega(p,q))
'''
def fib (n):
    if n<2:
        return 1
    else: return fib(n-2)+fib(n-1)

for n in range(9):
    print (fib(n),end=" ")
