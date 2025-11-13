def main(args):
    t1 = np.array([5, 10, 15, 20])
    t2 = np.array([2, 1, 2, 4])
    t3 = np.array([9, 16, 8, 81])
    print (np.negative(t1))  # Negacja [-5 -10 -15 -20]
    print (np.add(t1, t2))   # Dodawanie [7 11 17 24]
    print (np.subtract(t1, t2)) # Odejmowanie: [5 10 15 20]
    print (np.multiply(t1, t2)) # Mnożenie [14 11 34 96]
    print (np.divide(t1, t2)) # Dzielenie [3.5 11. 8.5 6.]
    print(np.power(t1, t2)) # Potęgowanie: [25 10 225 160000]  
    print(np.sqrt(t3))  # Pierwiastek kwadratowy: [3. 4. 2.82842712 9.]
  


if __name__=="__main__":
    import numpy as np
    import sys
    sys.exit(main(sys.argv))