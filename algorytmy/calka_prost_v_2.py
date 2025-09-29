#!/usr/bin/env python

def integrate(function, a, b, i):
  dx = (b - a) / i
  integr = 0
  for x in range(i):
    x = x * dx + a
    integr += dx * eval(function)   
  return integr

def main(args):
  function = input("Funkcja: ")     # np. x**2 
  a = float(input("Początek przedziału: "))
  b = float(input("Koniec przedziału: "))
  i = int(input("Liczba podprzedziałów: "))
  print("Całka z funkcji {funkcjon} po przedziale od {a} do {b} = {integrate}".format(funkcjon = function, a = a, b = b, integrate = integrate(function, a, b, i)))
  return 0

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
