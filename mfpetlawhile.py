"""
i= 0
while i<10:
    print("***************************")
    i = i + 1
"""

while True:
    print ("1. Dodawanie")
    print ("2. Odejmowanie")
    print ("3. Mnożenie")
    print ("4. Dzielenie")
    print ("5. Koniec")
    wybor = input("Twój wybór? ")
    if wybor == "1":
        x = eval(input("x="))
        y = eval(input("y="))
        print (f"{x} + {y} = {x + y}")
    elif wybor=="4":
        x = eval(input("x="))
        y = eval(input("y="))
        if y==0:
            print("Błąd dzielenia przez 0!")
        else:
            print(f"{x} / {y} = {x / y}")
    
    elif wybor=="5":
        break
    else:
        print("Wybierz 1,2,3,4 lub 5")
print("koniec.")
