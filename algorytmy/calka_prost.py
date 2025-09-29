def f(x):
    return x**2+x+2

def calka_prost(a,b,n):
    x = (b-a) / n
    S=0
    srodek = a + (b-a) / (2*n)

    for i in range(n):
        S= S + f(srodek)
        srodek=srodek+x

    return S*x
    


def integrate(a, b, i, function):
  dx = (b - a) / i
  integr = 0
  for x in range(i):
    x = x * dx + a
    integr += dx * function(x)
  return integr

print (calka_prost(2,10,1000))
print (integrate(2,10,1000,f))
