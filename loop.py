'''
for i in range (10):
    print(i)
print("----------------------")
for i in range (2, 8, 2):
    print(i)
'''
kolumna = eval(input("ilość kolumn: "))
wiersz = eval(input("Ilość wierszy: "))

for j in range(wiersz):
    for i in range(kolumna):
        print("*", end="")
    print()


