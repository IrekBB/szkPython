# Konfiguracja widgetów
"""
Do konfiguracji widgetów zwykle uzywamy opcji, nie zaś wywołania metod.
Typowe opcje to kolor, rozmiar, wywołania funkcji zwrotnych
(command callbacks) itp.
"""

# Konfiguracja interfejsu
"""
# tworzenie instancji widgetu

     widgetclass (master, option=value,.....) -> widget

# Zwraca aktualną wartość opcji. Zarówno nazwa opcji jak i wartość
# zwracana to  stringi. Można również uzyskać nazwę opcji stosują str(widget) 	

     cget(option) -> string

# Ustawianie opcji

     configure(option=value,.....)
     config(option=value,.....)

Niektóre nazwy opcji są słowami zastrzeżonymi w pythonie. Aby z nich skorzystać
musimy w powyższych wywołaniach dodać na końcu nazwy opcji podkreślenie (class_,
from_, itd). Możemy także użyć zapisu:

      value = widget[option]
      widget[option] = value

# metoda keys

      keys() -> list

Zwraca listę wszystkich opcji widgetu, nazwa opcji nie jest załączona do listy.




