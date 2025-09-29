def f(x):
    return x**2+x+2

def calka_trapez(a,b,n) :
    h = (b-a) / n 
    S = 0
    podstawa_a = f(a)

    for i in range(1,n+1):
        podstawa_b = f(a+h*i)
        S = S + (podstawa_a + podstawa_b)
        podstawa_a = podstawa_b
        

    return S *0.5 * h
    
print (calka_trapez(10,2,1000))
