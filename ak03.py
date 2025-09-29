'''
i=0
while i < 100:
    print ("***************************")
    i=i+1
print ("koniec")

# break

'''

while True:
    print("1. Dodaj")
    print("2. Odejmij")
    print("3. Pomnóż")
    print ("4. Podziel")
    print("5. Zakończ")
    odp = input("Twój wybór? ")
    if odp=="1":
        x = eval(input("x="))
        y = eval(input("y="))
        suma  = x + y
        print (f"{x} + {y} = {suma}")
    elif odp=="4":
        x = eval(input("x="))
        y = eval(input("y="))
        if y==0:
            print("Error: Division by zero")
        else:
            dziel  = x / y
            print (f"{x} / {y} = {dziel}")
    elif odp=="5":
        break
    
    else:
        print (f"Wybrałeś {odp}. Błąd. Dobry wybór to 1,2,3,4,5")
print("koniec.")
