login = "Adam"
haslo = "Cobra123"

log = input("podaj  swój login: ")
has = input ("podaj swoje hasło: ")

# ==, <=,>=,<,>, != -różny
if login==log and haslo==has:
    print (f"Wita {login} w systemie Windows 88.05")
else:
    print (f"{log}! Twój login lub hasło jest niepoprawne")
