import datetime
import sys

"""
Przykładowe kody formatujące strptime i strftime:
%Y: Pełny rok (np. 2025)
%y: Rok bez stulecia (np. 25)
%m: Miesiąc jako liczba dziesiętna (01-12)
%B: Pełna nazwa miesiąca (np. styczeń)
%b: Skrócona nazwa miesiąca (np. sty)
%d: Dzień miesiąca jako liczba dziesiętna (01-31)
%A: Pełna nazwa dnia tygodnia (np. poniedziałek)
%a: Skrócona nazwa dnia tygodnia (np. pon)
%H: Godzina w formacie 24-godzinnym (00-23)
%I: Godzina w formacie 12-godzinnym (01-12)
%M: Minuty (00-59)
%S: Sekundy (00-59)
%p: Wartość AM lub PM 
%x Lokalna reprezentacja daty
%X Lokalna reprezentacja czasu
%j Dni roku pisane 3-cyfrowo (od 001 do 366)
%Z Nazwa strefy czasowej (np. UTC, GM, może być pusta)
%w Dni tygodnia kodowane jako 0--6 (od niedzieli do soboty)
%c Lokalna reprezentacja daty i czasu
%U Numery tygodni pisane 2-cyfrowo (00,...,53). Niedziela to pierszy dzień tygodnia
%W Numery tygodni pisane 2-cyfrowo (00,...,53). Poniedziałek to pierwszy dzień tygodnia
"""


def main(args):
    teraz = datetime.datetime.now()

    # Format: Dzień.Miesiąc.Rok Godzina:Minuta
    format_data_czas = teraz.strftime("%d.%m.%Y %H:%M")
    print(format_data_czas)
    # Przykładowy wynik: 30.10.2025 14:30

    # Format: Poniedziałek, 30 Października 2025
    format_dnia_miesiac_rok = teraz.strftime("%A, %d %B %Y")
    print(format_dnia_miesiac_rok)
    # Przykładowy wynik: czwartek, 30 października 2025

    print(teraz.strftime("%Y-%m-%d %H:%M:%S"))
    print(teraz.strftime("%d/%m/%Y Nr tygodnia: %U"))
    print(teraz.strftime("%Y\\%m\\%d"))
    print(teraz.strftime("%I:%M:%S %p"))
    print(teraz.strftime("%A - %b %d, %Y"))

if __name__=="__main__":
    sys.exit(main(sys.argv))