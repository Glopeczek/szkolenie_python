from prettytable import PrettyTable as pt
import time
# #otwarcie plików

# # plik=open(r'DATA\moje_dane.txt')
# # zaw=plik.read()
# # plik.close()

# # alternatywa żeby odczytać dane i automatycznie zamknąć plik

# with open(r'DATA\moje_dane.txt') as plik:
#     zaw=plik.read()

# print(zaw)

# #zapisywanie do pliku
# with open(r'DATA\moje_dane.txt',"a") as plik:
#     plik.write("\nAle bydle")

######################################################################

MAX = -1
# Import samochody z pliku dane.csv
i = 0

suma_total = 0
ile_total = 0
pojazdy = {}  # pusty słownik
czas_start=time.time()

with open(r"DATA\dane_2_mln.csv", encoding="utf-8") as plik:
    for wiersz in plik:
        if i == 0:  # pominiecie pierwszego wiersza
            i += 1
            continue
        # print(wiersz.strip())
        i += 1
        if i == MAX:
            break
        lista = wiersz.split(";")
        pojazd = lista[1]
        cena = float(lista[2])
        suma_total += cena
        ile_total += 1

        # uzupełnij słownik
        if pojazd not in pojazdy:
            pojazdy[pojazd] = [0, 0]  # pusta lista
        cena_obliczona = pojazdy[pojazd][0] + cena
        liczba_obl = pojazdy[pojazd][1] + 1
        pojazdy[pojazd] = [cena_obliczona, liczba_obl]
# print(f"autek:{ile_total}, cena total:{suma_total}")
# print(pojazdy)
tab = pt(["Pojazd", "Cena", "Ilość",'Średnia cena'])
for Pojazd, x in pojazdy.items():
    ceny = f"{x[0]:_.0f}".replace("_", " ")
    ile = x[1]
    srednia = f"{x[0]/x[1]:_.0f}".replace("_"," ")
    tab.add_row([Pojazd, ceny, ile, srednia])
print(tab)
with open(r"DATA\moje_dane.txt", "w", encoding="utf=8", newline="") as plik:
    plik.write(tab.get_string())
    plik.write("\n\n")
    plik.write(tab.get_csv_string(delimiter=";"))
czas_stop=time.time()
czas=f"{czas_stop-czas_start:.2f} s"
print(czas)